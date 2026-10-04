# MANUAL TÉCNICO Y SUSTENTACIÓN DEL SIMULADOR 4D DE DATA CENTER VIVO
## SISTEMA INTELIGENTE DE MONITOREO Y RESPUESTA A INCIDENTES CON IA AUTÓNOMA

* **Institución:** I.E.S.T.P. "Hermanos Cárcamo" - Paita, Piura
* **Carrera:** Arquitectura de Plataformas y Servicios de Tecnologías de la Información
* **Docente Asesor:** Dr. Javier Eduardo Jaramillo Atoche
* **Estudiantes (Grupo de 5):**
  1. Gerson Misael Pintado Huamán (Líder / Desarrollador)
  2. Manuel Danilo López Garay
  3. Mariana Juliet Clavijo Pinzón
  4. Pedro Miguel Aguilar Flores
  5. Dayron Antonio Urbina Zapata
* **Entrega y Sustentación:** Lunes

---

### 1. PROPÓSITO DEL PROYECTO
Desarrollar una aplicación web interactiva de **Simulación 4D en Tiempo Real** que combine la **arquitectura física y lógica de un Data Center Tier III (ANSI/TIA-942 y norma ISO/IEC 27001)** con un **motor algorítmico de decisión y una Red Neuronal autónoma (con Mente Propia)**.

El sistema permite visualizar, evaluar y mitigar amenazas en tiempo real mediante:
1. Navegación en 360° con ratón y primera persona (WASD).
2. Cámaras de videovigilancia PTZ que giran físicamente hacia los incidentes.
3. Simulación física de fuego, humo, apagón eléctrico (blackout) y forzado de puertas mecánicas.
4. Alarmas sonoras y lumínicas con diseño acústico y cromático único para cada tipo de incidente.

---

### 2. ARQUITECTURA DE SEGURIDAD INTEGRAL (5 BLOQUES DEL PROFESOR)

| Bloque | Componentes Físicos y Lógicos | Estándar / Norma |
| :--- | :--- | :--- |
| **1. Control de Acceso** | Esclusa Mantrap interbloqueada, cerraduras electromagnéticas de 1200 lbs, lector biométrico de huella/iris y tarjetas RFID Mifare DESFire. | ISO 27001 - A.7.1 y A.7.2 |
| **2. CCTV** | Cámaras IP PTZ 1080p con infrarrojos, cobertura traslapada sin puntos ciegos, almacenamiento NVR con RAID-6 y retención de 90 días. | ISO 27001 - A.7.4 |
| **3. Sensores** | Detección de humo por aspiración láser VESDA (Very Early Smoke Detection Apparatus), sondas térmicas en pasillo frío/caliente, sensores de inundación y presurización positiva a 25 Pa. | ANSI/TIA-942 / NFPA 2001 |
| **4. Seguridad Lógica** | Firewall de Nueva Generación (NGFW), IDS/IPS Snort/Suricata, microsegmentación de VLANs, autenticación MFA y almacenamiento inmutable WORM para Base de Datos. | ISO 27001 - A.8.20 y A.8.13 |
| **5. Respaldo / Continuidad** | Banco de baterías UPS modular online de doble conversión con conmutación en CERO milisegundos (0 ms), conmutador de transferencia automática ATS y grupo electrógeno diésel con 72h de autonomía. | ANSI/TIA-942 Tier III |

---

### 3. EFECTOS FÍSICOS Y VISUALES 4D IMPLEMENTADOS

#### A. Cámaras de Seguridad PTZ con Movimiento Físico
* En la sala 3D se encuentran modeladas **4 cámaras robóticas domo** en las esquinas del techo con soportes articulados, lentes de enfoque y LEDs rojos de grabación activa.
* **Seguimiento Robótico:** Al dispararse un incidente o cambiar de cámara (CAM 01 a CAM 05), las cámaras físicas giran suavemente (`lookAt`) orientándose hacia la posición espacial exacta de la amenaza.
* **Monitor PIP:** La ventana superior derecha proyecta el feed con scanlines, timestamp en vivo y modo estática en caso de fallo PoE.

#### B. Mecánica de Puerta Esclusa (Intruso y Robo)
* Al simular **"Acceso no autorizado"**, la puerta acrílica de la esclusa Mantrap se desplaza mecánicamente a un lado simulando el forzado exterior.
* Aparece una **silueta holográfica en rojo del intruso** en el umbral.
* Inmediatamente, el sistema de seguridad activa los electroimanes de 1200 lbs, tiñe la puerta de rojo brillante y proyecta el haz láser de contención, bloqueando al intruso.

