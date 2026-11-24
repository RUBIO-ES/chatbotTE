
import os
import re
import sys
import json
import socket
import unicodedata
from pathlib import Path
from difflib import get_close_matches, SequenceMatcher

from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters
)

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

TOKEN = (os.getenv("TELEGRAM_TOKEN") or "").strip()
ARCHIVO = BASE_DIR / "catalogo.json"
CARPETA_IMAGENES = BASE_DIR / "imagenes"
EXTENSIONES_IMAGEN = (".jpg", ".jpeg", ".png", ".webp")
TIMEOUT_RED = 30
TIMEOUT_CONEXION = 15

try:
    from datos_motos import DATOS as DATOS_TECNICOS
except ImportError:
    DATOS_TECNICOS = {}

# ============================================================
# 1. TIPOS DE MOTOCICLETAS
# ============================================================

TIPOS = {
    "Deportiva": "Motos deportivas y supersport",
    "Superbike": "Deportivas de altas prestaciones",
    "Naked": "Motos sin carenado completo",
    "Street": "Motos urbanas",
    "Doble propósito": "Ciudad y terrenos variados",
    "Adventure": "Viajes y aventura",
    "Touring": "Viajes de larga distancia",
    "Sport Touring": "Deportiva para viajes",
    "Enduro": "Uso todoterreno",
    "Motocross": "Uso deportivo en circuitos de tierra",
    "Trial": "Pruebas de equilibrio y obstáculos",
    "Supermoto": "Uso mixto con configuración supermotard",
    "Scooter": "Motonetas automáticas",
    "Maxi Scooter": "Scooters de mayor cilindrada",
    "Cruiser": "Estilo clásico de carretera",
    "Chopper": "Estilo personalizado",
    "Bobber": "Estilo clásico minimalista",
    "Café Racer": "Estilo deportivo clásico",
    "Scrambler": "Estilo clásico de uso mixto",
    "Clásica": "Motocicletas de diseño tradicional",
    "Urbana": "Transporte diario",
    "Semiautomática": "Transmisión semiautomática",
    "CUB": "Motocicletas compactas",
    "Underbone": "Diseño urbano de chasis inferior",
    "Eléctrica": "Motor eléctrico",
    "Cuatrimoto": "Vehículo de cuatro ruedas"
}

# ============================================================
# 2. CATÁLOGO DE MARCAS Y MODELOS
# ============================================================

CATALOGO_BASE = {
    "Yamaha": {
        "Deportiva": [
            "YZF-R1", "YZF-R1M", "YZF-R6", "YZF-R7",
            "YZF-R3", "YZF-R15", "YZF-R125"
        ],
        "Naked": [
            "MT-01", "MT-03", "MT-07", "MT-09",
            "MT-09 SP", "MT-10", "MT-15", "MT-125",
            "FZ16", "FZ25", "FZ-S", "FZ-X"
        ],
        "Doble propósito": [
            "XTZ125", "XTZ150", "XTZ250", "XTZ660",
            "Ténéré 700", "Ténéré 700 World Raid",
            "WR155R", "WR250R", "WR450F"
        ],
        "Scooter": [
            "NMAX 125", "NMAX 155", "XMAX 250",
            "XMAX 300", "TMAX", "Ray ZR", "Aerox"
        ],
        "Urbana": [
            "Crypton FI", "YBR125", "SZ-RR",
            "FZ-S FI", "Libero 125", "YCZ110"
        ],
        "Touring": ["Tracer 7", "Tracer 9", "FJR1300"],
        "Cruiser": ["Bolt", "V Star 250", "Star Venture"]
    },

    "Honda": {
        "Deportiva": [
            "CBR125R", "CBR150R", "CBR250RR",
            "CBR300R", "CBR500R", "CBR600RR",
            "CBR650R", "CBR1000RR-R Fireblade"
        ],
        "Naked": [
            "CB125F", "CB150R", "CB300R",
            "CB500F", "CB650R", "CB750 Hornet",
            "CB1000 Hornet"
        ],
        "Doble propósito": [
            "XR125L", "XR150L", "XR190L",
            "XRE190", "XRE300", "CRF150L",
            "CRF250L", "CRF300L", "CRF450L"
        ],
        "Adventure": [
            "NX500", "Transalp XL750",
            "Africa Twin CRF1100L",
            "CRF1100L Adventure Sports"
        ],
        "Scooter": [
            "Dio", "PCX125", "PCX160",
            "ADV160", "Forza 350", "X-ADV"
        ],
        "Urbana": ["Wave 110", "CB125F", "Biz 125"],
        "Touring": ["Gold Wing", "NT1100"],
        "Cruiser": ["Rebel 300", "Rebel 500", "Rebel 1100"]
    },

    "Kawasaki": {
        "Deportiva": [
            "Ninja 125", "Ninja 250", "Ninja 300",
            "Ninja 400", "Ninja 500", "Ninja 650",
            "Ninja ZX-4R", "Ninja ZX-6R",
            "Ninja ZX-10R", "Ninja ZX-10RR",
            "Ninja H2", "Ninja H2R", "Ninja 7 Hybrid"
        ],
        "Naked": [
            "Z125", "Z250", "Z300", "Z400",
            "Z500", "Z650", "Z750", "Z800",
            "Z900", "Z900RS", "Z1000",
            "Z H2", "Z H2 SE"
        ],
        "Adventure": [
            "Versys-X 300", "Versys 650",
            "Versys 1000", "KLE500"
        ],
        "Doble propósito": [
            "KLX110", "KLX140", "KLX230",
            "KLX250", "KLX300", "KLX450R",
            "KX85", "KX250", "KX450"
        ],
        "Touring": ["Concours 14", "Ninja 1000SX"],
        "Cruiser": ["Vulcan S", "Vulcan 900", "Vulcan 1700"]
    },

    "Suzuki": {
        "Deportiva": [
            "GSX-R125", "GSX-R150", "GSX-R600",
            "GSX-R750", "GSX-R1000R", "Hayabusa"
        ],
        "Naked": [
            "GSX-S125", "GSX-S150", "GSX-S750",
            "GSX-S950", "GSX-S1000", "GSX-8S",
            "Gixxer 150", "Gixxer 250"
        ],
        "Adventure": [
            "V-Strom 250", "V-Strom 650",
            "V-Strom 800", "V-Strom 1050"
        ],
        "Doble propósito": [
            "DR150", "DR200", "DR650",
            "DR-Z400", "DR-Z4S"
        ],
        "Urbana": ["GN125", "EN125", "AX100"],
        "Scooter": ["Burgman 125", "Burgman 200", "Burgman 400"],
        "Cruiser": ["Intruder 150", "Boulevard M109R"]
    },

    "Bajaj": {
        "Naked": [
            "Pulsar NS125", "Pulsar NS160",
            "Pulsar NS200", "Pulsar NS400Z"
        ],
        "Deportiva": [
            "Pulsar RS200", "Pulsar RS400"
        ],
        "Urbana": [
            "Boxer CT100", "Boxer BM150",
            "Boxer 150X", "CT125", "Platina 100",
            "Platina 110"
        ],
        "Touring": ["Dominar 250", "Dominar 400"],
        "Cruiser": ["Avenger 160", "Avenger 220"]
    },

    "AKT": {
        "Urbana": [
            "NKD 125", "NKD 125 EIII", "Special 110",
            "Dynamic K 125", "Dynamic Pro 125"
        ],
        "Naked": [
            "CR4 125", "CR4 162", "CR5 200",
            "TT DS 200", "TT 250"
        ],
        "Doble propósito": [
            "TTR 125", "TTR 180", "TTR 200",
            "TTR 200 Enduro"
        ],
        "Scooter": ["Dynamic Pro", "Jet 125", "Jet 150"]
    },

    "TVS": {
        "Deportiva": ["Apache RR 310", "Apache RTR 200"],
        "Naked": [
            "Apache RTR 160", "Apache RTR 160 4V",
            "Apache RTR 180", "Apache RTR 200 4V",
            "Ronin 225"
        ],
        "Urbana": ["Raider 125", "Sport 100", "Star City Plus"],
        "Scooter": ["Ntorq 125", "Jupiter 125", "Zest 110"],
        "Doble propósito": ["Apache RTX 300"]
    },

    "Hero": {
        "Naked": [
            "Hunk 125 R", "Hunk 160R", "Hunk 160R 4V",
            "Xtreme 160R", "Xtreme 200S"
        ],
        "Doble propósito": ["Xpulse 200", "Xpulse 200 4V"],
        "Urbana": [
            "Eco Deluxe", "Ignitor 125",
            "Splendor Plus", "Passion Pro"
        ],
        "Scooter": ["Destini 125", "Pleasure Plus"]
    },

    "Royal Enfield": {
        "Clásica": [
            "Classic 350", "Classic 500", "Bullet 350",
            "Bullet 500", "Hunter 350", "Meteor 350"
        ],
        "Adventure": [
            "Himalayan 411", "Himalayan 450",
            "Scram 411", "Scram 440"
        ],
        "Naked": ["Guerrilla 450"],
        "Café Racer": ["Continental GT 650"],
        "Cruiser": ["Super Meteor 650"],
        "Touring": ["Interceptor 650"]
    },

    "KTM": {
        "Naked": [
            "Duke 125", "Duke 200", "Duke 250",
            "Duke 390", "Duke 790", "Duke 890",
            "Duke 990", "1290 Super Duke R"
        ],
        "Deportiva": ["RC 125", "RC 200", "RC 390"],
        "Adventure": [
            "390 Adventure", "790 Adventure",
            "890 Adventure", "1290 Super Adventure"
        ],
        "Enduro": ["EXC 250", "EXC 300", "EXC 450", "EXC 500"],
        "Motocross": ["SX 125", "SX 250", "SX-F 450"]
    },

    "BMW Motorrad": {
        "Deportiva": ["S 1000 RR", "M 1000 RR"],
        "Naked": ["F 900 R", "R 12", "R 12 nineT"],
        "Adventure": [
            "G 310 GS", "F 750 GS", "F 800 GS",
            "F 850 GS", "F 900 GS", "R 1250 GS",
            "R 1300 GS", "R 1300 GS Adventure"
        ],
        "Touring": ["R 1250 RT", "R 1300 RT", "K 1600 GT"],
        "Scooter": ["C 400 GT", "CE 04"]
    },

    "Ducati": {
        "Deportiva": [
            "Panigale V2", "Panigale V4",
            "Panigale V4 R", "Superleggera V4"
        ],
        "Naked": [
            "Monster", "Monster SP", "Streetfighter V2",
            "Streetfighter V4"
        ],
        "Adventure": [
            "Multistrada V2", "Multistrada V4",
            "DesertX", "DesertX Rally"
        ],
        "Cruiser": ["Diavel V4", "XDiavel"],
        "Scrambler": ["Scrambler Icon", "Scrambler Full Throttle"]
    },

    "Triumph": {
        "Naked": ["Trident 660", "Street Triple 765", "Speed Triple 1200"],
        "Adventure": ["Tiger Sport 660", "Tiger 900", "Tiger 1200"],
        "Clásica": ["Bonneville T100", "Bonneville T120"],
        "Scrambler": ["Scrambler 400 X", "Scrambler 900", "Scrambler 1200"],
        "Cruiser": ["Bonneville Bobber", "Bonneville Speedmaster"],
        "Deportiva": ["Daytona 660"]
    },

    "Aprilia": {
        "Deportiva": ["RS 125", "RS 457", "RS 660", "RSV4"],
        "Naked": ["Tuono 125", "Tuono 660", "Tuono V4"],
        "Adventure": ["Tuareg 660"],
        "Scooter": ["SR GT 125", "SR GT 200"]
    },

    "Husqvarna": {
        "Naked": ["Svartpilen 125", "Svartpilen 250", "Svartpilen 401",
                  "Vitpilen 401"],
        "Adventure": ["Norden 901"],
        "Enduro": ["TE 250", "TE 300", "FE 350", "FE 450"],
        "Motocross": ["TC 125", "TC 250", "FC 250", "FC 450"]
    },

    "CFMOTO": {
        "Naked": ["150NK", "250NK", "300NK", "450NK", "650NK", "800NK"],
        "Deportiva": ["300SR", "450SR", "675SR-R"],
        "Adventure": ["450MT", "650MT", "700MT", "800MT"],
        "Cruiser": ["450CL-C", "700CL-X"]
    },

    "Benelli": {
        "Naked": ["TNT 125", "TNT 135", "TNT 150", "TNT 300", "TNT 600"],
        "Adventure": ["TRK 251", "TRK 502", "TRK 702", "TRK 800"],
        "Clásica": ["Leoncino 250", "Leoncino 500", "Imperiale 400"],
        "Cruiser": ["502C"]
    },

    "QJMotor": {
        "Naked": ["SRK 125", "SRK 400", "SRK 600", "SRK 800"],
        "Deportiva": ["SRK 400 RR", "SRK 800 RR"],
        "Adventure": ["SRT 550", "SRT 700", "SRT 800"],
        "Cruiser": ["SRV 300", "SRV 550"]
    },

    "Zontes": {
        "Naked": ["125 U", "350 R", "703 R"],
        "Adventure": ["310 T", "350 T", "703 F"],
        "Scooter": ["M310", "350 E", "368 G"],
        "Deportiva": ["350 GK"]
    },

    "Voge": {
        "Naked": ["300R", "500R", "525R", "800R"],
        "Adventure": ["300DS", "525DSX", "650DS", "800DS"],
        "Deportiva": ["300AC", "500AC"]
    },

    "Kove": {
        "Adventure": ["450 Rally", "510X", "800X", "800X Pro"],
        "Deportiva": ["450RR"],
        "Naked": ["500F"]
    },

    "Kymco": {
        "Scooter": [
            "Agility 125", "Agility 150", "Like 125",
            "Like 150", "X-Town 300", "AK 550",
            "Downtown 350"
        ]
    },

    "SYM": {
        "Scooter": [
            "Jet 14", "Jet X", "Symphony",
            "Cruisym 300", "Joymax Z"
        ]
    },

    "Piaggio": {
        "Scooter": ["Liberty 150", "Medley 150", "Beverly 300", "MP3 530"]
    },

    "Vespa": {
        "Scooter": ["Primavera 150", "Sprint 150", "GTS 300", "GTV 300"]
    },

    "NIU": {
        "Eléctrica": ["NQi", "MQi", "RQi", "FQi"]
    },

    "Super Soco": {
        "Eléctrica": ["TC", "TC Max", "TS", "CUx"]
    },

    "Starker": {
        "Eléctrica": ["Avanti", "Skuty", "E3"]
    },

    "Gogoro": {
        "Eléctrica": ["Viva", "Viva XL", "SuperSport"]
    },

    "Vento": {
        "Urbana": ["Crossmax", "Screamer", "Nitrox"],
        "Doble propósito": ["Crossmax 250"]
    },

    "Victory": {
        "Urbana": ["Bomber", "One", "Switch"],
        "Doble propósito": ["MRX 125", "MRX 150"]
    },

    "Bera": {
        "Urbana": ["BR 150", "SBR", "Socialista"],
        "Naked": ["RKV"]
    },

    "Fratelli": {
        "Urbana": ["Diversa 125", "Urban 150"]
    },

    "GasGas": {
        "Enduro": ["EC 250", "EC 300"],
        "Motocross": ["MC 125", "MC 250", "MC 450"]
    }
}

