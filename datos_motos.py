"""Datos técnicos del catálogo MotoGuía.

Cada entrada usa la clave "Marca|Modelo" EXACTAMENTE como aparece en
CATALOGO_BASE de bot.py. Solo se escriben los datos conocidos: el bot
rellena el resto como "No verificado", así que agregar una moto nueva
es tan simple como añadir una línea en MOTOS.

Notación corta (se traduce al esquema completo de la ficha):

    cc       cilindrada en cc            hp      potencia (HP)
    rpm      rpm de la potencia          nm      torque (Nm)
    rpm_nm   rpm del torque              kg      peso en orden de marcha
    tanque   capacidad de combustible    asiento altura del asiento (mm)
    vel      número de velocidades       abs     True/False
    abs_doble, cbs, tc                    precio  precio nuevo aprox. (COP)
    vmax     velocidad máxima (km/h)     consumo km/L aprox.
    anio     año de referencia           estado  "Disponible"/"Descontinuada"
    version, tipo, cil, refrig, alim, comp, arranque, freno_d, freno_t,
    llanta_d, llanta_t
    extra    diccionario para cualquier sección completa (suspensión,
             tecnología, mantenimiento, comercial, etc.)

Fuente: fichas de fabricante e importadores. Los valores son
aproximados y pueden variar según año, versión y mercado.
Última revisión: 2026-11.
"""

