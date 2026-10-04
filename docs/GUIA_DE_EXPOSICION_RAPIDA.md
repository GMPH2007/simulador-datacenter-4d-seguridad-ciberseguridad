# GUÍA DE EXPOSICIÓN RÁPIDA – SEGURIDAD EN DATA CENTER
## ESTRATEGIA PARA SACAR 20 EN LA PRESENTACIÓN ANTE EL PROFESOR

* **Docente:** Dr. Javier Eduardo Jaramillo Atoche
* **Integrantes:** Gerson Misael Pintado, Manuel Danilo López, Mariana Juliet Clavijo, Pedro Miguel Aguilar, Dayron Antonio Urbina.
* **Tiempo estimado de exposición:** 3 a 5 minutos.

---

### 1. INTRODUCCIÓN (Quién expone: Presentador 1)
> *"Buenos días profesor y compañeros. Nuestro grupo ha desarrollado el caso práctico y mapa conceptual sobre la Seguridad Física y Lógica en un Data Center, tomando como referencia una empresa real de la región: **FinanSur Data Cloud S.A.C.**, que procesa más de 85,000 transacciones bancarias al día."*

---

### 2. EL INCIDENTE Y DIAGNÓSTICO (Quién expone: Presentador 2)
> *"El problema comenzó con un apagón eléctrico en la zona industrial. Se presentaron dos fallas críticas:*
> 1. ***Falla Física:*** *Las baterías de las UPS colapsaron en 7 minutos por falta de mantenimiento, y el generador no arrancó porque el conmutador ATS estaba en manual. La sala subió a 39°C, los servidores se apagaron por emergencia y se abrieron las puertas para ventilar, permitiendo que personal externo ingrese sin registro.*
> 2. ***Falla Lógica:*** *Al regresar la luz, atacantes externos aprovecharon que el puerto RDP (3389) estaba abierto a Internet sin VPN ni doble factor de autenticación (MFA), ejecutando un ataque de fuerza bruta sobre la cuenta Administrador."*

---

### 3. PROPUESTA DE SOLUCIÓN TÉCNICA (Quién expone: Presentador 3)
> *"Para resolver esto de raíz aplicamos dos estándares internacionales: **ANSI/TIA-942 Tier III** e **ISO/IEC 27001**:*
> * **En Seguridad Física:** Implementamos una esclusa **Mantrap** con biometría dactilar/facial y RFID; climatización de precisión con pasillo frío/caliente (18°-22°C); detección temprana **VESDA** y extinción por gas limpio **Novec 1230** (cero agua); y doble respaldo eléctrico con UPS modular y generador automático con ATS.
> * **En Seguridad Lógica:** Segmentamos la red mediante **VLANs** y DMZ con un Firewall **NGFW**; cerramos todos los puertos directos exigiendo **VPN**; activamos **MFA (Doble Factor)** obligatorio; monitoreo de intrusiones con **IDS/IPS y SIEM 24/7**; y copias de seguridad bajo la regla **Backup 3-2-1 con inmutabilidad WORM** para frenar el Ransomware."*

---

### 4. DEFENSA DEL MAPA CONCEPTUAL (Quién expone: Presentador 4 o 5)
> *"En nuestro mapa conceptual mostramos que la seguridad en un Data Center se sostiene en la **Tríada CID** (Confidencialidad, Integridad y Disponibilidad) y se divide en dos brazos inseparables:
> * El brazo **Físico** (izquierda) protege lo tangible: acceso, vigilancia, clima, fuego y energía.
> * El brazo **Lógico** (derecha) protege lo virtual: perímetro NGFW, VLANs, control IAM/MFA, cifrado AES-256 y respaldos en la nube.
>
> **Conclusión clave:** La seguridad lógica no sirve si la física falla (cualquiera puede desconectar el servidor con la mano); y una sala blindada no sirve si dejamos los puertos lógicos abiertos a Internet. Ambas deben trabajar integradas."*
