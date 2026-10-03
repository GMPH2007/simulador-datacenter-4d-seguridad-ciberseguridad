import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def create_case_study():
    doc = docx.Document()

    # Set standard margins (1 inch)
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.9)
        section.right_margin = Inches(0.9)

    # Helper styling functions
    primary_color = RGBColor(26, 54, 93)     # Deep Navy Blue
    secondary_color = RGBColor(43, 108, 176) # Medium Slate Blue
    dark_text = RGBColor(45, 55, 72)         # Charcoal Dark
    accent_color = RGBColor(197, 48, 48)     # Accent Red/Crimson

    def set_cell_shading(cell, color_hex):
        shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
        cell._tc.get_or_add_tcPr().append(shading)

    def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
        tcPr = cell._tc.get_or_add_tcPr()
        tcMar = OxmlElement('w:tcMar')
        for margin, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
            node = OxmlElement(f'w:{margin}')
            node.set(qn('w:w'), str(val))
            node.set(qn('w:type'), 'dxa')
            tcMar.append(node)
        tcPr.append(tcMar)

    # --- PORTADA / ENCABEZADO ---
    title_p = doc.add_paragraph()
    title_p.paragraph_format.space_before = Pt(0)
    title_p.paragraph_format.space_after = Pt(4)
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_inst = title_p.add_run("ACTIVIDAD PRÁCTICA DE APRENDIZAJE")
    run_inst.font.name = "Calibri"
    run_inst.font.size = Pt(13)
    run_inst.font.bold = True
    run_inst.font.color.rgb = secondary_color

    main_title = doc.add_paragraph()
    main_title.paragraph_format.space_before = Pt(0)
    main_title.paragraph_format.space_after = Pt(8)
    main_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_title = main_title.add_run("CASO PRÁCTICO: SOLUCIONES EN HABILIDADES BLANDAS Y DURAS EN ENTORNOS DE EMPRESA")
    run_title.font.name = "Calibri"
    run_title.font.size = Pt(17)
    run_title.font.bold = True
    run_title.font.color.rgb = primary_color

    # Datos Informativos Box
    meta_table = doc.add_table(rows=4, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_table.autofit = False

    meta_data = [
        ("Estudiante:", "Gerson Misael Pintado Huaman"),
        ("Docente:", "Javier Eduardo Jaramillo Atoche"),
        ("Tema:", "Soluciones integrales de Habilidades Blandas (Soft Skills) y Duras (Hard Skills)"),
        ("Empresa Caso:", "Logística y Distribución Comercial del Norte S.A.C. (LogiNorte)")
    ]

    for i, (label, val) in enumerate(meta_data):
        row = meta_table.rows[i]
        c0 = row.cells[0]
        c1 = row.cells[1]
        c0.width = Inches(1.8)
        c1.width = Inches(4.8)

        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_before = Pt(2)
        p0.paragraph_format.space_after = Pt(2)
        r0 = p0.add_run(label)
        r0.font.name = "Calibri"
        r0.font.bold = True
        r0.font.size = Pt(10.5)
        r0.font.color.rgb = primary_color

        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_before = Pt(2)
        p1.paragraph_format.space_after = Pt(2)
        r1 = p1.add_run(val)
        r1.font.name = "Calibri"
        r1.font.size = Pt(10.5)
        r1.font.color.rgb = dark_text

        set_cell_shading(c0, "F0F4F8")
        set_cell_shading(c1, "F8FAFC")
        set_cell_margins(c0, top=60, bottom=60, left=100, right=100)
        set_cell_margins(c1, top=60, bottom=60, left=100, right=100)

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # --- SECCIÓN 1: INTRODUCCIÓN Y CONTEXTO ---
    h1 = doc.add_heading(level=1)
    h1.paragraph_format.space_before = Pt(12)
    h1.paragraph_format.space_after = Pt(4)
    r_h1 = h1.add_run("1. Contexto de la Empresa y Situación Problemática")
    r_h1.font.color.rgb = primary_color
    r_h1.font.size = Pt(14)
    r_h1.font.bold = True

    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.line_spacing = 1.15
    p.add_run(
        "La empresa ficticia «LogiNorte S.A.C.» es una compañía con 60 colaboradores dedicada al almacenamiento, control de inventarios y distribución de mercadería. Durante el último semestre, la empresa ha experimentado un incremento del 35% en reclamos de clientes, pérdidas económicas por descuadre de inventarios y un clima laboral crítico marcado por discusiones constantes entre las áreas de Almacén, Ventas y Transporte."
    )

    p2 = doc.add_paragraph()
    p2.paragraph_format.space_after = Pt(10)
    p2.paragraph_format.line_spacing = 1.15
    p2.add_run(
        "Al realizar una auditoría interna, la gerencia descubrió que el problema no radicaba únicamente en la infraestructura ni en el presupuesto, sino en un desbalance crítico entre las "
    )
    r_bold1 = p2.add_run("habilidades duras (técnicas)")
    r_bold1.bold = True
    p2.add_run(" y las ")
    r_bold2 = p2.add_run("habilidades blandas (socioemocionales y de comunicación)")
    r_bold2.bold = True
    p2.add_run(" del equipo de trabajo.")

    # --- SECCIÓN 2: DIAGNÓSTICO DE BRECHAS ---
    h2 = doc.add_heading(level=1)
    h2.paragraph_format.space_before = Pt(12)
    h2.paragraph_format.space_after = Pt(4)
    r_h2 = h2.add_run("2. Diagnóstico de Brechas Identificadas")
    r_h2.font.color.rgb = primary_color
    r_h2.font.size = Pt(14)
    r_h2.font.bold = True

    # Tabla comparativa de problemas
    diag_table = doc.add_table(rows=4, cols=2)
    diag_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    diag_table.autofit = False

    diag_headers = ["Deficiencias en Habilidades Duras (Hard Skills)", "Deficiencias en Habilidades Blandas (Soft Skills)"]
    for j, text in enumerate(diag_headers):
        cell = diag_table.rows[0].cells[j]
        cell.width = Inches(3.3)
        set_cell_shading(cell, "2B6CB0")
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(text)
        r.font.name = "Calibri"
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.size = Pt(11)
        set_cell_margins(cell, top=100, bottom=100, left=120, right=120)

    diag_rows = [
        ("• Manejo deficiente de software ERP/WMS: Los operarios registran entradas y salidas manualmente en hojas de cálculo no estandarizadas, provocando errores en stock.",
         "• Comunicación inasertiva y hostil: Cuando surgen errores, los supervisores culpan a los operarios de forma agresiva en lugar de orientar a la solución conjunta."),
        ("• Desconocimiento de análisis de datos y KPIs: El personal no sabe interpretar indicadores de rotación, tiempos de entrega ni tasa de devoluciones.",
         "• Falta de trabajo en equipo e individualismo: Las áreas de Almacén y Distribución operan como 'islas', negándose a colaborar ante sobrecargas de pedidos."),
        ("• Inobservancia de normas técnicas y protocolos de seguridad (BPM / 5S): Desorden físico en almacén que retrasa los tiempos de picking y packing.",
         "• Nula tolerancia a la frustración y mal manejo de conflictos: Discusiones acaloradas ante picos de demanda y alta rotación de personal por desmotivación.")
    ]

    for i, (col1, col2) in enumerate(diag_rows, start=1):
        row = diag_table.rows[i]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width = Inches(3.3)
        c1.width = Inches(3.3)
        set_cell_shading(c0, "F8FAFC" if i % 2 == 1 else "EDF2F7")
        set_cell_shading(c1, "F8FAFC" if i % 2 == 1 else "EDF2F7")

        for c, text in [(c0, col1), (c1, col2)]:
            p = c.paragraphs[0]
            p.paragraph_format.space_before = Pt(3)
            p.paragraph_format.space_after = Pt(3)
            p.paragraph_format.line_spacing = 1.15
            r = p.add_run(text)
            r.font.name = "Calibri"
            r.font.size = Pt(10)
            r.font.color.rgb = dark_text
            set_cell_margins(c, top=80, bottom=80, left=100, right=100)

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # --- SECCIÓN 3: PROPUESTA DE SOLUCIONES ---
    h3 = doc.add_heading(level=1)
    h3.paragraph_format.space_before = Pt(12)
    h3.paragraph_format.space_after = Pt(4)
    r_h3 = h3.add_run("3. Propuesta Integral de Soluciones para la Empresa")
    r_h3.font.color.rgb = primary_color
    r_h3.font.size = Pt(14)
    r_h3.font.bold = True

    # 3.1 Hard Skills
    sub1 = doc.add_heading(level=2)
    r_sub1 = sub1.add_run("A. Soluciones basadas en Habilidades Duras (Hard Skills)")
    r_sub1.font.color.rgb = secondary_color
    r_sub1.font.size = Pt(12)
    r_sub1.font.bold = True

    hard_solutions = [
        ("Capacitación y Certificación en ERP/WMS Logístico:", "Implementar un programa de entrenamiento intensivo de 20 horas teórico-prácticas sobre el uso del software de gestión de almacén, automatizando el escaneo de código de barras para eliminar el registro manual."),
        ("Entrenamiento en Métricas y Análisis de Datos (Excel Avanzado y Power BI):", "Formar a coordinadores y líderes de área en paneles de control (dashboards) en tiempo real para monitorear pedidos pendientes, tasa de merma y cumplimiento de plazos de entrega."),
        ("Estandarización de Procesos Operativos y Metodología 5S:", "Redactar manuales de Procedimientos Operativos Estandarizados (POE) y aplicar la metodología 5S (Clasificar, Ordenar, Limpiar, Estandarizar y Disciplina) en el almacén central para reducir tiempos de búsqueda.")
    ]

    for title, desc in hard_solutions:
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        r_title = p.add_run(f"{title} ")
        r_title.bold = True
        r_title.font.color.rgb = primary_color
        r_desc = p.add_run(desc)
        r_desc.font.color.rgb = dark_text

    # 3.2 Soft Skills
    sub2 = doc.add_heading(level=2)
    r_sub2 = sub2.add_run("B. Soluciones basadas en Habilidades Blandas (Soft Skills)")
    r_sub2.font.color.rgb = secondary_color
    r_sub2.font.size = Pt(12)
    r_sub2.font.bold = True

    soft_solutions = [
        ("Taller Vivencial de Comunicación Asertiva y Escucha Activa:", "Dinámicas de role-playing donde operarios y supervisores practiquen el canal de comunicación adecuado, evitando agresiones verbales y sustituyendo reproches por retroalimentación constructiva (feedback SBI: Situación, Comportamiento, Impacto)."),
        ("Programa de Liderazgo Transformacional y Gestión de Conflictos:", "Capacitación exclusiva para mandos medios en técnicas de mediación de disputas, empatía y motivación de equipos sin recurrir a la imposición autoritaria."),
        ("Fortalecimiento del Trabajo en Equipo y Adaptabilidad al Cambio:", "Jornadas de integración interdepartamental para alinear objetivos comunes entre Almacén y Distribución, enfatizando que el éxito de la entrega final depende de la colaboración de toda la cadena."),
        ("Taller de Gestión del Tiempo y Manejo del Estrés Laboral:", "Capacitación en técnicas de priorización (Matriz de Eisenhower) y técnicas de respiración / pausas activas para evitar el colapso emocional en horas punta de despacho.")
    ]

    for title, desc in soft_solutions:
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        r_title = p.add_run(f"{title} ")
        r_title.bold = True
        r_title.font.color.rgb = primary_color
        r_desc = p.add_run(desc)
        r_desc.font.color.rgb = dark_text

    # --- SECCIÓN 4: MATRIZ DE INTEGRACIÓN Y PLAN DE ACCIÓN ---
    h4 = doc.add_heading(level=1)
    h4.paragraph_format.space_before = Pt(12)
    h4.paragraph_format.space_after = Pt(4)
    r_h4 = h4.add_run("4. Matriz de Integración: ¿Cómo se complementan en el trabajo real?")
    r_h4.font.color.rgb = primary_color
    r_h4.font.size = Pt(14)
    r_h4.font.bold = True

    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(6)
    p.add_run("En la práctica empresarial, una habilidad dura sin una blanda genera empleados técnicamente competentes pero tóxicos o aislados; por el contrario, una habilidad blanda sin habilidad dura produce personas motivadas pero ineficientes. A continuación se detalla su articulación:")

    matrix_table = doc.add_table(rows=4, cols=4)
    matrix_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    matrix_table.autofit = False

    m_headers = ["Desafío Operativo", "Habilidad Dura Clave", "Habilidad Blanda Clave", "Impacto Esperado"]
    widths = [Inches(1.5), Inches(1.7), Inches(1.7), Inches(1.7)]

    for j, text in enumerate(m_headers):
        cell = matrix_table.rows[0].cells[j]
        cell.width = widths[j]
        set_cell_shading(cell, "1A365D")
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(text)
        r.font.name = "Calibri"
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.size = Pt(10)
        set_cell_margins(cell, top=100, bottom=100, left=80, right=80)

    m_rows = [
        ("Retraso de despachos en horas punta", "Optimización de rutas con software WMS / GPS", "Trabajo en equipo y flexibilidad bajo presión", "Reducción del 40% en retrasos y cero horas extra improductivas."),
        ("Discrepancias de inventario y pérdidas", "Técnicas de conteo cíclico y Excel automatizado", "Ética profesional y comunicación transparente", "Precisión del inventario superior al 98%."),
        ("Reclamos de clientes por mercadería dañada", "Control de embalaje según norma técnica", "Empatía y orientación al cliente en resolución", "Disminución del 50% en quejas y aumento de fidelización.")
    ]

    for i, row_data in enumerate(m_rows, start=1):
        row = matrix_table.rows[i]
        for j, text in enumerate(row_data):
            cell = row.cells[j]
            cell.width = widths[j]
            set_cell_shading(cell, "F8FAFC" if i % 2 == 1 else "EDF2F7")
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.15
            r = p.add_run(text)
            r.font.name = "Calibri"
            r.font.size = Pt(9.5)
            r.font.color.rgb = dark_text
            set_cell_margins(cell, top=80, bottom=80, left=80, right=80)

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # --- SECCIÓN 5: CONCLUSIONES ---
    h5 = doc.add_heading(level=1)
    h5.paragraph_format.space_before = Pt(12)
    h5.paragraph_format.space_after = Pt(4)
    r_h5 = h5.add_run("5. Conclusiones y Aprendizaje")
    r_h5.font.color.rgb = primary_color
    r_h5.font.size = Pt(14)
    r_h5.font.bold = True

    conclusions = [
        ("Sinergia Indispensable:", "Las habilidades duras garantizan la calidad técnica del producto o servicio, pero son las habilidades blandas las que permiten que los equipos colaboren, se comuniquen y superen contingencias de manera sostenible."),
        ("Rentabilidad Organizacional:", "La inversión simultánea en formación técnica (ERP, metodologías) y desarrollo humano (liderazgo, asertividad) reduce costos operativos derivados de errores y mitiga la rotación de talento."),
        ("Perfil Profesional Moderno (T-Shaped):", "En el entorno laboral actual, las organizaciones valoran al profesional que no solo posee conocimientos técnicos sólidos, sino también la inteligencia emocional suficiente para integrarse a entornos dinámicos y multidisciplinarios.")
    ]

    for title, text in conclusions:
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        r_title = p.add_run(f"{title} ")
        r_title.bold = True
        r_title.font.color.rgb = primary_color
        r_text = p.add_run(text)
        r_text.font.color.rgb = dark_text

    # Save document
    filename = "Caso_Practico_Habilidades_Blandas_y_Duras_Gerson_Pintado.docx"
    doc.save(filename)
    print(f"Document successfully created: {filename}")

if __name__ == "__main__":
    create_case_study()
