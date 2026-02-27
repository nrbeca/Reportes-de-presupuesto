# ============================================================================
# CONFIGURACIÓN GLOBAL PARA SADER REPORTES
# ============================================================================

from datetime import date, timedelta
from dateutil.relativedelta import relativedelta, MO
from decimal import Decimal, ROUND_HALF_UP
try:
    from num2words import num2words
except ImportError:
    def num2words(n, lang='es'):
        return str(n)

# ============================================================================
# LOGO BASE64
# ============================================================================

LOGO_BASE64 = """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
"""
# ============================================================================
# MESES Y MAPEOS
# ============================================================================

MONTH_NAMES = ['ENE', 'FEB', 'MAR', 'ABR', 'MAY', 'JUN', 'JUL', 'AGO', 'SEP', 'OCT', 'NOV', 'DIC']
MONTH_NAMES_FULL = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                    'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

MONTH_MAP = {name: idx + 1 for idx, name in enumerate(MONTH_NAMES)}

# ============================================================================
# MAPEO DE URs (compartido entre MAP y SICOP)
# ============================================================================

UR_MAP = {
    121: 260, 122: 261, 123: 262, 124: 263, 125: 264, 126: 265, 127: 266, 128: 267,
    129: 268, 130: 269, 131: 270, 132: 271, 133: 272, 134: 273, 135: 274, 136: 275,
    137: 276, 138: 277, 139: 278, 140: 279, 141: 280, 142: 281, 143: 282, 144: 283,
    145: 284, 146: 285, 147: 286, 148: 287, 149: 288, 150: 289, 151: 290, 152: 291,
    153: 292, 108: 810, 215: 220, 300: 225, 310: 226, 700: 227, 600: 230, 612: 231,
    312: 232, 315: 233, 400: 235, 311: 237, 314: 245, 113: 250
}

# ============================================================================
# CONFIGURACIÓN MAP - PROGRAMAS 2025
# ============================================================================

PROGRAMAS_NOMBRES_2025 = {
    'B004': 'Adquisición de leche nacional',
    'S052': 'Programa de Abasto Social de Leche a cargo de Liconsa, S.A. de C.V.',
    'S053': 'Programa de Abasto Rural a cargo de Diconsa, S.A. de C.V.',
    'S263': 'Sanidad e Inocuidad Agroalimentaria',
    'S290': 'Precios de Garantía a Productos Alimentarios Básicos',
    'S292': 'Fertilizantes',
    'S293': 'Producción para el Bienestar',
    'S304': 'Programa de Fomento a la Agricultura, Ganadería, Pesca y Acuicultura',
    'P001': 'Diseño y Aplicación de la Política Agropecuaria',
    'E001': 'Desarrollo, aplicación de programas educativos e investigación en materia agroalimentaria',
    'E006': 'Generación de Proyectos de Investigación',
    'G001': 'Regulación, supervisión y aplicación de las políticas públicas en materia agropecuaria',
    'O001': 'Actividades de apoyo a la función pública y buen gobierno',
    'M001': 'Actividades de apoyo administrativo',
    'U027': 'Cosechando Soberanía',
    'W001': 'Operaciones ajenas',
}

PROGRAMAS_ESPECIFICOS_2025 = ['B004', 'S052', 'S053', 'S263', 'S290', 'S292', 'S293', 'S304']

NOMBRES_ESPECIALES_2025 = {
    'S263': 'Sanidad e Inocuidad Agroalimentaria 3/',
    'S293': 'Producción para el Bienestar 4/',
    'S304': 'Programa de Fomento a la Agricultura, Ganadería, Pesca y Acuicultura 5/',
}

FUSION_PROGRAMAS_2025 = {}

# ============================================================================
# CONFIGURACIÓN MAP - PROGRAMAS 2026
# ============================================================================

PROGRAMAS_NOMBRES_2026 = {
    'S052': 'Programa de Abasto Social y Precios de Garantía a cargo de Leche para el Bienestar, S.A. de C.V.',
    'S053': 'Programa de Abasto Rural',
    'S263': 'Sanidad e Inocuidad Agroalimentaria',
    'S290': 'Acopio para el Bienestar',
    'S292': 'Fertilizantes para el Bienestar',
    'S293': 'Producción para el Bienestar',
    'S304': 'Pesca y Acuacultura Sustentables',
    'B006': 'Adquisición, industrialización y comercialización de productos agroalimentarios',
    'B004': 'Adquisición de leche nacional',
    'P001': 'Diseño y Aplicación de la Política Agropecuaria',
    'E001': 'Desarrollo, aplicación de programas educativos e investigación en materia agroalimentaria',
    'E006': 'Generación de Proyectos de Investigación',
    'G001': 'Regulación, supervisión y aplicación de las políticas públicas',
    'M001': 'Actividades de apoyo administrativo',
    'O001': 'Actividades de apoyo a la función pública y buen gobierno',
    'W001': 'Operaciones ajenas',
}

PROGRAMAS_ESPECIFICOS_2026 = ['S052', 'S053', 'S263', 'S290', 'S292', 'S293', 'S304', 'B006']

NOMBRES_ESPECIALES_2026 = {
    'S263': 'Sanidad e Inocuidad Agroalimentaria 3/',
    'S293': 'Producción para el Bienestar 4/',
    'S304': 'Pesca y Acuacultura Sustentables 5/',
}

FUSION_PROGRAMAS_2026 = {
    'B004': 'B006',
}

# ============================================================================
# CONFIGURACIÓN SICOP - DENOMINACIONES URs 2025
# ============================================================================

