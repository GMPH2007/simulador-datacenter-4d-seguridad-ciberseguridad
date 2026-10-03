import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_concept_map():
    fig, ax = plt.subplots(figsize=(15, 10), dpi=300)
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Color Palette
    c_central = "#0F2C59"       # Deep Navy
    c_fisica = "#1E5AA0"        # Blue
    c_logica = "#0D9488"        # Teal
    c_sub_fis = "#EBF3FB"       # Soft Blue bg
    c_sub_log = "#F0FDFA"       # Soft Teal bg
    border_fis = "#2563EB"
    border_log = "#0D9488"

    # Background canvas color
    fig.patch.set_facecolor("#FFFFFF")

    # Helper function to draw rounded boxes
    def draw_box(x, y, w, h, text, bg_color, border_color, text_color="#FFFFFF", fontsize=10, bold=True):
        box = patches.FancyBboxPatch((x, y), w, h,
                                     boxstyle="round,pad=0.2,rounding_size=0.15",
                                     linewidth=1.8, edgecolor=border_color,
                                     facecolor=bg_color)
        ax.add_patch(box)
        weight = 'bold' if bold else 'normal'
        ax.text(x + w/2, y + h/2, text, color=text_color, fontsize=fontsize,
                fontweight=weight, ha='center', va='center', fontfamily='sans-serif',
                multialignment='center')

    # Connecting lines with arrows
    def draw_arrow(x1, y1, x2, y2, color="#64748B"):
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="->", color=color, lw=1.8,
                                    shrinkA=4, shrinkB=4,
                                    connectionstyle="arc3,rad=0"))

    # 1. Central Node
    draw_box(4.5, 8.5, 6.0, 0.9, "SEGURIDAD INTEGRAL EN UN DATA CENTER\n(Protección Física y Lógica)", c_central, c_central, "#FFFFFF", 12, True)

    # 2. Main Branches
    # Left: Seguridad Física
    draw_box(1.2, 7.0, 4.8, 0.75, "SEGURIDAD FÍSICA\n(Infraestructura, Accesos e Instalaciones)", c_fisica, border_fis, "#FFFFFF", 10.5, True)
    draw_arrow(6.0, 8.5, 3.6, 7.75, border_fis)

    # Right: Seguridad Lógica
    draw_box(9.0, 7.0, 4.8, 0.75, "SEGURIDAD LÓGICA\n(Datos, Redes, Sistemas y Aplicaciones)", c_logica, border_log, "#FFFFFF", 10.5, True)
    draw_arrow(9.0, 8.5, 11.4, 7.75, border_log)

    # 3. Sub-nodes Física (Left Side)
    fis_items = [
        ("Control de Acceso Perimetral", "• Esclusa de paso (Mantrap)\n• Autenticación biométrica + RFID\n• Registro estricto de visitantes", 5.6),
        ("Videovigilancia y Sensores", "• CCTV HD con grabación 24/7\n• Sensores infrarrojos y volumétricos\n• Alertas de intrusión en tiempo real", 4.3),
        ("Climatización de Precisión (HVAC)", "• Confinamiento de pasillo frío/caliente\n• Humedad controlada (40% - 60%)\n• Sensores de detección de líquidos", 3.0),
        ("Protección Contra Incendios", "• Detección ultra temprana (VESDA)\n• Extinción con gas limpio (Novec 1230)\n• Cero uso de agua en salas TI", 1.7),
        ("Respaldo y Continuidad Eléctrica", "• UPS online de doble conversión\n• Grupo electrógeno redundante (N+1)\n• Transferencia automática (ATS)", 0.4)
    ]

    for title, desc, y_pos in fis_items:
        draw_box(0.5, y_pos, 5.8, 1.05, f"{title}\n{desc}", c_sub_fis, border_fis, "#0F2C59", 8.5, False)
        # connect branch to subnode
        draw_arrow(3.6, 7.0, 3.6, y_pos + 1.05, border_fis)

    # 4. Sub-nodes Lógica (Right Side)
    log_items = [
        ("Seguridad Perimetral y Redes", "• Firewalls de Nueva Generación (NGFW)\n• Segmentación de red (VLANs / DMZ)\n• Túneles VPN con cifrado IPsec/SSL", 5.6),
        ("Control de Identidad y Accesos (IAM)", "• Autenticación Multifactor (MFA)\n• Principio de Menor Privilegio (RBAC)\n• Gestión centralizada de credenciales", 4.3),
        ("Detección y Monitoreo (SOC / SIEM)", "• Sistema IDS / IPS anti-intrusiones\n• Correlación de logs 24/7 (SIEM)\n• Bloqueo preventivo de anomalías", 3.0),
        ("Cifrado y Protección de Datos", "• Cifrado en reposo (AES-256)\n• Cifrado en tránsito (TLS 1.3)\n• Prevención de fugas de datos (DLP)", 1.7),
        ("Respaldos y Recuperación (DRP)", "• Estrategia de Backup 3-2-1\n• Copias inmutables (anti-ransomware)\n• Plan de Recuperación ante Desastres", 0.4)
    ]

    for title, desc, y_pos in log_items:
        draw_box(8.7, y_pos, 5.8, 1.05, f"{title}\n{desc}", c_sub_log, border_log, "#064E3B", 8.5, False)
        # connect branch to subnode
        draw_arrow(11.4, 7.0, 11.4, y_pos + 1.05, border_log)

    plt.tight_layout()
    plt.savefig("mapa_conceptual_datacenter.png", dpi=300, bbox_inches='tight')
    plt.close()
    print("Mapa conceptual generado exitosamente en mapa_conceptual_datacenter.png")

if __name__ == "__main__":
    draw_concept_map()
