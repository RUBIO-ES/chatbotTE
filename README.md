# 🏍️ MotoGuía

Bot de Telegram con **catálogo de motocicletas**: fichas técnicas dinámicas, navegación por marca/categoría, búsqueda, comparador y mantenimiento básico.

---

## ✨ Características

| Función | Descripción |
|---------|-------------|
| 🏍️ Catálogo navegable | Marca → categoría → modelo → ficha, todo con botones |
| 📄 Fichas dinámicas | Solo se muestran los campos que tienen dato real, con indicador de cobertura |
| 🔎 Búsqueda inteligente | Coincidencia por palabras, errores de escritura y categorías ("scooter", "adventure") |
| ⚖️ Comparador | Contrasta dos motos campo por campo |
| 📊 Estadísticas | Referencias por marca y categoría, cobertura de datos |
| 🔧 Mantenimiento | Aceite, filtros, cadena/CVT e intervalos; completados con valores referenciales cuando el modelo no trae datos propios |
| 📷 Foto por modelo | Al abrir una ficha se envía la imagen de la moto con su atribución y debajo la ficha técnica |

El catálogo contiene **450 referencias de 34 marcas**. **150 modelos tienen ficha técnica con datos reales** (incluida la Yamaha MT-15); el resto se conserva como referencia y se completará agregando líneas en `datos_motos.py`.

---

## 📁 Estructura del proyecto

```
machine-learning-Bot-telegram/
├── bot.py                # Bot de Telegram: catálogo + menú + mantenimiento
├── datos_motos.py        # Datos técnicos reales (fuente única de verdad)
├── descargar_imagenes.py # Descarga fotos de referencia desde Wikipedia
├── limpieza.py           # Borra __pycache__ y archivos temporales
├── catalogo.json         # Catálogo generado (no editar a mano)
├── imagenes/             # Fotos por modelo + creditos.json
├── requirements.txt
├── .env                  # TELEGRAM_TOKEN (no se sube al repositorio)
└── README.md
```

`catalogo.json` se regenera al iniciar el bot mezclando `CATALOGO_BASE` (bot.py) con `datos_motos.py`. Los modelos nuevos agregados a `CATALOGO_BASE` se incorporan automáticamente sin perder lo que ya exista en el catálogo.

---

## ⚙️ Instalación

```bash
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt
```

### Configuración del token

Crea un archivo `.env` en la misma carpeta:

```
TELEGRAM_TOKEN=tu_token_de_botfather
```