DENOMINACIONES_2025 = {
    '100': 'Secretaría',
    '109': 'Dirección General de Normalización Agroalimentaria',
    '110': 'Unidad de Asuntos Jurídicos, Derechos Humanos y Normalización',
    '111': 'Dirección General de Comunicación Social',
    '112': 'Dirección General de Enlace Legislativo',
    '117': 'Coordinación General de Asuntos Internacionales',
    '200': 'Subsecretaría de Agricultura y Desarrollo Rural',
    '212': 'Dirección General de Organización para la Productividad',
    '214': 'Dirección General de la Autosuficiencia Alimentaria',
    '220': 'Coordinación General de Bienestar para el Campo',
    '221': 'Dirección General de Fertilizantes para el Bienestar',
    '222': 'Dirección General de Producción para el Bienestar',
    '225': 'Coordinación General de Producción Agrícola y Ganadera',
    '226': 'Dirección General de Producción Agrícola',
    '227': 'Dirección General de Producción Ganadera',
    '228': 'Dirección General de Implementación de Acuerdos Sectoriales',
    '230': 'Coordinación General de Comercialización y Financiamiento',
    '231': 'Dirección General de Precios y Ordenamiento Comercial',
    '232': 'Dirección General de Financiamiento y Gestión de Riesgos',
    '233': 'Dirección General de Agregación de Valor y Comercialización',
    '235': 'Coordinación General de Eficiencia Hídrica Agroalimentaria',
    '236': 'Dirección General de Eficiencia Hídrica en el Riego',
    '237': 'Dirección General de Eficiencia Hídrica en el Temporal',
    '240': 'Coordinación General de Innovación y Transición Agroecológica',
    '241': 'Dirección General de Innovación',
    '242': 'Dirección General de Transición Agroecológica',
    '245': 'Coordinación General de Sustentabilidad y Resiliencia Climática',
    '246': 'Dirección General de Sustentabilidad',
    '247': 'Dirección General de Financiamiento Verde',
    '250': 'Coordinación General de Operación Territorial',
    '251': 'Dirección General de Integración Territorial de Programas',
    '252': 'Dirección General de Intervención Territorial Estratégica',
    '260': 'Oficina de Representación en Aguascalientes',
    '261': 'Oficina de Representación en Baja California',
    '262': 'Oficina de Representación en Baja California Sur',
    '263': 'Oficina de Representación en Campeche',
    '264': 'Oficina de Representación en Coahuila',
    '265': 'Oficina de Representación en Colima',
    '266': 'Oficina de Representación en Chiapas',
    '267': 'Oficina de Representación en Chihuahua',
    '268': 'Oficina de Representación en la Ciudad de México',
    '269': 'Oficina de Representación en Durango',
    '270': 'Oficina de Representación en Guanajuato',
    '271': 'Oficina de Representación en Guerrero',
    '272': 'Oficina de Representación en Hidalgo',
    '273': 'Oficina de Representación en Jalisco',
    '274': 'Oficina de Representación en el Estado de México',
    '275': 'Oficina de Representación en Michoacán',
    '276': 'Oficina de Representación en Morelos',
    '277': 'Oficina de Representación en Nayarit',
    '278': 'Oficina de Representación en Nuevo León',
    '279': 'Oficina de Representación en Oaxaca',
    '280': 'Oficina de Representación en Puebla',
    '281': 'Oficina de Representación en Querétaro',
    '282': 'Oficina de Representación en Quintana Roo',
    '283': 'Oficina de Representación en San Luis Potosí',
    '284': 'Oficina de Representación en Sinaloa',
    '285': 'Oficina de Representación en Sonora',
    '286': 'Oficina de Representación en Tabasco',
    '287': 'Oficina de Representación en Tamaulipas',
    '288': 'Oficina de Representación en Tlaxcala',
    '289': 'Oficina de Representación en Veracruz',
    '290': 'Oficina de Representación en Yucatán',
    '291': 'Oficina de Representación en Zacatecas',
    '292': 'Oficina de Representación en la Región Lagunera',
    '410': 'Dirección General de Fortalecimiento a la Agricultura Familiar',
    '411': 'Dirección General de Integración Económica',
    '413': 'Dirección General de Investigación, Desarrollo Tecnológico y Extensionismo',
    '500': 'Unidad de Administración y Finanzas',
    '510': 'Dirección General de Programación, Presupuesto y Finanzas',
    '511': 'Dirección General de Capital Humano y Desarrollo Organizacional',
    '512': 'Dirección General de Recursos Materiales, Inmuebles y Servicios',
    '513': 'Dirección General de Tecnologías de la Información y Comunicaciones',
    '610': 'Dirección General de Comercialización',
    '611': 'Dirección General de Administración de Riesgos de Precios',
    '710': 'Dirección General de Repoblamiento Ganadero',
    '711': 'Dirección General de Sustentabilidad de Tierras de Uso Ganadero',
    '800': 'Coordinación General de Información, Inteligencia y Evaluación',
    '810': 'Dirección General de Evaluación, Políticas y Programas',
    '811': 'Dirección General del Servicio de Información Agroalimentaria y Pesquera',
    '812': 'Dirección General de Planeación',
    'B00': 'Servicio Nacional de Sanidad, Inocuidad y Calidad Agroalimentaria',
    'C00': 'Servicio Nacional de Inspección y Certificación de Semillas',
    'D00': 'Colegio Superior Agropecuario del Estado de Guerrero',
    'I00': 'Comisión Nacional de Acuacultura y Pesca',
    'A1I': 'Universidad Autónoma Chapingo',
    'AFU': 'Comité Nacional para el Desarrollo Sustentable de la Caña de Azúcar',
    'I6L': 'Fideicomiso de Riesgo Compartido',
    'I9H': 'Instituto Nacional para el Desarrollo de Capacidades del Sector Rural, A.C.',
    'IZC': 'Colegio de Postgraduados',
    'IZI': 'Comisión Nacional de las Zonas Áridas',
    'JAG': 'Instituto Nacional de Investigaciones Forestales, Agrícolas y Pecuarias',
    'JBP': 'Seguridad Alimentaria Mexicana',
    'RJL': 'Instituto Mexicano de Investigación en Pesca y Acuacultura Sustentables',
    'VSS': 'Alimentación para el Bienestar, S.A de C.V.',
    'VST': 'Leche para el Bienestar, S.A. de C.V.',
}

SECTOR_CENTRAL_2025 = ['100', '109', '110', '111', '112', '117', '200', '212', '214',
                       '220', '221', '222', '225', '226', '227', '228', '230', '231', '232', '233',
                       '235', '236', '237', '240', '241', '242', '245', '246', '247', '250', '251', '252',
                       '410', '411', '413', '500', '510', '511', '512', '513',
                       '610', '611', '710', '711', '800', '810', '811', '812']

OFICINAS_2025 = ['260', '261', '262', '263', '264', '265', '266', '267', '268', '269',
                 '270', '271', '272', '273', '274', '275', '276', '277', '278', '279',
                 '280', '281', '282', '283', '284', '285', '286', '287', '288', '289',
                 '290', '291', '292']

ORGANOS_DESCONCENTRADOS_2025 = ['B00', 'C00', 'D00', 'I00']

ENTIDADES_PARAESTATALES_2025 = ['A1I', 'AFU', 'I6L', 'I9H', 'IZC', 'IZI', 'JAG', 'JBP', 'RJL', 'VSS', 'VST']