MOTOS = {
    # ==========================================================
    # YAMAHA
    # ==========================================================
    "Yamaha|YZF-R1": dict(
        cc=998, hp=197, rpm=13500, nm=113, rpm_nm=11500, kg=201, tanque=17,
        asiento=860, vel=6, abs=True, abs_doble=True, tc=True,
        precio=129990000, vmax=299, consumo=14, cil=4, refrig="Líquida",
        tipo="4T, DOHC, 4 cilindros en línea, 16V", comp="13.0:1",
        freno_d="Doble disco Ø320 mm", freno_t="Disco Ø220 mm",
        llanta_d="120/70 ZR17", llanta_t="190/55 ZR17",
        extra={
            "tecnologia": {
                "tablero": "TFT a color",
                "iluminacion": "Full LED",
                "modos_conduccion": "4 modos",
                "quickshifter": True,
                "control_crucero": True,
                "conectividad": "App Yamaha MyRide",
            },
            "rendimiento": {"aceleracion": "0-100 km/h en 2,9 s aprox."},
            "suspension": {
                "delantera": "Horquilla invertida KYB Ø43 mm ajustable",
                "trasera": "Monoamortiguador KYB ajustable",
            },
        },
    ),
    "Yamaha|YZF-R6": dict(
        cc=599, hp=118, rpm=14500, nm=61.7, rpm_nm=10500, kg=190, tanque=17,
        asiento=850, vel=6, abs=True, abs_doble=True, precio=None,
        vmax=262, consumo=15, anio=2020, estado="Descontinuada", cil=4,
        refrig="Líquida", tipo="4T, DOHC, 4 cilindros en línea, 16V",
        freno_d="Doble disco Ø320 mm", freno_t="Disco Ø220 mm",
        llanta_d="120/70 ZR17", llanta_t="180/55 ZR17",
    ),
    "Yamaha|YZF-R7": dict(
        cc=689, hp=73.4, rpm=8750, nm=67, rpm_nm=6500, kg=188, tanque=13,
        asiento=835, vel=6, abs=True, abs_doble=True,
        precio=54990000, vmax=224, consumo=20, cil=2, refrig="Líquida",
        tipo="4T, DOHC, bicilíndrico CP2, 8V", comp="11.5:1",
        freno_d="Doble disco Ø298 mm", freno_t="Disco Ø245 mm",
        llanta_d="120/70 ZR17", llanta_t="180/55 ZR17",
    ),
    "Yamaha|YZF-R3": dict(
        cc=321, hp=42, rpm=10750, nm=29.6, rpm_nm=9000, kg=169, tanque=14,
        asiento=780, vel=6, abs=True, abs_doble=True,
        precio=32990000, vmax=180, consumo=26, cil=2, refrig="Líquida",
        tipo="4T, DOHC, bicilíndrico en línea, 8V",
        freno_d="Disco Ø298 mm", freno_t="Disco Ø220 mm",
        llanta_d="110/70 R17", llanta_t="140/70 R17",
    ),
    "Yamaha|YZF-R15": dict(
        cc=155, hp=18.8, rpm=10000, nm=14.2, rpm_nm=7500, kg=142, tanque=11,
        asiento=815, vel=6, abs=True, precio=18490000, vmax=136, consumo=40,
        cil=1, refrig="Líquida", tipo="4T, SOHC, monocilíndrico VVA, 4V",
        comp="10.5:1", freno_d="Disco Ø282 mm", freno_t="Disco Ø220 mm",
        llanta_d="100/80 R17", llanta_t="140/70 R17",
    ),
    "Yamaha|MT-03": dict(
        cc=321, hp=42, rpm=10750, nm=29.6, rpm_nm=9000, kg=169, tanque=14,
        asiento=780, vel=6, abs=True, abs_doble=True,
        precio=27990000, vmax=180, consumo=26, cil=2, refrig="Líquida",
        tipo="4T, DOHC, bicilíndrico en línea, 8V",
        freno_d="Disco Ø298 mm", freno_t="Disco Ø220 mm",
        llanta_d="110/70 R17", llanta_t="140/70 R17",
    ),
    "Yamaha|MT-07": dict(
        cc=689, hp=73.4, rpm=8750, nm=67, rpm_nm=6500, kg=184, tanque=14,
        asiento=805, vel=6, abs=True, abs_doble=True,
        precio=49990000, vmax=214, consumo=21, cil=2, refrig="Líquida",
        tipo="4T, DOHC, bicilíndrico CP2, 8V",
        freno_d="Doble disco Ø298 mm", freno_t="Disco Ø245 mm",
        llanta_d="120/70 R17", llanta_t="180/55 R17",
    ),
    "Yamaha|MT-09": dict(
        cc=890, hp=119, rpm=10000, nm=93, rpm_nm=7000, kg=193, tanque=14,
        asiento=825, vel=6, abs=True, abs_doble=True, tc=True,
        precio=69990000, vmax=240, consumo=17, cil=3, refrig="Líquida",
        tipo="4T, DOHC, tricilíndrico CP3, 12V",
        freno_d="Doble disco Ø298 mm", freno_t="Disco Ø245 mm",
        llanta_d="120/70 R17", llanta_t="180/55 R17",
        extra={
            "tecnologia": {
                "tablero": "TFT a color",
                "iluminacion": "Full LED",
                "modos_conduccion": "4 modos",
                "quickshifter": True,
                "conectividad": "App Yamaha MyRide",
            },
        },
    ),
    "Yamaha|MT-15": dict(
        cc=155, hp=18.1, rpm=10000, nm=14.2, rpm_nm=7500, kg=141, tanque=10,
        asiento=810, vel=6, abs=True, precio=13990000, vmax=130, consumo=45,
        cil=1, refrig="Líquida", tipo="4T, SOHC, monocilíndrico VVA, 4V",
        comp="11.6:1", freno_d="Disco Ø282 mm", freno_t="Disco Ø220 mm",
        llanta_d="110/80 R17", llanta_t="140/70 R17",
        extra={
            "tecnologia": {
                "tablero": "LCD negativo",
                "iluminacion": "Full LED",
                "conectividad": "App Yamaha Y-Connect (según versión)",
            },
            "suspension": {
                "delantera": "Horquilla invertida (según versión)",
                "trasera": "Monoamortiguador con precarga ajustable",
            },
        },
    ),
    "Yamaha|FZ25": dict(
        cc=249, hp=20.8, rpm=8000, nm=20.1, rpm_nm=6000, kg=151, tanque=14,
        asiento=795, vel=5, abs=True, precio=12990000, vmax=130, consumo=38,
        cil=1, refrig="Aire", tipo="4T, SOHC, monocilíndrico, 2V",
        comp="9.8:1", freno_d="Disco Ø282 mm", freno_t="Disco Ø220 mm",
        llanta_d="100/80 R17", llanta_t="140/70 R17",
        extra={
            "mantenimiento": {
                "aceite_recomendado": "Yamalube 10W-40 semisintético",
                "cantidad_aceite_l": 1.0,
                "intervalos": [
                    "Revisión inicial a los 1.000 km",
                    "Cambio de aceite cada 6.000 km",
                ],
            },
        },
    ),
    "Yamaha|FZ16": dict(
        cc=153, hp=14, rpm=7500, nm=13.6, rpm_nm=6000, kg=137, tanque=12,
        asiento=790, vel=5, abs=False, precio=8490000, vmax=115, consumo=42,
        cil=1, refrig="Aire", tipo="4T, SOHC, monocilíndrico, 2V",
        freno_d="Disco Ø267 mm", freno_t="Tambor",
        llanta_d="100/80 R17", llanta_t="140/60 R17",
    ),
    "Yamaha|XTZ125": dict(
        cc=124, hp=11.4, rpm=8000, nm=11.6, rpm_nm=6000, kg=118, tanque=12,
        asiento=840, vel=5, abs=False, precio=8290000, vmax=105, consumo=45,
        cil=1, refrig="Aire", tipo="4T, SOHC, monocilíndrico, 2V",
        freno_d="Disco Ø245 mm", freno_t="Tambor",
        llanta_d="2.75-21", llanta_t="4.10-18",
    ),
    "Yamaha|XTZ150": dict(
        cc=149, hp=12.7, rpm=7500, nm=13.3, rpm_nm=6000, kg=132, tanque=12,
        asiento=845, vel=5, abs=False, precio=9990000, vmax=110, consumo=42,
        cil=1, refrig="Aire", tipo="4T, SOHC, monocilíndrico, 2V",
        freno_d="Disco Ø245 mm", freno_t="Tambor",
        llanta_d="2.75-21", llanta_t="4.10-18",
        extra={
            "mantenimiento": {
                "aceite_recomendado": "Yamalube 10W-40",
                "cantidad_aceite_l": 1.0,
                "intervalos": [
                    "Revisión inicial a los 1.000 km",
                    "Cambio de aceite cada 6.000 km",
                ],
            },
        },
    ),
    "Yamaha|XTZ250": dict(
        cc=249, hp=20.7, rpm=8000, nm=20.5, rpm_nm=6500, kg=154, tanque=16,
        asiento=865, vel=5, abs=True, precio=17990000, vmax=135, consumo=33,
        cil=1, refrig="Líquida", tipo="4T, SOHC, monocilíndrico, 4V",
        freno_d="Disco Ø282 mm", freno_t="Disco Ø245 mm",
        llanta_d="90/90-21", llanta_t="120/80-18",
    ),
    "Yamaha|Ténéré 700": dict(
        cc=689, hp=72.4, rpm=9000, nm=68, rpm_nm=6500, kg=204, tanque=16,
        asiento=875, vel=6, abs=True, abs_doble=True,
        precio=64990000, vmax=190, consumo=22, cil=2, refrig="Líquida",
        tipo="4T, DOHC, bicilíndrico CP2, 8V",
        freno_d="Doble disco Ø282 mm", freno_t="Disco Ø245 mm",
        llanta_d="90/90-21", llanta_t="150/70 R18",
        extra={
            "suspension": {
                "delantera": "Horquilla invertida Ø43 mm, 210 mm de recorrido",
                "trasera": "Monoamortiguador con 200 mm de recorrido",
                "recorrido_delantero_mm": 210,
                "recorrido_trasero_mm": 200,
            },
        },
    ),
    "Yamaha|NMAX 155": dict(
        cc=155, hp=15.4, rpm=8000, nm=13.9, rpm_nm=6500, kg=131, tanque=7.1,
        asiento=765, vel=None, abs=True, precio=15490000, vmax=120, consumo=45,
        cil=1, refrig="Líquida", tipo="4T, SOHC, monocilíndrico VVA, 4V",
        version="CVT", freno_d="Disco Ø230 mm", freno_t="Disco Ø230 mm",
        llanta_d="110/70 R13", llanta_t="130/70 R13",
        extra={
            "transmision": {"tipo_caja": "Automática CVT",
                            "transmision_final": "Correa"},
            "tecnologia": {"tablero": "LCD", "iluminacion": "Full LED",
                           "conectividad": "App Y-Connect",
                           "puerto_usb": True, "inmovilizador": True},
            "mantenimiento": {
                "aceite_recomendado": "Yamalube 10W-40 semisintético",
                "cantidad_aceite_l": 0.9,
                "intervalos": [
                    "Revisión inicial a los 1.000 km",
                    "Cambio de aceite cada 6.000 km",
                ],
            },
        },
    ),
    "Yamaha|XMAX 300": dict(
        cc=292, hp=28, rpm=7250, nm=29, rpm_nm=5750, kg=183, tanque=13,
        asiento=795, abs=True, abs_doble=True, tc=True,
        precio=27990000, vmax=145, consumo=30, cil=1, refrig="Líquida",
        tipo="4T, SOHC, monocilíndrico, 4V",
        extra={
            "transmision": {"tipo_caja": "Automática CVT",
                            "transmision_final": "Correa"},
            "tecnologia": {"tablero": "LCD", "iluminacion": "Full LED",
                           "control_crucero": False, "puerto_usb": True},
        },
    ),
    "Yamaha|Aerox": dict(
        cc=155, hp=15, rpm=8000, nm=13.9, rpm_nm=6500, kg=125, tanque=5.5,
        asiento=790, abs=True, precio=13490000, vmax=118, consumo=40, cil=1,
        refrig="Líquida", tipo="4T, SOHC, monocilíndrico VVA, 4V",
        extra={
            "transmision": {"tipo_caja": "Automática CVT",
                            "transmision_final": "Correa"},
        },
    ),
    "Yamaha|Crypton FI": dict(
        cc=113, hp=8.9, rpm=8000, nm=9.5, rpm_nm=6000, kg=105, tanque=4.2,
        asiento=770, abs=False, precio=6590000, vmax=95, consumo=55, cil=1,
        refrig="Aire", tipo="4T, SOHC, monocilíndrico, 2V",
        extra={
            "transmision": {"tipo_caja": "Automática CVT",
                            "transmision_final": "Correa"},
        },
    ),
    "Yamaha|YBR125": dict(
        cc=124, hp=10.5, rpm=7800, nm=10.4, rpm_nm=6000, kg=120, tanque=13,
        asiento=780, vel=5, abs=False, precio=6990000, vmax=105, consumo=50,
        cil=1, refrig="Aire", tipo="4T, SOHC, monocilíndrico, 2V",
        freno_d="Disco Ø245 mm", freno_t="Tambor",
        llanta_d="2.75-18", llanta_t="90/90-18",
    ),
    "Yamaha|Tracer 9": dict(
        cc=890, hp=119, rpm=10000, nm=93, rpm_nm=7000, kg=213, tanque=18,
        asiento=820, vel=6, abs=True, abs_doble=True, tc=True,
        precio=79990000, vmax=230, consumo=18, cil=3, refrig="Líquida",
        tipo="4T, DOHC, tricilíndrico CP3, 12V",
        extra={
            "tecnologia": {
                "tablero": "TFT doble a color",
                "iluminacion": "Full LED",
                "modos_conduccion": "4 modos",
                "quickshifter": True,
                "control_crucero": True,
            },
        },
    ),

    # ==========================================================
    # HONDA
    # ==========================================================
    "Honda|CB125F": dict(
        cc=124, hp=10.7, rpm=7500, nm=10.6, rpm_nm=6000, kg=117, tanque=11,
        asiento=775, vel=5, abs=False, cbs=True, precio=7490000, vmax=100,
        consumo=55, cil=1, refrig="Aire", tipo="4T, SOHC, monocilíndrico, 2V",
        freno_d="Disco Ø240 mm", freno_t="Tambor",
        llanta_d="80/100-18", llanta_t="90/90-18",
        extra={
            "mantenimiento": {
                "aceite_recomendado": "Honda 10W-30",
                "cantidad_aceite_l": 0.8,
                "intervalos": [
                    "Revisión inicial a los 1.000 km",
                    "Cambio de aceite cada 6.000 km",
                ],
            },
        },
    ),
    "Honda|CB150R": dict(
        cc=149, hp=16.6, rpm=9000, nm=14.5, rpm_nm=7000, kg=137, tanque=12,
        asiento=795, vel=6, abs=True, precio=10990000, vmax=120, consumo=40,
        cil=1, refrig="Líquida", tipo="4T, DOHC, monocilíndrico, 4V",
        freno_d="Disco Ø296 mm", freno_t="Disco Ø220 mm",
        llanta_d="100/80 R17", llanta_t="130/70 R17",
    ),
    "Honda|CBR150R": dict(
        cc=149, hp=17.1, rpm=9000, nm=14.4, rpm_nm=7000, kg=137, tanque=12,
        asiento=782, vel=6, abs=True, abs_doble=True,
        precio=13990000, vmax=130, consumo=38, cil=1, refrig="Líquida",
        tipo="4T, DOHC, monocilíndrico, 4V",
        freno_d="Disco Ø296 mm", freno_t="Disco Ø220 mm",
        llanta_d="100/80 R17", llanta_t="130/70 R17",
    ),
    "Honda|CBR250RR": dict(
        cc=250, hp=41, rpm=13000, nm=25, rpm_nm=11000, kg=168, tanque=14.5,
        asiento=790, vel=6, abs=True, abs_doble=True,
        precio=34990000, vmax=180, consumo=28, cil=2, refrig="Líquida",
        tipo="4T, DOHC, bicilíndrico en línea, 8V",
        freno_d="Doble disco Ø310 mm", freno_t="Disco Ø240 mm",
        llanta_d="110/70 R17", llanta_t="140/70 R17",
    ),
    "Honda|CBR500R": dict(
        cc=471, hp=47, rpm=8500, nm=43, rpm_nm=6500, kg=194, tanque=17,
        asiento=785, vel=6, abs=True, abs_doble=True,
        precio=44990000, vmax=180, consumo=28, cil=2, refrig="Líquida",
        tipo="4T, DOHC, bicilíndrico en línea, 8V",
        freno_d="Doble disco Ø296 mm", freno_t="Disco Ø240 mm",
        llanta_d="120/70 R17", llanta_t="160/60 R17",
    ),
    "Honda|CBR650R": dict(
        cc=649, hp=95, rpm=12000, nm=63, rpm_nm=9500, kg=212, tanque=15.4,
        asiento=810, vel=6, abs=True, abs_doble=True,
        precio=59990000, vmax=230, consumo=21, cil=4, refrig="Líquida",
        tipo="4T, DOHC, 4 cilindros en línea, 16V",
        freno_d="Doble disco Ø310 mm", freno_t="Disco Ø240 mm",
        llanta_d="120/70 R17", llanta_t="180/55 R17",
    ),
    "Honda|CB300R": dict(
        cc=286, hp=31, rpm=8500, nm=27.5, rpm_nm=7500, kg=144, tanque=10.1,
        asiento=800, vel=6, abs=True, abs_doble=True,
        precio=24990000, vmax=150, consumo=32, cil=1, refrig="Líquida",
        tipo="4T, DOHC, monocilíndrico, 4V",
        freno_d="Disco Ø296 mm", freno_t="Disco Ø220 mm",
        llanta_d="110/70 R17", llanta_t="150/60 R17",
    ),
    "Honda|CB650R": dict(
        cc=649, hp=95, rpm=12000, nm=63, rpm_nm=9500, kg=202, tanque=15.4,
        asiento=810, vel=6, abs=True, abs_doble=True,
        precio=54990000, vmax=220, consumo=21, cil=4, refrig="Líquida",
        tipo="4T, DOHC, 4 cilindros en línea, 16V",
        freno_d="Doble disco Ø310 mm", freno_t="Disco Ø240 mm",
        llanta_d="120/70 R17", llanta_t="180/55 R17",
    ),
    "Honda|CB750 Hornet": dict(
        cc=755, hp=90.5, rpm=9500, nm=75, rpm_nm=7250, kg=190, tanque=15.2,
        asiento=795, vel=6, abs=True, abs_doble=True, tc=True,
        precio=56990000, vmax=210, consumo=23, cil=2, refrig="Líquida",
        tipo="4T, SOHC, bicilíndrico paralelo, 8V",
        freno_d="Doble disco Ø296 mm", freno_t="Disco Ø240 mm",
        llanta_d="120/70 R17", llanta_t="160/60 R17",
        extra={
            "tecnologia": {"tablero": "TFT a color", "iluminacion": "Full LED",
                           "modos_conduccion": "3 modos",
                           "quickshifter": True, "conectividad": "Honda RoadSync"},
        },
    ),
    "Honda|XR150L": dict(
        cc=149, hp=12.5, rpm=8000, nm=12.5, rpm_nm=6000, kg=127, tanque=12,
        asiento=825, vel=5, abs=False, precio=9290000, vmax=110, consumo=45,
        cil=1, refrig="Aire", tipo="4T, SOHC, monocilíndrico, 2V",
        freno_d="Disco Ø240 mm", freno_t="Tambor",
        llanta_d="2.75-21", llanta_t="4.10-18",
        extra={
            "mantenimiento": {
                "aceite_recomendado": "Honda 10W-30",
                "cantidad_aceite_l": 0.9,
                "intervalos": [
                    "Revisión inicial a los 1.000 km",
                    "Cambio de aceite cada 6.000 km",
                ],
            },
        },
    ),
    "Honda|XR190L": dict(
        cc=184, hp=15.6, rpm=8000, nm=15.7, rpm_nm=6000, kg=132, tanque=12,
        asiento=830, vel=5, abs=True, precio=10990000, vmax=115, consumo=40,
        cil=1, refrig="Aire", tipo="4T, SOHC, monocilíndrico, 2V",
        freno_d="Disco Ø240 mm", freno_t="Tambor",
        llanta_d="2.75-21", llanta_t="4.10-18",
        extra={
            "mantenimiento": {
                "aceite_recomendado": "Honda 10W-30",
                "cantidad_aceite_l": 1.0,
                "intervalos": [
                    "Revisión inicial a los 1.000 km",
                    "Cambio de aceite cada 6.000 km",
                ],
            },
        },
    ),
    "Honda|XRE190": dict(
        cc=184, hp=15.6, rpm=8000, nm=15.7, rpm_nm=6000, kg=137, tanque=13,
        asiento=835, vel=5, abs=True, precio=13490000, vmax=115, consumo=38,
        cil=1, refrig="Aire", tipo="4T, SOHC, monocilíndrico, 2V",
        freno_d="Disco Ø240 mm", freno_t="Disco Ø220 mm",
        llanta_d="90/90-19", llanta_t="110/90-17",
    ),
    "Honda|XRE300": dict(
        cc=291, hp=25, rpm=7500, nm=27, rpm_nm=6000, kg=166, tanque=13.8,
        asiento=860, vel=6, abs=True, abs_doble=True,
        precio=22990000, vmax=130, consumo=32, cil=1, refrig="Líquida",
        tipo="4T, DOHC, monocilíndrico, 4V",
        freno_d="Disco Ø296 mm", freno_t="Disco Ø220 mm",
        llanta_d="90/90-19", llanta_t="110/90-17",
    ),
    "Honda|CRF250L": dict(
        cc=249, hp=24.8, rpm=9000, nm=22.6, rpm_nm=7000, kg=148, tanque=7.8,
        asiento=880, vel=6, abs=True, precio=27990000, vmax=130, consumo=30,
        cil=1, refrig="Líquida", tipo="4T, DOHC, monocilíndrico, 4V",
        freno_d="Disco Ø256 mm", freno_t="Disco Ø220 mm",
        llanta_d="3.00-21", llanta_t="120/80-18",
    ),
    "Honda|NX500": dict(
        cc=471, hp=47, rpm=8500, nm=43, rpm_nm=6500, kg=196, tanque=17.5,
        asiento=830, vel=6, abs=True, abs_doble=True,
        precio=52990000, vmax=180, consumo=27, cil=2, refrig="Líquida",
        tipo="4T, DOHC, bicilíndrico en línea, 8V",
        freno_d="Doble disco Ø296 mm", freno_t="Disco Ø240 mm",
        llanta_d="110/80 R19", llanta_t="160/60 R17",
    ),
    "Honda|Transalp XL750": dict(
        cc=755, hp=90.5, rpm=9500, nm=75, rpm_nm=7250, kg=208, tanque=16.9,
        asiento=850, vel=6, abs=True, abs_doble=True, tc=True,
        precio=69990000, vmax=200, consumo=22, cil=2, refrig="Líquida",
        tipo="4T, SOHC, bicilíndrico paralelo, 8V",
        freno_d="Doble disco Ø310 mm", freno_t="Disco Ø256 mm",
        llanta_d="90/90-21", llanta_t="150/70 R18",
        extra={
            "tecnologia": {"tablero": "TFT a color", "iluminacion": "Full LED",
                           "modos_conduccion": "5 modos",
                           "quickshifter": True, "conectividad": "Honda RoadSync"},
        },
    ),
    "Honda|Africa Twin CRF1100L": dict(
        cc=1084, hp=101, rpm=7500, nm=105, rpm_nm=6250, kg=226, tanque=18.8,
        asiento=870, vel=6, abs=True, abs_doble=True, tc=True,
        precio=99990000, vmax=200, consumo=18, cil=2, refrig="Líquida",
        tipo="4T, SOHC, bicilíndrico paralelo, 8V",
        freno_d="Doble disco Ø310 mm", freno_t="Disco Ø256 mm",
        llanta_d="90/90-21", llanta_t="150/70 R18",
        extra={
            "tecnologia": {"tablero": "TFT táctil a color",
                           "iluminacion": "Full LED", "modos_conduccion": "6 modos",
                           "control_crucero": True,
                           "conectividad": "Apple CarPlay / Android Auto"},
            "suspension": {"delantera": "Horquilla invertida Showa Ø45 mm",
                           "trasera": "Monoamortiguador Showa ajustable"},
        },
    ),
    "Honda|PCX160": dict(
        cc=156, hp=15.8, rpm=8500, nm=14.7, rpm_nm=6500, kg=132, tanque=8.1,
        asiento=764, abs=True, precio=16490000, vmax=115, consumo=45, cil=1,
        refrig="Líquida", tipo="4T, SOHC, monocilíndrico eSP+, 4V",
        freno_d="Disco Ø220 mm", freno_t="Tambor",
        llanta_d="100/80 R14", llanta_t="120/70 R14",
        extra={
            "transmision": {"tipo_caja": "Automática CVT",
                            "transmision_final": "Correa"},
            "tecnologia": {"tablero": "LCD", "iluminacion": "Full LED",
                           "puerto_usb": True, "inmovilizador": True,
                           "conectividad": "Honda Smart Key"},
        },
    ),
    "Honda|ADV160": dict(
        cc=156, hp=15.8, rpm=8500, nm=14.7, rpm_nm=6500, kg=133, tanque=8.1,
        asiento=795, abs=True, tc=True, precio=18990000, vmax=115, consumo=42,
        cil=1, refrig="Líquida", tipo="4T, SOHC, monocilíndrico eSP+, 4V",
        freno_d="Disco Ø240 mm", freno_t="Disco Ø220 mm",
        llanta_d="110/80 R14", llanta_t="130/70 R13",
        extra={
            "transmision": {"tipo_caja": "Automática CVT",
                            "transmision_final": "Correa"},
        },
    ),
    "Honda|Dio": dict(
        cc=109, hp=8.7, rpm=7500, nm=9.1, rpm_nm=6000, kg=105, tanque=4.2,
        asiento=765, abs=False, precio=6290000, vmax=90, consumo=55, cil=1,
        refrig="Aire", tipo="4T, SOHC, monocilíndrico, 2V",
        extra={
            "transmision": {"tipo_caja": "Automática CVT",
                            "transmision_final": "Correa"},
        },
    ),
    "Honda|Wave 110": dict(
        cc=109, hp=8.5, rpm=7500, nm=8.8, rpm_nm=6000, kg=97, tanque=3.7,
        asiento=760, abs=False, precio=5990000, vmax=90, consumo=60, cil=1,
        refrig="Aire", tipo="4T, SOHC, monocilíndrico, 2V",
    ),
    "Honda|Rebel 500": dict(
        cc=471, hp=47, rpm=8500, nm=43, rpm_nm=6500, kg=191, tanque=11.2,
        asiento=690, vel=6, abs=True, abs_doble=True,
        precio=42990000, vmax=160, consumo=30, cil=2, refrig="Líquida",
        tipo="4T, DOHC, bicilíndrico en línea, 8V",
        freno_d="Disco Ø296 mm", freno_t="Disco Ø240 mm",
        llanta_d="130/90-16", llanta_t="150/80-16",
    ),
    "Honda|Gold Wing": dict(
        cc=1833, hp=125, rpm=5500, nm=170, rpm_nm=4500, kg=383, tanque=21,
        asiento=745, vel=6, abs=True, abs_doble=True, tc=True,
        precio=179990000, vmax=200, consumo=15, cil=6, refrig="Líquida",
        tipo="4T, SOHC, 6 cilindros bóxer, 24V",
        extra={
            "tecnologia": {"tablero": "TFT a color", "iluminacion": "Full LED",
                           "control_crucero": True,
                           "conectividad": "Apple CarPlay / Android Auto"},
            "transmision": {"tipo_caja": "DCT de doble embrague (7 vel.)",
                            "transmision_final": "Eje cardán"},
        },
    ),

    # ==========================================================
    # KAWASAKI
    # ==========================================================
    "Kawasaki|Ninja 250": dict(
        cc=249, hp=38.5, rpm=12500, nm=23.5, rpm_nm=10000, kg=164, tanque=14,
        asiento=795, vel=6, abs=True, abs_doble=True,
        precio=25990000, vmax=165, consumo=30, cil=2, refrig="Líquida",
        tipo="4T, DOHC, bicilíndrico en línea, 8V",
        freno_d="Disco Ø310 mm", freno_t="Disco Ø220 mm",
        llanta_d="110/70 R17", llanta_t="140/70 R17",
    ),
    "Kawasaki|Ninja 400": dict(
        cc=399, hp=45, rpm=10000, nm=38, rpm_nm=8000, kg=168, tanque=14,
        asiento=785, vel=6, abs=True, abs_doble=True,
        precio=29990000, vmax=180, consumo=28, cil=2, refrig="Líquida",
        tipo="4T, DOHC, bicilíndrico en línea, 8V",
        freno_d="Disco Ø310 mm", freno_t="Disco Ø220 mm",
        llanta_d="110/70 R17", llanta_t="150/60 R17",
        extra={
            "tecnologia": {"tablero": "LCD", "iluminacion": "LED",
                           "modos_conduccion": "No"},
        },
    ),
    "Kawasaki|Ninja 500": dict(
        cc=451, hp=45.4, rpm=9000, nm=42.6, rpm_nm=6000, kg=171, tanque=14,
        asiento=785, vel=6, abs=True, abs_doble=True,
        precio=31990000, vmax=180, consumo=27, cil=2, refrig="Líquida",
        tipo="4T, DOHC, bicilíndrico en línea, 8V",
        freno_d="Disco Ø310 mm", freno_t="Disco Ø220 mm",
        llanta_d="110/70 R17", llanta_t="150/60 R17",
    ),
    "Kawasaki|Ninja 650": dict(
        cc=649, hp=68, rpm=8000, nm=64, rpm_nm=6700, kg=193, tanque=15,
        asiento=790, vel=6, abs=True, abs_doble=True, tc=True,
        precio=39990000, vmax=200, consumo=23, cil=2, refrig="Líquida",
        tipo="4T, DOHC, bicilíndrico en línea, 8V",
        freno_d="Doble disco Ø300 mm", freno_t="Disco Ø220 mm",
        llanta_d="120/70 R17", llanta_t="160/60 R17",
    ),
    "Kawasaki|Z400": dict(
        cc=399, hp=45, rpm=10000, nm=38, rpm_nm=8000, kg=167, tanque=14,
        asiento=785, vel=6, abs=True, abs_doble=True,
        precio=27990000, vmax=180, consumo=28, cil=2, refrig="Líquida",
        tipo="4T, DOHC, bicilíndrico en línea, 8V",
        freno_d="Disco Ø310 mm", freno_t="Disco Ø220 mm",
        llanta_d="110/70 R17", llanta_t="150/60 R17",
    ),
    "Kawasaki|Z500": dict(
        cc=451, hp=45.4, rpm=9000, nm=42.6, rpm_nm=6000, kg=168, tanque=14,
        asiento=785, vel=6, abs=True, abs_doble=True,
        precio=29990000, vmax=180, consumo=27, cil=2, refrig="Líquida",
        tipo="4T, DOHC, bicilíndrico en línea, 8V",
        freno_d="Disco Ø310 mm", freno_t="Disco Ø220 mm",
        llanta_d="110/70 R17", llanta_t="150/60 R17",
    ),
    "Kawasaki|Z650": dict(
        cc=649, hp=68, rpm=8000, nm=64, rpm_nm=6700, kg=187, tanque=15,
        asiento=790, vel=6, abs=True, abs_doble=True, tc=True,
        precio=35990000, vmax=195, consumo=23, cil=2, refrig="Líquida",
        tipo="4T, DOHC, bicilíndrico en línea, 8V",
        freno_d="Doble disco Ø300 mm", freno_t="Disco Ø220 mm",
        llanta_d="120/70 R17", llanta_t="160/60 R17",
    ),
    "Kawasaki|Z900": dict(
        cc=948, hp=125, rpm=9500, nm=98.6, rpm_nm=7700, kg=212, tanque=17,
        asiento=820, vel=6, abs=True, abs_doble=True, tc=True,
        precio=56990000, vmax=240, consumo=18, cil=4, refrig="Líquida",
        tipo="4T, DOHC, 4 cilindros en línea, 16V",
        freno_d="Doble disco Ø300 mm", freno_t="Disco Ø250 mm",
        llanta_d="120/70 R17", llanta_t="180/55 R17",
        extra={
            "tecnologia": {"tablero": "TFT a color", "iluminacion": "Full LED",
                           "modos_conduccion": "4 modos", "quickshifter": True,
                           "conectividad": "App Rideology"},
        },
    ),
    "Kawasaki|Versys 650": dict(
        cc=649, hp=66, rpm=8500, nm=61, rpm_nm=7000, kg=217, tanque=21,
        asiento=845, vel=6, abs=True, abs_doble=True, tc=True,
        precio=42990000, vmax=190, consumo=22, cil=2, refrig="Líquida",
        tipo="4T, DOHC, bicilíndrico en línea, 8V",
        freno_d="Doble disco Ø300 mm", freno_t="Disco Ø250 mm",
        llanta_d="120/70 R17", llanta_t="160/60 R17",
    ),
    "Kawasaki|KLX230": dict(
        cc=233, hp=20, rpm=7600, nm=19.5, rpm_nm=6100, kg=132, tanque=7.5,
        asiento=885, vel=6, abs=True, precio=18990000, vmax=120, consumo=35,
        cil=1, refrig="Aire", tipo="4T, SOHC, monocilíndrico, 2V",
        freno_d="Disco Ø240 mm", freno_t="Disco Ø220 mm",
        llanta_d="2.75-21", llanta_t="4.10-18",
    ),
    "Kawasaki|Ninja ZX-6R": dict(
        cc=636, hp=124, rpm=13000, nm=69, rpm_nm=10800, kg=194, tanque=17,
        asiento=830, vel=6, abs=True, abs_doble=True, tc=True,
        precio=62990000, vmax=250, consumo=17, cil=4, refrig="Líquida",
        tipo="4T, DOHC, 4 cilindros en línea, 16V",
        freno_d="Doble disco Ø310 mm", freno_t="Disco Ø220 mm",
        llanta_d="120/70 ZR17", llanta_t="180/55 ZR17",
    ),
    "Kawasaki|Ninja ZX-10R": dict(
        cc=998, hp=203, rpm=13200, nm=114.9, rpm_nm=11400, kg=207, tanque=17,
        asiento=835, vel=6, abs=True, abs_doble=True, tc=True,
        precio=89990000, vmax=299, consumo=14, cil=4, refrig="Líquida",
        tipo="4T, DOHC, 4 cilindros en línea, 16V",
        freno_d="Doble disco Ø330 mm", freno_t="Disco Ø220 mm",
        llanta_d="120/70 ZR17", llanta_t="190/55 ZR17",
        extra={
            "tecnologia": {"tablero": "TFT a color", "iluminacion": "LED",
                           "modos_conduccion": "3 modos", "quickshifter": True,
                           "control_crucero": True},
        },
    ),

    # ==========================================================
    # SUZUKI
    # ==========================================================
    "Suzuki|Gixxer 150": dict(
        cc=155, hp=13.6, rpm=8000, nm=13.8, rpm_nm=6000, kg=141, tanque=12,
        asiento=795, vel=5, abs=True, precio=8990000, vmax=120, consumo=42,
        cil=1, refrig="Aire", tipo="4T, SOHC, monocilíndrico, 2V",
        freno_d="Disco Ø266 mm", freno_t="Disco Ø240 mm",
        llanta_d="100/80 R17", llanta_t="140/60 R17",
    ),
    "Suzuki|Gixxer 250": dict(
        cc=249, hp=26.5, rpm=9300, nm=22.2, rpm_nm=7300, kg=156, tanque=12,
        asiento=800, vel=6, abs=True, abs_doble=True,
        precio=14990000, vmax=145, consumo=35, cil=1, refrig="Líquida",
        tipo="4T, SOHC, monocilíndrico, 4V",
        freno_d="Disco Ø300 mm", freno_t="Disco Ø220 mm",
        llanta_d="110/70 R17", llanta_t="150/60 R17",
    ),
    "Suzuki|GSX-S150": dict(
        cc=147, hp=19.2, rpm=10500, nm=14, rpm_nm=9000, kg=135, tanque=11,
        asiento=785, vel=6, abs=False, precio=10490000, vmax=130, consumo=36,
        cil=1, refrig="Líquida", tipo="4T, DOHC, monocilíndrico, 4V",
        freno_d="Disco Ø290 mm", freno_t="Disco Ø187 mm",
        llanta_d="90/80 R17", llanta_t="130/70 R17",
    ),
    "Suzuki|GSX-R150": dict(
        cc=147, hp=19.2, rpm=10500, nm=14, rpm_nm=9000, kg=131, tanque=11,
        asiento=785, vel=6, abs=True, precio=12990000, vmax=140, consumo=35,
        cil=1, refrig="Líquida", tipo="4T, DOHC, monocilíndrico, 4V",
        freno_d="Disco Ø290 mm", freno_t="Disco Ø187 mm",
        llanta_d="90/80 R17", llanta_t="130/70 R17",
    ),
    "Suzuki|V-Strom 250": dict(
        cc=249, hp=26.5, rpm=9300, nm=22.2, rpm_nm=7300, kg=167, tanque=12,
        asiento=835, vel=6, abs=True, abs_doble=True,
        precio=18990000, vmax=140, consumo=32, cil=1, refrig="Líquida",
        tipo="4T, SOHC, monocilíndrico, 4V",
        freno_d="Disco Ø310 mm", freno_t="Disco Ø240 mm",
        llanta_d="100/90-19", llanta_t="140/70 R17",
    ),
    "Suzuki|V-Strom 650": dict(
        cc=645, hp=70, rpm=8800, nm=62, rpm_nm=6500, kg=216, tanque=20,
        asiento=835, vel=6, abs=True, abs_doble=True, tc=True,
        precio=49990000, vmax=190, consumo=22, cil=2, refrig="Líquida",
        tipo="4T, DOHC, bicilíndrico en V a 90°, 8V",
        freno_d="Doble disco Ø310 mm", freno_t="Disco Ø260 mm",
        llanta_d="110/80 R19", llanta_t="150/70 R17",
    ),
    "Suzuki|GN125": dict(
        cc=124, hp=12.5, rpm=9000, nm=9.8, rpm_nm=7000, kg=110, tanque=10,
        asiento=735, vel=5, abs=False, precio=5990000, vmax=95, consumo=48,
        cil=1, refrig="Aire", tipo="4T, SOHC, monocilíndrico, 2V",
        freno_d="Disco Ø240 mm", freno_t="Tambor",
        llanta_d="2.75-18", llanta_t="3.50-16",
    ),
    "Suzuki|DR150": dict(
        cc=149, hp=12.3, rpm=8000, nm=11.6, rpm_nm=6000, kg=135, tanque=12,
        asiento=825, vel=5, abs=False, precio=7490000, vmax=105, consumo=42,
        cil=1, refrig="Aire", tipo="4T, SOHC, monocilíndrico, 2V",
        freno_d="Disco Ø240 mm", freno_t="Tambor",
        llanta_d="2.75-21", llanta_t="4.10-18",
    ),
    "Suzuki|Burgman 200": dict(
        cc=199, hp=18.1, rpm=8000, nm=17.4, rpm_nm=6000, kg=163, tanque=10.5,
        asiento=735, abs=True, precio=18990000, vmax=120, consumo=32, cil=1,
        refrig="Líquida", tipo="4T, SOHC, monocilíndrico, 4V",
        freno_d="Disco Ø260 mm", freno_t="Disco Ø240 mm",
        llanta_d="110/90-13", llanta_t="130/70-13",
        extra={
            "transmision": {"tipo_caja": "Automática CVT",
                            "transmision_final": "Correa"},
        },
    ),
    "Suzuki|Hayabusa": dict(
        cc=1340, hp=190, rpm=9700, nm=150, rpm_nm=7000, kg=266, tanque=20,
        asiento=800, vel=6, abs=True, abs_doble=True, tc=True,
        precio=129990000, vmax=299, consumo=14, cil=4, refrig="Líquida",
        tipo="4T, DOHC, 4 cilindros en línea, 16V",
        freno_d="Doble disco Brembo Ø320 mm", freno_t="Disco Ø260 mm",
        llanta_d="120/70 ZR17", llanta_t="190/50 ZR17",
        extra={
            "tecnologia": {"tablero": "TFT a color", "iluminacion": "LED",
                           "modos_conduccion": "3 modos", "quickshifter": True,
                           "control_crucero": True},
        },
    ),

    # ==========================================================
    # BAJAJ
    # ==========================================================
    "Bajaj|Pulsar NS125": dict(
        cc=124.4, hp=12, rpm=8500, nm=11, rpm_nm=7000, kg=144, tanque=12,
        asiento=805, vel=5, abs=False, cbs=True, precio=6990000, vmax=100,
        consumo=48, cil=1, refrig="Aire", tipo="4T, SOHC, monocilíndrico, 4V",
        freno_d="Disco Ø240 mm", freno_t="Tambor",
        llanta_d="80/100 R17", llanta_t="100/90 R17",
    ),
    "Bajaj|Pulsar NS160": dict(
        cc=160.3, hp=17.2, rpm=8500, nm=14.7, rpm_nm=6500, kg=151, tanque=12,
        asiento=805, vel=5, abs=True, precio=9490000, vmax=120, consumo=42,
        cil=1, refrig="Aceite", tipo="4T, SOHC, monocilíndrico, 4V",
        freno_d="Disco Ø260 mm", freno_t="Disco Ø230 mm",
        llanta_d="90/90 R17", llanta_t="120/80 R17",
    ),
    "Bajaj|Pulsar NS200": dict(
        cc=199.5, hp=24.13, rpm=9750, nm=18.74, rpm_nm=8000, kg=158, tanque=12,
        asiento=805, vel=6, abs=True, precio=11490000, vmax=136, consumo=36,
        cil=1, refrig="Líquida", tipo="4T, SOHC, monocilíndrico, 4V",
        comp="11.0:1", freno_d="Disco Ø300 mm", freno_t="Disco Ø230 mm",
        llanta_d="100/80 R17", llanta_t="130/70 R17",
    ),
    "Bajaj|Pulsar RS200": dict(
        cc=199.5, hp=24.5, rpm=9750, nm=18.7, rpm_nm=8000, kg=166, tanque=13,
        asiento=810, vel=6, abs=True, precio=12990000, vmax=140, consumo=34,
        cil=1, refrig="Líquida", tipo="4T, SOHC, monocilíndrico, 4V",
        freno_d="Disco Ø300 mm", freno_t="Disco Ø230 mm",
        llanta_d="100/80 R17", llanta_t="130/70 R17",
    ),
    "Bajaj|Pulsar NS400Z": dict(
        cc=373, hp=40, rpm=8800, nm=35, rpm_nm=6500, kg=174, tanque=12,
        asiento=807, vel=6, abs=True, abs_doble=True, tc=True,
        precio=15990000, vmax=160, consumo=30, cil=1, refrig="Líquida",
        tipo="4T, DOHC, monocilíndrico, 4V",
        freno_d="Disco Ø320 mm", freno_t="Disco Ø230 mm",
        llanta_d="110/70 R17", llanta_t="150/60 R17",
        extra={
            "tecnologia": {"tablero": "TFT a color", "iluminacion": "Full LED",
                           "modos_conduccion": "3 modos"},
        },
    ),
    "Bajaj|Boxer CT100": dict(
        cc=102, hp=7.9, rpm=7500, nm=8.3, rpm_nm=5500, kg=113, tanque=10.5,
        asiento=800, vel=4, abs=False, precio=4990000, vmax=90, consumo=60,
        cil=1, refrig="Aire", tipo="4T, SOHC, monocilíndrico, 2V",
        freno_d="Tambor", freno_t="Tambor",
        llanta_d="2.75-17", llanta_t="3.00-17",
    ),
    "Bajaj|Platina 110": dict(
        cc=115.2, hp=8.6, rpm=7500, nm=9.81, rpm_nm=5000, kg=121, tanque=11.5,
        asiento=805, vel=4, abs=False, cbs=True, precio=5690000, vmax=95,
        consumo=65, cil=1, refrig="Aire", tipo="4T, SOHC, monocilíndrico, 2V",
        freno_d="Tambor", freno_t="Tambor",
        llanta_d="2.75-17", llanta_t="3.00-17",
    ),
    "Bajaj|Dominar 400": dict(
        cc=373, hp=40, rpm=8800, nm=35, rpm_nm=6500, kg=193, tanque=13,
        asiento=800, vel=6, abs=True, abs_doble=True,
        precio=13990000, vmax=150, consumo=28, cil=1, refrig="Líquida",
        tipo="4T, DOHC, monocilíndrico, 4V",
        freno_d="Disco Ø320 mm", freno_t="Disco Ø230 mm",
        llanta_d="110/70 R17", llanta_t="150/60 R17",
    ),
    "Bajaj|Avenger 220": dict(
        cc=219.9, hp=19, rpm=8500, nm=17.55, rpm_nm=7000, kg=163, tanque=13,
        asiento=730, vel=5, abs=True, precio=10990000, vmax=120, consumo=38,
        cil=1, refrig="Aire", tipo="4T, SOHC, monocilíndrico, 2V",
        freno_d="Disco Ø260 mm", freno_t="Tambor",
        llanta_d="90/90-17", llanta_t="130/80-15",
    ),

    # ==========================================================
    # AKT
    # ==========================================================
    "AKT|NKD 125": dict(
        cc=124.6, hp=11.5, rpm=8500, nm=10.5, rpm_nm=6500, kg=122, tanque=12.2,
        asiento=795, vel=5, abs=False, precio=6190000, vmax=100, consumo=50,
        cil=1, refrig="Aire", tipo="4T, SOHC, monocilíndrico, 2V",
        freno_d="Disco Ø240 mm", freno_t="Tambor",
        llanta_d="2.75-18", llanta_t="3.50-16",
    ),
    "AKT|NKD 125 EIII": dict(
        cc=124.6, hp=11.5, rpm=8500, nm=10.5, rpm_nm=6500, kg=122, tanque=12.2,
        asiento=795, vel=5, abs=False, precio=6490000, vmax=100, consumo=50,
        cil=1, refrig="Aire", tipo="4T, SOHC, monocilíndrico, 2V",
        version="EIII", freno_d="Disco Ø240 mm", freno_t="Tambor",
        llanta_d="2.75-18", llanta_t="3.50-16",
    ),
    "AKT|Special 110": dict(
        cc=109, hp=8.3, rpm=8000, nm=8.1, rpm_nm=6000, kg=105, tanque=9,
        asiento=770, vel=4, abs=False, precio=4690000, vmax=85, consumo=58,
        cil=1, refrig="Aire", tipo="4T, SOHC, monocilíndrico, 2V",
        freno_d="Tambor", freno_t="Tambor",
    ),
    "AKT|CR4 125": dict(
        cc=124.6, hp=11.2, rpm=8500, nm=10.5, rpm_nm=6500, kg=127, tanque=12,
        asiento=810, vel=5, abs=False, precio=6990000, vmax=105, consumo=48,
        cil=1, refrig="Aire", tipo="4T, SOHC, monocilíndrico, 2V",
        freno_d="Disco Ø240 mm", freno_t="Tambor",
        llanta_d="2.75-18", llanta_t="3.50-17",
    ),
    "AKT|Dynamic K 125": dict(
        cc=124.6, hp=11.5, rpm=8500, nm=10.5, rpm_nm=6500, kg=124, tanque=12,
        asiento=790, vel=5, abs=False, precio=6290000, vmax=100, consumo=50,
        cil=1, refrig="Aire", tipo="4T, SOHC, monocilíndrico, 2V",
        freno_d="Disco Ø240 mm", freno_t="Tambor",
    ),
    "AKT|TTR 200": dict(
        cc=197, hp=15.6, rpm=8000, nm=15.8, rpm_nm=6000, kg=139, tanque=12,
        asiento=860, vel=5, abs=False, precio=9990000, vmax=115, consumo=38,
        cil=1, refrig="Aire", tipo="4T, SOHC, monocilíndrico, 2V",
        freno_d="Disco Ø260 mm", freno_t="Tambor",
        llanta_d="2.75-21", llanta_t="4.10-18",
    ),
    "AKT|TT DS 200": dict(
        cc=197, hp=15.6, rpm=8000, nm=15.8, rpm_nm=6000, kg=144, tanque=12,
        asiento=850, vel=5, abs=False, precio=10490000, vmax=115, consumo=36,
        cil=1, refrig="Aire", tipo="4T, SOHC, monocilíndrico, 2V",
        freno_d="Disco Ø260 mm", freno_t="Tambor",
        llanta_d="2.75-21", llanta_t="4.10-18",
    ),

    # ==========================================================
    # TVS
    # ==========================================================
    "TVS|Apache RTR 160 4V": dict(
        cc=159.7, hp=17.55, rpm=9250, nm=14.73, rpm_nm=7250, kg=144, tanque=12,
        asiento=800, vel=5, abs=True, precio=9990000, vmax=114, consumo=45,
        cil=1, refrig="Aceite", tipo="4T, SOHC, monocilíndrico, 4V",
        freno_d="Disco Ø270 mm", freno_t="Disco Ø200 mm",
        llanta_d="90/90 R17", llanta_t="110/80 R17",
    ),
    "TVS|Apache RTR 200 4V": dict(
        cc=197.75, hp=20.82, rpm=9000, nm=17.25, rpm_nm=7250, kg=153, tanque=12,
        asiento=800, vel=5, abs=True, precio=12490000, vmax=127, consumo=40,
        cil=1, refrig="Aceite", tipo="4T, SOHC, monocilíndrico, 4V",
        freno_d="Disco Ø270 mm", freno_t="Disco Ø240 mm",
        llanta_d="90/90 R17", llanta_t="130/70 R17",
    ),
    "TVS|Apache RR 310": dict(
        cc=312.2, hp=34, rpm=9700, nm=27.3, rpm_nm=7700, kg=174, tanque=11,
        asiento=810, vel=6, abs=True, abs_doble=True, tc=True,
        precio=21990000, vmax=160, consumo=30, cil=1, refrig="Líquida",
        tipo="4T, DOHC, monocilíndrico, 4V",
        freno_d="Disco Ø300 mm", freno_t="Disco Ø240 mm",
        llanta_d="110/70 R17", llanta_t="150/60 R17",
        extra={
            "tecnologia": {"tablero": "TFT a color", "iluminacion": "Full LED",
                           "modos_conduccion": "4 modos"},
        },
    ),
    "TVS|Raider 125": dict(
        cc=124.8, hp=11.38, rpm=7500, nm=11.2, rpm_nm=6000, kg=123, tanque=10,
        asiento=780, vel=5, abs=False, cbs=True, precio=7990000, vmax=99,
        consumo=55, cil=1, refrig="Aire", tipo="4T, SOHC, monocilíndrico, 3V",
        freno_d="Disco Ø240 mm", freno_t="Tambor",
    ),
    "TVS|Ntorq 125": dict(
        cc=124.8, hp=9.4, rpm=7000, nm=10.5, rpm_nm=5500, kg=116, tanque=5.8,
        asiento=765, abs=False, cbs=True, precio=8490000, vmax=95, consumo=45,
        cil=1, refrig="Aire", tipo="4T, SOHC, monocilíndrico, 3V",
        extra={
            "transmision": {"tipo_caja": "Automática CVT",
                            "transmision_final": "Correa"},
            "tecnologia": {"tablero": "LCD", "iluminacion": "LED",
                           "conectividad": "SmartXonnect", "puerto_usb": True},
        },
    ),
    "TVS|Ronin 225": dict(
        cc=225.9, hp=20.4, rpm=7750, nm=19.93, rpm_nm=3750, kg=160, tanque=14,
        asiento=795, vel=5, abs=True, abs_doble=True,
        precio=13990000, vmax=120, consumo=38, cil=1, refrig="Aceite",
        tipo="4T, SOHC, monocilíndrico, 4V",
        freno_d="Disco Ø300 mm", freno_t="Disco Ø240 mm",
        llanta_d="110/70 R17", llanta_t="130/70 R17",
    ),

    # ==========================================================
    # HERO
    # ==========================================================
    "Hero|Xpulse 200": dict(
        cc=199.6, hp=18.08, rpm=8500, nm=16.15, rpm_nm=6500, kg=157, tanque=13,
        asiento=823, vel=5, abs=True, precio=11990000, vmax=110, consumo=35,
        cil=1, refrig="Aire", tipo="4T, SOHC, monocilíndrico, 2V",
        freno_d="Disco Ø276 mm", freno_t="Disco Ø220 mm",
        llanta_d="90/90-21", llanta_t="120/80-18",
    ),
    "Hero|Xpulse 200 4V": dict(
        cc=199.6, hp=18.9, rpm=8500, nm=17.35, rpm_nm=6500, kg=158, tanque=13,
        asiento=823, vel=5, abs=True, precio=12990000, vmax=112, consumo=34,
        cil=1, refrig="Aire", tipo="4T, SOHC, monocilíndrico, 4V",
        freno_d="Disco Ø276 mm", freno_t="Disco Ø220 mm",
        llanta_d="90/90-21", llanta_t="120/80-18",
    ),
    "Hero|Hunk 160R 4V": dict(
        cc=163.2, hp=16.8, rpm=8500, nm=14.2, rpm_nm=6500, kg=146, tanque=10,
        asiento=790, vel=5, abs=False, cbs=True, precio=9490000, vmax=110,
        consumo=42, cil=1, refrig="Aire", tipo="4T, SOHC, monocilíndrico, 4V",
        freno_d="Disco Ø276 mm", freno_t="Disco Ø220 mm",
        llanta_d="100/80 R17", llanta_t="130/70 R17",
    ),
    "Hero|Eco Deluxe": dict(
        cc=97.2, hp=7.7, rpm=8000, nm=7.9, rpm_nm=5000, kg=116, tanque=9.5,
        asiento=805, vel=4, abs=False, precio=4590000, vmax=80, consumo=65,
        cil=1, refrig="Aire", tipo="4T, SOHC, monocilíndrico, 2V",
        freno_d="Tambor", freno_t="Tambor",
    ),

    # ==========================================================
    # ROYAL ENFIELD
    # ==========================================================
    "Royal Enfield|Classic 350": dict(
        cc=349, hp=20.2, rpm=6100, nm=27, rpm_nm=4000, kg=195, tanque=13,
        asiento=805, vel=5, abs=True, abs_doble=True,
        precio=20990000, vmax=120, consumo=35, cil=1, refrig="Aire",
        tipo="4T, SOHC, monocilíndrico J, 2V",
        freno_d="Disco Ø300 mm", freno_t="Disco Ø270 mm",
        llanta_d="100/90-19", llanta_t="120/80-18",
    ),
    "Royal Enfield|Hunter 350": dict(
        cc=349, hp=20.2, rpm=6100, nm=27, rpm_nm=4000, kg=181, tanque=13,
        asiento=790, vel=5, abs=True, abs_doble=True,
        precio=18990000, vmax=120, consumo=36, cil=1, refrig="Aire",
        tipo="4T, SOHC, monocilíndrico J, 2V",
        freno_d="Disco Ø300 mm", freno_t="Disco Ø270 mm",
        llanta_d="110/70-17", llanta_t="140/70-17",
    ),
    "Royal Enfield|Meteor 350": dict(
        cc=349, hp=20.2, rpm=6100, nm=27, rpm_nm=4000, kg=191, tanque=15,
        asiento=765, vel=5, abs=True, abs_doble=True,
        precio=21990000, vmax=115, consumo=35, cil=1, refrig="Aire",
        tipo="4T, SOHC, monocilíndrico J, 2V",
        freno_d="Disco Ø300 mm", freno_t="Disco Ø270 mm",
    ),
    "Royal Enfield|Himalayan 411": dict(
        cc=411, hp=24.3, rpm=6500, nm=32, rpm_nm=4250, kg=199, tanque=15,
        asiento=800, vel=5, abs=True, abs_doble=True,
        precio=22990000, vmax=130, consumo=32, cil=1, refrig="Aire-aceite",
        tipo="4T, SOHC, monocilíndrico, 4V",
        freno_d="Disco Ø300 mm", freno_t="Disco Ø240 mm",
        llanta_d="90/90-21", llanta_t="120/90-17",
    ),
    "Royal Enfield|Himalayan 450": dict(
        cc=452, hp=39.5, rpm=8000, nm=40, rpm_nm=5500, kg=196, tanque=17,
        asiento=825, vel=6, abs=True, abs_doble=True, tc=True,
        precio=29990000, vmax=150, consumo=30, cil=1, refrig="Líquida",
        tipo="4T, DOHC, monocilíndrico Sherpa 450, 4V",
        freno_d="Disco Ø320 mm", freno_t="Disco Ø270 mm",
        llanta_d="90/90-21", llanta_t="140/80-17",
        extra={
            "tecnologia": {"tablero": "TFT circular a color",
                           "iluminacion": "Full LED",
                           "modos_conduccion": "2 modos",
                           "conectividad": "Google Maps (RE App)"},
        },
    ),
    "Royal Enfield|Scram 411": dict(
        cc=411, hp=24.3, rpm=6500, nm=32, rpm_nm=4250, kg=185, tanque=15,
        asiento=795, vel=5, abs=True, precio=20990000, vmax=125, consumo=33,
        cil=1, refrig="Aire-aceite", tipo="4T, SOHC, monocilíndrico, 4V",
        freno_d="Disco Ø300 mm", freno_t="Disco Ø240 mm",
        llanta_d="19\" delantera", llanta_t="17\" trasera",
    ),
    "Royal Enfield|Continental GT 650": dict(
        cc=648, hp=47, rpm=7250, nm=52, rpm_nm=5150, kg=198, tanque=12.5,
        asiento=793, vel=6, abs=True, abs_doble=True,
        precio=31990000, vmax=170, consumo=28, cil=2, refrig="Aire-aceite",
        tipo="4T, SOHC, bicilíndrico paralelo, 8V",
        freno_d="Doble disco Ø320 mm", freno_t="Disco Ø240 mm",
        llanta_d="100/90-18", llanta_t="130/70-18",
    ),
    "Royal Enfield|Interceptor 650": dict(
        cc=648, hp=47, rpm=7250, nm=52, rpm_nm=5150, kg=202, tanque=13.7,
        asiento=804, vel=6, abs=True, abs_doble=True,
        precio=30990000, vmax=170, consumo=28, cil=2, refrig="Aire-aceite",
        tipo="4T, SOHC, bicilíndrico paralelo, 8V",
        freno_d="Doble disco Ø320 mm", freno_t="Disco Ø240 mm",
        llanta_d="100/90-18", llanta_t="130/70-18",
    ),
    "Royal Enfield|Super Meteor 650": dict(
        cc=648, hp=47, rpm=7250, nm=52, rpm_nm=5150, kg=241, tanque=15.7,
        asiento=740, vel=6, abs=True, abs_doble=True,
        precio=34990000, vmax=160, consumo=26, cil=2, refrig="Aire-aceite",
        tipo="4T, SOHC, bicilíndrico paralelo, 8V",
        freno_d="Disco Ø320 mm", freno_t="Disco Ø300 mm",
        llanta_d="100/90-19", llanta_t="150/80-16",
    ),
    "Royal Enfield|Guerrilla 450": dict(
        cc=452, hp=39.5, rpm=8000, nm=40, rpm_nm=5500, kg=185, tanque=11,
        asiento=780, vel=6, abs=True, abs_doble=True, tc=True,
        precio=25990000, vmax=150, consumo=30, cil=1, refrig="Líquida",
        tipo="4T, DOHC, monocilíndrico Sherpa 450, 4V",
        freno_d="Disco Ø320 mm", freno_t="Disco Ø270 mm",
        llanta_d="120/70-17", llanta_t="160/60-17",
    ),

    # ==========================================================
    # KTM
    # ==========================================================
    "KTM|Duke 200": dict(
        cc=199.5, hp=25, rpm=10000, nm=19.2, rpm_nm=8000, kg=159, tanque=13.4,
        asiento=822, vel=6, abs=True, abs_doble=True,
        precio=16990000, vmax=138, consumo=34, cil=1, refrig="Líquida",
        tipo="4T, DOHC, monocilíndrico, 4V",
        freno_d="Disco Ø320 mm", freno_t="Disco Ø230 mm",
        llanta_d="110/70 R17", llanta_t="150/60 R17",
        extra={
            "tecnologia": {"tablero": "LCD", "iluminacion": "LED",
                           "modos_conduccion": "No"},
        },
    ),
    "KTM|Duke 250": dict(
        cc=249, hp=30.5, rpm=9000, nm=24, rpm_nm=7250, kg=162, tanque=13.4,
        asiento=830, vel=6, abs=True, abs_doble=True, tc=True,
        precio=21990000, vmax=148, consumo=32, cil=1, refrig="Líquida",
        tipo="4T, DOHC, monocilíndrico, 4V",
        freno_d="Disco Ø320 mm", freno_t="Disco Ø230 mm",
        llanta_d="110/70 R17", llanta_t="150/60 R17",
        extra={
            "tecnologia": {"tablero": "TFT a color", "iluminacion": "Full LED",
                           "modos_conduccion": "2 modos", "quickshifter": True,
                           "conectividad": "KTM My Ride"},
        },
    ),
    "KTM|Duke 390": dict(
        cc=398.7, hp=44, rpm=8500, nm=37, rpm_nm=7000, kg=165, tanque=15,
        asiento=820, vel=6, abs=True, abs_doble=True, tc=True,
        precio=28990000, vmax=170, consumo=28, cil=1, refrig="Líquida",
        tipo="4T, DOHC, monocilíndrico, 4V",
        freno_d="Disco Ø320 mm", freno_t="Disco Ø230 mm",
        llanta_d="110/70 R17", llanta_t="150/60 R17",
        extra={
            "tecnologia": {"tablero": "TFT a color", "iluminacion": "Full LED",
                           "modos_conduccion": "2 modos", "quickshifter": True,
                           "conectividad": "KTM My Ride"},
        },
    ),
    "KTM|RC 200": dict(
        cc=199.5, hp=25, rpm=10000, nm=19.2, rpm_nm=8000, kg=160, tanque=13.4,
        asiento=835, vel=6, abs=True, abs_doble=True,
        precio=17990000, vmax=140, consumo=33, cil=1, refrig="Líquida",
        tipo="4T, DOHC, monocilíndrico, 4V",
        freno_d="Disco Ø320 mm", freno_t="Disco Ø230 mm",
        llanta_d="110/70 R17", llanta_t="150/60 R17",
    ),
    "KTM|RC 390": dict(
        cc=373, hp=44, rpm=9000, nm=36, rpm_nm=7000, kg=172, tanque=13.4,
        asiento=820, vel=6, abs=True, abs_doble=True, tc=True,
        precio=27990000, vmax=170, consumo=28, cil=1, refrig="Líquida",
        tipo="4T, DOHC, monocilíndrico, 4V",
        freno_d="Disco Ø320 mm", freno_t="Disco Ø230 mm",
        llanta_d="110/70 R17", llanta_t="150/60 R17",
        extra={
            "tecnologia": {"tablero": "TFT a color", "iluminacion": "Full LED",
                           "modos_conduccion": "2 modos", "quickshifter": True},
        },
    ),
    "KTM|390 Adventure": dict(
        cc=373, hp=43, rpm=9000, nm=37, rpm_nm=7000, kg=172, tanque=14.5,
        asiento=855, vel=6, abs=True, abs_doble=True, tc=True,
        precio=27990000, vmax=160, consumo=28, cil=1, refrig="Líquida",
        tipo="4T, DOHC, monocilíndrico, 4V",
        freno_d="Disco Ø320 mm", freno_t="Disco Ø230 mm",
        llanta_d="100/90-19", llanta_t="130/80-17",
        extra={
            "suspension": {"delantera": "Horquilla WP Apex Ø43 mm",
                           "trasera": "Monoamortiguador WP Apex",
                           "recorrido_delantero_mm": 170,
                           "recorrido_trasero_mm": 177},
        },
    ),
    "KTM|Duke 790": dict(
        cc=799, hp=105, rpm=9000, nm=87, rpm_nm=8000, kg=169, tanque=14,
        asiento=825, vel=6, abs=True, abs_doble=True, tc=True,
        precio=49990000, vmax=220, consumo=20, cil=2, refrig="Líquida",
        tipo="4T, DOHC, bicilíndrico paralelo, 8V",
        freno_d="Doble disco Ø300 mm", freno_t="Disco Ø240 mm",
        llanta_d="120/70 R17", llanta_t="180/55 R17",
    ),

    # ==========================================================
    # BMW MOTORRAD
    # ==========================================================
    "BMW Motorrad|G 310 GS": dict(
        cc=313, hp=34, rpm=9500, nm=28, rpm_nm=7500, kg=169, tanque=11,
        asiento=835, vel=6, abs=True, abs_doble=True,
        precio=29990000, vmax=143, consumo=30, cil=1, refrig="Líquida",
        tipo="4T, DOHC, monocilíndrico, 4V",
        freno_d="Disco Ø300 mm", freno_t="Disco Ø240 mm",
        llanta_d="110/80 R19", llanta_t="150/70 R17",
    ),
    "BMW Motorrad|F 850 GS": dict(
        cc=853, hp=95, rpm=8250, nm=92, rpm_nm=6250, kg=229, tanque=15,
        asiento=860, vel=6, abs=True, abs_doble=True, tc=True,
        precio=62990000, vmax=200, consumo=20, cil=2, refrig="Líquida",
        tipo="4T, DOHC, bicilíndrico en línea, 8V",
        freno_d="Doble disco Ø305 mm", freno_t="Disco Ø265 mm",
        llanta_d="90/90-21", llanta_t="150/70 R17",
    ),
    "BMW Motorrad|R 1250 GS": dict(
        cc=1254, hp=136, rpm=7750, nm=143, rpm_nm=6250, kg=249, tanque=20,
        asiento=850, vel=6, abs=True, abs_doble=True, tc=True,
        precio=119990000, vmax=210, consumo=18, cil=2, refrig="Aire-líquida",
        tipo="4T, DOHC, bicilíndrico bóxer, 8V",
        freno_d="Doble disco Ø305 mm", freno_t="Disco Ø276 mm",
        llanta_d="120/70 R19", llanta_t="170/60 R17",
        extra={
            "tecnologia": {"tablero": "TFT a color", "iluminacion": "Full LED",
                           "modos_conduccion": "2 modos", "control_crucero": True,
                           "quickshifter": True,
                           "conectividad": "BMW Motorrad Connected"},
            "transmision": {"transmision_final": "Eje cardán"},
        },
    ),
    "BMW Motorrad|R 1300 GS": dict(
        cc=1300, hp=145, rpm=7750, nm=149, rpm_nm=6500, kg=237, tanque=19,
        asiento=850, vel=6, abs=True, abs_doble=True, tc=True,
        precio=129990000, vmax=220, consumo=18, cil=2, refrig="Aire-líquida",
        tipo="4T, DOHC, bicilíndrico bóxer, 8V",
        freno_d="Doble disco Ø310 mm", freno_t="Disco Ø285 mm",
        llanta_d="120/70 R19", llanta_t="170/60 R17",
        extra={
            "tecnologia": {"tablero": "TFT a color", "iluminacion": "Full LED",
                           "modos_conduccion": "4 modos", "control_crucero": True,
                           "quickshifter": True,
                           "conectividad": "BMW Motorrad Connected"},
            "transmision": {"transmision_final": "Eje cardán"},
        },
    ),
    "BMW Motorrad|S 1000 RR": dict(
        cc=999, hp=205, rpm=13000, nm=113, rpm_nm=11000, kg=197, tanque=16.5,
        asiento=824, vel=6, abs=True, abs_doble=True, tc=True,
        precio=119990000, vmax=299, consumo=15, cil=4, refrig="Líquida",
        tipo="4T, DOHC, 4 cilindros en línea, 16V",
        freno_d="Doble disco Ø320 mm", freno_t="Disco Ø220 mm",
        llanta_d="120/70 ZR17", llanta_t="190/55 ZR17",
        extra={
            "tecnologia": {"tablero": "TFT a color", "iluminacion": "LED",
                           "modos_conduccion": "4 modos", "quickshifter": True,
                           "control_crucero": True},
        },
    ),
    "BMW Motorrad|C 400 GT": dict(
        cc=350, hp=34, rpm=7500, nm=35, rpm_nm=6000, kg=214, tanque=12.8,
        asiento=765, abs=True, abs_doble=True, tc=True,
        precio=42990000, vmax=140, consumo=28, cil=1, refrig="Líquida",
        tipo="4T, SOHC, monocilíndrico, 4V",
        extra={
            "transmision": {"tipo_caja": "Automática CVT",
                            "transmision_final": "Correa"},
            "tecnologia": {"tablero": "TFT a color", "iluminacion": "Full LED",
                           "conectividad": "BMW Motorrad Connected",
                           "puerto_usb": True},
        },
    ),

    # ==========================================================
    # DUCATI
    # ==========================================================
    "Ducati|Panigale V4": dict(
        cc=1103, hp=210, rpm=13500, nm=123, rpm_nm=10000, kg=195, tanque=17,
        asiento=850, vel=6, abs=True, abs_doble=True, tc=True,
        precio=139990000, vmax=299, consumo=13, cil=4, refrig="Líquida",
        tipo="4T, Desmodromico, V4 a 90°, 16V",
        freno_d="Doble disco Ø330 mm Brembo", freno_t="Disco Ø245 mm",
        llanta_d="120/70 ZR17", llanta_t="200/60 ZR17",
        extra={
            "tecnologia": {"tablero": "TFT a color", "iluminacion": "Full LED",
                           "modos_conduccion": "4 modos", "quickshifter": True,
                           "control_crucero": True},
        },
    ),
    "Ducati|Monster": dict(
        cc=937, hp=111, rpm=9250, nm=93, rpm_nm=6500, kg=188, tanque=14,
        asiento=820, vel=6, abs=True, abs_doble=True, tc=True,
        precio=79990000, vmax=220, consumo=19, cil=2, refrig="Líquida",
        tipo="4T, Desmodromico, bicilíndrico en L, 8V",
        freno_d="Doble disco Ø320 mm", freno_t="Disco Ø245 mm",
        llanta_d="120/70 ZR17", llanta_t="180/55 ZR17",
    ),
    "Ducati|Multistrada V4": dict(
        cc=1158, hp=170, rpm=10500, nm=125, rpm_nm=8750, kg=229, tanque=22,
        asiento=840, vel=6, abs=True, abs_doble=True, tc=True,
        precio=129990000, vmax=240, consumo=17, cil=4, refrig="Líquida",
        tipo="4T, V4 Granturismo, 16V",
        freno_d="Doble disco Ø330 mm", freno_t="Disco Ø265 mm",
        llanta_d="120/70 R19", llanta_t="170/60 R17",
        extra={
            "tecnologia": {"tablero": "TFT a color", "iluminacion": "Full LED",
                           "modos_conduccion": "4 modos", "quickshifter": True,
                           "control_crucero": True,
                           "conectividad": "Ducati Connect"},
        },
    ),
    "Ducati|Scrambler Icon": dict(
        cc=803, hp=73, rpm=8250, nm=66.2, rpm_nm=5750, kg=189, tanque=13.5,
        asiento=795, vel=6, abs=True, precio=59990000, vmax=190, consumo=22,
        cil=2, refrig="Aire", tipo="4T, Desmodromico, bicilíndrico en L, 4V",
        freno_d="Disco Ø330 mm", freno_t="Disco Ø245 mm",
        llanta_d="110/80 R18", llanta_t="180/55 R17",
    ),
    "Ducati|Streetfighter V4": dict(
        cc=1103, hp=208, rpm=13000, nm=123, rpm_nm=9500, kg=201, tanque=16,
        asiento=845, vel=6, abs=True, abs_doble=True, tc=True,
        precio=119990000, vmax=290, consumo=13, cil=4, refrig="Líquida",
        tipo="4T, Desmodromico, V4 a 90°, 16V",
        freno_d="Doble disco Ø330 mm Brembo", freno_t="Disco Ø245 mm",
        llanta_d="120/70 ZR17", llanta_t="200/60 ZR17",
    ),

    # ==========================================================
    # TRIUMPH
    # ==========================================================
    "Triumph|Trident 660": dict(
        cc=660, hp=81, rpm=10250, nm=64, rpm_nm=6250, kg=189, tanque=14,
        asiento=805, vel=6, abs=True, abs_doble=True, tc=True,
        precio=54990000, vmax=210, consumo=22, cil=3, refrig="Líquida",
        tipo="4T, DOHC, tricilíndrico en línea, 12V",
        freno_d="Doble disco Ø310 mm", freno_t="Disco Ø255 mm",
        llanta_d="120/70 R17", llanta_t="180/55 R17",
        extra={
            "tecnologia": {"tablero": "TFT a color", "iluminacion": "Full LED",
                           "modos_conduccion": "2 modos", "quickshifter": True},
        },
    ),
    "Triumph|Street Triple 765": dict(
        cc=765, hp=120, rpm=11500, nm=80, rpm_nm=9500, kg=188, tanque=15,
        asiento=836, vel=6, abs=True, abs_doble=True, tc=True,
        precio=74990000, vmax=230, consumo=20, cil=3, refrig="Líquida",
        tipo="4T, DOHC, tricilíndrico en línea, 12V",
        freno_d="Doble disco Ø310 mm", freno_t="Disco Ø220 mm",
        llanta_d="120/70 R17", llanta_t="180/55 R17",
        extra={
            "tecnologia": {"tablero": "TFT a color", "iluminacion": "Full LED",
                           "modos_conduccion": "4 modos", "quickshifter": True},
        },
    ),
    "Triumph|Tiger 900": dict(
        cc=888, hp=107, rpm=8500, nm=90, rpm_nm=7250, kg=228, tanque=20,
        asiento=810, vel=6, abs=True, abs_doble=True, tc=True,
        precio=79990000, vmax=210, consumo=21, cil=3, refrig="Líquida",
        tipo="4T, DOHC, tricilíndrico T-Plane, 12V",
        freno_d="Doble disco Ø320 mm", freno_t="Disco Ø255 mm",
        llanta_d="100/90-19", llanta_t="150/70 R17",
        extra={
            "tecnologia": {"tablero": "TFT a color", "iluminacion": "Full LED",
                           "modos_conduccion": "4 modos", "quickshifter": True,
                           "control_crucero": True},
        },
    ),
    "Triumph|Bonneville T120": dict(
        cc=1200, hp=79, rpm=6550, nm=105, rpm_nm=3500, kg=236, tanque=14.5,
        asiento=790, vel=6, abs=True, abs_doble=True, tc=True,
        precio=69990000, vmax=175, consumo=22, cil=2, refrig="Líquida",
        tipo="4T, SOHC, bicilíndrico paralelo, 8V",
        freno_d="Doble disco Ø310 mm", freno_t="Disco Ø255 mm",
        llanta_d="100/90-18", llanta_t="150/70-17",
    ),
    "Triumph|Scrambler 400 X": dict(
        cc=398, hp=40, rpm=8000, nm=37.5, rpm_nm=6500, kg=179, tanque=13,
        asiento=835, vel=6, abs=True, abs_doble=True, tc=True,
        precio=29990000, vmax=150, consumo=30, cil=1, refrig="Líquida",
        tipo="4T, DOHC, monocilíndrico, 4V",
        freno_d="Disco Ø320 mm", freno_t="Disco Ø230 mm",
        llanta_d="100/90-19", llanta_t="140/80-17",
    ),

    # ==========================================================
    # APRILIA
    # ==========================================================
    "Aprilia|RS 660": dict(
        cc=659, hp=100, rpm=10500, nm=67, rpm_nm=8500, kg=183, tanque=15,
        asiento=820, vel=6, abs=True, abs_doble=True, tc=True,
        precio=69990000, vmax=230, consumo=20, cil=2, refrig="Líquida",
        tipo="4T, DOHC, bicilíndrico paralelo, 8V",
        freno_d="Doble disco Ø320 mm", freno_t="Disco Ø220 mm",
        llanta_d="120/70 ZR17", llanta_t="180/55 ZR17",
        extra={
            "tecnologia": {"tablero": "TFT a color", "iluminacion": "Full LED",
                           "modos_conduccion": "5 modos", "quickshifter": True,
                           "control_crucero": True},
        },
    ),
    "Aprilia|RSV4": dict(
        cc=1099, hp=217, rpm=13000, nm=125, rpm_nm=10500, kg=202, tanque=17.9,
        asiento=845, vel=6, abs=True, abs_doble=True, tc=True,
        precio=129990000, vmax=299, consumo=13, cil=4, refrig="Líquida",
        tipo="4T, DOHC, V4 a 65°, 16V",
        freno_d="Doble disco Ø330 mm Brembo", freno_t="Disco Ø220 mm",
        llanta_d="120/70 ZR17", llanta_t="200/55 ZR17",
    ),
    "Aprilia|Tuono 660": dict(
        cc=659, hp=100, rpm=10500, nm=67, rpm_nm=8500, kg=183, tanque=15,
        asiento=820, vel=6, abs=True, abs_doble=True, tc=True,
        precio=67990000, vmax=230, consumo=20, cil=2, refrig="Líquida",
        tipo="4T, DOHC, bicilíndrico paralelo, 8V",
        freno_d="Doble disco Ø320 mm", freno_t="Disco Ø220 mm",
        llanta_d="120/70 ZR17", llanta_t="180/55 ZR17",
    ),

    # ==========================================================
    # HUSQVARNA
    # ==========================================================
    "Husqvarna|Svartpilen 401": dict(
        cc=398.7, hp=44, rpm=9000, nm=37, rpm_nm=7000, kg=152, tanque=9.5,
        asiento=835, vel=6, abs=True, abs_doble=True, tc=True,
        precio=27990000, vmax=160, consumo=30, cil=1, refrig="Líquida",
        tipo="4T, DOHC, monocilíndrico, 4V",
        freno_d="Disco Ø320 mm", freno_t="Disco Ø230 mm",
        llanta_d="110/70 R17", llanta_t="150/60 R17",
    ),
    "Husqvarna|Vitpilen 401": dict(
        cc=398.7, hp=44, rpm=9000, nm=37, rpm_nm=7000, kg=152, tanque=9.5,
        asiento=835, vel=6, abs=True, abs_doble=True, tc=True,
        precio=27990000, vmax=160, consumo=30, cil=1, refrig="Líquida",
        tipo="4T, DOHC, monocilíndrico, 4V",
        freno_d="Disco Ø320 mm", freno_t="Disco Ø230 mm",
        llanta_d="110/70 R17", llanta_t="150/60 R17",
    ),
    "Husqvarna|Norden 901": dict(
        cc=889, hp=105, rpm=8000, nm=100, rpm_nm=6500, kg=204, tanque=19,
        asiento=854, vel=6, abs=True, abs_doble=True, tc=True,
        precio=79990000, vmax=200, consumo=20, cil=2, refrig="Líquida",
        tipo="4T, DOHC, bicilíndrico paralelo, 8V",
        freno_d="Doble disco Ø320 mm", freno_t="Disco Ø260 mm",
        llanta_d="90/90-21", llanta_t="150/70 R18",
    ),

    # ==========================================================
    # CFMOTO
    # ==========================================================
    "CFMOTO|250NK": dict(
        cc=250, hp=27, rpm=9750, nm=22, rpm_nm=7500, kg=151, tanque=12.5,
        asiento=795, vel=6, abs=True, abs_doble=True,
        precio=15990000, vmax=130, consumo=32, cil=1, refrig="Líquida",
        tipo="4T, DOHC, monocilíndrico, 4V",
        freno_d="Disco Ø300 mm", freno_t="Disco Ø240 mm",
        llanta_d="110/70 R17", llanta_t="150/60 R17",
    ),
    "CFMOTO|450MT": dict(
        cc=449, hp=44, rpm=8500, nm=44, rpm_nm=6250, kg=175, tanque=17.5,
        asiento=820, vel=6, abs=True, abs_doble=True, tc=True,
        precio=32990000, vmax=160, consumo=28, cil=2, refrig="Líquida",
        tipo="4T, DOHC, bicilíndrico paralelo, 8V",
        freno_d="Doble disco Ø320 mm", freno_t="Disco Ø240 mm",
        llanta_d="90/90-21", llanta_t="140/70-17",
        extra={
            "tecnologia": {"tablero": "TFT a color", "iluminacion": "Full LED",
                           "modos_conduccion": "2 modos",
                           "conectividad": "CFMOTO Ride"},
        },
    ),
    "CFMOTO|450SR": dict(
        cc=449, hp=50, rpm=9500, nm=39, rpm_nm=7600, kg=168, tanque=14,
        asiento=795, vel=6, abs=True, abs_doble=True, tc=True,
        precio=27990000, vmax=190, consumo=26, cil=2, refrig="Líquida",
        tipo="4T, DOHC, bicilíndrico paralelo, 8V",
        freno_d="Doble disco Ø320 mm", freno_t="Disco Ø240 mm",
        llanta_d="110/70 R17", llanta_t="150/60 R17",
        extra={
            "tecnologia": {"tablero": "TFT a color", "iluminacion": "Full LED",
                           "modos_conduccion": "2 modos",
                           "conectividad": "CFMOTO Ride"},
        },
    ),
    "CFMOTO|675SR-R": dict(
        cc=674, hp=95, rpm=11000, nm=70, rpm_nm=8250, kg=195, tanque=15,
        asiento=810, vel=6, abs=True, abs_doble=True, tc=True,
        precio=45990000, vmax=230, consumo=20, cil=3, refrig="Líquida",
        tipo="4T, DOHC, tricilíndrico en línea, 12V",
        freno_d="Doble disco Ø320 mm", freno_t="Disco Ø245 mm",
        llanta_d="120/70 R17", llanta_t="180/55 R17",
        extra={
            "tecnologia": {"tablero": "TFT a color", "iluminacion": "Full LED",
                           "quickshifter": True, "modos_conduccion": "3 modos"},
        },
    ),
    "CFMOTO|800MT": dict(
        cc=799, hp=95, rpm=9000, nm=75, rpm_nm=7500, kg=231, tanque=19,
        asiento=825, vel=6, abs=True, abs_doble=True, tc=True,
        precio=59990000, vmax=200, consumo=20, cil=2, refrig="Líquida",
        tipo="4T, DOHC, bicilíndrico paralelo, 8V",
        freno_d="Doble disco Ø320 mm", freno_t="Disco Ø260 mm",
        llanta_d="110/80 R19", llanta_t="150/70 R17",
        extra={
            "tecnologia": {"tablero": "TFT a color", "iluminacion": "Full LED",
                           "modos_conduccion": "2 modos", "quickshifter": True,
                           "control_crucero": True},
        },
    ),
    "CFMOTO|650MT": dict(
        cc=649, hp=70, rpm=8750, nm=62, rpm_nm=7000, kg=218, tanque=18,
        asiento=840, vel=6, abs=True, abs_doble=True,
        precio=41990000, vmax=180, consumo=22, cil=2, refrig="Líquida",
        tipo="4T, DOHC, bicilíndrico paralelo, 8V",
        freno_d="Doble disco Ø300 mm", freno_t="Disco Ø240 mm",
        llanta_d="110/80 R19", llanta_t="150/70 R17",
    ),
    "CFMOTO|700MT": dict(
        cc=693, hp=75, rpm=8750, nm=68, rpm_nm=6500, kg=226, tanque=18,
        asiento=840, vel=6, abs=True, abs_doble=True,
        precio=47990000, vmax=190, consumo=21, cil=2, refrig="Líquida",
        tipo="4T, DOHC, bicilíndrico paralelo, 8V",
        freno_d="Doble disco Ø320 mm", freno_t="Disco Ø240 mm",
        llanta_d="110/80 R19", llanta_t="150/70 R17",
    ),

    # ==========================================================
    # BENELLI
    # ==========================================================
    "Benelli|TRK 502": dict(
        cc=500, hp=47, rpm=8500, nm=46, rpm_nm=6000, kg=235, tanque=20,
        asiento=820, vel=6, abs=True, abs_doble=True,
        precio=36990000, vmax=170, consumo=24, cil=2, refrig="Líquida",
        tipo="4T, DOHC, bicilíndrico paralelo, 8V",
        freno_d="Doble disco Ø320 mm", freno_t="Disco Ø260 mm",
        llanta_d="120/70 R17", llanta_t="160/60 R17",
    ),
    "Benelli|TRK 702": dict(
        cc=698, hp=76, rpm=8500, nm=68.2, rpm_nm=6250, kg=220, tanque=20,
        asiento=830, vel=6, abs=True, abs_doble=True,
        precio=43990000, vmax=180, consumo=22, cil=2, refrig="Líquida",
        tipo="4T, DOHC, bicilíndrico paralelo, 8V",
        freno_d="Doble disco Ø320 mm", freno_t="Disco Ø260 mm",
        llanta_d="110/80 R19", llanta_t="150/70 R17",
    ),
    "Benelli|TNT 150": dict(
        cc=149, hp=13.4, rpm=8000, nm=13.5, rpm_nm=6000, kg=155, tanque=13.5,
        asiento=780, vel=5, abs=True, precio=9990000, vmax=110, consumo=42,
        cil=1, refrig="Aire", tipo="4T, SOHC, monocilíndrico, 2V",
        freno_d="Disco Ø280 mm", freno_t="Disco Ø240 mm",
        llanta_d="110/70 R17", llanta_t="140/70 R17",
    ),
    "Benelli|Leoncino 500": dict(
        cc=500, hp=47, rpm=8500, nm=46, rpm_nm=6000, kg=207, tanque=12.7,
        asiento=800, vel=6, abs=True, abs_doble=True,
        precio=32990000, vmax=160, consumo=25, cil=2, refrig="Líquida",
        tipo="4T, DOHC, bicilíndrico paralelo, 8V",
        freno_d="Doble disco Ø320 mm", freno_t="Disco Ø260 mm",
        llanta_d="120/70 R17", llanta_t="160/60 R17",
    ),

    # ==========================================================
    # SCOOTERS Y OTRAS MARCAS
    # ==========================================================
    "Kymco|Agility 125": dict(
        cc=125, hp=9.5, rpm=7500, nm=9.8, rpm_nm=6000, kg=105, tanque=5,
        asiento=780, abs=False, precio=7490000, vmax=90, consumo=50, cil=1,
        refrig="Aire", tipo="4T, SOHC, monocilíndrico, 2V",
        extra={
            "transmision": {"tipo_caja": "Automática CVT",
                            "transmision_final": "Correa"},
        },
    ),
    "Vespa|Primavera 150": dict(
        cc=155, hp=12.9, rpm=7750, nm=12.8, rpm_nm=6500, kg=114, tanque=8,
        asiento=790, abs=True, precio=21990000, vmax=100, consumo=42, cil=1,
        refrig="Aire", tipo="4T, SOHC, monocilíndrico, 3V",
        llanta_d="110/70-11", llanta_t="120/70-11",
        extra={
            "transmision": {"tipo_caja": "Automática CVT",
                            "transmision_final": "Correa"},
            "tecnologia": {"tablero": "LCD", "iluminacion": "LED",
                           "puerto_usb": True, "conectividad": "Vespa MIA"},
        },
    ),
    "Vespa|GTS 300": dict(
        cc=278, hp=23.8, rpm=7750, nm=26, rpm_nm=5250, kg=158, tanque=8.5,
        asiento=790, abs=True, tc=True, precio=32990000, vmax=130,
        consumo=32, cil=1, refrig="Líquida", tipo="4T, SOHC, monocilíndrico, 4V",
        llanta_d="120/70-12", llanta_t="130/70-12",
        extra={
            "transmision": {"tipo_caja": "Automática CVT",
                            "transmision_final": "Correa"},
            "tecnologia": {"tablero": "LCD", "iluminacion": "LED",
                           "puerto_usb": True, "conectividad": "Vespa MIA"},
        },
    ),
    "Piaggio|Liberty 150": dict(
        cc=155, hp=12.9, rpm=7750, nm=13, rpm_nm=6500, kg=124, tanque=6,
        asiento=790, abs=True, precio=17990000, vmax=100, consumo=42, cil=1,
        refrig="Aire", tipo="4T, SOHC, monocilíndrico, 3V",
        extra={
            "transmision": {"tipo_caja": "Automática CVT",
                            "transmision_final": "Correa"},
        },
    ),
    "SYM|Cruisym 300": dict(
        cc=278, hp=27, rpm=7500, nm=27.5, rpm_nm=5750, kg=198, tanque=12,
        asiento=760, abs=True, tc=True, precio=24990000, vmax=130,
        consumo=28, cil=1, refrig="Líquida", tipo="4T, SOHC, monocilíndrico, 4V",
        extra={
            "transmision": {"tipo_caja": "Automática CVT",
                            "transmision_final": "Correa"},
        },
    ),
    "Victory|MRX 125": dict(
        cc=124, hp=12, rpm=8000, nm=10, rpm_nm=6000, kg=121, tanque=12,
        asiento=820, vel=5, abs=False, precio=6490000, vmax=105, consumo=45,
        cil=1, refrig="Aire", tipo="4T, SOHC, monocilíndrico, 2V",
        freno_d="Disco Ø240 mm", freno_t="Tambor",
        llanta_d="2.75-21", llanta_t="4.10-18",
    ),
    "Victory|MRX 150": dict(
        cc=149, hp=13.9, rpm=8000, nm=13, rpm_nm=6000, kg=131, tanque=12.5,
        asiento=825, vel=5, abs=False, precio=7490000, vmax=110, consumo=42,
        cil=1, refrig="Aire", tipo="4T, SOHC, monocilíndrico, 2V",
        freno_d="Disco Ø240 mm", freno_t="Tambor",
        llanta_d="2.75-21", llanta_t="4.10-18",
    ),
    "NIU|NQi": dict(
        cc=None, hp=None, kg=90, asiento=780, abs=False, precio=12990000,
        vmax=70, anio=2025, refrig="Aire",
        tipo="Motor eléctrico de 3 kW con batería de litio",
        extra={
            "motor": {"potencia_kw": 3, "combustible": "Eléctrico",
                      "alimentacion": "Batería de litio 60 V"},
            "rendimiento": {"autonomia_km": 100},
            "transmision": {"tipo_caja": "Automática", "transmision_final": "Correa"},
            "comercial": {"garantia": "2 años en batería (referencia)"},
        },
    ),
}

