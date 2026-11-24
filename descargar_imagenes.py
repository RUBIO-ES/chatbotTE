"""
Descarga una foto de referencia por moto desde los articulos de Wikipedia.

Uso:
    python descargar_imagenes.py                 # modelos con datos tecnicos
    python descargar_imagenes.py --limite 10     # solo los primeros 10
    python descargar_imagenes.py --marca Yamaha  # solo una marca
    python descargar_imagenes.py --solo "Yamaha YZF-R1"
    python descargar_imagenes.py --forzar        # reemplaza fotos existentes
    python descargar_imagenes.py --workers 6     # descargas en paralelo

Las fotos se guardan en imagenes/<marca>_<modelo>.jpg y la atribucion en
imagenes/creditos.json. El bot muestra ese credito en el pie de la foto.
"""

import argparse
import json
import re
import socket
import sys
import time
import unicodedata
from concurrent.futures import ThreadPoolExecutor, as_completed
from difflib import SequenceMatcher
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urlencode, urlparse
from urllib.request import Request, urlopen

from datos_motos import MOTOS

CARPETA = Path("imagenes")
ARCHIVO_CREDITOS = CARPETA / "creditos.json"
EXTENSIONES = (".jpg", ".jpeg", ".png", ".webp")
IDIOMAS = ("es", "en")
PAUSA = 0.5
AGENTE = (
    "MotoGuiaBot/1.0 (proyecto academico; "
    "https://github.com/rubisabel00/machine-learning-Bot-telegram)"
)


def normalizar(texto):
    texto = unicodedata.normalize("NFD", str(texto).lower())
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]+", " ", texto).strip()


def clave_archivo(texto):
    return re.sub(r"[^a-z0-9]+", "_", normalizar(texto)).strip("_")


def palabras(texto):
    return [p for p in normalizar(texto).split() if p]


def limpiar_html(texto):
    texto = re.sub(r"<[^>]+>", "", str(texto))
    return re.sub(r"\s+", " ", texto).strip()


def similitud(titulo, marca, modelo):
    return SequenceMatcher(
        None,
        f"{normalizar(marca)} {normalizar(modelo)}",
        normalizar(titulo),
    ).ratio()


def pegar_letras_numeros(texto):
    """'S 1000 RR' -> 'S1000RR', que es como titula Wikipedia algunos modelos."""
    return re.sub(r"(?<=[A-Za-z])\s+(?=\d)|(?<=\d)\s+(?=[A-Za-z])", "", texto)


def coincide(titulo, marca, modelo):
    titulo_n = normalizar(titulo)
    modelo_n = normalizar(modelo)

    if modelo_n and modelo_n in titulo_n:
        return True

    compacto_modelo = modelo_n.replace(" ", "")
    compacto_titulo = titulo_n.replace(" ", "")
    if compacto_modelo and compacto_modelo in compacto_titulo:
        return True

    # Cada palabra del modelo debe aparecer tal cual (KLX230 != W230,
    # Duke 250 != 790, Burgman 200 != 650). Mejor sin foto que con la moto equivocada.
    tokens = [p for p in palabras(modelo) if len(p) > 1]
    if tokens:
        return all(token in compacto_titulo for token in tokens)

    return similitud(titulo, marca, modelo) >= 0.8


def preferir_ipv4():
    """Evita IPv6: en algunas redes el IPv6 de Wikimedia se queda colgado."""
    original = socket.getaddrinfo

    def solo_ipv4(host, puerto, familia=0, tipo=0, proto=0, flags=0):
        return original(host, puerto, socket.AF_INET, tipo, proto, flags)

    socket.getaddrinfo = solo_ipv4


def abrir(peticion, timeout):
    for intento in range(3):
        try:
            return urlopen(peticion, timeout=timeout)
        except HTTPError as error:
            if error.code == 429:
                espera = 8 * (intento + 1)
                cabecera = error.headers.get("Retry-After") if error.headers else None
                if cabecera and cabecera.isdigit():
                    espera = max(espera, int(cabecera))
                time.sleep(espera)
                continue
            raise
        except (URLError, TimeoutError, OSError):
            if intento == 2:
                raise
            time.sleep(2 * (intento + 1))


def consultar(idioma, parametros, dominio=None):
    parametros = {"format": "json", **parametros}
    host = dominio or f"{idioma}.wikipedia.org"
    url = f"https://{host}/w/api.php?{urlencode(parametros)}"
    peticion = Request(url, headers={"User-Agent": AGENTE})

    with abrir(peticion, timeout=25) as respuesta:
        contenido = json.loads(respuesta.read().decode("utf-8"))

    time.sleep(PAUSA)
    return contenido


def candidatos(marca, modelo):
    titulos = [f"{marca} {modelo}"]
    partes = modelo.split()

    if len(partes) > 1:
        titulos.append(f"{marca} {' '.join(partes[1:] + partes[:1])}")

    primera = marca.split()[0]
    if primera != marca:
        titulos.append(f"{primera} {modelo}")

    for titulo in list(titulos):
        pegado = pegar_letras_numeros(titulo)
        if pegado != titulo:
            titulos.append(pegado)

    vistos = []
    for titulo in titulos:
        if titulo not in vistos:
            vistos.append(titulo)
    return vistos