MAPEO_UR_2025 = {
    'G00': '811', 108: '810', 113: '250',
    121: '260', 122: '261', 123: '262', 124: '263', 125: '264', 126: '265', 127: '266', 128: '267', 129: '268', 130: '269',
    131: '270', 132: '271', 133: '272', 134: '273', 135: '274', 136: '275', 137: '276', 138: '277', 139: '278', 140: '279',
    141: '280', 142: '281', 143: '282', 144: '283', 145: '284', 146: '285', 147: '286', 148: '287', 149: '288', 150: '289',
    151: '290', 152: '291', 153: '292',
    215: '220', 300: '225', 310: '226', 700: '227', 600: '230', 612: '231', 312: '232', 315: '233', 400: '235', 311: '237', 314: '245',
}

# ============================================================================
# CONFIGURACIÓN SICOP - DENOMINACIONES URs 2026
# ============================================================================

DENOMINACIONES_2026 = {
    '100': 'Secretaría',
    '110': 'Unidad de Asuntos Jurídicos',
    '106': 'Coordinación de Legislación y Consulta',
    '107': 'Coordinación de lo Contencioso',
    '111': 'Dirección General de Comunicación Social',
    '112': 'Coordinación de Atención Legislativa',
    '117': 'Coordinación de Asuntos Internacionales',
    '119': 'Dirección General de Planeación y Evaluación de Políticas y Programas',
    '120': 'Dirección General del Servicio de Información Agroalimentaria y Pesquera',
    '200': 'Subsecretaría de Agricultura y Desarrollo Rural',
    '220': 'Unidad de Bienestar para el Campo',
    '221': 'Dirección General de Fertilizantes para el Bienestar',
    '222': 'Dirección General de Producción para el Bienestar',
    '250': 'Unidad de Operación Territorial y Eficiencia Hídrica Agroalimentaria',
    '252': 'Dirección General de Intervención Territorial Estratégica',
    '253': 'Dirección General de Eficacia Hídrica en Riego y Temporal',
    '260': 'Oficina de Representación en Aguascalientes',
    '261': 'Oficina de Representación en Baja California',
    '262': 'Oficina de Representación en Baja California Sur',
    '263': 'Oficina de Representación en Campeche',
    '264': 'Oficina de Representación en Coahuila',
    '265': 'Oficina de Representación en Colima',
    '266': 'Oficina de Representación en Chiapas',
    '267': 'Oficina de Representación en Chihuahua',
    '268': 'Oficina de Representación en la Ciudad de México',
    '269': 'Oficina de Representación en Durango',
    '270': 'Oficina de Representación en Guanajuato',
    '271': 'Oficina de Representación en Guerrero',
    '272': 'Oficina de Representación en Hidalgo',
    '273': 'Oficina de Representación en Jalisco',
    '274': 'Oficina de Representación en el Estado de México',
    '275': 'Oficina de Representación en Michoacán',
    '276': 'Oficina de Representación en Morelos',
    '277': 'Oficina de Representación en Nayarit',
    '278': 'Oficina de Representación en Nuevo León',
    '279': 'Oficina de Representación en Oaxaca',
    '280': 'Oficina de Representación en Puebla',
    '281': 'Oficina de Representación en Querétaro',
    '282': 'Oficina de Representación en Quintana Roo',
    '283': 'Oficina de Representación en San Luis Potosí',
    '284': 'Oficina de Representación en Sinaloa',
    '285': 'Oficina de Representación en Sonora',
    '286': 'Oficina de Representación en Tabasco',
    '287': 'Oficina de Representación en Tamaulipas',
    '288': 'Oficina de Representación en Tlaxcala',
    '289': 'Oficina de Representación en Veracruz',
    '290': 'Oficina de Representación en Yucatán',
    '291': 'Oficina de Representación en Zacatecas',
    '292': 'Oficina de Representación en la Región Lagunera',
    '500': 'Unidad de Administración y Finanzas',
    '510': 'Dirección General de Programación, Presupuesto y Finanzas',
    '511': 'Dirección General de Capital Humano y Desarrollo Organizacional',
    '512': 'Dirección General de Recursos Materiales, Inmuebles y Servicios',
    '513': 'Dirección General de Tecnologías de la Información y Comunicaciones',
    '900': 'Coordinación General de Producción, Comercialización, Sustentabilidad e Innovación',
    '910': 'Unidad de Innovación, Sustentabilidad y Resiliencia Climática',
    '911': 'Dirección General de Desarrollo e Innovación',
    '912': 'Dirección General de Sustentabilidad y Resiliencia Climática',
    '920': 'Unidad de Producción, Comercialización y Financiamiento',
    '921': 'Dirección General de Producción Agrícola',
    '922': 'Dirección General de Producción Ganadera, Pesquera y Acuícola',
    '923': 'Dirección General de Precios, Ordenamiento Comercial y Valor Agregado',
    '924': 'Dirección General de Financiamiento y Gestión de Riesgos',
    'B00': 'Servicio Nacional de Sanidad, Inocuidad y Calidad Agroalimentaria',
    'C00': 'Servicio Nacional de Inspección y Certificación de Semillas',
    'D00': 'Colegio Superior Agropecuario del Estado de Guerrero',
    'I00': 'Comisión Nacional de Acuacultura y Pesca',
    'A1I': 'Universidad Autónoma Chapingo',
    'AFU': 'Comité Nacional para el Desarrollo Sustentable de la Caña de Azúcar',
    'I6L': 'Fideicomiso de Riesgo Compartido',
    'I9H': 'Instituto Nacional para el Desarrollo de Capacidades del Sector Rural, A.C.',
    'IZC': 'Colegio de Postgraduados',
    'IZI': 'Comisión Nacional de las Zonas Áridas',
    'JAG': 'Instituto Nacional de Investigaciones Forestales, Agrícolas y Pecuarias',
    'JAL': 'Productora de Semillas para el Bienestar',
    'JBK': 'Productora Nacional de Biológicos Veterinarios',
    'RJL': 'Instituto Mexicano de Investigación en Pesca y Acuacultura Sustentables',
    'VSS': 'Alimentación para el Bienestar, S.A de C.V.',
    'VST': 'Leche para el Bienestar, S.A. de C.V.',
}

SECTOR_CENTRAL_2026 = ['100', '110', '106', '107', '111', '112', '117', '119', '120', '200',
                       '220', '221', '222', '250', '252', '253',
                       '500', '510', '511', '512', '513',
                       '900', '910', '911', '912', '920', '921', '922', '923', '924']

