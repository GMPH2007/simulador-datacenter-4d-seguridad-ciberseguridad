# 🏢 Simulador 4D de Centro de Datos Tier III & SOC de Ciberseguridad

[![GitHub Pages](https://img.shields.io/badge/Demo_en_Vivo-GitHub_Pages-00F0FF?style=for-the-badge&logo=github&logoColor=white)](https://gmph2007.github.io/simulador-datacenter-4d-seguridad-ciberseguridad/)
[![Tier III SLA](https://img.shields.io/badge/TIA--942-Tier_III_99.999%25_SLA-10B981?style=for-the-badge&logo=serverfault&logoColor=white)](https://gmph2007.github.io/simulador-datacenter-4d-seguridad-ciberseguridad/)
[![ISO 27001](https://img.shields.io/badge/Estándar-ISO%2FIEC_27001-3B82F6?style=for-the-badge&logo=securityscorecard&logoColor=white)](https://gmph2007.github.io/simulador-datacenter-4d-seguridad-ciberseguridad/)
[![Three.js](https://img.shields.io/badge/Motor_3D-Three.js_r128-black?style=for-the-badge&logo=three.js&logoColor=white)](https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js)
[![Web Audio API](https://img.shields.io/badge/Audio-Web_Audio_Sintetizado-purple?style=for-the-badge&logo=audacity&logoColor=white)](https://gmph2007.github.io/simulador-datacenter-4d-seguridad-ciberseguridad/)
[![Licencia](https://img.shields.io/badge/Licencia-MIT-green?style=for-the-badge)](LICENSE)

---

## 🏛️ Identificación Institucional y Académica

* **Institución:** Instituto de Educación Superior Tecnológico Público **"Hermanos Cárcamo"** (Paita, Piura, Perú).
* **Programa de Estudios:** Arquitectura de Plataformas y Servicios de Tecnologías de la Información.
* **Unidad Didáctica:** Seguridad Informática y Auditoría de TI.
* **Docente Especialista:** **Dr. Javier Eduardo Jaramillo Atoche** *(Doctor en Tecnologías de la Información y Comunicaciones - UNP)*.
* **Equipo de Investigación y Desarrollo:**
  1. **Gerson Misael Pintado Huamán** *(Líder de Proyecto / Modelado 3D & Arquitectura)*
  2. **Manuel Danilo López Garay** *(Análisis de Redes y Seguridad Lógica)*
  3. **Mariana Juliet Clavijo Pinzón** *(Evaluación de Riesgos y Matriz ISO 27001)*
  4. **Pedro Miguel Aguilar Flores** *(Infraestructura Eléctrica y Climatización TIA-942)*
  5. **Dayron Antonio Urbina Zapata** *(Sistemas Biométricos y Vigilancia CCTV)*

---

## 🌐 Enlaces de Acceso Inmediato

| Recurso | Enlace Directo | Descripción |
| :--- | :--- | :--- |
| **🚀 Simulador 4D en Vivo (GitHub Pages)** | [**Abrir Simulador 4D Online**](https://gmph2007.github.io/simulador-datacenter-4d-seguridad-ciberseguridad/) | Ejecución 100% web en tiempo real sin instalar programas. |
| **🗺️ Mapa Conceptual Interactivo** | [**Abrir Mapa Conceptual**](https://gmph2007.github.io/simulador-datacenter-4d-seguridad-ciberseguridad/MAPA_CONCEPTUAL_INTERACTIVO.html) | Dashboard dinámico de conceptos clave de seguridad física y lógica. |
| **📄 Informe Académico PDF** | [**Ver Documento PDF**](docs/TRABAJO_DATA_CENTER_PRO_MAX.pdf) | Monografía formal completa con rúbrica, cuestionario y matriz de riesgos. |
| **📘 Manual Técnico 3D** | [**Ver Manual Técnico**](docs/MANUAL_TECNICO_SIMULADOR_3D.md) | Especificaciones de Three.js, shaders, Web Audio y telemetría. |
| **🎤 Guía de Exposición Rápida** | [**Ver Guía de Exposición**](docs/GUIA_DE_EXPOSICION_RAPIDA.md) | Discurso paso a paso para la defensa ante el profesor. |

---

## 📋 Matriz de Simulación de Incidentes (Rúbrica del Docente)

El docente **Dr. Javier Eduardo Jaramillo Atoche** *(Doctor en Tecnologías de la Información y Comunicaciones - UNP)* estableció como requisito fundamental la simulación interactiva de cada vector de amenaza, clasificando con exactitud si corresponde a **Acceso Físico o Acceso Lógico**, y reportando si el centro de datos queda en estado **Protegido o con Vulnerabilidad Mitigada**.

| N° | Incidente Simulado | Clasificación Requerida | Estado de Protección | Contramedida Autónoma en el Simulador 4D |
| :---: | :--- | :---: | :---: | :--- |
| **0** | **Operación Normal (Baseline)** | **Físico y Lógico** | **PROTEGIDO** | Monitoreo continuo de 128 sensores IoT. Variables dentro de parámetros TIA-942 e ISO 27001. |
| **1** | **Intrusión en Esclusa Mantrap** | **ACCESO FÍSICO** | **BLOQUEADO Y PROTEGIDO** | Tarjeta RFID clonada sin match biométrico. Bloqueo electromagnético (1200 lbs), baliza estroboscópica 360°, sirena policial y PTZ enfocada. |
| **2** | **Detección de Humo y Fuego** | **FÍSICO / AMBIENTAL** | **EXTINCIÓN ACTIVA (PROTEGIDO)** | Sensor óptico y VESDA aspiran combustión en Rack A1. Corte selectivo EPO y descarga de gas limpio **NOVEC 1230** sin daño a componentes. |
| **3** | **Sobrecalentamiento Térmico** | **FÍSICO / CLIMATIZACIÓN** | **CONMUTACIÓN N+1 (PROTEGIDO)** | Falla en compresor CRAC-01 (>28°C). Conmutación automática a turbina CRAC-02 a **1450 RPM** y apertura de ventilación de piso técnico. |
| **4** | **Cámara Desconectada (Caída 3D)** | **FÍSICO / VULNERABILIDAD** | **VULNERABILIDAD MITIGADA** | Corte de cable PoE en CAM-02. **La cámara se agacha físicamente cayendo 80° con chispas**, estática en CCTV, activación de cobertura cruzada y PIR. |
| **5** | **Corte de Energía (Blackout)** | **FÍSICO / ELÉCTRICO** | **CONTINUIDAD TIER III (PROTEGIDO)** | Caída de acometida pública. **Parpadeo de tensión, sonido de disyuntor y apagón total**, transferencia a UPS 2N en 4ms y arranque de diésel ATS. |
| **6** | **Ciberataque DDoS (85 Gbps)** | **ACCESO LÓGICO** | **MITIGACIÓN LÓGICA (PROTEGIDO)** | Inundación SYN-Flood hacia la base de datos. Desvío BGP Anycast a Scrubbing Center, filtrado en NGFW Fortinet y microsegmentación Zero Trust. |
| **7** | **Ataque de Ransomware (Matrix)** | **ACCESO LÓGICO** | **SELLADO INMUTABLE (PROTEGIDO)** | Intento de cifrado en FinanSur Core DB. **Cascada digital Matrix en verde fluyendo en los racks**, sellado WORM inmutable en SAN y aislamiento de VLAN. |

---

## 🎮 Efectos Especiales y Gráficos 4D de Grado Industrial

```
                           SISTEMA 4D INTEGRADO
     ┌─────────────────────────────────────────────────────────────┐
     │                    CANVAS WEBGL THREE.JS                    │
     │  ┌─────────────────┐ ┌─────────────────┐ ┌───────────────┐  │
     │  │  10 Racks 42U   │ │ Turbinas CRAC   │ │  Esclusa      │  │
     │  │  Blades + LEDs  │ │  6 Aspas 3D     │ │  Biométrica   │  │
     │  └────────┬────────┘ └────────┬────────┘ └───────┬───────┘  │
     │           │                   │                  │          │
     │  ┌────────┴───────────────────┴──────────────────┴───────┐  │
     │  │  Efectos: Cascada Matrix Verde | Caída Cámara 3D      │  │
     │  │  Apagón Dinámico | Baliza 360° | Niebla Criogénica    │  │
     │  └────────────────────────────┬──────────────────────────┘  │
     └───────────────────────────────┼─────────────────────────────┘
                                     │
     ┌───────────────────────────────┴─────────────────────────────┐
     │                 TABLERO DE MANDO SOC & TELEMETRÍA           │
     │  ┌───────────────┐ ┌─────────────────┐ ┌─────────────────┐  │
     │  │ 4 Gráficas    │ │  Mente Propia   │ │  Terminal       │  │
     │  │ SVG en Vivo   │ │  Red Neuronal   │ │  Syslog RFC5424 │  │
     │  └───────────────┘ └─────────────────┘ └─────────────────┘  │
     └─────────────────────────────────────────────────────────────┘
```

1. **📷 Cámara Desconectada y Caída Física 3D**:
   * Al simular el fallo, la cámara del pasillo frío (**CAM-02**) rota su eje `X` suavemente hasta los 80°, **agachándose hacia el suelo** como un equipo descolgado por pérdida de alimentación PoE.
   * Se emiten **chispas eléctricas de partículas** en la caja de paso conduit.
   * La pantalla del monitor CCTV conmuta inmediatamente a **estática de nieve animada**, cambiando el indicador a `OFFLINE`.
2. **❇️ Cascada Digital Matrix en Verde Fósforo**:
   * En caso de ataque de virus o ransomware, la fachada frontal de los servidores blade se recubre de una **lluvia digital animada de caracteres Matrix (`#00FF66`)** generada dinámicamente en memoria canvas a 60 FPS.
   * El Rack A2 de la Base de Datos FinanSur Core queda protegido dentro de un **escudo holográfico verde de cuarentena inmutable**.
3. **⚡ Apagón Eléctrico Dinámico (Blackout Comercial)**:
   * Simula un corte real de media tensión: las luces troffer parpadean 3 veces erráticamente, salta un arco de chispas en el tablero, y la sala queda **completamente a oscuras** con un estruendoso golpe de disyuntor (`CLACK!`), entrando únicamente tenues luces de emergencia nocturnas.
   * Las aspas de las turbinas CRAC se frenan a 0 RPM.
4. **🚨 Baliza Giratoria 360° y Alarma Sonora Nítida**:
   * Baliza estroboscópica de domo rojo instalada en el techo que rota continuamente en 3D proyectando un foco SpotLight de 360° sobre las paredes durante las alertas.
   * Sirena industrial modulada en frecuencia con doble oscilador sintetizado por **Web Audio API** para máxima nitidez sonora.
5. **❄️ Contención de Pasillo Frío (*Cold Aisle Containment*)**:
   * Techo abovedado de policarbonato translúcido y puertas corredizas de vidrio templado en los extremos del pasillo de servidores con tiras LED cyan.
6. **🌀 Unidades CRAC con Turbinas 3D Giratorias**:
   * Dos unidades de climatización industrial con túnel de viento cilíndrico, 6 aspas anguladas girando en tiempo real, rejillas concéntricas de seguridad y anillo LED de estado.
7. **🖧 Bandejas Portacables & FiberGuide Amarillo**:
   * Sistema de malla electrogalvanizada suspendida del techo con varillas roscadas *unistrut*, mazo de cables CAT6A azul y canaleta amarilla FiberGuide de fibra óptica con bajantes en cascada a cada rack.

---

## 🔊 Motor de Audio Sintetizado en Tiempo Real (Web Audio API)

No requiere archivos de audio externos (cero enlaces rotos, 100% autónomo y funcional sin conexión):

* **Clic Táctil Cyber:** Respuesta mecánica táctil de 1400 Hz a 800 Hz en cada interacción.
* **Sirena Policial de Intrusión:** Oscilador de onda diente de sierra modulado entre 600 Hz y 1100 Hz.
* **Buzzer Triple de Evacuación:** Tres ráfagas de onda cuadrada a 920 Hz para incendios y humo.
* **Chispa Eléctrica y Desconexión:** Ráfaga de ruido blanco pasabanda de 2200 Hz y caída de tono.
* **Colapso Eléctrico:** Disyuntor mecánico seguido de caída en sub-graves (*sub-bass drop*) de 120 Hz a 20 Hz.
* **Matrix Cyber Synth:** Arpegios electrónicos rápidos en escala pentatónica para ciberataques.
* **Zumbido Ambiental CRAC:** Tono grave de 62 Hz con filtro pasa-bajo que simula las turbinas en marcha (activable con el botón `🌀`).
* **Narrador de Voz con IA:** Síntesis de voz en español (`SpeechSynthesisUtterance`) que narra el vector de amenaza y la contramedida en tiempo real.

---

## 📂 Estructura del Repositorio

```bash
├── index.html                               # Aplicación principal 4D lista para GitHub Pages
├── SIMULADOR_DATA_CENTER_3D.html            # Archivo maestro del simulador 3D / 4D
├── MAPA_CONCEPTUAL_INTERACTIVO.html        # Mapa conceptual interactivo en HTML5/CSS3
├── README.md                                # Documentación técnica y académica completa
├── LICENSE                                  # Licencia de código abierto MIT
├── .gitignore                               # Exclusiones de Git
│
├── docs/                                    # Carpeta de Documentación Formal
│   ├── TRABAJO_DATA_CENTER_PRO_MAX.pdf      # Informe académico final en formato PDF (667 KB)
│   ├── TRABAJO_DATA_CENTER_PRO_MAX.docx     # Informe editable en Microsoft Word (2.35 MB)
│   ├── Caso_Practico_Seguridad_DataCenter.md# Análisis detallado de los casos prácticos
│   ├── MANUAL_TECNICO_SIMULADOR_3D.md       # Manual de ingeniería y Three.js
│   ├── GUIA_DE_EXPOSICION_RAPIDA.md         # Guion de defensa oral ante el jurado
│   └── Caso_Practico_Habilidades_Blandas.md # Caso complementario de habilidades
│
├── assets/                                  # Recursos Gráficos e Infografías
│   ├── datacenter_seguridad_fisica.jpg      # Render de infraestructura física
│   ├── datacenter_seguridad_logica.jpg      # Render de seguridad lógica y redes
│   ├── mapa_conceptual_datacenter.png       # Diagrama de mapa conceptual
│   ├── mapa_conceptual_datacenter_hd.png    # Versión en alta resolución HD
│   └── mapa_conceptual_infografia.jpg       # Infografía ejecutiva de seguridad
│
└── src/                                     # Scripts de Generación y Herramientas Python
    ├── make_simulator_html.py               # Generador del simulador 4D
    ├── generar_mapa_hd.py                   # Generador del mapa conceptual
    └── crear_doc_datacenter.py              # Generador de documentos Word/PDF
```

---

## 🛠️ Instalación y Ejecución Local

No requiere NodeJS, servidores Apache ni dependencias complejas. Es completamente autónomo:

```bash
# 1. Clonar el repositorio
git clone https://github.com/GMPH2007/simulador-datacenter-4d-seguridad-ciberseguridad.git

# 2. Entrar al directorio
cd simulador-datacenter-4d-seguridad-ciberseguridad

# 3. Abrir en cualquier navegador moderno (Chrome, Edge, Firefox, Brave)
start index.html
```

---

## 📜 Licencia y Derechos de Autor

Este proyecto ha sido desarrollado con fines académicos y de investigación científica para el **I.E.S.T.P. "Hermanos Cárcamo" - Paita**. Distribuido bajo los términos de la [Licencia MIT](LICENSE).

**© 2026 Gerson Misael Pintado Huamán y Equipo de Investigación.**