# ============================================================
# 3. FICHA TÉCNICA COMPLETA
# ============================================================

def ficha_vacia():
    return {
        "identificacion": {
            "marca": "",
            "modelo": "",
            "familia": "",
            "categoria": "",
            "anio": None,
            "version": "",
            "cilindrada_comercial": "",
            "pais_fabricacion": "",
            "estado_comercial": ""
        },
        "motor": {
            "tipo": "",
            "cilindrada_cc": None,
            "cilindros": None,
            "configuracion": "",
            "potencia_hp": None,
            "potencia_kw": None,
            "rpm_potencia": None,
            "torque_nm": None,
            "rpm_torque": None,
            "refrigeracion": "",
            "alimentacion": "",
            "combustible": "",
            "compresion": "",
            "diametro_mm": None,
            "carrera_mm": None,
            "valvulas": None,
            "distribucion": "",
            "lubricacion": "",
            "arranque": ""
        },
        "transmision": {
            "velocidades": None,
            "tipo_caja": "",
            "embrague": "",
            "transmision_final": "",
            "relaciones_caja": ""
        },
        "dimensiones": {
            "largo_mm": None,
            "ancho_mm": None,
            "alto_mm": None,
            "distancia_ejes_mm": None,
            "altura_asiento_mm": None,
            "altura_suelo_mm": None,
            "peso_seco_kg": None,
            "peso_operacion_kg": None,
            "capacidad_tanque_l": None,
            "capacidad_aceite_l": None,
            "capacidad_refrigerante_l": None,
            "carga_maxima_kg": None
        },
        "suspension": {
            "delantera": "",
            "trasera": "",
            "recorrido_delantero_mm": None,
            "recorrido_trasero_mm": None
        },
        "frenos": {
            "delantero": "",
            "trasero": "",
            "abs": None,
            "abs_doble_canal": None,
            "cbs": None,
            "control_traccion": None
        },
        "llantas": {
            "delantera": "",
            "trasera": "",
            "rines": "",
            "tipo": ""
        },
        "tecnologia": {
            "tablero": "",
            "iluminacion": "",
            "modos_conduccion": "",
            "quickshifter": None,
            "conectividad": "",
            "puerto_usb": None,
            "inmovilizador": None,
            "control_crucero": None
        },
        "rendimiento": {
            "velocidad_maxima_kmh": None,
            "aceleracion": "",
            "consumo_km_l": None,
            "autonomia_km": None
        },
        "mantenimiento": {
            "aceite_recomendado": "",
            "cantidad_aceite_l": None,
            "bujia": "",
            "filtro_aceite": "",
            "filtro_aire": "",
            "kit_arrastre": "",
            "intervalos": [],
            "repuestos": {
                "pastillas_delanteras_cop": None,
                "pastillas_traseras_cop": None,
                "kit_arrastre_cop": None,
                "llanta_delantera_cop": None,
                "llanta_trasera_cop": None,
                "bateria_cop": None,
                "filtro_aire_cop": None,
                "filtro_aceite_cop": None
            },
            "costo_servicio_cop": None
        },
        "comercial": {
            "precio_nuevo_cop": None,
            "precio_usado_cop": None,
            "garantia": "",
            "disponibilidad": "",
            "fuente": "",
            "fecha_verificacion": ""
        }
    }