OFICINAS_2026 = ['260', '261', '262', '263', '264', '265', '266', '267', '268', '269',
                 '270', '271', '272', '273', '274', '275', '276', '277', '278', '279',
                 '280', '281', '282', '283', '284', '285', '286', '287', '288', '289',
                 '290', '291', '292']

ORGANOS_DESCONCENTRADOS_2026 = ['B00', 'C00', 'D00', 'I00']

ENTIDADES_PARAESTATALES_2026 = ['A1I', 'AFU', 'I6L', 'I9H', 'IZC', 'IZI', 'JAG', 'JAL', 'JBK', 'RJL', 'VSS', 'VST']

MAPEO_UR_2026_BASE = {
    'G00': '811', 108: '810', 113: '250',
    121: '260', 122: '261', 123: '262', 124: '263', 125: '264', 126: '265', 127: '266', 128: '267', 129: '268', 130: '269',
    131: '270', 132: '271', 133: '272', 134: '273', 135: '274', 136: '275', 137: '276', 138: '277', 139: '278', 140: '279',
    141: '280', 142: '281', 143: '282', 144: '283', 145: '284', 146: '285', 147: '286', 148: '287', 149: '288', 150: '289',
    151: '290', 152: '291', 153: '292',
    215: '220', 300: '225', 310: '226', 700: '227', 600: '230', 612: '231', 312: '232', 315: '233', 400: '235', 311: '237', 314: '245',
}

FUSION_URS_2026 = {
    '810': '119', '812': '119',
    '800': '120', '811': '120',
    '235': '250',
    '236': '253', '237': '253',
    '225': '900',
    '245': '910',
    '241': '911',
    '246': '912', '247': '912',
    '230': '920',
    '226': '921',
    '227': '922',
    '231': '923',
    '232': '924',
}

# ============================================================================
# FUNCIONES AUXILIARES
# ============================================================================

def round_like_excel(value, decimals=2):
    """Redondea como Excel (ROUND_HALF_UP)"""
    import pandas as pd
    if pd.isna(value):
        return 0
    d = Decimal(str(value))
    return float(d.quantize(Decimal(10) ** -decimals, rounding=ROUND_HALF_UP))


def numero_a_letras_mx(numero):
    """Convierte número a texto en español mexicano"""
    entero = int(numero)
    centavos = int(round((numero - entero) * 100))
    if entero == 0:
        texto_entero = "Cero"
    else:
        texto_entero = num2words(entero, lang='es').title()
        texto_entero = texto_entero.replace('Mil Millones', 'Mil millones')
        texto_entero = texto_entero.replace('Millones', 'millones')
        texto_entero = texto_entero.replace('Millón', 'millón')
        texto_entero = texto_entero.replace('Mil ', 'mil ')
    return f"{texto_entero} pesos {centavos:02d}/100 M.N."


def formatear_fecha(fecha):
    """Formatea fecha en español"""
    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
             "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    return f"{fecha.day} de {meses[fecha.month - 1]} de {fecha.year}"


def obtener_ultimo_dia_habil(fecha_referencia=None):
    """Obtiene el último día hábil antes de la fecha de referencia"""
    if fecha_referencia is None:
        fecha_referencia = date.today()
    año_actual = fecha_referencia.year
    festivos = [
        date(año_actual, 1, 1), date(año_actual, 5, 1), date(año_actual, 5, 5),
        date(año_actual, 9, 16), date(año_actual, 12, 25),
        date(año_actual, 2, 1) + relativedelta(weekday=MO(1)),
        date(año_actual, 3, 1) + relativedelta(weekday=MO(3)),
        date(año_actual, 11, 1) + relativedelta(weekday=MO(3))
    ]
    dia_analizado = fecha_referencia - timedelta(days=1)
    while True:
        if dia_analizado.weekday() < 5 and dia_analizado not in festivos:
            break
        dia_analizado -= timedelta(days=1)
    return dia_analizado


def detectar_fecha_archivo(filename):
    """Detecta la fecha del nombre del archivo"""
    import re
    month_match = re.search(
        r'(\d{2})[-_]?(ENE|FEB|MAR|ABR|MAY|JUN|JUL|AGO|SEP|OCT|NOV|DIC)[-_]?(\d{4})?',
        filename, re.IGNORECASE
    )
    if month_match:
        dia = int(month_match.group(1))
        mes_nombre = month_match.group(2).upper()
        año = int(month_match.group(3)) if month_match.group(3) else date.today().year
        mes = MONTH_MAP[mes_nombre]
        return date(año, mes, dia), mes, año
    return date.today(), date.today().month, date.today().year


def get_config_by_year(año):
    """Obtiene la configuración según el año"""
    if año <= 2025:
        return {
            'programas_nombres': PROGRAMAS_NOMBRES_2025,
            'programas_especificos': PROGRAMAS_ESPECIFICOS_2025,
            'nombres_especiales': NOMBRES_ESPECIALES_2025,
            'fusion_programas': FUSION_PROGRAMAS_2025,
            'denominaciones': DENOMINACIONES_2025,
            'sector_central': SECTOR_CENTRAL_2025,
            'oficinas': OFICINAS_2025,
            'organos_desconcentrados': ORGANOS_DESCONCENTRADOS_2025,
            'entidades_paraestatales': ENTIDADES_PARAESTATALES_2025,
            'mapeo_ur': MAPEO_UR_2025,
            'fusion_urs': {},
            'usar_2026': False,
        }
    else:
        return {
            'programas_nombres': PROGRAMAS_NOMBRES_2026,
            'programas_especificos': PROGRAMAS_ESPECIFICOS_2026,
            'nombres_especiales': NOMBRES_ESPECIALES_2026,
            'fusion_programas': FUSION_PROGRAMAS_2026,
            'denominaciones': DENOMINACIONES_2026,
            'sector_central': SECTOR_CENTRAL_2026,
            'oficinas': OFICINAS_2026,
            'organos_desconcentrados': ORGANOS_DESCONCENTRADOS_2026,
            'entidades_paraestatales': ENTIDADES_PARAESTATALES_2026,
            'mapeo_ur': MAPEO_UR_2026_BASE,
            'fusion_urs': FUSION_URS_2026,
            'usar_2026': True,
        }

# ============================================================================
# CATÁLOGO DE PARTIDAS ESPECÍFICAS
# ============================================================================

