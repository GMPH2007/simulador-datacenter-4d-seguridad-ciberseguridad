import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def build_pro_case_study():
    doc = docx.Document()

    # Configuración de márgenes estándar (2.2 cm aprox)
    for section in doc.sections:
        section.top_margin = Inches(0.85)
        section.bottom_margin = Inches(0.85)
        section.left_margin = Inches(0.9)
        section.right_margin = Inches(0.9)

    # Paleta de Colores Ejecutiva y Elegante
    NAVY = RGBColor(15, 44, 89)        # #0F2C59 - Primario elegante
    SKY_BLUE = RGBColor(30, 90, 160)   # #1E5AA0 - Subtítulos
    CHARCOAL = RGBColor(51, 65, 85)     # #334155 - Texto legible y suave
    EMERALD = RGBColor(16, 120, 80)     # #107850 - Éxito / Resultados
    DARK_RED = RGBColor(160, 30, 30)    # #A01E1E - Problemas
    LIGHT_BG = "F8FAFC"
    ALT_BG = "F1F5F9"
    BORDER_COLOR = "CBD5E1"

    # Funciones de estilo XML para tablas
    def set_cell_background(cell, color_hex):
        shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
        cell._tc.get_or_add_tcPr().append(shading)

    def set_cell_padding(cell, top=100, bottom=100, left=150, right=150):
        tcPr = cell._tc.get_or_add_tcPr()
        tcMar = OxmlElement('w:tcMar')
        for margin, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
            node = OxmlElement(f'w:{margin}')
            node.set(qn('w:w'), str(val))
            node.set(qn('w:type'), 'dxa')
            tcMar.append(node)
        tcPr.append(tcMar)

    def set_callout_left_border(cell, border_hex="1E5AA0", border_size="24"):
        tcPr = cell._tc.get_or_add_tcPr()
        borders = parse_xml(
            f'<w:tcBorders {nsdecls("w")}>'
            f'<w:top w:val="none"/>'
            f'<w:left w:val="single" w:sz="{border_size}" w:space="0" w:color="{border_hex}"/>'
            f'<w:bottom w:val="none"/>'
            f'<w:right w:val="none"/>'
            f'</w:tcBorders>'
        )
        tcPr.append(borders)

    def set_table_borders(table, border_hex="CBD5E1"):
        tblPr = table._tbl.tblPr
        borders = parse_xml(
            f'<w:tblBorders {nsdecls("w")}>'
            f'<w:top w:val="single" w:sz="6" w:space="0" w:color="{border_hex}"/>'
            f'<w:left w:val="none"/>'
            f'<w:bottom w:val="single" w:sz="6" w:space="0" w:color="{border_hex}"/>'
            f'<w:right w:val="none"/>'
            f'<w:insideH w:val="single" w:sz="4" w:space="0" w:color="{border_hex}"/>'
            f'<w:insideV w:val="none"/>'
            f'</w:tblBorders>'
        )
        tblPr.append(borders)

    # =========================================================================
    # ENCABEZADO Y PORTADA INSTITUCIONAL EJECUTIVA
    # =========================================================================
    header_box = doc.add_table(rows=1, cols=1)
    header_box.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell_h = header_box.rows[0].cells[0]
    cell_h.width = Inches(6.7)
    set_cell_background(cell_h, "0F2C59")
    set_cell_padding(cell_h, top=160, bottom=160, left=200, right=200)

    p_sub = cell_h.paragraphs[0]
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(2)
    r_sub = p_sub.add_run("ACTIVIDAD FORMATIVA – CASO DE ESTUDIO EMPRESARIAL")
    r_sub.font.name = "Arial"
    r_sub.font.size = Pt(10)
    r_sub.font.bold = True
    r_sub.font.color.rgb = RGBColor(210, 230, 255)

    p_main = cell_h.add_paragraph()
    p_main.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_main.paragraph_format.space_after = Pt(4)
    r_main = p_main.add_run("SOLUCIONES EN HABILIDADES BLANDAS Y DURAS EN ENTORNOS DE EMPRESA")
    r_main.font.name = "Arial"
    r_main.font.size = Pt(15)
    r_main.font.bold = True
    r_main.font.color.rgb = RGBColor(255, 255, 255)

    p_tag = cell_h.add_paragraph()
    p_tag.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_tag.paragraph_format.space_after = Pt(0)
    r_tag = p_tag.add_run("Caso Aplicado: Optimización Operativa y Relacional en «LogiTrans del Norte S.A.C.»")
    r_tag.font.name = "Arial"
    r_tag.font.size = Pt(10.5)
    r_tag.font.italic = True
    r_tag.font.color.rgb = RGBColor(226, 232, 240)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # FICHA TÉCNICA INFORMATIVA
    info_table = doc.add_table(rows=4, cols=2)
    info_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    info_table.autofit = False
    set_table_borders(info_table, border_hex="E2E8F0")

    metadata = [
        ("Estudiante:", "Gerson Misael Pintado Huaman"),
        ("Docente Asesor:", "Dr. Javier Eduardo Jaramillo Atoche"),
        ("Eje Temático:", "Articulación de Hard Skills (Técnicas) y Soft Skills (Humanas)"),
        ("Propósito:", "Diagnosticar cuellos de botella y diseñar soluciones aplicadas al entorno real")
    ]

    for i, (label, val) in enumerate(metadata):
        c0, c1 = info_table.rows[i].cells[0], info_table.rows[i].cells[1]
        c0.width, c1.width = Inches(1.8), Inches(4.9)
        set_cell_background(c0, "F8FAFC")
        set_cell_background(c1, "FFFFFF")
        set_cell_padding(c0, top=60, bottom=60, left=100, right=100)
        set_cell_padding(c1, top=60, bottom=60, left=100, right=100)

        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_after = Pt(0)
        r0 = p0.add_run(label)
        r0.font.name = "Arial"
        r0.font.size = Pt(9.5)
        r0.font.bold = True
        r0.font.color.rgb = NAVY

        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_after = Pt(0)
        r1 = p1.add_run(val)
        r1.font.name = "Arial"
        r1.font.size = Pt(9.5)
        r1.font.color.rgb = CHARCOAL

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # Helper para encabezados de sección
    def add_section_header(title, num=""):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        
        r_num = p.add_run(num + " ")
        r_num.font.name = "Arial"
        r_num.font.size = Pt(13)
        r_num.font.bold = True
        r_num.font.color.rgb = SKY_BLUE

        r_title = p.add_run(title)
        r_title.font.name = "Arial"
        r_title.font.size = Pt(13)
        r_title.font.bold = True
        r_title.font.color.rgb = NAVY

    # Helper para párrafos estándar
    def add_p(text, bold_prefix="", italic=False):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(5)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_b = p.add_run(bold_prefix + " ")
            r_b.font.name = "Arial"
            r_b.font.size = Pt(10)
            r_b.font.bold = True
            r_b.font.color.rgb = NAVY
        r = p.add_run(text)
        r.font.name = "Arial"
        r.font.size = Pt(10)
        r.font.italic = italic
        r.font.color.rgb = CHARCOAL
        return p

    # Helper para cuadro de llamada (Callout humanizado)
    def add_callout(quote_text, author_tag=""):
        t = doc.add_table(rows=1, cols=1)
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = t.rows[0].cells[0]
        cell.width = Inches(6.7)
        set_cell_background(cell, "F1F5F9")
        set_callout_left_border(cell, border_hex="1E5AA0", border_size="28")
        set_cell_padding(cell, top=80, bottom=80, left=150, right=120)
        
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.15
        r = p.add_run(f'«{quote_text}»')
        r.font.name = "Arial"
        r.font.size = Pt(9.5)
        r.font.italic = True
        r.font.color.rgb = RGBColor(30, 41, 59)

        if author_tag:
            p2 = cell.add_paragraph()
            p2.paragraph_format.space_after = Pt(0)
            p2.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            r2 = p2.add_run(f"— {author_tag}")
            r2.font.name = "Arial"
            r2.font.size = Pt(8.5)
            r2.font.bold = True
            r2.font.color.rgb = SKY_BLUE

        doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # =========================================================================
    # SECCIÓN 1: INTRODUCCIÓN Y CONTEXTO
    # =========================================================================
    add_section_header("Contexto de la Empresa: «LogiTrans del Norte S.A.C.»", "1.")
    add_p(
        "LogiTrans del Norte S.A.C. es una empresa logística con sede operativa en la zona norte (Paita / Piura), encargada del almacenamiento frigorífico, control de stock y transporte terrestre de mercancías agroindustriales e hidrobiológicas hacia el puerto y distribuidores locales. Cuenta con una planilla de 50 colaboradores divididos entre almaceneros, despachadores, choferes y personal administrativo."
    )
    add_p(
        "A pesar de contar con camiones modernos y contratos de gran volumen, la empresa cerró el último trimestre con números alarmantes: un incremento del 38% en pérdidas por pedidos despachados con retraso, multas por parte de los clientes y un clima de hostilidad interna que provocó la renuncia de tres de sus mejores coordinadores de turno."
    )

    # =========================================================================
    # SECCIÓN 2: LA HISTORIA REAL (HUMANIZADA Y ENTENDIBLE)
    # =========================================================================
    add_section_header("El Problema en la Vida Real: ¿Qué pasaba en el turno de las 6:00 a.m.?", "2.")
    add_p(
        "Para comprender el problema, no basta con mirar hojas de cálculo; hay que ver la realidad del patio de maniobras:"
    )

    add_callout(
        "Hace dos meses, la gerencia compró un sistema moderno para controlar los pedidos en tablets digitales (Software WMS). Sin embargo, a los operarios de almacén solo les dieron un manual impreso de 60 páginas y ninguna capacitación práctica. ¿El resultado? En la hora pico de las 6:00 a.m., los operarios no sabían cómo registrar la carga refrigerada en el sistema, las tablets se congelaban y los camiones no podían salir. El supervisor, desesperado por la hora, empezó a gritar a los operarios tratándolos de incapaces. Los trabajadores se frustraron, dejaron de usar las tablets y volvieron a anotar todo en cuadernos a mano con lápiz. Esa misma mañana, un contenedor de conservas salió sin guía oficial y la empresa recibió una penalidad de S/. 25,000.",
        "Relato testimonial del jefe de patio durante la auditoría interna"
    )

    add_p(
        "Este suceso refleja la realidad de cientos de empresas peruanas: El problema no fue la máquina ni la tecnología, sino el choque entre una carencia técnica evidente (habilidad dura no enseñada) y una respuesta emocional destructiva (habilidad blanda inexistente)."
    )

    # =========================================================================
    # SECCIÓN 3: DIAGNÓSTICO COMPARATIVO TÉCNICO
    # =========================================================================
    add_section_header("Diagnóstico Técnico de Brechas: ¿Qué faltaba en cada lado?", "3.")

    diag_table = doc.add_table(rows=5, cols=2)
    diag_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    diag_table.autofit = False
    set_table_borders(diag_table)

    headers = ["BRECHAS EN HABILIDADES DURAS (Lo Técnico)", "BRECHAS EN HABILIDADES BLANDAS (Lo Humano)"]
    for j, h_text in enumerate(headers):
        cell = diag_table.rows[0].cells[j]
        cell.width = Inches(3.35)
        set_cell_background(cell, "0F2C59")
        set_cell_padding(cell, top=100, bottom=100, left=120, right=120)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h_text)
        r.font.name = "Arial"
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    brechas = [
        ("• Desconocimiento de software de almacén (ERP/WMS): Los trabajadores no dominaban las funciones de escaneo, ruteo ni cierre de inventarios.",
         "• Comunicación agresiva y reproches: En lugar de orientar cuando ocurre un fallo, los supervisores recurrían al sarcasmo y a la amenaza de despido."),
        ("• Nulo manejo de indicadores de control (KPIs): No se medían tiempos de carga, merma ni exactitud de inventario en Excel o tableros de control.",
         "• Ruptura del trabajo en equipo («Cultura de islas»): Almacén y Transporte no se hablaban; si un camión se retrasaba, se culpaban mutuamente."),
        ("• Desorden operativo y falta de método 5S: Productos sin rotulado correcto, pasillos obstruidos y pérdida de 35 minutos buscando cada palet.",
         "• Nula tolerancia a la frustración y estrés desmedido: Pérdida del control en horas de alta presión, generando licencias médicas y renuncias."),
        ("• Desconocimiento de normativas técnicas de frío: Descuido en la calibración térmica durante la estiba de alimentos perecibles.",
         "• Ausencia de empatía y liderazgo servicial: Jefaturas distantes que veían al colaborador como un número y no como una persona.")
    ]

    for i, (col_dura, col_blanda) in enumerate(brechas, start=1):
        bg = LIGHT_BG if i % 2 == 1 else "FFFFFF"
        row = diag_table.rows[i]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width, c1.width = Inches(3.35), Inches(3.35)
        set_cell_background(c0, bg)
        set_cell_background(c1, bg)
        set_cell_padding(c0, top=70, bottom=70, left=100, right=100)
        set_cell_padding(c1, top=70, bottom=70, left=100, right=100)

        for c, txt in [(c0, col_dura), (c1, col_blanda)]:
            p = c.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.15
            r = p.add_run(txt)
            r.font.name = "Arial"
            r.font.size = Pt(9)
            r.font.color.rgb = CHARCOAL

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # =========================================================================
    # SECCIÓN 4: PROPUESTA DE SOLUCIÓN: PLAN INTEGRAL "TRANSFORMA LOGITRANS"
    # =========================================================================
    add_section_header("Propuesta de Solución: El Plan Integral «Transforma LogiTrans»", "4.")
    add_p(
        "Para revertir la situación no bastaba con dar un curso motivacional ni con comprar más máquinas. Se diseñó un plan de acción equilibrado en dos brazos que se apoyan mutuamente:"
    )

    # 4.1 BRAZO DE HABILIDADES DURAS
    p_b1 = doc.add_paragraph()
    p_b1.paragraph_format.space_before = Pt(8)
    p_b1.paragraph_format.space_after = Pt(2)
    r_b1 = p_b1.add_run("BLOQUE A: SOLUCIONES EN HABILIDADES DURAS (Capacidades Técnicas)")
    r_b1.font.name = "Arial"
    r_b1.font.size = Pt(11)
    r_b1.font.bold = True
    r_b1.font.color.rgb = SKY_BLUE

    hard_solutions = [
        ("1. Taller Práctico en Puesto de Trabajo sobre ERP/WMS (15 horas):",
         "En lugar de manuales aburridos, se implementó capacitación vivencial con pistolas lectoras de código de barras simulando despachos reales. Se crearon 'Guías Rápidas en una Sola Página' plastificadas y pegadas en cada montacargas."),
        ("2. Estandarización de Procesos bajo Metodología 5S:",
         "Se demarcaron zonas con pintura epóxica (Seiri, Seiton, Seiso, Seiketsu, Shitsuke). Todo producto tiene ubicación fija y código visible, reduciendo el tiempo de búsqueda de 35 a solo 4 minutos por palet."),
        ("3. Gestión Visual de Indicadores Clave (KPIs en Tablero):",
         "Capacitación a coordinadores en Excel y creación de un panel en la pared del almacén donde todo el equipo ve tres métricas diarias: % de despachos a tiempo, exactitud de inventario y temperatura de conservación.")
    ]

    for title, desc in hard_solutions:
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        r_t = p.add_run(title + " ")
        r_t.font.name = "Arial"
        r_t.font.size = Pt(9.5)
        r_t.font.bold = True
        r_t.font.color.rgb = NAVY
        r_d = p.add_run(desc)
        r_d.font.name = "Arial"
        r_d.font.size = Pt(9.5)
        r_d.font.color.rgb = CHARCOAL

    # 4.2 BRAZO DE HABILIDADES BLANDAS
    p_b2 = doc.add_paragraph()
    p_b2.paragraph_format.space_before = Pt(8)
    p_b2.paragraph_format.space_after = Pt(2)
    r_b2 = p_b2.add_run("BLOQUE B: SOLUCIONES EN HABILIDADES BLANDAS (Capacidades Humanas)")
    r_b2.font.name = "Arial"
    r_b2.font.size = Pt(11)
    r_b2.font.bold = True
    r_b2.font.color.rgb = SKY_BLUE

    soft_solutions = [
        ("1. Protocolo de Comunicación Asertiva «El Método SBI»:",
         "Se erradicaron los gritos e insultos. Supervisores y operarios fueron entrenados en el modelo Situación - Comportamiento - Impacto para dar retroalimentación: en lugar de decir «¡Siempre haces todo mal!», se enseña a decir «Hoy a las 6 a.m. (Situación), no registraste la guía en la tablet (Comportamiento), lo que retrasó al camión 20 minutos (Impacto). Revisemos qué botón se te complicó para solucionarlo»."),
        ("2. Liderazgo Empático y Gestión de Conflictos para Supervisores:",
         "Capacitación en inteligencia emocional para jefes de área, aprendiendo a escuchar activamente las dificultades operativas de los trabajadores antes de imponer órdenes."),
        ("3. Trabajo Colaborativo «Un Día en los Zapatos del Otro»:",
         "Se realizó una jornada de integración donde los coordinadores de despacho cargaron cajas durante dos horas y los operarios acompañaron a los choferes en ruta. Esto eliminó la enemistad entre áreas al comprender el esfuerzo ajeno."),
        ("4. Pausas Activas y Manejo del Estrés en Horas Punta:",
         "Implementación de 5 minutos de respiración y estiramiento muscular previo al turno de despacho más pesado, reduciendo la ansiedad y la irritabilidad colectiva.")
    ]

    for title, desc in soft_solutions:
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        r_t = p.add_run(title + " ")
        r_t.font.name = "Arial"
        r_t.font.size = Pt(9.5)
        r_t.font.bold = True
        r_t.font.color.rgb = NAVY
        r_d = p.add_run(desc)
        r_d.font.name = "Arial"
        r_d.font.size = Pt(9.5)
        r_d.font.color.rgb = CHARCOAL

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # =========================================================================
    # SECCIÓN 5: MATRIZ DE INTEGRACIÓN (LA CLAVE DEL TRABAJO)
    # =========================================================================
    add_section_header("Matriz de Articulación: Cómo se combinan en la práctica real", "5.")
    add_p(
        "Una habilidad técnica sin calidad humana es fría e ineficiente; una habilidad blanda sin destreza técnica es pura buena intención sin resultados. La siguiente matriz resume cómo se complementan:"
    )

    matrix_table = doc.add_table(rows=4, cols=4)
    matrix_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    matrix_table.autofit = False
    set_table_borders(matrix_table)

    m_headers = ["Situación Crítica", "Solución Técnica (Dura)", "Solución Humana (Blanda)", "Resultado Obtenido"]
    col_w = [Inches(1.5), Inches(1.7), Inches(1.75), Inches(1.75)]

    for j, h_text in enumerate(m_headers):
        cell = matrix_table.rows[0].cells[j]
        cell.width = col_w[j]
        set_cell_background(cell, "0F2C59")
        set_cell_padding(cell, top=100, bottom=100, left=80, right=80)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h_text)
        r.font.name = "Arial"
        r.font.size = Pt(9)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    m_rows = [
        ("Retraso en la salida de camiones congelados",
         "Uso de lectores de código de barras y ruteo GPS automatizado.",
         "Trabajo en equipo y comunicación por radiofrecuencia con respeto.",
         "Tiempo de carga reducido en 45%. Despachos 100% puntuales."),
        ("Diferencias de stock físico vs. sistema",
         "Conteo cíclico diario y conciliación automatizada en Excel.",
         "Ética laboral y transparencia para reportar pérdidas sin miedo a represalias.",
         "Exactitud de inventario subió de 82% a 98.7% en dos meses."),
        ("Mercadería maltratada y quejas de clientes",
         "Protocolo técnico estandarizado de estiba y embalaje seguro.",
         "Empatía y orientación de servicio al cliente final.",
         "Reclamos mensuales bajaron de 38 a solo 2 casos aislados.")
    ]

    for i, row_data in enumerate(m_rows, start=1):
        bg = LIGHT_BG if i % 2 == 1 else "FFFFFF"
        row = matrix_table.rows[i]
        for j, text in enumerate(row_data):
            cell = row.cells[j]
            cell.width = col_w[j]
            set_cell_background(cell, bg)
            set_cell_padding(cell, top=70, bottom=70, left=80, right=80)
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.15
            r = p.add_run(text)
            r.font.name = "Arial"
            r.font.size = Pt(8.5)
            r.font.color.rgb = CHARCOAL

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # =========================================================================
    # SECCIÓN 6: RESULTADOS CUANTITATIVOS Y CUALITATIVOS
    # =========================================================================
    add_section_header("Impacto y Resultados de la Intervención", "6.")

    res_table = doc.add_table(rows=3, cols=2)
    res_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    res_table.autofit = False
    set_table_borders(res_table)

    r_headers = ["Indicadores Técnicos (Duros)", "Indicadores de Clima y Personas (Blandos)"]
    for j, h_text in enumerate(r_headers):
        cell = res_table.rows[0].cells[j]
        cell.width = Inches(3.35)
        set_cell_background(cell, "1E5AA0")
        set_cell_padding(cell, top=80, bottom=80, left=100, right=100)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h_text)
        r.font.name = "Arial"
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    r_data = [
        ("• Exactitud de inventarios: Pasó del 82% al 98.7% en 60 días.\n• Tiempos de preparación de pedido (Picking): De 35 min a 12 min por orden.\n• Ahorro estimado: Eliminación de S/. 25,000 mensuales en penalidades.",
         "• Rotación voluntaria de personal: Se redujo a cero renuncias en el trimestre.\n• Nivel de satisfacción laboral: Subió de 41% a 87% en encuesta anónima.\n• Resolución de incidencias: De gritos diarios a reuniones breves de 10 min de coordinación."),
        ("• Cumplimiento de entregas a tiempo (OTIF): Subió de 64% al 94.5%.",
         "• Cultura organizacional: El error dejó de ser motivo de castigo y pasó a ser un dato para capacitar.")
    ]

    for i, (col1, col2) in enumerate(r_data, start=1):
        bg = LIGHT_BG if i % 2 == 1 else "FFFFFF"
        row = res_table.rows[i]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width, c1.width = Inches(3.35), Inches(3.35)
        set_cell_background(c0, bg)
        set_cell_background(c1, bg)
        set_cell_padding(c0, top=70, bottom=70, left=100, right=100)
        set_cell_padding(c1, top=70, bottom=70, left=100, right=100)

        for c, txt in [(c0, col1), (c1, col2)]:
            p = c.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.15
            r = p.add_run(txt)
            r.font.name = "Arial"
            r.font.size = Pt(9)
            r.font.color.rgb = CHARCOAL

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # =========================================================================
    # SECCIÓN 7: CONCLUSIONES Y REFLEXIÓN DEL ESTUDIANTE
    # =========================================================================
    add_section_header("Conclusiones y Aprendizaje Personal", "7.")

    conclusiones = [
        ("La técnica abre la puerta, pero el trato mantiene el trabajo:",
         "Una empresa puede comprar la tecnología más costosa del mundo, pero si sus colaboradores no saben comunicarse ni gestionar el estrés, la tecnología se vuelve un estorbo. Las habilidades duras aseguran la precisión; las blandas aseguran que las personas quieran trabajar juntas para lograrla."),
        ("El fin del jefe autoritario:",
         "En el entorno productivo actual, el liderazgo basado en gritos o amenazas solo produce ausentismo, fallas ocultas y desmotivación. El verdadero líder enseña la técnica (habilidad dura) y acompaña con respeto y escucha activa (habilidad blanda)."),
        ("El perfil que el mercado laboral busca hoy:",
         "Como futuros profesionales, este caso demuestra que no basta con ser un experto en sistemas, maquinaria o números si no sabemos dialogar, trabajar en equipo y resolver conflictos pacíficamente. El valor supremo de un egresado radica en dominar ambas dimensiones.")
    ]

    for title, desc in conclusiones:
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(5)
        p.paragraph_format.line_spacing = 1.15
        r_t = p.add_run(title + " ")
        r_t.font.name = "Arial"
        r_t.font.size = Pt(9.5)
        r_t.font.bold = True
        r_t.font.color.rgb = NAVY
        r_d = p.add_run(desc)
        r_d.font.name = "Arial"
        r_d.font.size = Pt(9.5)
        r_d.font.color.rgb = CHARCOAL

    # PIE DE PÁGINA FINAL
    doc.add_paragraph().paragraph_format.space_after = Pt(14)
    p_fin = doc.add_paragraph()
    p_fin.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_fin = p_fin.add_run("— Fin del Caso Práctico —")
    r_fin.font.name = "Arial"
    r_fin.font.size = Pt(9)
    r_fin.font.italic = True
    r_fin.font.color.rgb = RGBColor(148, 163, 184)

    output_path = "Caso_Practico_Habilidades_Blandas_y_Duras_GersonPintado.docx"
    doc.save(output_path)
    print(f"Document created successfully: {output_path}")

if __name__ == "__main__":
    build_pro_case_study()