# ============================================================
# 3.5 ESQUEMA DINÁMICO Y DATOS TÉCNICOS
# ============================================================

PAIS_MARCA = {
    "Yamaha": "Japón",
    "Honda": "Japón",
    "Kawasaki": "Japón",
    "Suzuki": "Japón",
    "Bajaj": "India",
    "AKT": "Colombia (ensamble)",
    "TVS": "India",
    "Hero": "India",
    "Royal Enfield": "India",
    "KTM": "Austria",
    "BMW Motorrad": "Alemania",
    "Ducati": "Italia",
    "Triumph": "Reino Unido",
    "Aprilia": "Italia",
    "Husqvarna": "Austria",
    "CFMOTO": "China",
    "Benelli": "China",
    "QJMotor": "China",
    "Zontes": "China",
    "Voge": "China",
    "Kove": "China",
    "Kymco": "Taiwán",
    "SYM": "Taiwán",
    "Piaggio": "Italia",
    "Vespa": "Italia",
    "NIU": "China",
    "Super Soco": "China",
    "Starker": "Colombia",
    "Gogoro": "Taiwán",
    "Vento": "México",
    "Victory": "Colombia",
    "Bera": "Colombia",
    "Fratelli": "Colombia",
    "GasGas": "Austria",
}

FUENTE_DATOS = "Fichas de fabricante e importadores (valores aproximados)"
FECHA_DATOS = "2026-11"

# Orden en el que se muestran las secciones de la ficha.
# (seccion, título, emoji, [(campo, etiqueta, unidad), ...])
ESQUEMA = [
    ("identificacion", "IDENTIFICACIÓN", "📌", [
        ("marca", "Marca", ""),
        ("modelo", "Modelo", ""),
        ("categoria", "Categoría", ""),
        ("anio", "Año de referencia", ""),
        ("version", "Versión", ""),
        ("cilindrada_comercial", "Cilindrada comercial", ""),
        ("pais_fabricacion", "País de fabricación", ""),
        ("estado_comercial", "Estado comercial", ""),
    ]),
    ("motor", "MOTOR", "⚙️", [
        ("tipo", "Tipo", ""),
        ("cilindrada_cc", "Cilindrada", "cc"),
        ("cilindros", "Cilindros", ""),
        ("configuracion", "Configuración", ""),
        ("potencia_hp", "Potencia", "HP"),
        ("potencia_kw", "Potencia en kW", "kW"),
        ("rpm_potencia", "RPM de potencia", "RPM"),
        ("torque_nm", "Torque", "Nm"),
        ("rpm_torque", "RPM de torque", "RPM"),
        ("refrigeracion", "Refrigeración", ""),
        ("alimentacion", "Alimentación", ""),
        ("combustible", "Combustible", ""),
        ("compresion", "Relación de compresión", ""),
        ("diametro_mm", "Diámetro", "mm"),
        ("valvulas", "Válvulas", ""),
        ("distribucion", "Distribución", ""),
        ("lubricacion", "Lubricación", ""),
        ("arranque", "Arranque", ""),
    ]),
    ("transmision", "TRANSMISIÓN", "🔀", [
        ("velocidades", "Velocidades", ""),
        ("tipo_caja", "Caja", ""),
        ("embrague", "Embrague", ""),
        ("transmision_final", "Transmisión final", ""),
        ("relaciones_caja", "Relaciones", ""),
    ]),
    ("dimensiones", "DIMENSIONES Y CAPACIDADES", "📐", [
        ("largo_mm", "Largo", "mm"),
        ("ancho_mm", "Ancho", "mm"),
        ("alto_mm", "Alto", "mm"),
        ("distancia_ejes_mm", "Distancia entre ejes", "mm"),
        ("altura_asiento_mm", "Altura del asiento", "mm"),
        ("altura_suelo_mm", "Altura libre al suelo", "mm"),
        ("peso_seco_kg", "Peso en seco", "kg"),
        ("peso_operacion_kg", "Peso en orden de marcha", "kg"),
        ("capacidad_tanque_l", "Capacidad del tanque", "L"),
        ("capacidad_aceite_l", "Aceite de motor", "L"),
        ("capacidad_refrigerante_l", "Refrigerante", "L"),
        ("carga_maxima_kg", "Carga máxima", "kg"),
    ]),
    ("suspension", "SUSPENSIÓN", "🔧", [
        ("delantera", "Delantera", ""),
        ("trasera", "Trasera", ""),
        ("recorrido_delantero_mm", "Recorrido delantero", "mm"),
        ("recorrido_trasero_mm", "Recorrido trasero", "mm"),
    ]),
    ("frenos", "FRENOS Y SEGURIDAD", "🛑", [
        ("delantero", "Freno delantero", ""),
        ("trasero", "Freno trasero", ""),
        ("abs", "ABS", ""),
        ("abs_doble_canal", "ABS doble canal", ""),
        ("cbs", "CBS (frenado combinado)", ""),
        ("control_traccion", "Control de tracción", ""),
    ]),
    ("llantas", "LLANTAS", "🛞", [
        ("delantera", "Delantera", ""),
        ("trasera", "Trasera", ""),
        ("rines", "Rines", ""),
        ("tipo", "Tipo", ""),
    ]),
    ("tecnologia", "TECNOLOGÍA", "📱", [
        ("tablero", "Tablero", ""),
        ("iluminacion", "Iluminación", ""),
        ("modos_conduccion", "Modos de conducción", ""),
        ("quickshifter", "Quickshifter", ""),
        ("conectividad", "Conectividad", ""),
        ("puerto_usb", "Puerto USB", ""),
        ("inmovilizador", "Inmovilizador", ""),
        ("control_crucero", "Control de crucero", ""),
    ]),
    ("rendimiento", "RENDIMIENTO", "🏁", [
        ("velocidad_maxima_kmh", "Velocidad máxima", "km/h"),
        ("aceleracion", "Aceleración", ""),
        ("consumo_km_l", "Consumo", "km/L"),
        ("autonomia_km", "Autonomía", "km"),
    ]),
    ("mantenimiento", "MANTENIMIENTO", "🧰", [
        ("aceite_recomendado", "Aceite recomendado", ""),
        ("cantidad_aceite_l", "Cantidad de aceite", "L"),
        ("bujia", "Bujía", ""),
        ("filtro_aceite", "Filtro de aceite", ""),
        ("filtro_aire", "Filtro de aire", ""),
        ("kit_arrastre", "Kit de arrastre", ""),
        ("intervalos", "Intervalos de servicio", ""),
        ("costo_servicio_cop", "Costo de servicio", "COP"),
    ]),
    ("comercial", "INFORMACIÓN COMERCIAL", "🏷️", [
        ("precio_nuevo_cop", "Precio nueva", "COP"),
        ("precio_usado_cop", "Precio usada", "COP"),
        ("garantia", "Garantía", ""),
        ("disponibilidad", "Disponibilidad", ""),
    ]),
]

ETIQUETAS_REPUESTO = {
    "pastillas_delanteras_cop": "Pastillas delanteras",
    "pastillas_traseras_cop": "Pastillas traseras",
    "kit_arrastre_cop": "Kit de arrastre",
    "llanta_delantera_cop": "Llanta delantera",
    "llanta_trasera_cop": "Llanta trasera",
    "bateria_cop": "Batería",
    "filtro_aire_cop": "Filtro de aire",
    "filtro_aceite_cop": "Filtro de aceite",
}


def tiene_dato(dato):
    """True si el valor debe mostrarse (False es un dato válido: 'No')."""
    if dato is None:
        return False
    if isinstance(dato, bool):
        return True
    if isinstance(dato, (int, float)):
        return True
    if isinstance(dato, (list, tuple, dict)):
        return len(dato) > 0
    return bool(str(dato).strip())