El token se obtiene en Telegram con [@BotFather](https://t.me/BotFather) → `/newbot`.

### Ejecutar

```bash
python bot.py
```

Al iniciar se imprimen las referencias cargadas, cuántas tienen ficha técnica y cuántas fotos hay en `imagenes/`.

Antes de arrancar, el bot consulta `getMe` con 30 segundos de espera. Si no hay red, muestra un diagnóstico en vez de una traza de error.

---

## 📷 Fotos de las motos

Al elegir un modelo, el bot envía la foto como imagen con un pie corto (marca, modelo, categoría y datos clave) y después la ficha técnica completa. En las listas, `📷` marca los modelos con foto, `✅` los que tienen ficha técnica y `▫️` los que solo son referencia. Si un modelo no tiene foto, la ficha indica `📷 Foto: no disponible para este modelo.`

Para descargar las fotos de referencia de todos los modelos con datos:

```bash
python descargar_imagenes.py
```

Opciones:

```bash
python descargar_imagenes.py --limite 10        # solo 10 modelos
python descargar_imagenes.py --marca Yamaha     # solo una marca
python descargar_imagenes.py --solo "Yamaha YZF-R1"
python descargar_imagenes.py --forzar           # reemplaza fotos existentes
python descargar_imagenes.py --todo             # intenta las 450 referencias
```

El script busca el artículo del modelo en Wikipedia (español e inglés), valida que el título corresponda y descarga la imagen principal en `imagenes/`. La atribución (autor y licencia) queda en `imagenes/creditos.json` y el bot la muestra en el pie de la foto.

### Limpiar temporales

```bash
python limpieza.py            # borra __pycache__, .pyc, .pyo, .tmp, .bak y .old
python limpieza.py --simular  # muestra qué borraría sin tocar nada
```

No modifica `catalogo.json`, `imagenes/`, `.env` ni el código fuente.

### Agregar una foto manualmente

Dos formas:

1. **Archivo local**: guarda la imagen como `imagenes/marca_modelo.jpg` (sin tildes, todo en minúsculas y separado por `_`). Ejemplo: `imagenes/honda_xr190l.jpg`.
2. **URL en los datos**:

```python
"Honda|XR190L": dict(
    cc=184,
    imagen="https://ejemplo.com/xr190l.jpg",
    imagen_credito="Foto: Autor · Licencia",
),
```

Extensiones admitidas: `.jpg`, `.jpeg`, `.png`, `.webp`. Si un modelo no tiene foto, la ficha se envía igual, solo que sin imagen.

---

## 🎯 Uso

### Menú principal

- **🏍️ Catálogo**: navegación con botones. El número indica referencias por marca; ✅ marca los modelos con ficha completa.
- **🔎 Buscar**: escribe marca y modelo.
- **📚 Categorías**: descripción de los tipos de moto.
- **🔧 Mantenimiento**: datos de servicio de un modelo.
- **⚖️ Comparar**: dos motos separadas por `|`.
- **📊 Estadísticas**: cobertura del catálogo.

### Comandos

| Comando | Ejemplo | Qué hace |
|---------|---------|----------|
| `/start` | `/start` | Bienvenida y menú |
| `/menu` | `/menu` | Menú principal |
| `/catalogo` | `/catalogo` | Navegador de marcas |
| `/marcas` | `/marcas` | Marcas con cantidad de modelos |
| `/modelos` | `/modelos Yamaha` | Modelos de una marca |
| `/tipos` | `/tipos` | Categorías de motocicletas |
| `/buscar` | `/buscar Yamaha R1` | Ficha de una moto |
| `/mantenimiento` | `/mantenimiento Yamaha FZ25` | Datos de mantenimiento |
| `/comparar` | `/comparar Yamaha MT-07 \| Kawasaki Z650` | Comparación |
| `/estadisticas` | `/estadisticas` | Cobertura y conteos |
| `/motos` | `/motos` | Vuelve al modo catálogo |

También puedes escribir directamente un modelo (`Yamaha R1`) sin comando.

---

## ➕ Cómo agregar o completar una moto

Todo se edita en `datos_motos.py`. La clave debe coincidir con `Marca|Modelo` del catálogo:

```python
"Marca|Modelo": dict(
    cc=249, hp=20.8, rpm=8000, nm=20.1, rpm_nm=6000,
    kg=151, tanque=14, asiento=795, vel=5,
    abs=True, precio=12990000, vmax=130, consumo=38,
    tipo="4T, SOHC, monocilíndrico, 2V",
    freno_d="Disco Ø282 mm", freno_t="Disco Ø220 mm",
    extra={
        "suspension": {"delantera": "...", "trasera": "..."},
        "mantenimiento": {"aceite_recomendado": "...",
                          "cantidad_aceite_l": 1.0,
                          "intervalos": ["Cada 6.000 km"]},
    },
),
```

Notación corta disponible: `cc, hp, rpm, nm, rpm_nm, kg, tanque, asiento, vel, abs, abs_doble, cbs, tc, precio, vmax, consumo, anio, estado, version, tipo, cil, refrig, alim, comp, arranque, freno_d, freno_t, llanta_d, llanta_t, rines`, más `imagen` e `imagen_credito`.

Cualquier campo que no escribas aparece simplemente como ausente en la ficha; no se inventan valores. La excepción es **mantenimiento**: si el modelo no trae datos propios, el bot completa aceite, filtros, cadena/CVT e intervalos con valores referenciales según categoría, cilindrada y refrigeración. Esos valores se muestran siempre con la advertencia de confirmarlos en el manual; si escribes datos reales en `datos_motos.py`, estos tienen prioridad.

Para que una moto nueva exista primero en el catálogo, agrégala a `CATALOGO_BASE` en `bot.py` (el catálogo se sincroniza al iniciar) y luego completa su ficha en `datos_motos.py`.

---

## 🌐 Si el bot no conecta (`TimedOut`)

`telegram.error.TimedOut` o `httpx.ConnectTimeout` significan que el programa no logró hablar con `api.telegram.org` a tiempo; casi nunca es un error del código.

El bot ya usa 30 segundos de timeout (el valor por defecto de la librería es 5), hace una comprobación previa y, si falla, reintenta forzando IPv4 (en algunas redes la ruta IPv6 se queda colgada). Si aun así falla:

1. Abre <https://web.telegram.org> en el navegador para confirmar que hay internet.
2. Desactiva VPN o proxy, o define `HTTPS_PROXY` si tu red los exige.
3. Permite `python.exe` en el firewall o antivirus.
4. Prueba con datos móviles para descartar al proveedor de internet.
5. Comprueba que el reloj de Windows esté en hora automática.

---

## ⚠️ Notas de seguridad

- No compartas el token ni lo escribas en archivos que se suban a Git.
- `.gitignore` excluye `.env` y `venv`.
- Si un token ya se publicó, revócalo en [@BotFather](https://t.me/BotFather) y genera uno nuevo.

---

## 📊 Datos y fuentes

Las especificaciones provienen de fichas de fabricante e importadores. Los precios son aproximados, de referencia del mercado colombiano (fecha de revisión: 2026-11), y pueden variar por año, versión y concesionario. La ficha indica siempre su fuente y su cobertura para que el usuario sepa qué está verificado.