def metadatos_archivo(idioma, archivo):
    datos = consultar(
        idioma,
        {
            "action": "query",
            "titles": f"File:{archivo}",
            "prop": "imageinfo",
            "iiprop": "url|extmetadata",
            "iiurlwidth": "800",
        },
    )

    for pagina in datos.get("query", {}).get("pages", {}).values():
        info = (pagina.get("imageinfo") or [{}])[0]
        url = info.get("thumburl") or info.get("url")
        if not url:
            continue

        extra = info.get("extmetadata", {})
        autor = limpiar_html(extra.get("Artist", {}).get("value", ""))
        licencia = limpiar_html(
            extra.get("LicenseShortName", {}).get("value", "")
        )
        credito = " · ".join(
            parte
            for parte in (autor, licencia, f"{idioma}.wikipedia.org")
            if parte
        )
        return url, credito[:160]

    return None


def imagen_de_titulos(idioma, titulos, marca, modelo):
    datos = consultar(
        idioma,
        {
            "action": "query",
            "redirects": "1",
            "titles": "|".join(titulos),
            "prop": "pageimages",
            "piprop": "thumbnail|name",
            "pithumbsize": "800",
        },
    )

    paginas = [
        pagina
        for pagina in datos.get("query", {}).get("pages", {}).values()
        if pagina.get("pageimage")
        and (
            coincide(pagina.get("title", ""), marca, modelo)
            or coincide(pagina.get("pageimage", ""), marca, modelo)
        )
    ]
    paginas.sort(
        key=lambda pagina: similitud(pagina["title"], marca, modelo),
        reverse=True,
    )

    for pagina in paginas:
        resultado = metadatos_archivo(idioma, pagina["pageimage"])
        if resultado:
            return resultado

    return None


def buscar_en_wikipedia(idioma, marca, modelo):
    consultas = [f"{marca} {modelo}"]
    primera = marca.split()[0]
    if primera != marca:
        consultas.append(f"{primera} {modelo}")
    if idioma == "es":
        consultas = [f"{consulta} motocicleta" for consulta in consultas]

    for consulta in consultas:
        datos = consultar(
            idioma,
            {
                "action": "query",
                "list": "search",
                "srsearch": consulta,
                "srlimit": "8",
            },
        )

        titulos = [
            resultado.get("title", "")
            for resultado in datos.get("query", {}).get("search", [])
            if coincide(resultado.get("title", ""), marca, modelo)
        ]

        if titulos:
            resultado = imagen_de_titulos(idioma, titulos, marca, modelo)
            if resultado:
                return resultado

    return None


def buscar_en_commons(marca, modelo):
    primera = marca.split()[0]
    consultas = [f"{marca} {modelo}"]
    if primera != marca:
        consultas.append(f"{primera} {modelo}")

    tokens = [p for p in palabras(modelo) if len(p) > 1]
    marca_n = normalizar(primera)
    descartes = ("logo", "diagram", "drawing", "badge", "emblem", "map ")

    for consulta in consultas:
        datos = consultar(
            "commons",
            {
                "action": "query",
                "generator": "search",
                "gsrsearch": f"filetype:bitmap {consulta}",
                "gsrnamespace": "6",
                "gsrlimit": "8",
                "prop": "imageinfo",
                "iiprop": "url|extmetadata",
                "iiurlwidth": "800",
            },
            dominio="commons.wikimedia.org",
        )

        for pagina in datos.get("query", {}).get("pages", {}).values():
            titulo = pagina.get("title", "")
            titulo_n = normalizar(titulo)

            if any(descarte in titulo_n for descarte in descartes):
                continue

            compacto = "".join(palabras(titulo))
            if marca_n not in compacto:
                continue
            if tokens and not all(token in compacto for token in tokens):
                continue

            info = (pagina.get("imageinfo") or [{}])[0]
            url = info.get("thumburl") or info.get("url")
            if not url:
                continue

            extra = info.get("extmetadata", {})
            autor = limpiar_html(extra.get("Artist", {}).get("value", ""))
            licencia = limpiar_html(
                extra.get("LicenseShortName", {}).get("value", "")
            )
            credito = " · ".join(
                parte
                for parte in (
                    autor,
                    licencia,
                    "commons.wikimedia.org",
                )
                if parte
            )
            return url, credito[:160]

    return None


def buscar_foto(marca, modelo):
    for idioma in IDIOMAS:
        resultado = imagen_de_titulos(
            idioma, candidatos(marca, modelo), marca, modelo
        )
        if resultado:
            return resultado

    for idioma in IDIOMAS:
        resultado = buscar_en_wikipedia(idioma, marca, modelo)
        if resultado:
            return resultado

    return buscar_en_commons(marca, modelo)


def extension_de(url):
    extension = Path(unquote(urlparse(url).path)).suffix.lower()
    return extension if extension in EXTENSIONES else ".jpg"