#### C. Fuego, Humo Volumétrico y Gas Limpio Novec 1230
* En el incidente de **"Detección de humo"**, se activa un sistema de doble partícula:
  1. *Fuego:* Partículas llameantes amarillas y anaranjadas titilando en la base del Rack 03.
  2. *Humo:* Nube densa grisácea que asciende verticalmente hacia la tubería roja VESDA en el techo.
  3. *Luz Titilante:* Un foco de luz puntual (`fireLight`) parpadea con intensidad estocástica iluminando las carcasas metálicas de los servidores.

#### D. Apagón Eléctrico General (Blackout)
* En el incidente de **"Corte eléctrico general"**, se produce un apagón instantáneo:
  * Los paneles LED del techo y el foco principal se apagan por completo.
  * La sala queda en penumbra y se iluminan exclusivamente las **tiras LED amarillas de emergencia** en el piso técnico y las bahías del Rack 10 (UPS).

#### E. Climatización Industrial CRAC / HVAC y Escalerillas Pasacables
* Dos torres de enfriamiento de precisión en la pared posterior cuentan con **aspas de turbina giratorias**.
* Si la temperatura sube a 32.5 °C, las turbinas aceleran su rotación de 4 a 16 RPM para disipar el calor.
* Sobre los racks corren **escalerillas pasacables amarillas** con haces de fibra óptica luminosa (cian y naranja).

---

### 4. DISEÑO DE ALARMAS SONORAS (WEB AUDIO API)

Cada emergencia cuenta con una firma acústica y cromática diferenciada:

| Incidente | Color de Alerta | Frecuencia y Tipo de Onda | Comportamiento Acústico |
| :--- | :--- | :--- | :--- |
| **Operación Normal** | Esmeralda `#10B981` | Senoidal 440 Hz / 520 Hz | Beep suave de confirmación |
| **Acceso No Autorizado** | Rojo `#EF4444` | Diente de sierra 600 Hz ➔ 1100 Hz | Sirena policial oscilante continua |
| **Fuego y Humo** | Naranja `#EA580C` | Cuadrada 920 Hz | Chicharra de incendios triple pulsante |
| **Temperatura Alta** | Ámbar `#F59E0B` | Senoidal 700 Hz | Pulso rítmico de precaución |
| **Intrusión de Red** | Púrpura `#A855F7` | Diente de sierra 1400 ➔ 600 Hz | Arpegio digital de glitch cibernético |
| **Cámara Desconectada** | Ámbar `#F59E0B` | Ruido estático 800 Hz | Ráfaga de estática de canal de video |
| **Corte de Luz (Blackout)** | Dorado `#EAB308` | Senoidal decreciente 280 ➔ 45 Hz | Drone de caída de tensión y apagón |
| **Ransomware** | Carmesí `#DC2626` | Diente de sierra modulada 1200 Hz | Tono de aislamiento crítico de Base de Datos |

---

### 5. GUÍA PARA LA DEFENSA ANTE EL PROFESOR JARAMILLO

1. **Apertura (30 seg):**
   > *"Doctor Jaramillo, le presentamos el Simulador 4D de Data Center del IESTP Hermanos Cárcamo. Desarrollamos un gemelo digital interactivo con Three.js que integra los 5 bloques de seguridad que usted nos solicitó, junto con un motor de decisiones algorítmico y una Red Neuronal autónoma."*

2. **Demostración de Navegación y Cámaras (1 min):**
   * Presiona **`📹 CAM 02 [Pasillo]`** y muestra la niebla fría flotando a 19.8 °C.
   * Haz clic sobre el **`RACK 01 - DB SAN`** para abrir la ventana de telemetría y explicar el almacenamiento NVMe RAID-10.
   * Selecciona las diferentes cámaras y muestra cómo los domos robóticos del techo giran automáticamente.

3. **Demostración de Emergencias Críticas (1.5 min):**
   * **Acceso no autorizado:** Muestra cómo la puerta de la esclusa se abre simulando la vulneración, aparece el intruso holográfico y la puerta se cierra con electroimanes mientras suena la sirena policial.
   * **Detección de humo:** Muestra las llamas y el humo subiendo hacia el VESDA con la chicharra de incendio.
   * **Corte eléctrico:** Muestra el apagón general en la sala y cómo las luces de piso sostienen la visibilidad junto a las baterías UPS con 0 ms de corte.
   * **Ransomware:** Muestra el escudo holográfico morado envolviendo la Base de Datos y la inmutabilidad WORM.

4. **Cierre y Cumplimiento de Normas (30 seg):**
   > *"Cada respuesta está respaldada por la norma ISO/IEC 27001 en seguridad de la información, el estándar ANSI/TIA-942 Tier III en mantenimiento concurrente, y la norma NFPA 2001 para extinción por gas limpio."*