def aplicar_datos_tecnicos(motos):
    """Mezcla datos_motos.py sobre el catálogo y completa valores por defecto."""
    aplicados = 0

    for moto in motos:
        i = moto["identificacion"]
        datos = DATOS_TECNICOS.get(f"{i['marca']}|{i['modelo']}")

        if not datos:
            continue

        for seccion, campos in datos.items():
            if seccion in ("imagen", "imagen_credito"):
                moto[seccion] = campos
            elif seccion == "mantenimiento" and "repuestos" in campos:
                moto["mantenimiento"]["repuestos"].update(campos["repuestos"])
                resto = {k: v for k, v in campos.items() if k != "repuestos"}
                moto["mantenimiento"].update(resto)
            else:
                moto.setdefault(seccion, {}).update(campos)

        i["anio"] = i["anio"] or 2025
        i["pais_fabricacion"] = i["pais_fabricacion"] or PAIS_MARCA.get(i["marca"], "")
        i["estado_comercial"] = i["estado_comercial"] or "Disponible"

        motor = moto["motor"]
        if not i["cilindrada_comercial"] and motor["cilindrada_cc"]:
            i["cilindrada_comercial"] = f"{motor['cilindrada_cc']} cc"
        if not motor["potencia_kw"] and motor["potencia_hp"]:
            motor["potencia_kw"] = round(motor["potencia_hp"] * 0.7457, 1)

        comercial = moto["comercial"]
        comercial["fuente"] = comercial["fuente"] or FUENTE_DATOS
        comercial["fecha_verificacion"] = (
            comercial["fecha_verificacion"] or FECHA_DATOS
        )

        aplicados += 1

    return aplicados


def _texto_plano(texto):
    texto = unicodedata.normalize("NFD", str(texto).lower())
    return "".join(c for c in texto if unicodedata.category(c) != "Mn")


def _litros_aceite(cc):
    if not cc:
        return None
    for limite, litros in (
        (125, 0.8), (150, 0.9), (170, 1.0), (200, 1.1), (250, 1.3),
        (400, 1.8), (500, 2.0), (700, 2.4), (900, 3.0),
    ):
        if cc <= limite:
            return litros
    return 3.6


def mantenimiento_referencial(moto):
    """Mantenimiento orientativo para modelos que no traen datos propios."""
    i = moto["identificacion"]
    motor = moto["motor"]
    categoria = _texto_plano(i.get("categoria", ""))
    refrigeracion = _texto_plano(motor.get("refrigeracion", ""))
    electrica = "electrica" in categoria
    scooter = "scooter" in categoria
    offroad = (
        "enduro" in categoria
        or "motocross" in categoria
        or "doble proposito" in categoria
    )

    datos = {}

    if electrica:
        datos["aceite_recomendado"] = "No aplica: motor eléctrico sin aceite"
        datos["filtro_aire"] = "No aplica (motor eléctrico)"
        datos["kit_arrastre"] = (
            "Correa o cadena: revisar tensión cada 5.000 km"
        )
        datos["intervalos"] = [
            "1.000 km: revisión inicial (frenos, tornillería, neumáticos)",
            "Cada 5.000 km: revisar batería, frenos y presión de neumáticos",
            "Líquido de frenos: cambiar cada 2 años",
            "Valores referenciales: confirma con el manual del año y versión",
        ]
        return datos

    if scooter:
        datos["aceite_recomendado"] = (
            "10W-30 o 10W-40 JASO MB (según manual)"
        )
        datos["filtro_aceite"] = "Tamiz interno; limpiar cada 6.000 km"
        datos["kit_arrastre"] = (
            "CVT: revisar correa y rodillos a los 8.000 km; "
            "cambiar correa 16.000-20.000 km"
        )
    else:
        if "liquida" in refrigeracion:
            datos["aceite_recomendado"] = (
                "10W-40 JASO MA2 semisintético o sintético"
            )
        else:
            datos["aceite_recomendado"] = (
                "10W-40 o 20W-50 JASO MA2 (mineral o semisintético)"
            )
        datos["filtro_aceite"] = (
            "Cartucho o tamiz; revisar en cada cambio de aceite"
        )
        datos["kit_arrastre"] = (
            "Cadena con retenes (o cardán): lubricar cada 500 km; "
            "kit completo 20.000-25.000 km"
        )

    litros = _litros_aceite(motor.get("cilindrada_cc"))
    if litros:
        datos["cantidad_aceite_l"] = litros

    datos["bujia"] = "NGK o Denso equivalente según manual"

    if offroad:
        datos["filtro_aire"] = (
            "Espuma o seco; limpiar cada 2.000-3.000 km, cambiar 8.000 km"
        )
    else:
        datos["filtro_aire"] = (
            "Tipo seco; limpiar 6.000 km, cambiar 12.000 km"
        )

    if scooter:
        intervalos = [
            "1.000 km: revisión inicial (aceite, ajustes y frenos)",
            "Aceite de motor: cambiar cada 4.000 km",
            "Aceite de transmisión CVT: cambiar cada 12.000 km",
            "Filtro de aire: limpiar 6.000 km / cambiar 12.000 km",
            "Válvulas: revisar cada 12.000 km",
            "Líquido de frenos: cambiar cada 2 años",
        ]
    else:
        intervalos = ["1.000 km: revisión inicial (aceite, ajustes y frenos)"]
        if "liquida" in refrigeracion:
            intervalos.append("Aceite de motor: cambiar cada 6.000-8.000 km")
            intervalos.append(
                "Refrigerante: revisar 12.000 km / cambiar cada 2 años"
            )
        else:
            intervalos.append("Aceite de motor: cambiar cada 4.000-6.000 km")
        intervalos.append(
            "Filtro de aire: limpiar 2.000-3.000 km / cambiar 8.000 km"
            if offroad
            else "Filtro de aire: limpiar 6.000 km / cambiar 12.000 km"
        )
        intervalos.append(
            "Válvulas: revisar cada 4.000-6.000 km"
            if offroad
            else "Válvulas: revisar cada 6.000-12.000 km"
        )
        intervalos.append("Líquido de frenos: cambiar cada 2 años")

    intervalos.append(
        "Valores referenciales: confirma con el manual del año y versión"
    )
    datos["intervalos"] = intervalos

    return datos


def aplicar_mantenimiento_referencial(motos):
    """Completa los campos de mantenimiento vacíos; nunca sobrescribe datos."""
    rellenados = 0

    for moto in motos:
        motor = moto["motor"]
        if not any(
            tiene_dato(motor.get(campo))
            for campo in ("cilindrada_cc", "potencia_hp", "potencia_kw")
        ):
            continue

        i = moto["identificacion"]
        explicitos = (
            DATOS_TECNICOS.get(f"{i['marca']}|{i['modelo']}", {}).get(
                "mantenimiento", {}
            )
        )
        mantenimiento = moto["mantenimiento"]

        for campo, dato in mantenimiento_referencial(moto).items():
            if dato is None:
                continue
            if tiene_dato(explicitos.get(campo)):
                continue
            mantenimiento[campo] = dato
            rellenados += 1

    return rellenados


# ============================================================
# 4. CREACIÓN AUTOMÁTICA DEL CATÁLOGO
# ============================================================

def crear_catalogo():
    motos = []

    for marca, categorias in CATALOGO_BASE.items():
        for categoria, modelos in categorias.items():
            for modelo in modelos:
                ficha = ficha_vacia()

                ficha["identificacion"].update({
                    "marca": marca,
                    "modelo": modelo,
                    "familia": modelo.split()[0],
                    "categoria": categoria
                })

                motos.append(ficha)

    return motos


def sincronizar_catalogo(motos):
    """Agrega modelos nuevos de CATALOGO_BASE sin alterar los existentes."""
    existentes = {
        (moto["identificacion"]["marca"], moto["identificacion"]["modelo"])
        for moto in motos
    }
    nuevas = 0

    for marca, categorias in CATALOGO_BASE.items():
        for categoria, modelos in categorias.items():
            for modelo in modelos:
                if (marca, modelo) in existentes:
                    continue

                ficha = ficha_vacia()
                ficha["identificacion"].update({
                    "marca": marca,
                    "modelo": modelo,
                    "familia": modelo.split()[0],
                    "categoria": categoria,
                })
                motos.append(ficha)
                existentes.add((marca, modelo))
                nuevas += 1

    return nuevas


def cargar_catalogo():
    datos = None

    if ARCHIVO.exists():
        try:
            with open(ARCHIVO, "r", encoding="utf-8") as archivo:
                contenido = json.load(archivo)

            if isinstance(contenido, list):
                datos = contenido

        except (json.JSONDecodeError, OSError):
            pass

    if datos is None:
        datos = crear_catalogo()

    nuevas = sincronizar_catalogo(datos)
    if nuevas:
        print(f"➕ {nuevas} modelo(s) nuevos agregados al catálogo.")

    guardar_catalogo(datos)
    return datos


def guardar_catalogo(datos):
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


MOTOS = cargar_catalogo()
MOTOS_CON_DATOS = aplicar_datos_tecnicos(MOTOS)
aplicar_mantenimiento_referencial(MOTOS)
guardar_catalogo(MOTOS)

MARCAS_ORDENADAS = sorted(CATALOGO_BASE)

# marca -> categoría -> [índices globales dentro de MOTOS]
MOTOS_POR_MARCA = {}
for _indice, _moto in enumerate(MOTOS):
    _i = _moto["identificacion"]
    MOTOS_POR_MARCA.setdefault(_i["marca"], {}).setdefault(
        _i["categoria"], []
    ).append(_indice)

# ============================================================
# 5. FUNCIONES DE BÚSQUEDA
# ============================================================

def normalizar(texto):
    texto = str(texto).lower().strip()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(
        c for c in texto if unicodedata.category(c) != "Mn"
    )
    return re.sub(r"[^a-z0-9 ]", " ", texto)


