"""Borra archivos temporales del proyecto sin tocar catalogo, fotos ni configuracion."""

import argparse
import shutil
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CARPETAS_TEMP = {"__pycache__"}
EXTENSIONES_TEMP = {".pyc", ".pyo", ".tmp", ".bak", ".old"}
CARPETAS_PROTEGIDAS = {".git", "imagenes", "venv", ".venv"}


def tamano_legible(bytes_):
    for unidad in ("B", "KB", "MB", "GB"):
        if bytes_ < 1024 or unidad == "GB":
            return f"{bytes_:.1f} {unidad}" if unidad != "B" else f"{int(bytes_)} B"
        bytes_ /= 1024


def tamano(ruta):
    if ruta.is_dir():
        return sum(archivo.stat().st_size for archivo in ruta.rglob("*") if archivo.is_file())
    return ruta.stat().st_size


def recolectar():
    carpetas = []
    archivos = []
    for ruta in BASE_DIR.rglob("*"):
        partes = set(ruta.relative_to(BASE_DIR).parts)
        if partes & CARPETAS_PROTEGIDAS:
            continue
        if ruta.is_dir() and ruta.name in CARPETAS_TEMP:
            carpetas.append(ruta)
        elif (
            ruta.is_file()
            and ruta.suffix.lower() in EXTENSIONES_TEMP
            and not (partes & CARPETAS_TEMP)
        ):
            archivos.append(ruta)
    return archivos, carpetas


def limpiar(dry_run=False):
    archivos, carpetas = recolectar()

    if not archivos and not carpetas:
        print("✨ No hay nada que limpiar: el proyecto está ordenado.")
        return 0

    total = 0
    fallos = 0

    for archivo in archivos:
        tam = tamano(archivo)
        total += tam
        relativa = archivo.relative_to(BASE_DIR)
        if dry_run:
            print(f"  [simulación] archivo: {relativa} ({tamano_legible(tam)})")
            continue
        try:
            archivo.unlink()
            print(f"  🗑️  {relativa} ({tamano_legible(tam)})")
        except OSError as error:
            fallos += 1
            print(f"  ⚠️  No se pudo borrar {relativa}: {error}")

    for carpeta in sorted(carpetas, key=lambda r: len(r.parts), reverse=True):
        tam = tamano(carpeta)
        total += tam
        relativa = carpeta.relative_to(BASE_DIR)
        if dry_run:
            print(f"  [simulación] carpeta: {relativa}/ ({tamano_legible(tam)})")
            continue
        try:
            shutil.rmtree(carpeta)
            print(f"  🗑️  {relativa}/ ({tamano_legible(tam)})")
        except OSError as error:
            fallos += 1
            print(f"  ⚠️  No se pudo borrar {relativa}/: {error}")

    verbo = "Se liberarían" if dry_run else "Liberados"
    icono = "🔍" if dry_run else "🧹"
    print(f"\n{icono} {verbo} {tamano_legible(total)} en total.")
    if fallos:
        print(f"⚠️  {fallos} elemento(s) no se pudieron borrar (puede que estén en uso).")
        return 1
    if dry_run:
        print("Ejecuta sin --simular para borrarlos de verdad.")
    return 0


def main():
    for salida in (sys.stdout, sys.stderr):
        try:
            salida.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

    parser = argparse.ArgumentParser(description="Limpia archivos temporales del proyecto.")
    parser.add_argument(
        "--simular",
        action="store_true",
        help="Muestra lo que se borraría sin borrar nada.",
    )
    argumentos = parser.parse_args()
    raise SystemExit(limpiar(dry_run=argumentos.simular))


if __name__ == "__main__":
    main()
