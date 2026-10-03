import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_enhanced_concept_map():
    # Creamos un lienzo amplio y de altísima resolución
    fig, ax = plt.subplots(figsize=(16, 11), dpi=300)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 11)
    ax.axis('off')
    fig.patch.set_facecolor("#FFFFFF")

    # Paleta de colores profesionales
    NAVY_MAIN = "#0A2540"      # Azul noche elegante
    BLUE_PHYS = "#1E40AF"      # Azul rey para física
    TEAL_LOG = "#0F766E"       # Verde azulado para lógica
    LIGHT_BLUE = "#EFF6FF"     # Fondo suave física
    LIGHT_TEAL = "#F0FDFA"     # Fondo suave lógica
    BORDER_BLUE = "#3B82F6"
    BORDER_TEAL = "#14B8A6"
    LINE_COLOR = "#64748B"

    # Función para dibujar cajas redondeadas estilizadas
    def draw_box(x, y, w, h, text, bg, border, text_color="#FFFFFF", fontsize=9.5, bold=True):
        box = patches.FancyBboxPatch((x, y), w, h,
                                     boxstyle="round,pad=0.2,rounding_size=0.15",
                                     linewidth=1.8, edgecolor=border,
                                     facecolor=bg)
        ax.add_patch(box)
        weight = 'bold' if bold else 'normal'
        ax.text(x + w/2, y + h/2, text, color=text_color, fontsize=fontsize,
                fontweight=weight, ha='center', va='center', fontfamily='sans-serif',
                multialignment='center')

    # Función para dibujar flechas conectores
    def draw_conn(x1, y1, x2, y2, color=LINE_COLOR, lw=2.0):
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                                    shrinkA=3, shrinkB=3,
                                    mutation_scale=14,
                                    connectionstyle="arc3,rad=0"))

    # TÍTULO DEL MAPA
    ax.text(8.0, 10.6, "MAPA CONCEPTUAL: SEGURIDAD FÍSICA Y LÓGICA EN UN DATA CENTER",
            color=NAVY_MAIN, fontsize=13, fontweight='bold', ha='center', va='center')
    ax.text(8.0, 10.25, "Normas de Referencia: ISO/IEC 27001 | ANSI/TIA-942 (Tier III)",
            color="#64748B", fontsize=9.5, fontstyle='italic', ha='center', va='center')

    # 1. NODO CENTRAL
    draw_box(4.5, 9.0, 7.0, 0.9,
             "SEGURIDAD INTEGRAL EN UN DATA CENTER\n(Garantía de Disponibilidad, Confidencialidad e Integridad)",
             NAVY_MAIN, NAVY_MAIN, "#FFFFFF", 11.5, True)

    # 2. RAMAS PRINCIPALES (NIVEL 2)
    # Izquierda: Seguridad Física
    draw_box(1.0, 7.6, 5.5, 0.8,
             "1. SEGURIDAD FÍSICA\nProtección de instalaciones, hardware y entorno ambiental",
             BLUE_PHYS, BORDER_BLUE, "#FFFFFF", 10.5, True)
    draw_conn(6.2, 9.0, 3.75, 8.4, BORDER_BLUE, 2.2)

    # Derecha: Seguridad Lógica
    draw_box(9.5, 7.6, 5.5, 0.8,
             "2. SEGURIDAD LÓGICA\nProtección de datos, redes, sistemas y accesos virtuales",
             TEAL_LOG, BORDER_TEAL, "#FFFFFF", 10.5, True)
    draw_conn(9.8, 9.0, 12.25, 8.4, BORDER_TEAL, 2.2)

    # 3. PILARES DE SEGURIDAD FÍSICA (Izquierda - 5 bloques)
    fisica_sub = [
        ("Control de Acceso Perimetral",
         "• Esclusas de paso interbloqueadas (Mantrap)\n• Autenticación biométrica (Huella/Facial) + RFID\n• Registro digital de visitas y bitácora obligatoria", 6.1),
        ("Videovigilancia y Sensores (CCTV)",
         "• Cámaras IP HD 24/7 con visión infrarroja\n• Sensores de apertura en racks de servidores\n• Retención mínima de grabaciones por 90 días", 4.7),
        ("Climatización de Precisión (HVAC)",
         "• Confinamiento de pasillos frío / caliente\n• Temperatura controlada: 18°C a 22°C\n• Humedad relativa: 40% - 60% y sensores de agua", 3.3),
        ("Protección Contra Incendios",
         "• Detección ultra temprana por humo (VESDA)\n• Extinción automática con gas limpio (Novec 1230)\n• Prohibición absoluta de rociadores de agua", 1.9),
        ("Respaldo Eléctrico Continuo (Tier III)",
         "• Doble alimentación eléctrica (Acometidas A y B)\n• Sistema UPS trifásico modular de doble conversión\n• Generador diésel con conmutación automática (ATS)", 0.5)
    ]

    for title, desc, y in fisica_sub:
        draw_box(0.5, y, 6.5, 1.1, f"{title}\n{desc}", LIGHT_BLUE, BORDER_BLUE, "#0F2942", 8.5, False)
        draw_conn(3.75, 7.6, 3.75, y + 1.1, BORDER_BLUE, 1.6)

    # 4. PILARES DE SEGURIDAD LÓGICA (Derecha - 5 bloques)
    logica_sub = [
        ("Seguridad Perimetral y Redes",
         "• Firewall de Nueva Generación (NGFW) en alta disponibilidad\n• Segmentación de red mediante VLANs dedicadas y DMZ\n• Acceso remoto exclusivamente por VPN con cifrado IPsec/SSL", 6.1),
        ("Control de Identidad y Accesos (IAM)",
         "• Autenticación Multifactor (MFA/2FA) obligatoria\n• Principio de Menor Privilegio y control por roles (RBAC)\n• Eliminación total de cuentas y contraseñas genéricas", 4.7),
        ("Detección y Monitoreo (SOC / SIEM)",
         "• Sistemas de detección y prevención de intrusos (IDS/IPS)\n• Servidor central de correlación de eventos y logs (SIEM)\n• Alertas y bloqueo automatizado ante ataques en tiempo real", 3.3),
        ("Cifrado y Protección de la Información",
         "• Cifrado de bases de datos y discos en reposo (AES-256)\n• Cifrado de comunicaciones en tránsito (TLS 1.3 / HTTPS)\n• Soluciones DLP para prevención de fuga de datos confidenciales", 1.9),
        ("Continuidad Operativa y Respaldos (DRP)",
         "• Estrategia de Backup 3-2-1 con copias en la nube\n• Almacenamiento inmutable WORM protegido contra Ransomware\n• Plan de Recuperación ante Desastres (DRP) con pruebas periódicas", 0.5)
    ]

    for title, desc, y in logica_sub:
        draw_box(9.0, y, 6.5, 1.1, f"{title}\n{desc}", LIGHT_TEAL, BORDER_TEAL, "#064E3B", 8.5, False)
        draw_conn(12.25, 7.6, 12.25, y + 1.1, BORDER_TEAL, 1.6)

    plt.tight_layout()
    plt.savefig("mapa_conceptual_datacenter_hd.png", dpi=300, bbox_inches='tight')
    plt.close()
    print("Mapa conceptual HD generado con éxito en mapa_conceptual_datacenter_hd.png")

if __name__ == "__main__":
    draw_enhanced_concept_map()