def nombre_completo(moto):
    i = moto["identificacion"]
    return normalizar(f"{i['marca']} {i['modelo']}")


def moto_con_datos(moto):
    motor = moto["motor"]
    return any(
        tiene_dato(motor.get(campo))
        for campo in ("cilindrada_cc", "potencia_hp", "potencia_kw")
    )


def puntaje_busqueda(moto, consulta, tokens):
    """Puntaje alto = mejor coincidencia (se ordena descendente)."""
    nombre = nombre_completo(moto)
    palabras = nombre.split()

    puntos = 10 * sum(1 for token in tokens if token in palabras)

    if consulta in nombre:
        puntos += 5

    modelo = normalizar(moto["identificacion"]["modelo"])
    if nombre.endswith(consulta) or modelo == consulta:
        puntos += 20

    puntos += 10 * SequenceMatcher(None, consulta, nombre).ratio()

    if moto_con_datos(moto):
        puntos += 2

    return puntos


def buscar_moto(texto):
    consulta = normalizar(texto)
    tokens = [t for t in consulta.split() if t]

    if not tokens:
        return []

    # Si escribe exactamente una categoría, se listan sus modelos
    for categoria in TIPOS:
        if normalizar(categoria) == consulta:
            resultados = [
                moto for moto in MOTOS
                if moto["identificacion"]["categoria"] == categoria
            ]
            resultados.sort(
                key=lambda m: (not moto_con_datos(m), nombre_completo(m))
            )
            return resultados[:15]

    # 1. Coincidencia de todas las palabras con "marca modelo"
    resultados = [
        moto for moto in MOTOS
        if all(token in nombre_completo(moto) for token in tokens)
    ]

    # 2. Coincidencia aproximada (errores de escritura)
    if not resultados:
        nombres = [nombre_completo(moto) for moto in MOTOS]
        coincidencias = get_close_matches(
            consulta, nombres, n=8, cutoff=0.6
        )
        resultados = [
            moto for moto, nombre in zip(MOTOS, nombres)
            if nombre in coincidencias
        ]

    # 3. Búsqueda por categoría (ej. "scooter", "adventure")
    if not resultados:
        for categoria in TIPOS:
            clave = normalizar(categoria)
            if clave in consulta or consulta in clave:
                resultados = [
                    moto for moto in MOTOS
                    if moto["identificacion"]["categoria"] == categoria
                ]
                break

    resultados.sort(
        key=lambda moto: puntaje_busqueda(moto, consulta, tokens),
        reverse=True
    )

    return resultados[:15]


def valor(dato, unidad=""):
    if not tiene_dato(dato):
        return "No verificado"

    if isinstance(dato, bool):
        return "Sí" if dato else "No"

    if isinstance(dato, (list, tuple)):
        return ", ".join(map(str, dato))

    if isinstance(dato, float) and dato.is_integer():
        dato = int(dato)

    if unidad == "COP" and isinstance(dato, (int, float)):
        return "$" + f"{dato:,.0f}".replace(",", ".") + " COP"

    return f"{dato} {unidad}".strip()


# ============================================================
# 6. CONSTRUIR LA FICHA PARA TELEGRAM
# ============================================================

def calcular_cobertura(moto):
    """Cuenta cuántos campos de la ficha tienen dato real."""
    llenos = 0
    total = 0

    for seccion, _, _, campos in ESQUEMA:
        for campo, _, _ in campos:
            total += 1
            if tiene_dato(moto[seccion].get(campo)):
                llenos += 1

    repuestos = moto["mantenimiento"].get("repuestos", {})
    total += len(repuestos)
    llenos += sum(1 for precio in repuestos.values() if tiene_dato(precio))

    porcentaje = round(llenos / total * 100) if total else 0
    return llenos, total, porcentaje


def construir_ficha(moto):
    i = moto["identificacion"]
    m = moto["motor"]
    d = moto["dimensiones"]

    resumen = [
        str(i["categoria"]),
        f"{m['cilindrada_cc']} cc" if tiene_dato(m["cilindrada_cc"]) else "",
        f"{valor(m['potencia_hp'])} HP" if tiene_dato(m["potencia_hp"]) else "",
        f"{valor(m['torque_nm'])} Nm" if tiene_dato(m["torque_nm"]) else "",
        f"{valor(d['peso_operacion_kg'])} kg" if tiene_dato(d["peso_operacion_kg"]) else "",
        f"Tanque {valor(d['capacidad_tanque_l'])} L" if tiene_dato(d["capacidad_tanque_l"]) else "",
    ]
    resumen = [dato for dato in resumen if dato]

    lineas = [
        "🏍️ FICHA TÉCNICA",
        "",
        f"{i['marca']} {i['modelo']}".strip(),
    ]

    if resumen:
        lineas += ["", " · ".join(resumen)]

    for seccion, titulo, icono, campos in ESQUEMA:
        bloque = []

        for campo, etiqueta, unidad in campos:
            dato = moto[seccion].get(campo)
            if tiene_dato(dato):
                bloque.append(f"{etiqueta}: {valor(dato, unidad)}")

        if seccion == "mantenimiento":
            repuestos = moto["mantenimiento"].get("repuestos", {})
            bloque_repuestos = [
                f"{ETIQUETAS_REPUESTO.get(clave, clave.replace('_', ' ').capitalize())}: "
                f"{valor(precio, 'COP')}"
                for clave, precio in repuestos.items()
                if tiene_dato(precio)
            ]
            if bloque_repuestos:
                bloque += ["", "💰 Repuestos:"] + bloque_repuestos

        if bloque:
            lineas += ["", f"{icono} {titulo}"] + bloque

    if imagen_de(moto)[0] is None:
        lineas += ["", "📷 Foto: no disponible para este modelo."]

    llenos, total, porcentaje = calcular_cobertura(moto)
    lineas += ["", f"📊 Cobertura de la ficha: {llenos}/{total} campos ({porcentaje}%)"]

    comercial = moto["comercial"]
    if comercial.get("fuente"):
        fecha = comercial.get("fecha_verificacion")
        lineas.append(
            f"Fuente: {comercial['fuente']}" + (f" · {fecha}" if fecha else "")
        )

    if porcentaje < 100:
        lineas += [
            "",
            "ℹ️ La ficha muestra solo los datos disponibles. "
            "Confirma año y versión con el fabricante antes de decidir.",
        ]

    return "\n".join(lineas)


# ============================================================
# 7. ENVÍO DE FICHAS POR PARTES
# ============================================================

async def enviar_texto_a(mensaje, texto):
    """Envía un texto largo respetando el límite de Telegram."""
    limite = 3800

    for inicio in range(0, len(texto), limite):
        await mensaje.reply_text(texto[inicio:inicio + limite])


async def enviar_texto(update, texto):
    await enviar_texto_a(update.message, texto)


# ============================================================
# 7.1 IMAGEN DE LA MOTO
# ============================================================

def _cargar_creditos():
    archivo = CARPETA_IMAGENES / "creditos.json"
    if not archivo.exists():
        return {}

    try:
        with open(archivo, "r", encoding="utf-8") as datos:
            contenido = json.load(datos)
        return contenido if isinstance(contenido, dict) else {}
    except (OSError, json.JSONDecodeError):
        return {}


CREDITOS_IMAGENES = _cargar_creditos()


def clave_imagen(texto):
    """Normaliza 'Yamaha YZF-R1' al nombre de archivo 'yamaha_yzf_r1'."""
    limpio = unicodedata.normalize("NFD", str(texto).lower())
    limpio = "".join(c for c in limpio if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]+", "_", limpio).strip("_")


def imagen_de(moto):
    """Devuelve (origen, crédito). origen es None si no hay imagen."""
    i = moto["identificacion"]
    credito = moto.get("imagen_credito") or CREDITOS_IMAGENES.get(
        f"{i['marca']}|{i['modelo']}", ""
    )

    propia = moto.get("imagen")
    if tiene_dato(propia):
        return propia, credito

    base = clave_imagen(f"{i['marca']} {i['modelo']}")
    for extension in EXTENSIONES_IMAGEN:
        ruta = CARPETA_IMAGENES / f"{base}{extension}"
        if ruta.exists():
            return ruta, credito

    return None, ""


def pie_de_foto(moto, credito=""):
    i = moto["identificacion"]
    m = moto["motor"]

    resumen = [str(i["categoria"])]
    if tiene_dato(m["cilindrada_cc"]):
        resumen.append(f"{m['cilindrada_cc']} cc")
    if tiene_dato(m["potencia_hp"]):
        resumen.append(f"{valor(m['potencia_hp'])} HP")
    if tiene_dato(m["torque_nm"]):
        resumen.append(f"{valor(m['torque_nm'])} Nm")

    texto = f"🏍️ {i['marca']} {i['modelo']}\n" + " · ".join(resumen)
    if credito:
        texto += f"\n📷 {credito}"

    return texto[:1000]