# ==============================================================
# EXPANSIÓN AL ESQUEMA COMPLETO DE LA FICHA
# ==============================================================

# Notación corta -> (sección de la ficha, campo del esquema)
CAMPOS = {
    "cc": ("motor", "cilindrada_cc"),
    "hp": ("motor", "potencia_hp"),
    "rpm": ("motor", "rpm_potencia"),
    "nm": ("motor", "torque_nm"),
    "rpm_nm": ("motor", "rpm_torque"),
    "kg": ("dimensiones", "peso_operacion_kg"),
    "tanque": ("dimensiones", "capacidad_tanque_l"),
    "asiento": ("dimensiones", "altura_asiento_mm"),
    "vel": ("transmision", "velocidades"),
    "abs": ("frenos", "abs"),
    "abs_doble": ("frenos", "abs_doble_canal"),
    "cbs": ("frenos", "cbs"),
    "tc": ("frenos", "control_traccion"),
    "precio": ("comercial", "precio_nuevo_cop"),
    "vmax": ("rendimiento", "velocidad_maxima_kmh"),
    "consumo": ("rendimiento", "consumo_km_l"),
    "anio": ("identificacion", "anio"),
    "estado": ("identificacion", "estado_comercial"),
    "version": ("identificacion", "version"),
    "tipo": ("motor", "tipo"),
    "cil": ("motor", "cilindros"),
    "refrig": ("motor", "refrigeracion"),
    "alim": ("motor", "alimentacion"),
    "comp": ("motor", "compresion"),
    "arranque": ("motor", "arranque"),
    "freno_d": ("frenos", "delantero"),
    "freno_t": ("frenos", "trasero"),
    "llanta_d": ("llantas", "delantera"),
    "llanta_t": ("llantas", "trasera"),
    "rines": ("llantas", "rines"),
}


def _expandir(datos):
    """Convierte la notación corta al esquema anidado de la ficha."""
    ficha = {}
    for clave, valor in datos.items():
        if clave in ("imagen", "imagen_credito"):
            ficha[clave] = valor
            continue
        if clave == "extra":
            for seccion, campos in valor.items():
                ficha.setdefault(seccion, {}).update(campos)
            continue
        seccion, campo = CAMPOS[clave]
        ficha.setdefault(seccion, {})[campo] = valor
    return ficha


DATOS = {clave: _expandir(datos) for clave, datos in MOTOS.items()}