def descargar(url, destino):
    peticion = Request(
        url,
        headers={
            "User-Agent": AGENTE,
            "Accept": "image/jpeg,image/png,image/webp;q=0.9,*/*;q=0.8",
        },
    )

    with abrir(peticion, timeout=40) as respuesta:
        contenido = respuesta.read()

    if len(contenido) < 5000:
        raise ValueError("archivo invalido o demasiado pequeno")

    destino.write_bytes(contenido)


def cargar_creditos():
    if ARCHIVO_CREDITOS.exists():
        try:
            with open(ARCHIVO_CREDITOS, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except (OSError, json.JSONDecodeError):
            pass
    return {}


def guardar_creditos(creditos):
    with open(ARCHIVO_CREDITOS, "w", encoding="utf-8") as archivo:
        json.dump(creditos, archivo, indent=2, ensure_ascii=False)


def foto_existente(base):
    for extension in EXTENSIONES:
        if (CARPETA / f"{base}{extension}").exists():
            return True
    return False


def procesar(nombre, base, forzar):
    marca, modelo = nombre.split("|", 1)

    if foto_existente(base) and not forzar:
        return "existe", None, "", ""

    try:
        resultado = buscar_foto(marca, modelo)
    except (HTTPError, URLError, TimeoutError, OSError):
        return "error", None, "", ""

    if not resultado:
        return "sin foto", None, "", ""

    url, credito = resultado
    origen = unquote(urlparse(url).path).rsplit("/", 1)[-1]
    destino = CARPETA / f"{base}{extension_de(url)}"

    try:
        descargar(url, destino)
    except (HTTPError, URLError, TimeoutError, OSError, ValueError):
        return "error", None, "", ""

    return "ok", destino.name, credito, origen


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limite", type=int, default=0,
                        help="maximo de modelos a procesar (0 = todos)")
    parser.add_argument("--marca", help="procesar solo esta marca")
    parser.add_argument("--solo", help='un modelo, ej: "Yamaha YZF-R1"')
    parser.add_argument("--forzar", action="store_true",
                        help="reemplazar fotos ya existentes")
    parser.add_argument("--workers", type=int, default=2,
                        help="descargas simultaneas (por defecto 2)")
    parser.add_argument("--todo", action="store_true",
                        help="incluye tambien las 449 referencias del catalogo")
    args = parser.parse_args()

    preferir_ipv4()
    CARPETA.mkdir(exist_ok=True)
    creditos = cargar_creditos()

    if args.solo:
        seleccion = [
            (clave, datos)
            for clave, datos in MOTOS.items()
            if normalizar(clave) == normalizar(args.solo)
        ]
        if not seleccion:
            print(f'No encontre "{args.solo}" en datos_motos.py')
            return 1
    else:
        seleccion = list(MOTOS.items())

        if args.todo and Path("catalogo.json").exists():
            try:
                with open("catalogo.json", "r", encoding="utf-8") as archivo:
                    catalogo = json.load(archivo)
            except (OSError, json.JSONDecodeError):
                catalogo = []

            claves = {clave for clave, _datos in seleccion}
            for moto in catalogo:
                i = moto["identificacion"]
                clave = f"{i['marca']}|{i['modelo']}"
                if clave not in claves:
                    seleccion.append((clave, None))
                    claves.add(clave)

    if args.marca:
        seleccion = [
            (clave, datos)
            for clave, datos in seleccion
            if normalizar(clave.split("|")[0]) == normalizar(args.marca)
        ]

    if args.limite > 0:
        seleccion = seleccion[: args.limite]

    total = len(seleccion)
    trabajos = {}

    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        for clave, _datos in seleccion:
            base = clave_archivo(clave.replace("|", " "))
            trabajos[
                pool.submit(procesar, clave, base, args.forzar)
            ] = clave

        resultados = {"ok": 0, "existe": 0}

        for numero, futuro in enumerate(as_completed(trabajos), start=1):
            clave = trabajos[futuro]
            nombre = clave.replace("|", " ")
            estado, archivo, credito, origen = futuro.result()
            resultados[estado] = resultados.get(estado, 0) + 1

            if estado == "ok":
                creditos[clave] = credito
                guardar_creditos(creditos)
                print(f"[{numero}/{total}] {nombre} -> OK {archivo} (origen: {origen})")
            elif estado == "existe":
                print(f"[{numero}/{total}] {nombre} -> ya existe")
            elif estado == "sin foto":
                print(f"[{numero}/{total}] {nombre} -> sin foto")
            else:
                print(f"[{numero}/{total}] {nombre} -> fallo la descarga")

    print("\nResumen")
    print(f"  descargadas: {resultados.get('ok', 0)}")
    print(f"  ya existian: {resultados.get('existe', 0)}")
    print(
        "  sin foto:    "
        f"{resultados.get('sin foto', 0) + resultados.get('error', 0)}"
    )
    print(
        "\nLas fotos que falten se pueden agregar a mano en imagenes/ "
        "con el nombre marca_modelo.jpg"
    )

    return 0


if __name__ == "__main__":
    sys.exit(main())