async def enviar_ficha(mensaje, moto):
    """Envía la foto de la moto (si existe) y debajo la ficha técnica."""
    origen, credito = imagen_de(moto)
    i = moto["identificacion"]

    if origen is not None:
        try:
            # telegram deja que la propia librería abra el Path y detecte el tipo
            await mensaje.reply_photo(
                photo=origen,
                caption=pie_de_foto(moto, credito)
            )
            print(f"📷 Foto enviada: {i['marca']} {i['modelo']}")
        except Exception as error:
            print(
                f"⚠️ No se pudo enviar la imagen de "
                f"{i['marca']} {i['modelo']}: {error}"
            )
    else:
        print(f"▫️ Sin foto: {i['marca']} {i['modelo']}")

    await enviar_texto_a(mensaje, construir_ficha(moto))


# ============================================================
# 8. MENÚ PRINCIPAL
# ============================================================

def teclado_principal():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🏍️ Catálogo", callback_data="catalogo"),
            InlineKeyboardButton("🔎 Buscar", callback_data="buscar")
        ],
        [
            InlineKeyboardButton("📚 Categorías", callback_data="tipos"),
            InlineKeyboardButton("🔧 Mantenimiento", callback_data="mantenimiento")
        ],
        [
            InlineKeyboardButton("⚖️ Comparar motos", callback_data="comparar"),
            InlineKeyboardButton("📊 Estadísticas", callback_data="estadisticas")
        ],
        [
            InlineKeyboardButton("ℹ️ Ayuda", callback_data="ayuda")
        ]
    ])


def teclado_marcas():
    filas = []
    fila = []

    for indice, marca in enumerate(MARCAS_ORDENADAS):
        categorias = MOTOS_POR_MARCA.get(marca, {})
        cantidad = sum(len(lista) for lista in categorias.values())
        fila.append(
            InlineKeyboardButton(
                f"{marca} ({cantidad})",
                callback_data=f"marca:{indice}"
            )
        )
        if len(fila) == 2:
            filas.append(fila)
            fila = []

    if fila:
        filas.append(fila)

    filas.append([InlineKeyboardButton("⬅️ Menú", callback_data="menu")])
    return InlineKeyboardMarkup(filas)


def teclado_categorias(indice_marca):
    marca = MARCAS_ORDENADAS[indice_marca]
    categorias = sorted(MOTOS_POR_MARCA.get(marca, {}))

    filas = [
        [
            InlineKeyboardButton(
                f"{categoria} ({len(MOTOS_POR_MARCA[marca][categoria])})",
                callback_data=f"cat:{indice_marca}:{indice_categoria}"
            )
        ]
        for indice_categoria, categoria in enumerate(categorias)
    ]

    filas.append([InlineKeyboardButton("⬅️ Marcas", callback_data="catalogo")])
    return InlineKeyboardMarkup(filas)


def teclado_modelos(indice_marca, indice_categoria):
    marca = MARCAS_ORDENADAS[indice_marca]
    categoria = sorted(MOTOS_POR_MARCA[marca])[indice_categoria]
    indices = MOTOS_POR_MARCA[marca][categoria]

    filas = []

    for indice in indices:
        moto = MOTOS[indice]
        modelo = moto["identificacion"]["modelo"]
        if imagen_de(moto)[0] is not None:
            marca_icono = "📷 "
        elif moto_con_datos(moto):
            marca_icono = "✅ "
        else:
            marca_icono = "▫️ "
        filas.append([
            InlineKeyboardButton(
                f"{marca_icono}{modelo}",
                callback_data=f"mf:{indice}"
            )
        ])

    filas.append([
        InlineKeyboardButton(
            "⬅️ Categorías",
            callback_data=f"marca:{indice_marca}"
        )
    ])
    return InlineKeyboardMarkup(filas)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["modo"] = "motos"

    mensaje = (
        "🏍️ BIENVENIDO A MOTOGUÍA\n\n"
        f"Catálogo con {len(MOTOS)} referencias de "
        f"{len(MARCAS_ORDENADAS)} marcas. "
        f"{MOTOS_CON_DATOS} tienen ficha técnica con datos reales.\n\n"
        "• Toca 🏍️ Catálogo para navegar marca → categoría → modelo.\n"
        "• Escribe cualquier modelo para buscarlo directo.\n"
        "• 🔧 Mantenimiento muestra aceite, intervalos y repuestos.\n\n"
        "Selecciona una opción:"
    )

    await update.message.reply_text(
        mensaje,
        reply_markup=teclado_principal()
    )


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏍️ MENÚ PRINCIPAL",
        reply_markup=teclado_principal()
    )


async def catalogo(update, context):
    await update.message.reply_text(
        "🏷️ ELIGE UNA MARCA\n\n"
        "El número indica cuántas referencias tiene la marca.\n"
        "📷 = con foto · ✅ = con ficha técnica · ▫️ = solo referencia.",
        reply_markup=teclado_marcas()
    )


async def ayuda(update, context):
    texto = (
        "ℹ️ AYUDA DE MOTOGUÍA\n\n"
        "BOTONES\n"
        "🏍️ Catálogo: navega por marca, categoría y modelo.\n"
        "🔎 Buscar: escribe marca y modelo (ej. Yamaha R1).\n"
        "⚖️ Comparar: dos motos separadas por |.\n"
        "🔧 Mantenimiento: aceite, filtros, cadena y costos de repuestos.\n\n"
        "COMANDOS\n"
        "/start - Iniciar el bot\n"
        "/menu - Menú principal\n"
        "/catalogo - Navegador de marcas\n"
        "/marcas - Lista de marcas con cantidad de modelos\n"
        "/modelos Yamaha - Modelos de una marca\n"
        "/tipos - Categorías de motocicletas\n"
        "/buscar Yamaha R1 - Ficha de una moto\n"
        "/mantenimiento Yamaha R1 - Datos de mantenimiento\n"
        "/comparar Yamaha R1 | Kawasaki Z900 - Comparar dos motos\n"
        "/estadisticas - Cobertura del catálogo\n"
        "/motos - Volver al modo catálogo\n\n"
        "CONSEJO\n"
        "Puedes escribir el modelo directamente, sin comando."
    )

    await enviar_texto(update, texto)


# ============================================================
# 9. CONSULTAR MARCAS
# ============================================================

async def marcas(update, context):
    texto = "🏷️ MARCAS DISPONIBLES\n\n"

    for marca in sorted(CATALOGO_BASE):
        cantidad = sum(
            len(modelos)
            for modelos in CATALOGO_BASE[marca].values()
        )
        texto += f"• {marca}: {cantidad} referencias\n"

    await enviar_texto(update, texto)


# ============================================================
# 10. CONSULTAR MODELOS DE UNA MARCA
# ============================================================

async def modelos(update, context):
    if not context.args:
        await update.message.reply_text(
            "Uso: /modelos Yamaha"
        )
        return

    marca = " ".join(context.args)

    marca_real = next(
        (m for m in CATALOGO_BASE
         if normalizar(m) == normalizar(marca)),
        None
    )

    if not marca_real:
        await update.message.reply_text("Marca no encontrada.")
        return

    texto = f"🏍️ MODELOS DE {marca_real.upper()}\n\n"

    for categoria, lista in CATALOGO_BASE[marca_real].items():
        texto += f"\n📌 {categoria}\n"
        for modelo in lista:
            texto += f"• {modelo}\n"

    await enviar_texto(update, texto)


# ============================================================
# 11. CONSULTAR CATEGORÍAS
# ============================================================

async def tipos(update, context):
    texto = "📚 TIPOS DE MOTOCICLETAS\n\n"

    for tipo, descripcion in TIPOS.items():
        texto += f"🏍️ {tipo}\n{descripcion}\n\n"

    await enviar_texto(update, texto)


# ============================================================
# 12. BUSCADOR
# ============================================================

async def buscar(update, context):
    if not context.args:
        await update.message.reply_text(
            "Escribe la marca y el modelo.\n\n"
            "Ejemplos:\n"
            "/buscar Yamaha R1\n"
            "/buscar Kawasaki Ninja ZX-10R\n"
            "/buscar Honda XR190L"
        )
        return

    consulta = " ".join(context.args)
    resultados = buscar_moto(consulta)

    if not resultados:
        await update.message.reply_text(
            "No encontré esa motocicleta.\n"
            "Comprueba la escritura o consulta /marcas."
        )
        return

    if len(resultados) == 1:
        moto = resultados[0]
        await enviar_ficha(update.message, moto)
        return

    botones = []

    for indice, moto in enumerate(resultados):
        i = moto["identificacion"]
        botones.append([
            InlineKeyboardButton(
                f"{i['marca']} {i['modelo']}",
                callback_data=f"ficha:{indice}"
            )
        ])

    context.user_data["resultados"] = resultados

    await update.message.reply_text(
        "Encontré varias coincidencias. Selecciona una:",
        reply_markup=InlineKeyboardMarkup(botones)
    )


# ============================================================
# 13. MANTENIMIENTO
# ============================================================