PARTIDAS_ESPECIFICAS = {
    11101: 'Dietas (Ramos Autónomos)',
    11201: 'Haberes',
    11301: 'Sueldos base',
    11401: 'Retribuciones por adscripción en el extranjero',
    12101: 'Honorarios',
    12201: 'Remuneraciones al personal eventual',
    12202: 'Compensaciones a sustitutos de profesores',
    12301: 'Retribuciones por servicios en período de formación profesional',
    12401: 'Retribución a los representantes de los trabajadores y de los patrones en la Junta Federal de Conciliación y Arbitraje',
    13101: 'Prima quinquenal por años de servicios efectivos prestados',
    13102: 'Acreditación por años de servicio en la docencia y al personal administrativo de las instituciones de educación superior',
    13103: 'Prima de perseverancia por años de servicio activo en el Ejército, Fuerza Aérea y Armada Mexicanos',
    13104: 'Antigüedad',
    13201: 'Primas de vacaciones y dominical',
    13202: 'Aguinaldo o gratificación de fin de año',
    13204: 'Primas de vacaciones y dominical de áreas administrativas (Ramos Autónomos)',
    13301: 'Remuneraciones por horas extraordinarias',
    13401: 'Acreditación por titulación en la docencia',
    13402: 'Acreditación al personal docente por años de estudio de licenciatura',
    13403: 'Compensaciones por servicios especiales',
    13404: 'Compensaciones por servicios eventuales',
    13405: 'Compensaciones de retiro',
    13406: 'Compensaciones de servicios',
    13407: 'Compensaciones adicionales por servicios especiales',
    13408: 'Asignaciones docentes, pedagógicas genéricas y específicas',
    13409: 'Compensación por adquisición de material didáctico',
    13410: 'Compensación por actualización y formación académica',
    13411: 'Compensaciones a médicos residentes',
    13412: 'Gastos contingentes para el personal radicado en el extranjero',
    13413: 'Asignaciones para la conclusión de servicios en la Administración Pública Federal',
    13414: 'Asignaciones conforme al régimen laboral',
    13501: 'Sobrehaberes',
    13601: 'Asignaciones de técnico',
    13602: 'Asignaciones de mando',
    13603: 'Asignaciones por comisión',
    13604: 'Asignaciones de vuelo',
    13605: 'Asignaciones de técnico especial',
    13701: 'Honorarios especiales',
    13801: 'Participaciones por vigilancia en el cumplimiento de las leyes y custodia de valores',
    14101: 'Aportaciones al ISSSTE',
    14102: 'Aportaciones al ISSFAM',
    14103: 'Aportaciones al IMSS',
    14104: 'Aportaciones de seguridad social contractuales',
    14105: 'Aportaciones al seguro de cesantía en edad avanzada y vejez',
    14201: 'Aportaciones al FOVISSSTE',
    14202: 'Aportaciones al INFONAVIT',
    14301: 'Aportaciones al Sistema de Ahorro para el Retiro',
    14302: 'Depósitos para el ahorro solidario',
    14401: 'Cuotas para el seguro de vida del personal civil',
    14402: 'Cuotas para el seguro de vida del personal militar',
    14403: 'Cuotas para el seguro de gastos médicos del personal civil',
    14404: 'Cuotas para el seguro de separación individualizado',
    14405: 'Cuotas para el seguro colectivo de retiro',
    14406: 'Seguro de responsabilidad civil, asistencia legal y otros seguros',
    15101: 'Cuotas para el fondo de ahorro del personal civil',
    15102: 'Cuotas para el fondo de ahorro de generales, almirantes, jefes y oficiales',
    15103: 'Cuotas para el fondo de trabajo del personal del Ejército, Fuerza Aérea y Armada Mexicanos',
    15201: 'Indemnizaciones por accidentes en el trabajo',
    15202: 'Pago de liquidaciones',
    15203: 'Fondo para indemnizaciones (Ramos Autónomos)',
    15301: 'Prestaciones de retiro',
    15302: 'Prestaciones y previsiones de retiro (Ramos Autónomos)',
    15401: 'Prestaciones establecidas por condiciones generales de trabajo o contratos colectivos de trabajo',
    15402: 'Compensación garantizada',
    15403: 'Asignaciones adicionales al sueldo',
    15405: 'Compensación de Apoyo (Ramos Autónomos)',
    15501: 'Apoyos a la capacitación de los servidores públicos',
    15901: 'Otras prestaciones',
    15902: 'Pago extraordinario por riesgo',
    16101: 'Incrementos a las percepciones',
    16102: 'Creación de plazas',
    16103: 'Otras medidas de carácter laboral y económico',
    16104: 'Previsiones para aportaciones al ISSSTE',
    16105: 'Previsiones para aportaciones al FOVISSSTE',
    16106: 'Previsiones para aportaciones al Sistema de Ahorro para el Retiro',
    16107: 'Previsiones para aportaciones al seguro de cesantía en edad avanzada y vejez',
    16108: 'Previsiones para los depósitos al ahorro solidario',
    16109: 'Previsiones por adecuaciones a las estructuras ocupacionales',
    17101: 'Estímulos por productividad y eficiencia',
    17102: 'Estímulos al personal operativo',
    21101: 'Materiales y útiles de oficina',
    21102: 'Material electoral (Ramos Autónomos)',
    21199: 'Materiales de administración, emisión de documentos y artículos oficiales',
    21201: 'Materiales y útiles de impresión y reproducción',
    21301: 'Material estadístico y geográfico',
    21401: 'Materiales y útiles consumibles para el procesamiento en equipos y bienes informáticos',
    21501: 'Material de apoyo informativo',
    21502: 'Material para información en actividades de investigación científica y tecnológica',
    21601: 'Material de limpieza',
    21701: 'Materiales y suministros para planteles educativos',
    21801: 'Materiales para el registro e identificación de bienes y personas',
    22101: 'Productos alimenticios para el Ejército, Fuerza Aérea y Armada Mexicanos',
    22102: 'Productos alimenticios para personas derivado de la prestación de servicios públicos',
    22103: 'Productos alimenticios para el personal que realiza labores en campo',
    22104: 'Productos alimenticios para el personal en las instalaciones',
    22105: 'Productos alimenticios para la población en caso de desastres naturales',
    22106: 'Productos alimenticios para el personal derivado de actividades extraordinarias',
    22199: 'Alimentos y utensilios',
    22201: 'Productos alimenticios para animales',
    22301: 'Utensilios para el servicio de alimentación',
    23101: 'Productos alimenticios, agropecuarios y forestales adquiridos como materia prima',
    23199: 'Materias primas y materiales de producción y comercialización',
    23201: 'Insumos textiles adquiridos como materia prima',
    23301: 'Productos de papel, cartón e impresos adquiridos como materia prima',
    23401: 'Combustibles, lubricantes, aditivos, carbón y sus derivados adquiridos como materia prima',
    23501: 'Productos químicos, farmacéuticos y de laboratorio adquiridos como materia prima',
    23601: 'Productos metálicos y a base de minerales no metálicos adquiridos como materia prima',
    23701: 'Productos de cuero, piel, plástico y hule adquiridos como materia prima',
    23801: 'Mercancías para su comercialización en tiendas del sector público',
    23901: 'Otros productos adquiridos como materia prima',
    23902: 'Petróleo, gas y sus derivados adquiridos como materia prima',
    24101: 'Productos minerales no metálicos',
    24199: 'Materiales y artículos de construcción y de reparación',
    24201: 'Cemento y productos de concreto',
    24301: 'Cal, yeso y productos de yeso',
    24401: 'Madera y productos de madera',
    24501: 'Vidrio y productos de vidrio',
    24601: 'Material eléctrico y electrónico',
    24701: 'Artículos metálicos para la construcción',
    24801: 'Materiales complementarios',
    24901: 'Otros materiales y artículos de construcción y reparación',
    25101: 'Productos químicos básicos',
    25199: 'Productos químicos, farmacéuticos y de laboratorio',
    25201: 'Plaguicidas, abonos y fertilizantes',
    25301: 'Medicinas y productos farmacéuticos',
    25401: 'Materiales, accesorios y suministros médicos',
    25501: 'Materiales, accesorios y suministros de laboratorio',
    25601: 'Fibras sintéticas, hules, plásticos y derivados',
    25901: 'Otros productos químicos',
    26101: 'Combustibles para programas de seguridad pública y nacional',
    26102: 'Combustibles para servicios públicos y operación de programas',
    26103: 'Combustibles para servicios administrativos',
    26104: 'Combustibles asignados a servidores públicos',
    26105: 'Combustibles para maquinaria y equipo de producción',
    26106: 'PIDIREGAS cargos variables',
    26107: 'Combustibles nacionales para plantas productivas',
    26108: 'Combustibles de importación para plantas productivas',
    26199: 'Combustibles, lubricantes y aditivos',
    27101: 'Vestuario y uniformes',
    27199: 'Vestuario, blancos, prendas de protección y artículos deportivos',
    27201: 'Prendas de protección personal',
    27301: 'Artículos deportivos',
    27401: 'Productos textiles',
    27501: 'Blancos y otros productos textiles, excepto prendas de vestir',
    28101: 'Sustancias y materiales explosivos',
    28199: 'Materiales y suministros para seguridad',
    28201: 'Materiales de seguridad pública',
    28301: 'Prendas de protección para seguridad pública y nacional',
    29101: 'Herramientas menores',
    29199: 'Herramientas, refacciones y accesorios menores',
    29201: 'Refacciones y accesorios menores de edificios',
    29301: 'Refacciones y accesorios menores de mobiliario y equipo',
    29401: 'Refacciones y accesorios para equipo de cómputo y telecomunicaciones',
    29501: 'Refacciones y accesorios menores de equipo e instrumental médico',
    29601: 'Refacciones y accesorios menores de equipo de transporte',
    29701: 'Refacciones y accesorios menores de equipo de defensa y seguridad',
    29801: 'Refacciones y accesorios menores de maquinaria y otros equipos',
    29901: 'Refacciones y accesorios menores otros bienes muebles',
    31101: 'Servicio de energía eléctrica',
    31199: 'Servicios básicos',
    31201: 'Servicio de gas',
    31301: 'Servicio de agua',
    31401: 'Servicio telefónico convencional',
    31501: 'Servicio de telefonía celular',
    31601: 'Servicio de radiolocalización',
    31602: 'Servicios de telecomunicaciones',
    31603: 'Servicios de Internet',
    31701: 'Servicios de conducción de señales analógicas y digitales',
    31801: 'Servicio postal',
    31802: 'Servicio telegráfico',
    31901: 'Servicios integrales de telecomunicación',
    31902: 'Contratación de otros servicios',
    31903: 'Servicios generales para planteles educativos',
    31904: 'Servicios integrales de infraestructura de cómputo',
    32101: 'Arrendamiento de terrenos',
    32199: 'Servicios de arrendamiento',
    32201: 'Arrendamiento de edificios y locales',
    32301: 'Arrendamiento de equipo y bienes informáticos',
    32302: 'Arrendamiento de mobiliario',
    32303: 'Arrendamiento de equipo de telecomunicaciones',
    32401: 'Arrendamiento de equipo e instrumental médico y de laboratorio',
    32501: 'Arrendamiento de vehículos para seguridad pública',
    32502: 'Arrendamiento de vehículos para servicios públicos',
    32503: 'Arrendamiento de vehículos para servicios administrativos',
    32504: 'Arrendamiento de vehículos para desastres naturales',
    32505: 'Arrendamiento de vehículos para servidores públicos',
    32601: 'Arrendamiento de maquinaria y equipo',
    32701: 'Patentes, derechos de autor, regalías y otros',
    32901: 'Arrendamiento de sustancias y productos químicos',
    32902: 'PIDIREGAS cargos fijos',
    32903: 'Otros arrendamientos',
    33101: 'Asesorías asociadas a convenios, tratados o acuerdos',
    33102: 'Asesorías por controversias en el marco de los tratados internacionales',
    33103: 'Consultorías para programas o proyectos financiados por organismos internacionales',
    33104: 'Otras asesorías para la operación de programas',
    33105: 'Servicios relacionados con procedimientos jurisdiccionales',
    33106: 'Servicios legales, de contabilidad, auditoría y relacionados',
    33199: 'Servicios profesionales, científicos, técnicos y otros servicios',
    33201: 'Servicios de diseño, arquitectura, ingeniería y actividades relacionadas',
    33301: 'Servicios de desarrollo de aplicaciones informáticas',
    33302: 'Servicios estadísticos y geográficos',
    33303: 'Servicios relacionados con certificación de procesos',
    33304: 'Servicios de mantenimiento de aplicaciones informáticas',
    33401: 'Servicios para capacitación a servidores públicos',
    33501: 'Estudios e investigaciones',
    33601: 'Servicios relacionados con traducciones',
    33602: 'Otros servicios comerciales',
    33603: 'Impresiones de documentos oficiales',
    33604: 'Impresión y elaboración de material informativo',
    33605: 'Información en medios masivos',
    33606: 'Servicios de digitalización',
    33701: 'Gastos de seguridad pública y nacional',
    33702: 'Gastos en actividades de seguridad y logística del Estado Mayor Presidencial',
    33801: 'Servicios de vigilancia',
    33901: 'Subcontratación de servicios con terceros',
    33902: 'Proyectos para prestación de servicios',
    33903: 'Servicios integrales',
    33904: 'Asignaciones derivadas de proyectos de asociación público privada',
    33905: 'Servicios integrales en materia de seguridad pública y nacional',
    33906: 'Asignaciones para cubrir el pago de obligaciones derivadas de títulos de concesión',
    34101: 'Servicios bancarios y financieros',
    34199: 'Servicios financieros, bancarios y comerciales',
    34301: 'Gastos inherentes a la recaudación',
    34401: 'Seguro de responsabilidad patrimonial del Estado',
    34501: 'Seguros de bienes patrimoniales',
    34601: 'Almacenaje, embalaje y envase',
    34701: 'Fletes y maniobras',
    34801: 'Comisiones por ventas',
    34901: 'Otros servicios financieros, bancarios y comerciales',
    35101: 'Mantenimiento y conservación de inmuebles para servicios administrativos',
    35102: 'Mantenimiento y conservación de inmuebles para servicios públicos',
    35199: 'Servicios de instalación, reparación, mantenimiento y conservación',
    35201: 'Mantenimiento y conservación de mobiliario y equipo de administración',
    35301: 'Mantenimiento y conservación de bienes informáticos',
    35401: 'Instalación, reparación y mantenimiento de equipo e instrumental médico',
    35501: 'Mantenimiento y conservación de vehículos',
    35601: 'Reparación y mantenimiento de equipo de defensa y seguridad',
    35701: 'Mantenimiento y conservación de maquinaria y equipo',
    35702: 'Mantenimiento y conservación de plantas e instalaciones productivas',
    35801: 'Servicios de lavandería, limpieza e higiene',
    35901: 'Servicios de jardinería y fumigación',
    36101: 'Difusión de mensajes sobre programas y actividades gubernamentales',
    36199: 'Servicios de comunicación social y publicidad',
    36201: 'Difusión de mensajes comerciales para promover la venta de productos',
    36301: 'Servicios de creatividad, preproducción y producción de publicidad',
    36401: 'Servicios de revelado de fotografías',
    36601: 'Servicio de creación y difusión de contenido a través de Internet',
    36901: 'Servicios relacionados con monitoreo de información en medios masivos',
    37101: 'Pasajes aéreos nacionales para labores en campo y de supervisión',
    37102: 'Pasajes aéreos nacionales asociados a los programas de seguridad pública',
    37103: 'Pasajes aéreos nacionales asociados a desastres naturales',
    37104: 'Pasajes aéreos nacionales para servidores públicos de mando',
    37105: 'Pasajes aéreos internacionales asociados a seguridad pública',
    37106: 'Pasajes aéreos internacionales para servidores públicos',
    37199: 'Servicios de traslado y viáticos',
    37201: 'Pasajes terrestres nacionales para labores en campo',
    37202: 'Pasajes terrestres nacionales asociados a seguridad pública',
    37203: 'Pasajes terrestres nacionales asociados a desastres naturales',
    37204: 'Pasajes terrestres nacionales para servidores públicos de mando',
    37205: 'Pasajes terrestres internacionales asociados a seguridad pública',
    37206: 'Pasajes terrestres internacionales para servidores públicos',
    37207: 'Pasajes terrestres nacionales por medio electrónico',
    37301: 'Pasajes marítimos para labores en campo y de supervisión',
    37302: 'Pasajes marítimos asociados a seguridad pública',
    37303: 'Pasajes marítimos asociados a desastres naturales',
    37304: 'Pasajes marítimos para servidores públicos de mando',
    37501: 'Viáticos nacionales para labores en campo y de supervisión',
    37502: 'Viáticos nacionales asociados a seguridad pública',
    37503: 'Viáticos nacionales asociados a desastres naturales',
    37504: 'Viáticos nacionales para servidores públicos',
    37601: 'Viáticos en el extranjero asociados a seguridad pública',
    37602: 'Viáticos en el extranjero para servidores públicos',
    37701: 'Instalación del personal federal',
    37801: 'Servicios integrales nacionales para servidores públicos',
    37802: 'Servicios integrales en el extranjero para servidores públicos',
    37901: 'Gastos para operativos y trabajos de campo en áreas rurales',
    38101: 'Gastos de ceremonial del titular del Ejecutivo Federal',
    38102: 'Gastos de ceremonial de los titulares de las dependencias',
    38103: 'Gastos inherentes a la investidura presidencial',
    38199: 'Servicios oficiales',
    38201: 'Gastos de orden social',
    38301: 'Congresos y convenciones',
    38401: 'Exposiciones',
    38501: 'Gastos para alimentación de servidores públicos de mando',
    39101: 'Funerales y pagas de defunción',
    39199: 'Otros servicios generales',
    39201: 'Impuestos y derechos de exportación',
    39202: 'Otros impuestos y derechos',
    39301: 'Impuestos y derechos de importación',
    39401: 'Erogaciones por resoluciones por autoridad competente',
    39402: 'Indemnizaciones por expropiación de predios',
    39403: 'Otras asignaciones derivadas de resoluciones de ley',
    39501: 'Penas, multas, accesorios y actualizaciones',
    39601: 'Pérdidas del erario federal',
    39602: 'Otros gastos por responsabilidades',
    39701: 'Erogaciones por pago de utilidades',
    39801: 'Impuesto sobre nóminas',
    39810: 'Otros impuestos sobre nóminas',
    39901: 'Gastos de las Comisiones Internacionales de Límites y Aguas',
    39902: 'Gastos de las oficinas del Servicio Exterior Mexicano',
    39903: 'Asignaciones a los grupos parlamentarios',
    39904: 'Participaciones en órganos de gobierno',
    39905: 'Actividades de coordinación con el Presidente Electo',
    39906: 'Servicios Corporativos prestados por las Entidades Paraestatales',
    39907: 'Servicios prestados entre Organismos de una Entidad Paraestatal',
    39908: 'Erogaciones por cuenta de terceros',
    39909: 'Erogaciones recuperables',
    39910: 'Apertura de Fondo Rotatorio',
    41501: 'Transferencias para cubrir el déficit de operación',
    41601: 'Transferencias a entidades empresariales no financieras',
    43101: 'Subsidios a la producción',
    43201: 'Subsidios a la distribución',
    43301: 'Subsidios para inversión',
    43401: 'Subsidios a la prestación de servicios públicos',
    43501: 'Subsidios para cubrir diferenciales de tasas de interés',
    43601: 'Subsidios para la adquisición de vivienda de interés social',
    43701: 'Subsidios al consumo',
    43801: 'Subsidios a Entidades Federativas y Municipios',
    43901: 'Subsidios para capacitación y becas',
    43902: 'Subsidios a fideicomisos privados y estatales',
    44101: 'Gastos relacionados con actividades culturales, deportivas y de ayuda extraordinaria',
    44102: 'Gastos por servicios de traslado de personas',
    44103: 'Premios, recompensas, pensiones de gracia y pensión recreativa estudiantil',
    44104: 'Premios, estímulos, recompensas, becas y seguros a deportistas',
    44105: 'Apoyo a voluntarios que participan en diversos programas federales',
    44106: 'Compensaciones por servicios de carácter social',
    44199: 'Ayudas sociales',
    44201: 'Otras ayudas para programas de capacitación',
    44401: 'Apoyos a la investigación científica y tecnológica',
    44402: 'Apoyos a la investigación científica en instituciones sin fines de lucro',
    44801: 'Mercancías para su distribución a la población',
    45201: 'Pago de pensiones y jubilaciones',
    45202: 'Pago de pensiones y jubilaciones contractuales',
    45203: 'Transferencias para el pago de pensiones y jubilaciones',
    45901: 'Pago de sumas aseguradas',
    45902: 'Prestaciones económicas distintas de pensiones y jubilaciones',
    46101: 'Aportaciones a fideicomisos públicos',
    46102: 'Aportaciones a mandatos públicos',
    46199: 'Transferencias a fideicomisos, mandatos y otros análogos',
    47101: 'Trasferencias para cuotas y aportaciones de seguridad social',
    47102: 'Transferencias para cuotas y aportaciones a los seguros de retiro',
    48101: 'Donativos a instituciones sin fines de lucro',
    48199: 'Donativos',
    48201: 'Donativos a entidades federativas o municipios',
    48301: 'Donativos a fideicomisos privados',
    48401: 'Donativos a fideicomisos estatales',
    48501: 'Donativos internacionales',
    49199: 'Transferencias al exterior',
    49201: 'Cuotas y aportaciones a organismos internacionales',
    49202: 'Otras aportaciones internacionales',
    51101: 'Mobiliario',
    51199: 'Mobiliario y equipo de administración',
    51201: 'Muebles, excepto de oficina y estantería',
    51301: 'Bienes artísticos y culturales',
    51501: 'Bienes informáticos',
    51901: 'Equipo de administración',
    51902: 'Adjudicaciones, expropiaciones e indemnizaciones de bienes muebles',
    52101: 'Equipos y aparatos audiovisuales',
    52199: 'Mobiliario y equipo educacional y recreativo',
    52201: 'Aparatos deportivos',
    52301: 'Cámaras fotográficas y de video',
    52901: 'Otro mobiliario y equipo educacional y recreativo',
    53101: 'Equipo médico y de laboratorio',
    53199: 'Equipo e instrumental médico y de laboratorio',
    53201: 'Instrumental médico y de laboratorio',
    54101: 'Vehículos y equipo terrestres para seguridad pública',
    54102: 'Vehículos y equipo terrestres para desastres naturales',
    54103: 'Vehículos y equipo terrestres para servicios públicos',
    54104: 'Vehículos y equipo terrestres para servicios administrativos',
    54105: 'Vehículos y equipo terrestres para servidores públicos',
    54199: 'Vehículos y equipo de transporte',
    54201: 'Carrocerías y remolques',
    54301: 'Vehículos y equipo aéreos para seguridad pública',
    54302: 'Vehículos y equipo aéreos para desastres naturales',
    54303: 'Vehículos y equipo aéreos para servicios públicos',
    54401: 'Equipo ferroviario',
    54501: 'Vehículos y equipo marítimo para seguridad pública',
    54502: 'Vehículos y equipo marítimo para servicios públicos',
    54503: 'Construcción de embarcaciones',
    54901: 'Otros equipos de transporte',
    55101: 'Maquinaria y equipo de defensa y seguridad pública',
    55102: 'Equipo de seguridad pública y nacional',
    55199: 'Equipo de defensa y seguridad',
    56101: 'Maquinaria y equipo agropecuario',
    56199: 'Maquinaria, otros equipos y herramientas',
    56201: 'Maquinaria y equipo industrial',
    56301: 'Maquinaria y equipo de construcción',
    56401: 'Sistemas de aire acondicionado, calefacción y de refrigeración',
    56501: 'Equipos y aparatos de comunicaciones y telecomunicaciones',
    56601: 'Maquinaria y equipo eléctrico y electrónico',
    56701: 'Herramientas y máquinas herramienta',
    56901: 'Bienes muebles por arrendamiento financiero',
    56902: 'Otros bienes muebles',
    57101: 'Animales de reproducción',
    57199: 'Activos biológicos',
    57201: 'Porcinos',
    57301: 'Aves',
    57401: 'Ovinos y caprinos',
    57501: 'Peces y acuicultura',
    57601: 'Animales de trabajo',
    57701: 'Animales de custodia y vigilancia',
    57801: 'Árboles y plantas',
    57901: 'Otros activos biológicos',
    58101: 'Terrenos',
    58199: 'Bienes inmuebles',
    58301: 'Edificios y locales',
    58901: 'Adjudicaciones, expropiaciones e indemnizaciones de inmuebles',
    58902: 'Bienes inmuebles en la modalidad de proyectos de infraestructura',
    58903: 'Bienes inmuebles por arrendamiento financiero',
    58904: 'Otros bienes inmuebles',
    59101: 'Software',
    59199: 'Activos intangibles',
    59401: 'Derechos',
    59701: 'Licencias informáticas e intelectuales',
    59901: 'Otros activos intangibles',
}

def obtener_denominacion_partida(partida):
    """Obtiene la denominación de una partida específica"""
    return PARTIDAS_ESPECIFICAS.get(int(partida), f'Partida {partida}')