async def mantenimiento(update, context):
    if not context.args:
        await update.message.reply_text(
            "Uso: /mantenimiento Yamaha FZ25\n\n"
            "También puedes abrir la ficha desde /catalogo."
        )
        return

    consulta = " ".join(context.args)
    resultados = buscar_moto(consulta)

    if not resultados:
        await update.message.reply_text("No encontré el modelo.")
        return

    moto = resultados[0]
    i = moto["identificacion"]
    m = moto["mantenimiento"]

    campos = [
        ("aceite_recomendado", "Aceite recomendado", ""),
        ("cantidad_aceite_l", "Cantidad de aceite", "L"),
        ("bujia", "Bujía", ""),
        ("filtro_aceite", "Filtro de aceite", ""),
        ("filtro_aire", "Filtro de aire", ""),
        ("kit_arrastre", "Kit de arrastre", ""),
        ("intervalos", "Intervalos", ""),
        ("costo_servicio_cop", "Costo de servicio", "COP"),
    ]

    datos = [
        f"{etiqueta}: {valor(m.get(campo), unidad)}"
        for campo, etiqueta, unidad in campos
        if tiene_dato(m.get(campo))
    ]

    repuestos = [
        f"{ETIQUETAS_REPUESTO.get(clave, clave.replace('_', ' ').capitalize())}: "
        f"{valor(precio, 'COP')}"
        for clave, precio in m.get("repuestos", {}).items()
        if tiene_dato(precio)
    ]

    if not datos and not repuestos:
        await update.message.reply_text(
            f"🔧 {i['marca']} {i['modelo']}\n\n"
            "Aún no hay datos de mantenimiento verificados para este modelo.\n"
            "Puedes ver la ficha técnica con /buscar."
        )
        return

    texto = [f"🔧 MANTENIMIENTO: {i['marca']} {i['modelo']}", ""]
    texto += datos

    if repuestos:
        texto += ["", "💰 Repuestos:"] + repuestos

    texto += [
        "",
        "Consulta el manual del año y versión correspondiente "
        "para confirmar los intervalos exactos.",
    ]

    await enviar_texto(update, "\n".join(texto))


# ============================================================
# 14. COMPARAR MOTOCICLETAS
# ============================================================

async def comparar(update, context):
    if not context.args:
        await update.message.reply_text(
            "Uso:\n"
            "/comparar Yamaha R1 | Kawasaki Ninja ZX-10R\n\n"
            "Separa las dos motos con el símbolo |"
        )
        return

    consulta = " ".join(context.args)
    partes = consulta.split("|")

    if len(partes) != 2:
        await update.message.reply_text(
            "Debes separar las motos con el símbolo |\n"
            "Ejemplo: /comparar Yamaha R1 | Kawasaki Z900"
        )
        return

    moto1 = buscar_moto(partes[0].strip())
    moto2 = buscar_moto(partes[1].strip())

    if not moto1 or not moto2:
        await update.message.reply_text(
            "No pude encontrar ambas motocicletas.\n"
            "Revisa la escritura o consulta /marcas."
        )
        return

    a = moto1[0]
    b = moto2[0]

    ia = a["identificacion"]
    ib = b["identificacion"]

    texto = (
        "⚖️ COMPARACIÓN DE MOTOCICLETAS\n\n"
        f"1. {ia['marca']} {ia['modelo']}\n"
        f"2. {ib['marca']} {ib['modelo']}"
    )

    for seccion, titulo, icono, campos in ESQUEMA:
        filas = []

        for campo, etiqueta, unidad in campos:
            if etiqueta in ("Marca", "Modelo", "Categoría"):
                continue

            valor1 = a[seccion].get(campo)
            valor2 = b[seccion].get(campo)

            if not tiene_dato(valor1) and not tiene_dato(valor2):
                continue

            filas.append(
                f"{etiqueta}: {valor(valor1, unidad)} | {valor(valor2, unidad)}"
            )

        if filas:
            texto += f"\n\n{icono} {titulo}\n" + "\n".join(filas)

    texto += (
        "\n\n📊 Cobertura: "
        f"{calcular_cobertura(a)[2]}% vs {calcular_cobertura(b)[2]}%"
    )

    await enviar_texto(update, texto)


# ============================================================
# 15. ESTADÍSTICAS
# ============================================================

def texto_estadisticas():
    categorias = {}
    por_marca = {}

    for moto in MOTOS:
        categoria = moto["identificacion"]["categoria"]
        categorias[categoria] = categorias.get(categoria, 0) + 1

        if moto_con_datos(moto):
            marca = moto["identificacion"]["marca"]
            por_marca[marca] = por_marca.get(marca, 0) + 1

    con_datos = sum(por_marca.values())
    coberturas = [
        calcular_cobertura(moto)[2] for moto in MOTOS if moto_con_datos(moto)
    ]
    promedio = round(sum(coberturas) / len(coberturas)) if coberturas else 0

    texto = (
        "📊 ESTADÍSTICAS DE MOTOGUÍA\n\n"
        f"Marcas: {len(MARCAS_ORDENADAS)}\n"
        f"Referencias registradas: {len(MOTOS)}\n"
        f"Con ficha técnica: {con_datos} "
        f"({round(con_datos / len(MOTOS) * 100)}%)\n"
        f"Con foto: {total_imagenes()}\n"
        f"Cobertura promedio de esas fichas: {promedio}%\n"
        f"Categorías: {len(categorias)}\n\n"
        "MOTOS POR CATEGORÍA\n"
    )

    for categoria, total in sorted(categorias.items()):
        texto += f"• {categoria}: {total}\n"

    texto += "\nMARCAS CON FICHA TÉCNICA\n"

    for marca, total in sorted(por_marca.items(), key=lambda x: (-x[1], x[0])):
        texto += f"• {marca}: {total}\n"

    texto += (
        "\nNota: las referencias sin ficha técnica están en el catálogo "
        "pero aún no tienen especificaciones verificadas."
    )
    return texto


async def estadisticas(update, context):
    await enviar_texto(update, texto_estadisticas())


# ============================================================
# 16. BOTONES INTERACTIVOS
# ============================================================

async def botones(update, context):
    query = update.callback_query
    await query.answer()

    opcion = query.data

    if opcion == "menu":
        await query.message.reply_text(
            "🏍️ MENÚ PRINCIPAL",
            reply_markup=teclado_principal()
        )

    elif opcion == "catalogo":
        await query.message.reply_text(
            "🏷️ ELIGE UNA MARCA\n\n"
            "El número indica cuántas referencias tiene.\n"
            "📷 = con foto · ✅ = con ficha técnica · ▫️ = solo referencia.",
            reply_markup=teclado_marcas()
        )

    elif opcion.startswith("marca:"):
        indice = int(opcion.split(":")[1])
        marca = MARCAS_ORDENADAS[indice]
        await query.message.reply_text(
            f"📚 {marca.upper()}\n\nElige una categoría:",
            reply_markup=teclado_categorias(indice)
        )

    elif opcion.startswith("cat:"):
        _, indice_marca, indice_categoria = opcion.split(":")
        indice_marca = int(indice_marca)
        indice_categoria = int(indice_categoria)
        marca = MARCAS_ORDENADAS[indice_marca]
        categoria = sorted(MOTOS_POR_MARCA[marca])[indice_categoria]
        await query.message.reply_text(
            f"🏍️ {marca} · {categoria}\n\nElige el modelo:",
            reply_markup=teclado_modelos(indice_marca, indice_categoria)
        )

    elif opcion.startswith("mf:"):
        indice = int(opcion.split(":")[1])
        await enviar_ficha(query.message, MOTOS[indice])

    elif opcion == "buscar":
        await query.message.reply_text(
            "🔎 Escribe la marca y el modelo.\n\n"
            "Ejemplos:\n"
            "Yamaha R1\n"
            "Kawasaki Ninja ZX-10R\n"
            "Honda XR190L\n\n"
            "También puedes usar /buscar Yamaha R1"
        )

    elif opcion == "marcas":
        await marcas_callback(query)

    elif opcion == "tipos":
        texto = "📚 TIPOS DE MOTOCICLETAS\n\n" + "\n".join(
            f"🏍️ {tipo}: {descripcion}"
            for tipo, descripcion in TIPOS.items()
        )
        await enviar_texto_a(query.message, texto)

    elif opcion == "mantenimiento":
        await query.message.reply_text(
            "🔧 Escribe:\n/mantenimiento Yamaha R1\n\n"
            "También puedes abrir la ficha desde el catálogo."
        )

    elif opcion == "comparar":
        await query.message.reply_text(
            "⚖️ Escribe:\n/comparar Yamaha R1 | Kawasaki ZX-10R"
        )

    elif opcion == "estadisticas":
        await enviar_texto_a(query.message, texto_estadisticas())

    elif opcion == "ayuda":
        await query.message.reply_text(
            "ℹ️ Escribe /ayuda para ver los comandos y cómo funciona cada modo."
        )

    elif opcion.startswith("ficha:"):
        indice = int(opcion.split(":")[1])
        resultados = context.user_data.get("resultados", [])

        if 0 <= indice < len(resultados):
            await enviar_ficha(query.message, resultados[indice])

    else:
        await query.message.reply_text(
            "Opción no reconocida. Usa /menu para volver al inicio."
        )


async def marcas_callback(query):
    texto = "🏷️ MARCAS DISPONIBLES\n\n"

    for marca in MARCAS_ORDENADAS:
        categorias = MOTOS_POR_MARCA.get(marca, {})
        cantidad = sum(len(lista) for lista in categorias.values())
        con_datos = sum(
            1
            for lista in categorias.values()
            for indice in lista
            if moto_con_datos(MOTOS[indice])
        )
        texto += f"• {marca}: {cantidad} referencias ({con_datos} con ficha)\n"

    texto += "\nToca 🏍️ Catálogo para navegar por marca."

    await enviar_texto_a(query.message, texto)


async def estadisticas_callback(query):
    await enviar_texto_a(query.message, texto_estadisticas())


async def modo_motos(update, context):
    context.user_data["modo"] = "motos"
    await update.message.reply_text(
        "🏍️ Modo catálogo activado.\n"
        "Escribe un modelo o usa el menú.",
        reply_markup=teclado_principal()
    )


# ============================================================
# 18. BUSCADOR POR MENSAJE NORMAL
# ============================================================

async def mensajes(update, context):
    consulta = update.message.text.strip()

    if len(consulta) < 2:
        return

    resultados = buscar_moto(consulta)

    if not resultados:
        await update.message.reply_text(
            "No encontré esa referencia.\n\n"
            "Prueba con la marca y el modelo (ej. Yamaha R1) "
            "o usa /catalogo para navegar."
        )
        return

    if len(resultados) == 1:
        await enviar_ficha(update.message, resultados[0])
        return

    botones_lista = []

    context.user_data["resultados"] = resultados

    for indice, moto in enumerate(resultados):
        i = moto["identificacion"]

        botones_lista.append([
            InlineKeyboardButton(
                f"{i['marca']} {i['modelo']}",
                callback_data=f"ficha:{indice}"
            )
        ])

    await update.message.reply_text(
        "Encontré estas referencias:",
        reply_markup=InlineKeyboardMarkup(botones_lista)
    )


# ============================================================
# 18. INICIO DEL PROGRAMA
# ============================================================

def forzar_ipv4():
    """Evita IPv6: en algunas redes esa ruta hacia Telegram se queda colgada."""
    original = socket.getaddrinfo

    def solo_ipv4(host, puerto, familia=0, tipo=0, proto=0, flags=0):
        return original(host, puerto, socket.AF_INET, tipo, proto, flags)

    socket.getaddrinfo = solo_ipv4


def hay_internet():
    import httpx

    try:
        with httpx.Client(timeout=httpx.Timeout(10)) as cliente:
            respuesta = cliente.get("https://www.gstatic.com/generate_204")
        return respuesta.status_code == 204
    except httpx.HTTPError:
        return False


def verificar_conexion(token):
    """Comprueba api.telegram.org antes de arrancar y explica cada fallo."""
    import httpx

    url = f"https://api.telegram.org/bot{token}/getMe"

    for intento in (1, 2):
        try:
            with httpx.Client(
                timeout=httpx.Timeout(TIMEOUT_RED, connect=TIMEOUT_CONEXION)
            ) as cliente:
                respuesta = cliente.get(url)
        except httpx.ConnectTimeout:
            print(
                f"⚠️ Intento {intento}: api.telegram.org no respondió "
                f"en {TIMEOUT_CONEXION} s."
            )
            continue
        except httpx.HTTPError as error:
            print(
                f"⚠️ Intento {intento}: error de red "
                f"({type(error).__name__})."
            )
            continue

        if respuesta.status_code == 200:
            usuario = respuesta.json().get("result", {}).get("username", "bot")
            print(f"✅ Conexión con Telegram correcta: @{usuario}")
            return True

        if respuesta.status_code == 401:
            print("❌ Token inválido o revocado (TELEGRAM_TOKEN).")
            return None

        print(f"⚠️ Telegram respondió HTTP {respuesta.status_code}.")
        return False

    if hay_internet():
        print(
            "\n❌ Hay internet, pero tu red está bloqueando a Telegram.\n"
            "   Lo más probable: el proveedor, la institución o un antivirus/VPN\n"
            "   está cortando api.telegram.org (aunque WhatsApp y el navegador sí funcionen).\n"
            "   Prueba, en este orden:\n"
            "   1. Datos móviles o hotspot del celular: si así arranca, el problema es tu red.\n"
            "   2. Desactiva la VPN y cualquier proxy del sistema.\n"
            "   3. Antivirus o firewall: permite python.exe y desactiva el escaneo HTTPS.\n"
            "   4. Si tu red exige un proxy, defínelo antes de arrancar:\n"
            "        set HTTPS_PROXY=http://usuario:clave@host:puerto\n"
            "   5. Cambia el DNS a 1.1.1.1 u 8.8.8.8 por si tu DNS está interviniendo."
        )
    else:
        print(
            "\n❌ No hay conexión a internet.\n"
            "   1. Revisa el cable o el WiFi y que otros sitios abran.\n"
            "   2. Si estás en un portal cautivo, inicia sesión primero.\n"
            "   3. Prueba con datos móviles para descartar al proveedor de internet."
        )
    return False


def total_imagenes():
    if not CARPETA_IMAGENES.exists():
        return 0
    return sum(
        1
        for archivo in CARPETA_IMAGENES.iterdir()
        if archivo.suffix.lower() in EXTENSIONES_IMAGEN
    )


def guardar_token(token):
    archivo = BASE_DIR / ".env"
    lineas = []

    if archivo.exists():
        lineas = [
            linea
            for linea in archivo.read_text(encoding="utf-8").splitlines()
            if not linea.strip().startswith("TELEGRAM_TOKEN")
        ]

    lineas.append(f"TELEGRAM_TOKEN={token}")
    archivo.write_text("\n".join(lineas) + "\n", encoding="utf-8")


def pedir_token_consola(mensaje):
    import getpass

    try:
        return getpass.getpass(mensaje).strip()
    except (EOFError, KeyboardInterrupt):
        return ""


def obtener_token():
    """Lee el token del .env o lo pide una vez y lo guarda para la próxima."""
    token = (os.getenv("TELEGRAM_TOKEN") or "").strip()
    if token:
        return token

    print(
        "🔑 No encontré el token del bot (TELEGRAM_TOKEN).\n"
        "   Se obtiene en Telegram con @BotFather (/newbot o /token).\n"
        "   Si compartiste un token antes, revócalo con /revoke.\n"
    )

    if not sys.stdin or not sys.stdin.isatty():
        print(
            "   Crea un archivo .env en la carpeta del bot con esta línea:\n"
            "      TELEGRAM_TOKEN=tu_token_aqui"
        )
        return None

    token = pedir_token_consola(
        "Pega el token (no se mostrará) o pulsa Enter para salir: "
    )

    if not token:
        return None

    if ":" not in token or len(token) < 30:
        print(
            "⚠️ Eso no parece un token de Telegram. "
            "Debe verse como 123456789:AA... (cópialo completo)."
        )
        return None

    guardar_token(token)
    print(f"✅ Token guardado en {BASE_DIR / '.env'}")
    return token


def main():
    token = obtener_token()
    if not token:
        raise SystemExit(1)

    print("🔌 Comprobando conexión con Telegram...")
    estado = verificar_conexion(token)

    if estado is None and sys.stdin and sys.stdin.isatty():
        nuevo = pedir_token_consola("Token nuevo (Enter para salir): ")

        if nuevo and ":" in nuevo and len(nuevo) >= 30:
            guardar_token(nuevo)
            token = nuevo
            print("✅ Token actualizado. Comprobando de nuevo...")
            estado = verificar_conexion(token)

    if estado is False:
        print("🔁 Reintentando solo con IPv4...")
        forzar_ipv4()
        estado = verificar_conexion(token)

    if not estado:
        raise SystemExit(1)

    app = (
        Application.builder()
        .token(token)
        .connect_timeout(TIMEOUT_RED)
        .read_timeout(TIMEOUT_RED)
        .write_timeout(TIMEOUT_RED)
        .pool_timeout(10)
        .get_updates_connect_timeout(TIMEOUT_RED)
        .get_updates_read_timeout(TIMEOUT_RED)
        .build()
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", menu))
    app.add_handler(CommandHandler("ayuda", ayuda))
    app.add_handler(CommandHandler("catalogo", catalogo))
    app.add_handler(CommandHandler("marcas", marcas))
    app.add_handler(CommandHandler("modelos", modelos))
    app.add_handler(CommandHandler("tipos", tipos))
    app.add_handler(CommandHandler("buscar", buscar))
    app.add_handler(CommandHandler("mantenimiento", mantenimiento))
    app.add_handler(CommandHandler("comparar", comparar))
    app.add_handler(CommandHandler("estadisticas", estadisticas))
    app.add_handler(CommandHandler("motos", modo_motos))

    app.add_handler(CallbackQueryHandler(botones))

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            mensajes
        )
    )

    print(
        f"🏍️ MotoGuía está funcionando...\n"
        f"   {len(MOTOS)} referencias · {len(MARCAS_ORDENADAS)} marcas\n"
        f"   {MOTOS_CON_DATOS} fichas con datos técnicos\n"
        f"   {total_imagenes()} fotos disponibles en imagenes/"
    )
    app.run_polling()


if __name__ == "__main__":
    main()
