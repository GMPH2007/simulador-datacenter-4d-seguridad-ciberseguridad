# -*- coding: utf-8 -*-
"""
Generador Maestro y Definitivo del Simulador 4D de Data Center
Correcciones de calidad estética y ergonomía solicitadas por el usuario:
1. Ventiladores industriales ultra realistas con rejillas de acero y turbinas aerodinámicas.
2. Cámaras de vigilancia CCTV profesionales montadas en paredes/techo con soportes y viseras (sin esferas flotantes).
3. Escalerillas pasacables metálicas con suspensión de techo y haces delgados de fibra óptica.
4. Iluminación suave sin manchas duras y niebla fría con partículas esféricas difusas (sin cubos).
5. Sistema anti-clic accidental: La cámara se rota con el ratón sin abrir mensajes molestos. Panel de telemetría HUD no invasivo.
"""
import os

html_code = r'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Simulador 4D de Data Center Autónomo - IESTP Hermanos Cárcamo</title>
  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <!-- Three.js y OrbitControls -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
  <style>
    @keyframes pulse-neon {
      0%, 100% { opacity: 1; filter: drop-shadow(0 0 10px #06B6D4); }
      50% { opacity: 0.55; filter: drop-shadow(0 0 3px #06B6D4); }
    }
    @keyframes pulse-alarm {
      0%, 100% { opacity: 1; filter: drop-shadow(0 0 16px var(--alarm-color, #EF4444)); }
      50% { opacity: 0.35; filter: drop-shadow(0 0 4px var(--alarm-color, #EF4444)); }
    }
    @keyframes flow-synapse {
      0% { stroke-dashoffset: 140; }
      100% { stroke-dashoffset: 0; }
    }
    .alarm-glow {
      animation: pulse-alarm 1.1s infinite ease-in-out;
    }
    .synapse-active {
      stroke-dasharray: 6;
      animation: flow-synapse 1s linear infinite;
    }
    .scanlines-overlay {
      background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.45) 50%);
      background-size: 100% 4px;
    }
    #canvas-container {
      position: relative;
      width: 100%;
      height: 640px;
      background: radial-gradient(circle at center, #0B1329 0%, #020617 100%);
      border-radius: 1.25rem;
      overflow: hidden;
      cursor: grab;
      user-select: none;
    }
    #canvas-container:active {
      cursor: grabbing;
    }
    .hud-glass {
      background: rgba(10, 15, 30, 0.90);
      backdrop-filter: blur(14px);
      border: 1px solid rgba(56, 189, 248, 0.28);
    }
    .tech-card {
      transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .tech-card:hover {
      transform: translateY(-2px);
      box-shadow: 0 10px 25px -5px rgba(6, 182, 212, 0.25);
    }
    /* Estilo del scrollbar */
    ::-webkit-scrollbar {
      width: 6px;
      height: 6px;
    }
    ::-webkit-scrollbar-track {
      background: #090D16;
    }
    ::-webkit-scrollbar-thumb {
      background: #1E293B;
      border-radius: 3px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: #0284C7;
    }
  </style>
</head>
<body class="bg-slate-950 text-slate-100 antialiased p-3 md:p-5 min-h-screen">

  <div class="max-w-7xl mx-auto space-y-4">

    <!-- 1. ENCABEZADO INSTITUCIONAL OFICIAL -->
    <header class="bg-slate-900 border border-slate-800 rounded-2xl p-4 md:p-5 shadow-2xl flex flex-col md:flex-row justify-between items-center gap-4 relative overflow-hidden">
      <!-- Glow decorativo superior -->
      <div id="header-glow" class="absolute -top-10 left-1/4 w-96 h-28 bg-cyan-500/15 rounded-full blur-3xl pointer-events-none transition-all duration-500"></div>

      <div class="flex items-center gap-4 relative z-10">
        <!-- Escudo Institucional de Paita -->
        <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-blue-700 via-indigo-950 to-cyan-900 p-1 flex items-center justify-center shadow-lg shadow-cyan-500/25 border border-cyan-400/40 relative overflow-hidden flex-shrink-0">
          <svg class="w-11 h-11 text-cyan-300" viewBox="0 0 64 64" fill="none" stroke="currentColor">
            <path d="M12 18L32 6L52 18V44C52 52 32 58 32 58C32 58 12 52 12 44V18Z" stroke-width="2.5" fill="#0A192F" />
            <circle cx="32" cy="22" r="5" stroke-width="2.5" />
            <path d="M32 27V46M22 36C22 44 42 44 42 36" stroke-width="2.5" stroke-linecap="round" />
            <path d="M26 31H38" stroke-width="2" stroke-linecap="round" />
          </svg>
          <div class="absolute bottom-0 inset-x-0 bg-blue-600/95 text-[8px] font-black text-center text-white tracking-widest py-0.5">PAITA</div>
        </div>

        <div>
          <div class="flex items-center gap-2 text-[11px] font-black tracking-widest text-cyan-400 uppercase">
            <span>I.E.S.T.P. "HERMANOS CÁRCAMO"</span>
            <span>•</span>
            <span class="text-blue-400">ARQUITECTURA DE PLATAFORMAS DE TI</span>
          </div>
          <h1 class="text-xl md:text-2xl font-black text-white tracking-tight flex items-center flex-wrap gap-2">
            SIMULADOR 4D DE DATA CENTER VIVO & AUTÓNOMO
            <span class="text-xs px-2.5 py-0.5 bg-gradient-to-r from-cyan-500 to-blue-600 text-white font-extrabold rounded-full shadow-md shadow-cyan-500/30">IA CON MENTE PROPIA</span>
          </h1>
          <p class="text-xs text-slate-400">Ventiladores CRAC de Turbina, Cámaras PTZ en Paredes, Escalerillas Pasacables, Niebla Suave y Control Suave con Ratón</p>
        </div>
      </div>

      <div class="flex items-center gap-3 bg-slate-800/80 px-4 py-2.5 rounded-xl border border-slate-700 text-xs relative z-10">
        <div>
          <span class="text-slate-400 block text-[10px] font-bold uppercase tracking-wider">DOCENTE ASESOR</span>
          <span class="font-extrabold text-cyan-300">Prof. Javier Eduardo Jaramillo Atoche</span>
        </div>
        <div class="h-8 w-px bg-slate-700"></div>
        <div>
          <span class="text-slate-400 block text-[10px] font-bold uppercase tracking-wider">GRUPO DE TRABAJO (5)</span>
          <span class="font-bold text-white" title="Gerson Pintado, Manuel Danilo López, Mariana Juliet Clavijo, Pedro Miguel Aguilar, Dayron Antonio Urbina">
            Gerson Pintado Huamán & Equipo
          </span>
        </div>
        <!-- Controles de Audio y Voz -->
        <div class="flex items-center gap-1.5 ml-1">
          <button onclick="toggleAudio()" id="btn-audio" class="p-2 rounded-lg bg-slate-700 hover:bg-slate-600 text-cyan-300 transition" title="Alarma Sonora ON/OFF">
            🔊
          </button>
          <button onclick="toggleSpeech()" id="btn-speech" class="p-2 rounded-lg bg-slate-700 hover:bg-slate-600 text-cyan-300 transition" title="Voz Sintetizada de IA ON/OFF">
            🎙️
          </button>
        </div>
      </div>
    </header>

    <!-- 2. BANNER DE ESTADO Y TELEMETRÍA DE LA IA -->
    <div id="banner-alerta" class="bg-slate-900 border border-slate-800 rounded-2xl p-4 shadow-lg transition-all duration-300">
      <div class="flex items-center justify-between flex-wrap gap-3">
        <div class="flex items-center gap-3">
          <span id="dot-alerta" class="w-4 h-4 rounded-full bg-emerald-500 shadow-lg shadow-emerald-500/50"></span>
          <div>
            <h2 id="titulo-alerta" class="font-black text-white text-sm md:text-base tracking-wide uppercase">
              ESTADO: OPERACIÓN NORMAL (SALA CLIMATIZADA)
            </h2>
            <p id="subtitulo-alerta" class="text-xs text-slate-400">
              Monitoreo activo de temperatura criogénica, sensores VESDA, tráfico de red y clúster de Base de Datos.
            </p>
          </div>
        </div>

        <div class="flex items-center gap-3">
          <div class="flex items-center gap-2 bg-slate-950 px-3.5 py-1.5 rounded-xl border border-slate-800 text-xs">
            <span class="w-2.5 h-2.5 rounded-full bg-cyan-400 animate-ping"></span>
            <span class="text-slate-400 text-[11px]">Agente Neuronal:</span>
            <span id="ai-status-tag" class="font-bold text-cyan-300">Vigilancia Autónoma Activa</span>
          </div>
          <div class="hidden sm:flex items-center gap-2 bg-blue-950/80 px-3 py-1.5 rounded-xl border border-blue-800/80 text-xs">
            <span class="text-slate-400 text-[11px]">Base de Datos:</span>
            <span id="kpi-db-header" class="font-extrabold text-emerald-400">SAN RAID-10 ONLINE ❄️</span>
          </div>
        </div>
      </div>
    </div>

    <!-- 3. CUATRO TARJETAS KPI PRINCIPALES (FORMATO DEL PROFESOR) -->
    <div class="grid grid-cols-2 md:grid-cols-4 gap-3 md:gap-4">
      <div class="bg-slate-900 border border-slate-800 rounded-xl p-3.5 shadow-md">
        <span class="text-xs text-slate-400 font-medium block">Acceso físico</span>
        <span id="kpi-acceso" class="text-xl md:text-2xl font-black text-white block mt-1">NORMAL</span>
        <span id="kpi-acceso-sub" class="text-[11px] text-emerald-400 font-bold block mt-0.5">Esclusas Cerradas</span>
      </div>

      <div class="bg-slate-900 border border-slate-800 rounded-xl p-3.5 shadow-md">
        <span class="text-xs text-slate-400 font-medium block">CCTV</span>
        <span id="kpi-cctv" class="text-xl md:text-2xl font-black text-white block mt-1">8 / 8</span>
        <span id="kpi-cctv-sub" class="text-[11px] text-emerald-400 font-bold block mt-0.5">Cámaras IP Online 24/7</span>
      </div>

      <div class="bg-slate-900 border border-slate-800 rounded-xl p-3.5 shadow-md">
        <span class="text-xs text-slate-400 font-medium block">Sensores de Clima</span>
        <span id="kpi-sensores" class="text-xl md:text-2xl font-black text-white block mt-1">12 / 12</span>
        <span id="kpi-sensores-sub" class="text-[11px] text-emerald-400 font-bold block mt-0.5">Pasillo Frío: 19.8 °C</span>
      </div>

      <div class="bg-slate-900 border border-slate-800 rounded-xl p-3.5 shadow-md">
        <span class="text-xs text-slate-400 font-medium block">Ciberseguridad</span>
        <span id="kpi-ciber" class="text-xl md:text-2xl font-black text-white block mt-1">PROTEGIDA</span>
        <span id="kpi-ciber-sub" class="text-[11px] text-emerald-400 font-bold block mt-0.5">Firewall NGFW Activo</span>
      </div>
    </div>

    <!-- 4. DATA CENTER 4D VIVO: VENTILADORES, CÁMARAS EN PAREDES, NIEBLA Y NAVEGACIÓN TOTAL -->
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 shadow-2xl relative">
      <div class="flex flex-col lg:flex-row justify-between items-start lg:items-center gap-2 mb-3">
        <div>
          <h3 class="font-extrabold text-white text-base flex items-center gap-2">
            <span class="text-cyan-400">⚡</span> ENTORNO 4D EN VIVO: CÁMARAS PROFESIONALES, TURBINAS CRAC & NAVEGACIÓN FLUIDA
          </h3>
          <p class="text-xs text-slate-400">
            <strong>Gira 360° libremente con el ratón</strong> sin interrupciones. La telemetría solo se abre al hacer clic intencional sobre un servidor.
          </p>
        </div>

        <!-- Presets de Cámara y Vistas Rápidas de Seguridad -->
        <div class="flex items-center gap-1.5 flex-wrap">
          <span class="text-[10px] text-slate-400 font-bold uppercase mr-1">Cámaras de Vigilancia:</span>
          <button onclick="switchSecurityCam(1)" id="btn-cam-1" class="px-2.5 py-1 bg-slate-800 hover:bg-cyan-700 text-slate-300 hover:text-white text-xs font-bold rounded-lg border border-slate-700 transition" title="Cámara 1: Esclusa Mantrap">
            📹 CAM 01 [Esclusa]
          </button>
          <button onclick="switchSecurityCam(2)" id="btn-cam-2" class="px-2.5 py-1 bg-cyan-700 text-white text-xs font-bold rounded-lg border border-cyan-400 transition shadow" title="Cámara 2: Pasillo Central Frío">
            📹 CAM 02 [Pasillo]
          </button>
          <button onclick="switchSecurityCam(3)" id="btn-cam-3" class="px-2.5 py-1 bg-slate-800 hover:bg-cyan-700 text-slate-300 hover:text-white text-xs font-bold rounded-lg border border-slate-700 transition" title="Cámara 3: Clúster Base de Datos">
            🗄️ CAM 03 [DB SAN]
          </button>
          <button onclick="switchSecurityCam(4)" id="btn-cam-4" class="px-2.5 py-1 bg-slate-800 hover:bg-cyan-700 text-slate-300 hover:text-white text-xs font-bold rounded-lg border border-slate-700 transition" title="Cámara 4: Sala Eléctrica y UPS">
            ⚡ CAM 04 [UPS]
          </button>
          <button onclick="switchSecurityCam(5)" id="btn-cam-5" class="px-2.5 py-1 bg-slate-800 hover:bg-cyan-700 text-slate-300 hover:text-white text-xs font-bold rounded-lg border border-slate-700 transition" title="Cámara 5: Domo Cenital Aéreo">
            🛰️ CAM 05 [Aérea]
          </button>

          <span class="text-slate-600 mx-1">|</span>

          <button onclick="toggleColdMist()" id="btn-toggle-mist" class="px-2.5 py-1 bg-cyan-950 text-cyan-300 border border-cyan-700 text-xs font-bold rounded-lg transition">
            ❄️ Niebla ON
          </button>
          <button onclick="toggleNeuralNet3D()" id="btn-toggle-net3d" class="px-2.5 py-1 bg-indigo-950 text-indigo-300 border border-indigo-700 text-xs font-bold rounded-lg transition">
            🧠 Red 3D
          </button>
          <button onclick="startCinematicTour()" id="btn-mode-tour" class="px-2.5 py-1 bg-purple-900/60 hover:bg-purple-800 text-purple-200 text-xs font-bold rounded-lg border border-purple-500 transition">
            🎬 Tour
          </button>
        </div>
      </div>

      <!-- Contenedor del Canvas 3D -->
      <div id="canvas-container">
        
        <!-- HUD Telemetría Superior Izquierda -->
        <div class="absolute top-3 left-3 hud-glass p-3 rounded-xl text-white text-xs z-10 shadow-2xl space-y-1.5 border border-cyan-500/30">
          <div class="flex items-center gap-2">
            <span id="hud-status-dot" class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
            <span id="hud-status-text" class="font-black uppercase tracking-wider text-emerald-300">Sala Climatizada</span>
          </div>
          <div class="text-[11px] text-slate-300 flex items-center gap-3">
            <span>Temp: <strong id="hud-temp" class="text-cyan-300">19.8 °C</strong></span>
            <span>Humedad: <strong id="hud-hum" class="text-cyan-300">46%</strong></span>
            <span>UPS: <strong id="hud-ups" class="text-cyan-300">100%</strong></span>
          </div>
          <div class="text-[10px] text-slate-300 border-t border-slate-700/60 pt-1 flex items-center justify-between gap-2">
            <span>Base de Datos SAN:</span>
            <strong id="hud-db-status" class="text-emerald-400 font-mono">ÓPTIMO REPLICADO ❄️</strong>
          </div>
          <div class="text-[9px] text-slate-400">
            Control: <strong class="text-cyan-400">Arrastre libre de ratón 360° • WASD</strong>
          </div>
        </div>

        <!-- PIP MONITOR CCTV EN TIEMPO REAL (Superior Derecha) -->
        <div class="absolute top-3 right-3 hud-glass p-2.5 rounded-xl z-10 shadow-2xl w-52 sm:w-64 border border-slate-700 text-xs">
          <div class="flex justify-between items-center mb-1">
            <span class="text-[10px] font-bold text-slate-400 flex items-center gap-1">
              <span class="w-2 h-2 rounded-full bg-red-500 animate-ping"></span>
              REC • <span id="cctv-cam-title">CAM-02 [PASILLO FRÍO]</span>
            </span>
            <span class="text-[9px] text-slate-400 font-mono" id="cctv-timer">12:00:00</span>
          </div>

          <!-- Feed Simulado -->
          <div class="relative w-full h-28 bg-black rounded-lg overflow-hidden border border-slate-800 flex items-center justify-center">
            <div id="cctv-feed-noise" class="absolute inset-0 bg-slate-900 scanlines-overlay hidden">
              <div class="absolute inset-0 flex flex-col items-center justify-center text-center p-2">
                <span class="text-amber-400 text-2xl animate-pulse">⚠️</span>
                <span class="text-[11px] font-mono text-amber-300 font-bold mt-1">SEÑAL DE VIDEO PERDIDA</span>
                <span class="text-[9px] font-mono text-slate-500">FALLO EN CANAL POE • CÁMARA 05</span>
              </div>
            </div>
            <div id="cctv-feed-normal" class="relative z-0 text-center space-y-1">
              <span id="cctv-icon" class="text-3xl block">❄️</span>
              <span id="cctv-status" class="text-[11px] font-mono text-cyan-300 font-bold block">PASILLO FRÍO REGULADO</span>
              <div class="flex justify-center gap-2 text-[9px] text-slate-400 font-mono">
                <span>FPS: 30.0</span>
                <span>•</span>
                <span>H.265 AES-256</span>
                <span>•</span>
                <span class="text-emerald-400">1080p</span>
              </div>
            </div>
          </div>

          <!-- Mini selector rápido de cámaras CCTV -->
          <div class="grid grid-cols-5 gap-1 mt-1.5">
            <button onclick="switchSecurityCam(1)" class="py-0.5 bg-slate-800 hover:bg-cyan-600 text-white rounded text-[9px] font-bold transition text-center">C1</button>
            <button onclick="switchSecurityCam(2)" class="py-0.5 bg-cyan-700 text-white rounded text-[9px] font-bold transition text-center">C2</button>
            <button onclick="switchSecurityCam(3)" class="py-0.5 bg-slate-800 hover:bg-cyan-600 text-white rounded text-[9px] font-bold transition text-center">C3</button>
            <button onclick="switchSecurityCam(4)" class="py-0.5 bg-slate-800 hover:bg-cyan-600 text-white rounded text-[9px] font-bold transition text-center">C4</button>
            <button onclick="switchSecurityCam(5)" class="py-0.5 bg-slate-800 hover:bg-cyan-600 text-white rounded text-[9px] font-bold transition text-center">C5</button>
          </div>
        </div>

        <!-- CONTROLES DIRECCIONALES D-PAD EN PANTALLA (Inferior Izquierda) -->
        <div class="absolute bottom-3 left-3 hud-glass p-2.5 rounded-xl z-20 flex flex-col items-center gap-1 shadow-2xl">
          <span class="text-[9px] text-slate-400 font-bold uppercase tracking-wider">Caminar Adentro</span>
          <button onclick="movePlayer('forward')" class="w-8 h-8 rounded-lg bg-slate-800 hover:bg-cyan-600 text-white font-bold flex items-center justify-center text-sm shadow transition" title="Avanzar (W o Flecha Arriba)">⬆️</button>
          <div class="flex gap-1">
            <button onclick="movePlayer('left')" class="w-8 h-8 rounded-lg bg-slate-800 hover:bg-cyan-600 text-white font-bold flex items-center justify-center text-sm shadow transition" title="Izquierda (A)">⬅️</button>
            <button onclick="movePlayer('backward')" class="w-8 h-8 rounded-lg bg-slate-800 hover:bg-cyan-600 text-white font-bold flex items-center justify-center text-sm shadow transition" title="Retroceder (S)">⬇️</button>
            <button onclick="movePlayer('right')" class="w-8 h-8 rounded-lg bg-slate-800 hover:bg-cyan-600 text-white font-bold flex items-center justify-center text-sm shadow transition" title="Derecha (D)">➡️</button>
          </div>
        </div>

        <!-- Banner de Emergencia 3D Flotante Dinámico -->
        <div id="hud-emergency-banner" class="absolute bottom-3 inset-x-1/4 bg-red-600/90 backdrop-blur-md py-2 px-4 rounded-xl text-white text-xs font-black text-center tracking-widest uppercase border border-red-400 z-10 hidden alarm-glow">
          ⚠️ ALERTA ACTIVADA: PROTOCOLO DE CONTENCIÓN EN CURSO
        </div>

        <!-- TARJETA HUD DE INSPECCIÓN LATERAL NO INVASIVA (Reemplaza al molesto modal emergente) -->
        <div id="hud-rack-panel" class="absolute bottom-3 right-3 hud-glass p-3 rounded-xl z-20 max-w-xs w-72 border border-cyan-500/40 text-xs shadow-2xl transition-all duration-300 hidden">
          <div class="flex justify-between items-start border-b border-slate-800 pb-1.5 mb-2">
            <div class="flex items-center gap-2">
              <span id="rack-panel-icon" class="text-xl">🗄️</span>
              <div>
                <h4 id="rack-panel-title" class="font-extrabold text-white text-[11px] leading-tight">RACK 01 - DB SAN</h4>
                <span id="rack-panel-status" class="text-[9px] text-cyan-400 font-mono">19.8 °C • ÓPTIMO ❄️</span>
              </div>
            </div>
            <button onclick="closeRackPanel()" class="text-slate-400 hover:text-white font-bold text-base leading-none p-1">&times;</button>
          </div>

          <div class="space-y-1 text-[10px]">
            <div class="flex justify-between py-0.5 border-b border-slate-800/60">
              <span class="text-slate-400">CPU / RAM:</span>
              <span id="rack-panel-perf" class="font-mono text-emerald-400 font-bold">14.2% • 42% RAM</span>
            </div>
            <div class="flex justify-between py-0.5 border-b border-slate-800/60">
              <span class="text-slate-400">Almacenamiento:</span>
              <span id="rack-panel-disk" class="font-mono text-cyan-300 font-bold">4,850 IOPS NVMe</span>
            </div>
            <div class="flex justify-between py-0.5">
              <span class="text-slate-400">Seguridad:</span>
              <span class="font-mono text-emerald-400 font-bold">AES-256 + WORM</span>
            </div>
          </div>
        </div>

        <!-- Indicador de Clic en Racks / Ayuda -->
        <div id="hint-click" class="absolute bottom-3 right-3 bg-slate-950/85 backdrop-blur-md px-3 py-1.5 rounded-lg text-cyan-300 text-[10px] z-10 border border-cyan-800/50 shadow-lg">
          💡 <strong>Tip:</strong> Clic intencional en cualquier servidor abre su telemetría lateral sin tapar la pantalla
        </div>
      </div>
    </div>

    <!-- 5. TERMINAL DEL AGENTE IA GUARDIÁN (CON MENTE PROPIA) -->
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 md:p-5 shadow-2xl space-y-3">
      <div class="flex justify-between items-center flex-wrap gap-2">
        <div class="flex items-center gap-2.5">
          <div class="w-9 h-9 rounded-xl bg-cyan-500/20 text-cyan-400 flex items-center justify-center font-bold text-xl border border-cyan-400/30">🧠</div>
          <div>
            <h3 class="font-extrabold text-white text-sm flex items-center gap-2">
              AGENTE IA GUARDIÁN AUTÓNOMO (MENTE PROPIA)
              <span class="text-[10px] px-2 py-0.5 bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 rounded-full font-bold">EN LÍNEA 24/7</span>
            </h3>
            <p class="text-xs text-slate-400">Análisis continuo de correlación espacio-temporal, telemetría térmica y toma de decisiones autónoma</p>
          </div>
        </div>
        <div class="flex items-center gap-2">
          <span class="text-xs font-mono bg-cyan-950 border border-cyan-800 text-cyan-300 px-3 py-1 rounded-full">
            Latencia Neural: <span id="ai-latency">0.8 ms</span>
          </span>
          <button onclick="aiSelfInspect()" class="px-3 py-1 bg-cyan-600 hover:bg-cyan-500 text-white text-xs font-bold rounded-lg transition shadow">
            ⚡ Autodiagnóstico IA
          </button>
        </div>
      </div>

      <!-- Consola de Diálogo Autónomo de la IA -->
      <div class="bg-black border border-slate-800 rounded-xl p-3.5 font-mono text-xs text-cyan-300 space-y-2 shadow-inner">
        <div class="flex items-center justify-between text-slate-400 text-[10px] border-b border-slate-800 pb-1.5">
          <div class="flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
            <span class="font-bold text-slate-300">FLUJO DE PENSAMIENTO AUTÓNOMO EN TIEMPO REAL:</span>
          </div>
          <span class="text-[9px] text-slate-500">Ciclo cognitivo continuo (3.5s)</span>
        </div>
        <div id="ai-thought-log" class="text-slate-200 leading-relaxed font-mono min-h-[38px] flex items-center">
          <span class="text-cyan-400 font-bold mr-2">[CÁRCAMO AI]:</span> Inicializando red neuronal Transformer. 10 racks en monitoreo. Base de datos refrigerada a 19.8°C. Cero intrusiones.
        </div>
      </div>

      <!-- Preguntas Técnicas Interactivas al Agente IA -->
      <div class="pt-1 border-t border-slate-800/80">
        <span class="text-[11px] font-bold text-slate-400 uppercase tracking-wider block mb-1.5">Consultar al Agente IA sobre Normas y Protección:</span>
        <div class="flex flex-wrap gap-2">
          <button onclick="askAITechnical('db_power')" class="px-2.5 py-1 bg-slate-950 hover:bg-slate-800 text-slate-300 hover:text-cyan-300 border border-slate-800 rounded-lg text-xs transition">
            ❓ ¿Cómo se protege la Base de Datos en un corte eléctrico?
          </button>
          <button onclick="askAITechnical('fire_gas')" class="px-2.5 py-1 bg-slate-950 hover:bg-slate-800 text-slate-300 hover:text-cyan-300 border border-slate-800 rounded-lg text-xs transition">
            ❓ ¿Por qué se usa gas Novec 1230 y no agua?
          </button>
          <button onclick="askAITechnical('ransom_worm')" class="px-2.5 py-1 bg-slate-950 hover:bg-slate-800 text-slate-300 hover:text-cyan-300 border border-slate-800 rounded-lg text-xs transition">
            ❓ ¿Cómo neutraliza la IA un ataque de Ransomware?
          </button>
          <button onclick="askAITechnical('mantrap_biometry')" class="px-2.5 py-1 bg-slate-950 hover:bg-slate-800 text-slate-300 hover:text-cyan-300 border border-slate-800 rounded-lg text-xs transition">
            ❓ ¿Qué hace la esclusa Mantrap si detectan a un intruso?
          </button>
        </div>
      </div>
    </div>

    <!-- 6. DIAGRAMA DE RED NEURONAL INTERCONECTADO -->
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 md:p-5 shadow-2xl">
      <div class="flex justify-between items-center mb-2 flex-wrap gap-2">
        <h3 class="font-extrabold text-white text-sm flex items-center gap-2">
          <span>🧠</span> ARQUITECTURA DE LA RED NEURONAL DE DETECCIÓN Y DECISIÓN
        </h3>
        <span class="text-xs text-slate-400 font-mono">Topología: Perceptrón Multicapa + Attention Layer</span>
      </div>

      <div class="bg-slate-950 border border-slate-800 rounded-xl p-4 overflow-x-auto">
        <svg class="w-full h-36 min-w-[620px]" viewBox="0 0 800 150">
          <g stroke="#1E293B" stroke-width="1.8">
            <line x1="100" y1="30" x2="300" y2="40" class="synapse-active" stroke="#0284C7" />
            <line x1="100" y1="75" x2="300" y2="75" class="synapse-active" stroke="#0284C7" />
            <line x1="100" y1="120" x2="300" y2="110" class="synapse-active" stroke="#0284C7" />
            <line x1="100" y1="30" x2="300" y2="110" stroke="#1E3A8A" />
            <line x1="100" y1="120" x2="300" y2="40" stroke="#1E3A8A" />

            <line x1="300" y1="40" x2="500" y2="40" class="synapse-active" stroke="#0D9488" />
            <line x1="300" y1="75" x2="500" y2="75" class="synapse-active" stroke="#0D9488" />
            <line x1="300" y1="110" x2="500" y2="110" class="synapse-active" stroke="#0D9488" />

            <line x1="500" y1="40" x2="700" y2="45" class="synapse-active" stroke="#38BDF8" id="syn-out-1" />
            <line x1="500" y1="75" x2="700" y2="75" class="synapse-active" stroke="#38BDF8" id="syn-out-2" />
            <line x1="500" y1="110" x2="700" y2="105" class="synapse-active" stroke="#38BDF8" id="syn-out-3" />
          </g>

          <!-- Nodos Entrada -->
          <circle cx="100" cy="30" r="13" fill="#0A2540" stroke="#38BDF8" stroke-width="2.5" />
          <text x="100" y="34" fill="#FFFFFF" font-size="8.5" text-anchor="middle" font-weight="bold">Biometría</text>

          <circle cx="100" cy="75" r="13" fill="#0A2540" stroke="#38BDF8" stroke-width="2.5" />
          <text x="100" y="79" fill="#FFFFFF" font-size="8.5" text-anchor="middle" font-weight="bold">VESDA</text>

          <circle cx="100" cy="120" r="13" fill="#0A2540" stroke="#38BDF8" stroke-width="2.5" />
          <text x="100" y="124" fill="#FFFFFF" font-size="8.5" text-anchor="middle" font-weight="bold">Red RDP</text>

          <!-- Nodos Ocultos -->
          <circle cx="300" cy="40" r="11" fill="#0F172A" stroke="#0D9488" stroke-width="2" />
          <circle cx="300" cy="75" r="11" fill="#0F172A" stroke="#0D9488" stroke-width="2" />
          <circle cx="300" cy="110" r="11" fill="#0F172A" stroke="#0D9488" stroke-width="2" />

          <circle cx="500" cy="40" r="11" fill="#0F172A" stroke="#2563EB" stroke-width="2" />
          <circle cx="500" cy="75" r="11" fill="#0F172A" stroke="#2563EB" stroke-width="2" />
          <circle cx="500" cy="110" r="11" fill="#0F172A" stroke="#2563EB" stroke-width="2" />

          <!-- Nodos Salida -->
          <circle cx="700" cy="45" r="15" fill="#0A2540" stroke="#10B981" stroke-width="3.5" id="node-out-normal" />
          <text x="700" y="49" fill="#10B981" font-size="9" text-anchor="middle" font-weight="bold">SEGURO</text>

          <circle cx="700" cy="75" r="15" fill="#0A2540" stroke="#64748B" stroke-width="2" id="node-out-alerta" />
          <text x="700" y="79" fill="#94A3B8" font-size="8.5" text-anchor="middle" font-weight="bold">ALERTA</text>

          <circle cx="700" cy="105" r="15" fill="#0A2540" stroke="#64748B" stroke-width="2" id="node-out-bloqueo" />
          <text x="700" y="109" fill="#94A3B8" font-size="8.5" text-anchor="middle" font-weight="bold">BLOQUEO</text>

          <text x="100" y="145" fill="#64748B" font-size="9" text-anchor="middle" font-weight="bold">Entrada (Sensores)</text>
          <text x="400" y="145" fill="#64748B" font-size="9" text-anchor="middle" font-weight="bold">Capas Ocultas (Extracción)</text>
          <text x="700" y="145" fill="#64748B" font-size="9" text-anchor="middle" font-weight="bold">Inferencia de Decisión</text>
        </svg>
      </div>
    </div>

    <!-- 7. DIAGRAMA DE ARQUITECTURA DE SEGURIDAD (5 BLOQUES DEL PROFESOR) -->
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 md:p-5 shadow-2xl">
      <h3 class="font-extrabold text-white text-sm mb-3">Diagrama de Arquitectura de Seguridad Integral</h3>

      <div class="bg-slate-950 border border-slate-800 rounded-xl p-4 relative overflow-hidden">
        <!-- Fila 1: 3 Bloques superiores -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4 relative z-10">
          <div id="box-acceso" class="tech-card bg-slate-900 border border-slate-800 rounded-xl p-4 text-center shadow-md">
            <h5 class="font-black text-xs text-white uppercase tracking-wide">CONTROL DE ACCESO</h5>
            <p class="text-[11px] text-slate-400 mt-1">Biometría • Tarjetas RFID</p>
            <p class="text-[11px] text-slate-400">Esclusas (Mantrap)</p>
          </div>

          <div id="box-cctv" class="tech-card bg-slate-900 border border-slate-800 rounded-xl p-4 text-center shadow-md">
            <h5 class="font-black text-xs text-white uppercase tracking-wide">CCTV</h5>
            <p class="text-[11px] text-slate-400 mt-1">Cámaras IP • PTZ Móviles</p>
            <p class="text-[11px] text-slate-400">Grabación NVR 90 días</p>
          </div>

          <div id="box-sensores" class="tech-card bg-slate-900 border border-slate-800 rounded-xl p-4 text-center shadow-md">
            <h5 class="font-black text-xs text-white uppercase tracking-wide">SENSORES</h5>
            <p class="text-[11px] text-slate-400 mt-1">Humo VESDA / temperatura</p>
            <p class="text-[11px] text-slate-400">Inundación / presión</p>
          </div>
        </div>

        <!-- Fila 2: 2 Bloques inferiores -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4 relative z-10 max-w-2xl mx-auto">
          <div id="box-logica" class="tech-card bg-slate-900 border border-slate-800 rounded-xl p-4 text-center shadow-md">
            <h5 class="font-black text-xs text-white uppercase tracking-wide">SEGURIDAD LÓGICA</h5>
            <p class="text-[11px] text-slate-400 mt-1">Firewall NGFW • IDS/IPS</p>
            <p class="text-[11px] text-slate-400">SIEM • MFA • Cifrado Base de Datos</p>
          </div>

          <div id="box-respaldo" class="tech-card bg-slate-900 border border-slate-800 rounded-xl p-4 text-center shadow-md">
            <h5 class="font-black text-xs text-white uppercase tracking-wide">RESPALDO / CONTINUIDAD</h5>
            <p class="text-[11px] text-slate-400 mt-1">UPS Doble Conversión • Generador ATS</p>
            <p class="text-[11px] text-slate-400">Redundancia Tier III 2N • WORM</p>
          </div>
        </div>
      </div>
    </div>

    <!-- 8. BOTONES DE SIMULACIÓN DE INCIDENTES (EXACTO AL PROFESOR + CRÍTICOS) -->
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 md:p-5 shadow-2xl">
      <div class="flex justify-between items-center mb-3">
        <h3 class="font-extrabold text-white text-sm">Simular incidente con Alarma Sonora y Efectos 3D</h3>
        <span class="text-xs text-cyan-400 font-mono">Cada emergencia tiene color, iluminación, movimiento y sonido únicos:</span>
      </div>

      <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-6 gap-2.5">
        <button onclick="triggerIncident('normal')" id="btn-normal" class="py-2.5 px-3 rounded-xl border-2 text-xs font-bold text-white bg-blue-600/40 border-cyan-400 flex items-center justify-center gap-1.5 shadow-md transition">
          <span>✓</span> Operación normal
        </button>

        <button onclick="triggerIncident('acceso')" id="btn-acceso" class="py-2.5 px-3 rounded-xl border text-xs font-bold text-slate-300 bg-slate-800 border-slate-700 hover:bg-slate-750 flex items-center justify-center gap-1.5 transition">
          <span class="text-amber-400">🚨</span> Acceso no autorizado
        </button>

        <button onclick="triggerIncident('humo')" id="btn-humo" class="py-2.5 px-3 rounded-xl border text-xs font-bold text-slate-300 bg-slate-800 border-slate-700 hover:bg-slate-750 flex items-center justify-center gap-1.5 transition">
          <span>🔥</span> Detección de humo
        </button>

        <button onclick="triggerIncident('temperatura')" id="btn-temperatura" class="py-2.5 px-3 rounded-xl border text-xs font-bold text-slate-300 bg-slate-800 border-slate-700 hover:bg-slate-750 flex items-center justify-center gap-1.5 transition">
          <span>🌡️</span> Temperatura elevada
        </button>

        <button onclick="triggerIncident('red')" id="btn-red" class="py-2.5 px-3 rounded-xl border text-xs font-bold text-slate-300 bg-slate-800 border-slate-700 hover:bg-slate-750 flex items-center justify-center gap-1.5 transition">
          <span>🌐</span> Intrusión de red
        </button>

        <button onclick="triggerIncident('camara')" id="btn-camara" class="py-2.5 px-3 rounded-xl border text-xs font-bold text-slate-300 bg-slate-800 border-slate-700 hover:bg-slate-750 flex items-center justify-center gap-1.5 transition">
          <span>📹</span> Cámara desconectada
        </button>
      </div>

      <div class="flex flex-wrap items-center gap-2 mt-3 pt-3 border-t border-slate-800">
        <span class="text-[11px] font-bold text-slate-400 uppercase">Simulaciones Críticas Avanzadas de Alta Disponibilidad:</span>
        <button onclick="triggerIncident('energia')" id="btn-energia" class="px-3 py-1.5 rounded-lg border text-xs font-semibold text-slate-300 bg-slate-950 border-slate-800 hover:border-amber-500 hover:text-amber-400 transition">
          ⚡ Corte Eléctrico General (Apagón Blackout + ATS)
        </button>
        <button onclick="triggerIncident('ransomware')" id="btn-ransomware" class="px-3 py-1.5 rounded-lg border text-xs font-semibold text-slate-300 bg-slate-950 border-slate-800 hover:border-red-500 hover:text-red-400 transition">
          🔒 Ataque de Ransomware / Inmutabilidad WORM
        </button>
      </div>
    </div>

    <!-- 9. RESPUESTA DEL SISTEMA & AUDITORÍA EN TIEMPO REAL -->
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 md:p-5 shadow-2xl space-y-4">
      <div>
        <h3 class="font-extrabold text-white text-sm mb-1">Respuesta del sistema</h3>
        <p id="texto-respuesta" class="text-sm font-semibold text-cyan-300">
          Todos los subsistemas se encuentran operando bajo parámetros normales certificados (ANSI/TIA-942 Tier III).
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-4 gap-3 bg-slate-950 p-4 rounded-xl border border-slate-800 text-xs">
        <div>
          <span class="text-slate-400 font-bold block uppercase tracking-wider">Dimensión Evaluada</span>
          <span id="diag-tipo" class="font-black text-white text-sm block mt-0.5">OPERACIONAL</span>
        </div>
        <div>
          <span class="text-slate-400 font-bold block uppercase tracking-wider">¿Está Protegido?</span>
          <span id="diag-protegido" class="font-black text-emerald-400 text-sm block mt-0.5">SÍ, PROTEGIDO</span>
        </div>
        <div>
          <span class="text-slate-400 font-bold block uppercase tracking-wider">Protocolo Ejecutado</span>
          <span id="diag-protocolo" class="font-bold text-slate-200 text-xs block mt-0.5">Monitoreo continuo activo</span>
        </div>
        <div>
          <span class="text-slate-400 font-bold block uppercase tracking-wider">Normativa Aplicable</span>
          <span id="diag-norma" class="font-bold text-cyan-400 text-xs block mt-0.5">ISO 27001 / ANSI/TIA-942</span>
        </div>
      </div>

      <!-- Consola SIEM -->
      <div>
        <div class="flex justify-between items-center mb-1.5">
          <span class="text-xs font-bold text-slate-400 uppercase tracking-wider">Consola SIEM de Auditoría Forense</span>
          <button onclick="clearLogs()" class="text-[10px] text-slate-500 hover:text-slate-300 underline">Reiniciar consola</button>
        </div>
        <div id="log-console" class="bg-black text-emerald-400 font-mono text-[11px] p-3.5 rounded-xl max-h-32 overflow-y-auto space-y-1 border border-slate-800">
          <div>[<span class="text-slate-500" id="time-init">12:00:00</span>] INFO: Motor de Red Neuronal Deep Learning cargado.</div>
          <div>[<span class="text-slate-500" id="time-init-2">12:00:01</span>] INFO: Render 4D activo. Sensores de niebla criogénica, cámaras robóticas y telemetría VESDA conectados.</div>
        </div>
      </div>
    </div>

  </div>

  <!-- SCRIPT THREE.JS: MOTOR 4D COMPLETO -->
  <script>
    // =========================================================================
    // BASE DE DATOS DE REGLAS DE INCIDENTES (FORMATO DEL PROFESOR JARAMILLO)
    // =========================================================================
    const incidentData = {
      normal: {
        bannerText: "ESTADO: OPERACIÓN NORMAL (SALA CLIMATIZADA)",
        bannerSub: "Monitoreo activo de temperatura criogénica, sensores VESDA y tráfico de red.",
        dotColor: "bg-emerald-500",
        alarmTheme: "#10B981",
        aiTag: "Patrón Estable (0.01% Anomalía)",
        aiProb: "0.01% (Bajo)",
        aiConf: "99.98%",
        aiAction: "Mantener telemetría",
        aiThought: "[CÁRCAMO AI]: Telemetría en orden. Servidor de Bases de Datos completamente refrigerado a 19.8°C. Cero paquetes maliciosos detectados.",
        outNode: "normal",
        kpiAcceso: "NORMAL",
        kpiAccesoSub: "Esclusas Cerradas",
        kpiAccesoColor: "text-emerald-400",
        kpiCctv: "8 / 8",
        kpiCctvSub: "Cámaras IP Online 24/7",
        kpiCctvColor: "text-emerald-400",
        kpiSensores: "12 / 12",
        kpiSensoresSub: "Pasillo Frío: 19.8 °C",
        kpiSensoresColor: "text-emerald-400",
        kpiCiber: "PROTEGIDA",
        kpiCiberSub: "Firewall NGFW Activo",
        kpiCiberColor: "text-emerald-400",
        highlightBox: null,
        respuestaTexto: "Todos los subsistemas se encuentran operando bajo parámetros normales certificados (ANSI/TIA-942 Tier III).",
        tipo: "OPERACIONAL",
        protegido: "SÍ, PROTEGIDO",
        protegidoColor: "text-emerald-400",
        protocolo: "Monitoreo continuo activo",
        norma: "ISO 27001 / ANSI/TIA-942",
        logMsg: "INFO: Sala en parámetros óptimos: 19.8°C, Humedad 46%, Cero paquetes anómalos.",
        logType: "text-emerald-400",
        temp: "19.8 °C",
        hum: "46%",
        ups: "100%",
        dbStatus: "ÓPTIMO REPLICADO ❄️",
        sceneState: "normal",
        camPos: { x: 0, y: 1.65, z: 3.2 },
        camLook: { x: 0, y: 1.5, z: 0 },
        cctvIcon: "❄️",
        cctvText: "PASILLO FRÍO REGULADO",
        cctvNoise: false
      },
      acceso: {
        bannerText: "ALERTA — ACCESO NO AUTORIZADO DETECTADO (PUERTA FORZADA)",
        bannerSub: "Intruso intentando vulnerar la esclusa perimetral Mantrap sin biometría.",
        dotColor: "bg-red-500",
        alarmTheme: "#EF4444",
        aiTag: "ANOMALÍA BIOMÉTRICA (98.4%)",
        aiProb: "98.4% (Crítico)",
        aiConf: "99.85%",
        aiAction: "Bloquear esclusa Mantrap",
        aiThought: "[CÁRCAMO AI]: Puerta perimetral forzada por intruso no identificado. Activando electroimanes de 1200 lbs en 0.2ms. Puerta sellada mecánicamente y sirena armada.",
        outNode: "bloqueo",
        kpiAcceso: "BLOQUEADO",
        kpiAccesoSub: "Esclusa Interbloqueada Activa",
        kpiAccesoColor: "text-red-400",
        kpiCctv: "8 / 8",
        kpiCctvSub: "Cámara 01 enfocando intruso",
        kpiCctvColor: "text-cyan-400",
        kpiSensores: "11 / 12",
        kpiSensoresSub: "Sensor puerta activado",
        kpiSensoresColor: "text-amber-400",
        kpiCiber: "PROTEGIDA",
        kpiCiberSub: "Cierre de sesión automático",
        kpiCiberColor: "text-emerald-400",
        highlightBox: "box-acceso",
        respuestaTexto: "Se detectó un intento de vulneración en la puerta de la esclusa. El mecanismo interbloqueado se cerró violentamente con electroimanes y la Cámara 01 enfocó al sujeto en alta definición.",
        tipo: "SEGURIDAD FÍSICA",
        protegido: "SÍ, BLOQUEADO",
        protegidoColor: "text-emerald-400",
        protocolo: "Bloqueo Mantrap + Cierre Forzado + Alerta Silenciosa",
        norma: "ISO/IEC 27001 - Cláusula A.7.1 y A.7.2",
        logMsg: "ALERTA FÍSICA CRÍTICA: Intento de forzado de puerta perimetral. Electroimanes de 1200 lbs activados. Intruso retenido en esclusa.",
        logType: "text-red-400",
        temp: "19.9 °C",
        hum: "46%",
        ups: "100%",
        dbStatus: "ÓPTIMO REPLICADO ❄️",
        sceneState: "alarm_door",
        camPos: { x: 0, y: 1.8, z: -2.8 },
        camLook: { x: 0, y: 1.5, z: -5.2 },
        cctvIcon: "🚨",
        cctvText: "INTRUSO RETENIDO EN PUERTA MANTRAP",
        cctvNoise: false
      },
      humo: {
        bannerText: "ALERTA MÁXIMA — FUEGO Y HUMO DETECTADOS EN RACK 03",
        bannerSub: "Sistema láser VESDA aspiró partículas de combustión. Alarma de gas armada.",
        dotColor: "bg-orange-600",
        alarmTheme: "#EA580C",
        aiTag: "COMBUSTIÓN TEMPRANA (96.2%)",
        aiProb: "96.2% (Crítico)",
        aiConf: "99.40%",
        aiAction: "Armar gas Novec 1230",
        aiThought: "[CÁRCAMO AI]: Llamas y humo denso detectados en el Rack 03. Suspensión de climatización de aire y presurización de agente limpio Novec 1230 sin agua para salvar componentes.",
        outNode: "alerta",
        kpiAcceso: "EVACUACIÓN",
        kpiAccesoSub: "Destrabe de emergencia",
        kpiAccesoColor: "text-amber-400",
        kpiCctv: "8 / 8",
        kpiCctvSub: "Enfocando fuego en Rack 03",
        kpiCctvColor: "text-cyan-400",
        kpiSensores: "10 / 12",
        kpiSensoresSub: "VESDA Activo (Nivel 2)",
        kpiSensoresColor: "text-red-400",
        kpiCiber: "PROTEGIDA",
        kpiCiberSub: "Backup preventivo WORM",
        kpiCiberColor: "text-emerald-400",
        highlightBox: "box-sensores",
        respuestaTexto: "El sensor láser VESDA detectó humo y flamas en el Rack 03. Se activó el conteo regresivo de 30s para descarga de gas limpio Novec 1230 (sin agua, protege los circuitos).",
        tipo: "SEGURIDAD AMBIENTAL / FÍSICA",
        protegido: "SÍ, EN RESPUESTA",
        protegidoColor: "text-emerald-400",
        protocolo: "Extinción por Gas Novec 1230 + Corte de Clima",
        norma: "Norma NFPA 2001 / ANSI/TIA-942",
        logMsg: "EMERGENCIA FUEGO/HUMO: Fuego activo en Rack 03. Conteo regresivo T-30s para inundación de gas limpio Novec 1230.",
        logType: "text-orange-400",
        temp: "34.5 °C",
        hum: "32%",
        ups: "100%",
        dbStatus: "ALERTA TÉRMICA 🔥",
        sceneState: "alarm_fire",
        camPos: { x: 1.1, y: 1.9, z: 1.6 },
        camLook: { x: -1.85, y: 1.5, z: 0 },
        cctvIcon: "🔥",
        cctvText: "FUEGO Y HUMO EN RACK 03",
        cctvNoise: false
      },
      temperatura: {
        bannerText: "ADVERTENCIA — TEMPERATURA ELEVADA (PÉRDIDA DE FRÍO)",
        bannerSub: "Fallo en compresor principal HVAC-01. Gradiente térmico subiendo a 32.5 °C.",
        dotColor: "bg-amber-500",
        alarmTheme: "#F59E0B",
        aiTag: "GRADIENTE TÉRMICO ANORMAL",
        aiProb: "74.8% (Medio)",
        aiConf: "98.90%",
        aiAction: "Activar HVAC N+1",
        aiThought: "[CÁRCAMO AI]: Pérdida del flujo frío en pasillo principal. Temperatura sube a 32.5°C. Turbinas de precisión CRAC acelerando al máximo y compresor N+1 acoplado.",
        outNode: "alerta",
        kpiAcceso: "NORMAL",
        kpiAccesoSub: "Acceso estándar",
        kpiAccesoColor: "text-slate-300",
        kpiCctv: "8 / 8",
        kpiCctvSub: "Operativo",
        kpiCctvColor: "text-emerald-400",
        kpiSensores: "11 / 12",
        kpiSensoresSub: "Sonda térmica: 32.5 °C",
        kpiSensoresColor: "text-amber-400",
        kpiCiber: "PROTEGIDA",
        kpiCiberSub: "Balanceo de carga",
        kpiCiberColor: "text-emerald-400",
        highlightBox: "box-sensores",
        respuestaTexto: "El sensor del pasillo caliente reporta 32.5°C por fallo en compresor 1. Se encendió automáticamente la unidad redundante N+1 (HVAC-03) acelerando las turbinas.",
        tipo: "SEGURIDAD AMBIENTAL / FÍSICA",
        protegido: "SÍ, MITIGADO",
        protegidoColor: "text-emerald-400",
        protocolo: "Conmutación a Aire de Precisión Redundante N+1",
        norma: "Estándar térmico ASHRAE TC 9.9 / TIA-942",
        logMsg: "ALERTA TÉRMICA: Temperatura subió a 32.5°C. Turbinas CRAC al 100% y compresor de respaldo N+1 acoplado.",
        logType: "text-amber-400",
        temp: "32.5 °C",
        hum: "38%",
        ups: "100%",
        dbStatus: "CALIENTE (REMEDIANDO 🌡️)",
        sceneState: "alarm_heat",
        camPos: { x: 0, y: 3.2, z: 4.5 },
        camLook: { x: 0, y: 1.4, z: 0 },
        cctvIcon: "🌡️",
        cctvText: "TEMP ALTA: 32.5°C (HVAC N+1 ON)",
        cctvNoise: false
      },
      red: {
        bannerText: "ALERTA — INTRUSIÓN DE RED DETECTADA (ATAQUE RDP)",
        bannerSub: "Intento de explotación de vulnerabilidad por puerto 3389 contra la VLAN de gestión.",
        dotColor: "bg-purple-600",
        alarmTheme: "#A855F7",
        aiTag: "ATAQUE FUERZA BRUTA (99.7%)",
        aiProb: "99.7% (Crítico)",
        aiConf: "99.96%",
        aiAction: "Bloqueo Drop en Firewall",
        aiThought: "[CÁRCAMO AI]: Ataque de fuerza bruta RDP interceptado. Inyectando regla DROP en Firewall perimetral y activando microsegmentación en clúster de Base de Datos.",
        outNode: "bloqueo",
        kpiAcceso: "NORMAL",
        kpiAccesoSub: "Físico normal",
        kpiAccesoColor: "text-slate-300",
        kpiCctv: "8 / 8",
        kpiCctvSub: "Operativo",
        kpiCctvColor: "text-emerald-400",
        kpiSensores: "12 / 12",
        kpiSensoresSub: "Normal",
        kpiSensoresColor: "text-emerald-400",
        kpiCiber: "AMENAZA AISLADA",
        kpiCiberSub: "IP bloqueada por IPS",
        kpiCiberColor: "text-purple-400",
        highlightBox: "box-logica",
        respuestaTexto: "El sistema IDS/IPS detectó un escaneo de puertos y ataque de fuerza bruta intentando acceder a la VLAN de gestión. El Firewall NGFW bloqueó la IP origen y aisló el segmento.",
        tipo: "SEGURIDAD LÓGICA",
        protegido: "SÍ, BLOQUEADO",
        protegidoColor: "text-emerald-400",
        protocolo: "Bloqueo por IPS + Regla de Drop en Firewall NGFW",
        norma: "ISO/IEC 27001 - Cláusula A.8.20 y A.8.22",
        logMsg: "CIBERATAQUE DETENIDO: 140 intentos RDP/segundo bloqueados. IP 185.220.101.4 agregada a Blacklist.",
        logType: "text-purple-400",
        temp: "19.8 °C",
        hum: "46%",
        ups: "100%",
        dbStatus: "ESCUDO ACTIVO 🛡️",
        sceneState: "alarm_net",
        camPos: { x: -0.9, y: 1.5, z: 0.8 },
        camLook: { x: -1.85, y: 1.4, z: 0 },
        cctvIcon: "🛡️",
        cctvText: "FIREWALL: RDP ATTACK BLOCKED",
        cctvNoise: false
      },
      camara: {
        bannerText: "ADVERTENCIA — CÁMARA CCTV DESCONECTADA (FALLO POE)",
        bannerSub: "Pérdida de señal de video en Cámara IP 05 (Pasillo Posterior).",
        dotColor: "bg-amber-500",
        alarmTheme: "#F59E0B",
        aiTag: "PÉRDIDA DE TELEMETRÍA (CCTV)",
        aiProb: "45.0% (Bajo)",
        aiConf: "99.10%",
        aiAction: "Preset PTZ adyacente",
        aiThought: "[CÁRCAMO AI]: Pérdida de paquetes en Cámara 05. Reorientando cámaras PTZ adyacentes con giro robótico para cubrir el punto ciego sin huecos de seguridad.",
        outNode: "alerta",
        kpiAcceso: "NORMAL",
        kpiAccesoSub: "Normal",
        kpiAccesoColor: "text-slate-300",
        kpiCctv: "7 / 8",
        kpiCctvSub: "Cámara 05 Offline",
        kpiCctvColor: "text-amber-400",
        kpiSensores: "12 / 12",
        kpiSensoresSub: "Normal",
        kpiSensoresColor: "text-emerald-400",
        kpiCiber: "PROTEGIDA",
        kpiCiberSub: "Monitoreo PoE activo",
        kpiCiberColor: "text-emerald-400",
        highlightBox: "box-cctv",
        respuestaTexto: "Se perdió la comunicación con la Cámara IP 05. Las cámaras adyacentes modificaron automáticamente su ángulo motorizado PTZ para cubrir el punto ciego.",
        tipo: "SEGURIDAD FÍSICA",
        protegido: "SÍ, COBERTURA TRASLAPADA",
        protegidoColor: "text-emerald-400",
        protocolo: "Traslape de Cámaras PTZ + Notificación al Técnico",
        norma: "ISO/IEC 27001 - Control A.7.4",
        logMsg: "ALERTA CCTV: Señal perdida en Cámara 05. Cámaras PTZ vecinas reorientadas.",
        logType: "text-amber-400",
        temp: "19.8 °C",
        hum: "46%",
        ups: "100%",
        dbStatus: "ÓPTIMO REPLICADO ❄️",
        sceneState: "alarm_cam",
        camPos: { x: 0, y: 4.2, z: 5.5 },
        camLook: { x: 0, y: 1.8, z: 0 },
        cctvIcon: "⚠️",
        cctvText: "CAM 05 DESCONECTADA",
        cctvNoise: true
      },
      energia: {
        bannerText: "EMERGENCIA — APAGÓN GENERAL DE RED PÚBLICA (BLACKOUT)",
        bannerSub: "Corte eléctrico general. Luces principales apagadas, baterías UPS en 0ms y generador ATS arrancado.",
        dotColor: "bg-yellow-500",
        alarmTheme: "#EAB308",
        aiTag: "BLACKOUT RED PÚBLICA (UPS ON)",
        aiProb: "99.1% (Crítico)",
        aiConf: "99.99%",
        aiAction: "Arranque diésel ATS",
        aiThought: "[CÁRCAMO AI]: Tensión eléctrica 220V caída a cero en Paita. Luces de sala conmutadas a modo emergencia. Baterías de litio UPS sostienen 100% de la carga con CERO corte.",
        outNode: "bloqueo",
        kpiAcceso: "RESTRINGIDO",
        kpiAccesoSub: "Solo personal de guardia",
        kpiAccesoColor: "text-amber-400",
        kpiCctv: "8 / 8",
        kpiCctvSub: "Alimentado por UPS",
        kpiCctvColor: "text-emerald-400",
        kpiSensores: "12 / 12",
        kpiSensoresSub: "Monitoreo de voltaje",
        kpiSensoresColor: "text-emerald-400",
        kpiCiber: "PROTEGIDA",
        kpiCiberSub: "Modo ahorro de energía",
        kpiCiberColor: "text-emerald-400",
        highlightBox: "box-respaldo",
        respuestaTexto: "Corte total de red pública. Las luces de techo se apagaron quedando solo las tiras de emergencia. El banco de UPS modular asumió la carga en 0 ms y el ATS arrancó el grupo diésel en 6.4s.",
        tipo: "SEGURIDAD FÍSICA / CONTINUIDAD",
        protegido: "SÍ, CERO CORTE (0 ms)",
        protegidoColor: "text-emerald-400",
        protocolo: "Conmutación Automática ATS + Autonomía UPS Tier III",
        norma: "ANSI/TIA-942 Tier III (Mantenimiento Concurrente)",
        logMsg: "ENERGÍA CRÍTICA: Apagón en red pública. Luces a modo emergencia. UPS sosteniendo servidores al 100%. Generador diésel sincronizado.",
        logType: "text-yellow-400",
        temp: "20.8 °C",
        hum: "47%",
        ups: "94% (Generador Sincronizado)",
        dbStatus: "ENERGIZADO POR UPS ⚡",
        sceneState: "alarm_power",
        camPos: { x: 1.0, y: 1.8, z: 2.2 },
        camLook: { x: 1.85, y: 1.4, z: 3.2 },
        cctvIcon: "⚡",
        cctvText: "BLACKOUT: UPS & ATS ACTIVO",
        cctvNoise: false
      },
      ransomware: {
        bannerText: "ALERTA MÁXIMA — ATAQUE DE RANSOMWARE (INTENTO DE CIFRADO)",
        bannerSub: "Proceso malicioso intentando cifrar tablas en la Base de Datos. Aislamiento WORM activado.",
        dotColor: "bg-red-700",
        alarmTheme: "#DC2626",
        aiTag: "RANSOMWARE SIGNATURE (99.9%)",
        aiProb: "99.9% (Amenaza Letal)",
        aiConf: "99.99%",
        aiAction: "Aislamiento WORM Inmediato",
        aiThought: "[CÁRCAMO AI]: Firma maliciosa de ransomware detectada en memoria. Desconectando interfaz virtual en 0.2s. Repositorio inmutable WORM sellado contra escritura.",
        outNode: "bloqueo",
        kpiAcceso: "NORMAL",
        kpiAccesoSub: "Físico normal",
        kpiAccesoColor: "text-slate-300",
        kpiCctv: "8 / 8",
        kpiCctvSub: "Normal",
        kpiCctvColor: "text-emerald-400",
        kpiSensores: "12 / 12",
        kpiSensoresSub: "Normal",
        kpiSensoresColor: "text-emerald-400",
        kpiCiber: "CONTENCIÓN INMEDIATA",
        kpiCiberSub: "Almacenamiento WORM Bloqueado",
        kpiCiberColor: "text-red-400",
        highlightBox: "box-logica",
        respuestaTexto: "El agente EDR detectó un patrón de cifrado masivo en el servidor transaccional. La máquina virtual fue aislada en una micro-VLAN en 1.2 segundos y se preservó la copia inmutable WORM.",
        tipo: "SEGURIDAD LÓGICA",
        protegido: "SÍ, CONTENIDO (CERO PÉRDIDA)",
        protegidoColor: "text-emerald-400",
        protocolo: "Aislamiento por Microsegmentación + Restauración WORM 3-2-1",
        norma: "ISO/IEC 27001 - A.8.13 (Copias inmutables) y A.8.16",
        logMsg: "ALERTA MÁXIMA: Ataque de Ransomware bloqueado por EDR con IA. Copia inmutable WORM verificada intacta.",
        logType: "text-red-400",
        temp: "19.8 °C",
        hum: "46%",
        ups: "100%",
        dbStatus: "INMUTABLE WORM SELLADO 🔒",
        sceneState: "alarm_ransom",
        camPos: { x: -0.9, y: 1.5, z: 0.8 },
        camLook: { x: -1.85, y: 1.4, z: 0 },
        cctvIcon: "🔒",
        cctvText: "RANSOMWARE MITIGATED (WORM SAFE)",
        cctvNoise: false
      }
    };

    // =========================================================================
    // MOTOR DE AUDIO SINTETIZADO AVANZADO (SONIDO ÚNICO PARA CADA INCIDENTE)
    // =========================================================================
    let audioCtx = null;
    let audioEnabled = true;
    let speechEnabled = false;

    function initAudio() {
      if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    }

    function playSirenPolice() {
      if (!audioEnabled) return;
      try {
        initAudio();
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = 'sawtooth';
        const now = audioCtx.currentTime;
        osc.frequency.setValueAtTime(600, now);
        osc.frequency.linearRampToValueAtTime(1100, now + 0.25);
        osc.frequency.linearRampToValueAtTime(600, now + 0.50);
        osc.frequency.linearRampToValueAtTime(1100, now + 0.75);
        gain.gain.setValueAtTime(0.18, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.85);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start(now);
        osc.stop(now + 0.85);
      } catch (e) {}
    }

    function playFireAlarmBuzzer() {
      if (!audioEnabled) return;
      try {
        initAudio();
        for (let i = 0; i < 3; i++) {
          const osc = audioCtx.createOscillator();
          const gain = audioCtx.createGain();
          osc.type = 'square';
          const t = audioCtx.currentTime + (i * 0.22);
          osc.frequency.setValueAtTime(920, t);
          gain.gain.setValueAtTime(0.14, t);
          gain.gain.exponentialRampToValueAtTime(0.001, t + 0.16);
          osc.connect(gain);
          gain.connect(audioCtx.destination);
          osc.start(t);
          osc.stop(t + 0.16);
        }
      } catch (e) {}
    }

    function playPowerCutoffSound() {
      if (!audioEnabled) return;
      try {
        initAudio();
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = 'sine';
        const now = audioCtx.currentTime;
        osc.frequency.setValueAtTime(280, now);
        osc.frequency.exponentialRampToValueAtTime(45, now + 0.7);
        gain.gain.setValueAtTime(0.25, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.75);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start(now);
        osc.stop(now + 0.75);
      } catch (e) {}
    }

    function playCyberGlitchSound() {
      if (!audioEnabled) return;
      try {
        initAudio();
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = 'sawtooth';
        const now = audioCtx.currentTime;
        osc.frequency.setValueAtTime(1400, now);
        osc.frequency.setValueAtTime(800, now + 0.08);
        osc.frequency.setValueAtTime(1800, now + 0.16);
        osc.frequency.setValueAtTime(600, now + 0.24);
        gain.gain.setValueAtTime(0.12, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.4);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start(now);
        osc.stop(now + 0.4);
      } catch (e) {}
    }

    function playBeep(freq = 880, duration = 0.12) {
      if (!audioEnabled) return;
      try {
        initAudio();
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
        gain.gain.setValueAtTime(0.08, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + duration);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start();
        osc.stop(audioCtx.currentTime + duration);
      } catch (e) {}
    }

    function toggleAudio() {
      audioEnabled = !audioEnabled;
      document.getElementById('btn-audio').innerText = audioEnabled ? '🔊' : '🔇';
      if (audioEnabled) playBeep(520, 0.1);
    }

    function toggleSpeech() {
      speechEnabled = !speechEnabled;
      document.getElementById('btn-speech').innerText = speechEnabled ? '🗣️' : '🎙️';
      if (speechEnabled) speakText("Voz del agente neuronal activada.");
    }

    function speakText(text) {
      if (!speechEnabled || !('speechSynthesis' in window)) return;
      window.speechSynthesis.cancel();
      const u = new SpeechSynthesisUtterance(text);
      u.lang = 'es-ES';
      u.rate = 1.05;
      window.speechSynthesis.speak(u);
    }

    // =========================================================================
    // CONTROL DEL SIMULADOR & IA AUTÓNOMA
    // =========================================================================
    function triggerIncident(key) {
      const data = incidentData[key];
      if (!data) return;

      if (key === 'normal') playBeep(440, 0.12);
      else if (key === 'acceso') playSirenPolice();
      else if (key === 'humo') playFireAlarmBuzzer();
      else if (key === 'energia') playPowerCutoffSound();
      else if (key === 'red' || key === 'ransomware') playCyberGlitchSound();
      else playBeep(700, 0.2);

      if (speechEnabled && key !== 'normal') {
        speakText("Alerta del sistema: " + data.tipo + ". " + data.protocolo);
      }

      document.documentElement.style.setProperty('--alarm-color', data.alarmTheme);
      document.getElementById('header-glow').style.backgroundColor = data.alarmTheme + '33';

      document.getElementById('titulo-alerta').innerText = data.bannerText;
      document.getElementById('subtitulo-alerta').innerText = data.bannerSub;
      document.getElementById('dot-alerta').className = `w-4 h-4 rounded-full ${data.dotColor} alarm-glow`;

      document.getElementById('ai-status-tag').innerText = data.aiTag;
      document.getElementById('ai-thought-log').innerHTML = `<span class="text-cyan-400 font-bold mr-2">[CÁRCAMO AI]:</span> ${data.aiThought.replace('[CÁRCAMO AI]: ', '')}`;
      document.getElementById('ai-latency').innerText = (Math.random() * 0.6 + 0.7).toFixed(1) + " ms";

      const nodes = ['node-out-normal', 'node-out-alerta', 'node-out-bloqueo'];
      nodes.forEach(n => {
        const el = document.getElementById(n);
        el.setAttribute('stroke', '#64748B');
        el.setAttribute('stroke-width', '2');
      });
      if (data.outNode === 'normal') {
        document.getElementById('node-out-normal').setAttribute('stroke', '#10B981');
        document.getElementById('node-out-normal').setAttribute('stroke-width', '3.5');
      } else if (data.outNode === 'alerta') {
        document.getElementById('node-out-alerta').setAttribute('stroke', '#F59E0B');
        document.getElementById('node-out-alerta').setAttribute('stroke-width', '3.5');
      } else if (data.outNode === 'bloqueo') {
        document.getElementById('node-out-bloqueo').setAttribute('stroke', '#EF4444');
        document.getElementById('node-out-bloqueo').setAttribute('stroke-width', '3.5');
      }

      document.getElementById('kpi-acceso').innerText = data.kpiAcceso;
      document.getElementById('kpi-acceso-sub').innerText = data.kpiAccesoSub;
      document.getElementById('kpi-acceso-sub').className = `text-[11px] font-bold block mt-0.5 ${data.kpiAccesoColor}`;

      document.getElementById('kpi-cctv').innerText = data.kpiCctv;
      document.getElementById('kpi-cctv-sub').innerText = data.kpiCctvSub;
      document.getElementById('kpi-cctv-sub').className = `text-[11px] font-bold block mt-0.5 ${data.kpiCctvColor}`;

      document.getElementById('kpi-sensores').innerText = data.kpiSensores;
      document.getElementById('kpi-sensores-sub').innerText = data.kpiSensoresSub;
      document.getElementById('kpi-sensores-sub').className = `text-[11px] font-bold block mt-0.5 ${data.kpiSensoresColor}`;

      document.getElementById('kpi-ciber').innerText = data.kpiCiber;
      document.getElementById('kpi-ciber-sub').innerText = data.kpiCiberSub;
      document.getElementById('kpi-ciber-sub').className = `text-[11px] font-bold block mt-0.5 ${data.kpiCiberColor}`;

      document.getElementById('kpi-db-header').innerText = data.dbStatus;

      const boxes = ['box-acceso', 'box-cctv', 'box-sensores', 'box-logica', 'box-respaldo'];
      boxes.forEach(b => {
        document.getElementById(b).className = 'tech-card bg-slate-900 border border-slate-800 rounded-xl p-4 text-center shadow-md';
      });
      if (data.highlightBox) {
        document.getElementById(data.highlightBox).className = 'tech-card bg-red-950/70 border-2 border-red-500 rounded-xl p-4 text-center shadow-lg shadow-red-500/20 alarm-glow';
      }

      const btns = ['normal', 'acceso', 'humo', 'temperatura', 'red', 'camara', 'energia', 'ransomware'];
      btns.forEach(b => {
        const btn = document.getElementById('btn-' + b);
        if (btn) {
          if (b === key) btn.className = 'py-2.5 px-3 rounded-xl border-2 text-xs font-bold text-white bg-blue-600/40 border-cyan-400 flex items-center justify-center gap-1.5 shadow-lg shadow-cyan-500/20';
          else btn.className = 'py-2.5 px-3 rounded-xl border text-xs font-bold text-slate-300 bg-slate-800 border-slate-700 hover:bg-slate-750 flex items-center justify-center gap-1.5 transition';
        }
      });

      document.getElementById('texto-respuesta').innerText = data.respuestaTexto;
      document.getElementById('diag-tipo').innerText = data.tipo;
      document.getElementById('diag-protegido').innerText = data.protegido;
      document.getElementById('diag-protegido').className = `font-black text-sm block mt-0.5 ${data.protegidoColor}`;
      document.getElementById('diag-protocolo').innerText = data.protocolo;
      document.getElementById('diag-norma').innerText = data.norma;

      document.getElementById('hud-temp').innerText = data.temp;
      document.getElementById('hud-hum').innerText = data.hum;
      document.getElementById('hud-ups').innerText = data.ups;
      document.getElementById('hud-status-text').innerText = data.tipo;
      document.getElementById('hud-db-status').innerText = data.dbStatus;
      document.getElementById('hud-status-dot').className = `w-2.5 h-2.5 rounded-full ${data.dotColor}`;

      const bannerEmerg = document.getElementById('hud-emergency-banner');
      if (key === 'normal') bannerEmerg.classList.add('hidden');
      else {
        bannerEmerg.classList.remove('hidden');
        bannerEmerg.innerText = "⚠️ " + data.bannerText;
      }

      updateCCTVFeed(data);
      animateCameraTo(data.camPos, data.camLook);
      update3DEffects(data.sceneState);
      aimPhysicalCameras(data.camLook);

      addLog(data.logMsg, data.logType);
    }

    function updateCCTVFeed(data) {
      document.getElementById('cctv-icon').innerText = data.cctvIcon;
      document.getElementById('cctv-status').innerText = data.cctvText;
      const noise = document.getElementById('cctv-feed-noise');
      const normal = document.getElementById('cctv-feed-normal');
      if (data.cctvNoise) {
        noise.classList.remove('hidden');
        normal.classList.add('hidden');
      } else {
        noise.classList.add('hidden');
        normal.classList.remove('hidden');
      }
    }

    function switchSecurityCam(camNum) {
      const camPresets = {
        1: { name: "CAM-01 [ESCLUSA MANTRAP]", pos: { x: 0, y: 1.8, z: -2.8 }, look: { x: 0, y: 1.5, z: -5.2 } },
        2: { name: "CAM-02 [PASILLO FRÍO CENTRAL]", pos: { x: 0, y: 1.65, z: 3.2 }, look: { x: 0, y: 1.5, z: 0 } },
        3: { name: "CAM-03 [CLÚSTER DB SAN CORE]", pos: { x: -0.9, y: 1.5, z: 0.8 }, look: { x: -1.85, y: 1.4, z: 0 } },
        4: { name: "CAM-04 [SALA ELÉCTRICA UPS & ATS]", pos: { x: 1.0, y: 1.8, z: 2.2 }, look: { x: 1.85, y: 1.4, z: 3.2 } },
        5: { name: "CAM-05 [DOMO CENITAL AÉREO 360°]", pos: { x: 0, y: 4.5, z: 5.8 }, look: { x: 0, y: 1.4, z: 0 } }
      };

      const preset = camPresets[camNum] || camPresets[2];
      document.getElementById('cctv-cam-title').innerText = preset.name;
      playBeep(640, 0.08);

      for (let i = 1; i <= 5; i++) {
        const btn = document.getElementById('btn-cam-' + i);
        if (btn) {
          if (i === camNum) btn.className = 'px-2.5 py-1 bg-cyan-700 text-white text-xs font-bold rounded-lg border border-cyan-400 transition shadow';
          else btn.className = 'px-2.5 py-1 bg-slate-800 hover:bg-cyan-700 text-slate-300 hover:text-white text-xs font-bold rounded-lg border border-slate-700 transition';
        }
      }

      animateCameraTo(preset.pos, preset.look);
      aimPhysicalCameras(preset.look);
    }

    function aiSelfInspect() {
      playBeep(980, 0.15);
      const thoughts = [
        "[CÁRCAMO AI]: Escaneando 10 racks... Tasa de transmisión: 100 Gbps. Niebla fría a 19.8°C. Integridad de base de datos verificada al 100%.",
        "[CÁRCAMO AI]: Análisis heurístico de tráfico... Red neuronal recalibrando pesos sinápticos. Cero vectores de ataque activos.",
        "[CÁRCAMO AI]: Inspección de esclusa Mantrap completada: Cerrojo electromagnético de 1200 lbs y lector biométrico en sincronía con bitácora.",
        "[CÁRCAMO AI]: Verificación de banco de baterías UPS y conmutador ATS diésel: Respaldo continuo N+1 certificado."
      ];
      const randomThought = thoughts[Math.floor(Math.random() * thoughts.length)];
      document.getElementById('ai-thought-log').innerHTML = `<span class="text-cyan-400 font-bold mr-2">[CÁRCAMO AI]:</span> ${randomThought.replace('[CÁRCAMO AI]: ', '')}`;
      addLog("IA AUTODIAGNÓSTICO: Autochequeo heurístico completado con 100% de éxito.", "text-cyan-400");
    }

    function askAITechnical(topic) {
      playBeep(820, 0.1);
      let reply = "";
      if (topic === 'db_power') {
        reply = "La Base de Datos está alimentada por UPS online de doble conversión con conmutación en CERO milisegundos (0 ms). Antes de que el UPS baje de 90%, el conmutador ATS enciende el grupo electrógeno diésel de Paita (Tier III).";
      } else if (topic === 'fire_gas') {
        reply = "El agua dañaría irreversiblemente los microprocesadores y discos SAN. El gas Novec 1230 o FM-200 inunda la sala por absorción de calor sin mojar, sin asfixiar a operadores y sin conductividad eléctrica (NFPA 2001).";
      } else if (topic === 'ransom_worm') {
        reply = "La IA del EDR detecta el cifrado masivo anómalo y aísla la tarjeta de red en 0.4s. La Base de Datos se recupera instantáneamente desde el repositorio inmutable WORM (Write Once, Read Many), donde ningún ransomware puede sobreescribir.";
      } else if (topic === 'mantrap_biometry') {
        reply = "La esclusa Mantrap tiene dos puertas interbloqueadas mecánicamente: jamás pueden abrirse al mismo tiempo. Si la biometría falla, los electroimanes bloquean ambas puertas reteniendo al intruso y alertando al centro de seguridad.";
      }
      document.getElementById('ai-thought-log').innerHTML = `<span class="text-amber-400 font-bold mr-2">[RESPUESTA IA]:</span> ${reply}`;
      addLog("CONSULTA TÉCNICA RESUELTA: " + topic, "text-cyan-300");
      if (speechEnabled) speakText(reply);
    }

    setInterval(() => {
      const liveInsights = [
        "Monitoreo térmico: Flujo de aire pasillo frío 19.8°C / pasillo caliente 31.2°C. Eficiencia PUE: 1.28 óptima.",
        "Auditoría SIEM: 12,450 paquetes TCP/IP inspeccionados en los últimos 3 segundos. Cero firmas maliciosas.",
        "Base de Datos Oracle/Postgres FinanSur: 4,850 transacciones por segundo. Espejo síncrono activo sin desfase.",
        "Presión atmosférica en sala técnica: Presurización positiva contra polvo exterior mantenida a 25 Pa.",
        "Sistemas de extinción: Cilindro de gas Novec 1230 presurizado a 360 PSI listo para descarga inmediata.",
        "Generador ATS de respaldo: Precalentador de aceite activo, tanque de combustible diésel con 72h de autonomía."
      ];
      const r = liveInsights[Math.floor(Math.random() * liveInsights.length)];
      const currentStatus = document.getElementById('titulo-alerta').innerText;
      if (currentStatus.includes("OPERACIÓN NORMAL")) {
        document.getElementById('ai-thought-log').innerHTML = `<span class="text-cyan-400 font-bold mr-2">[CÁRCAMO AI]:</span> ${r}`;
      }
    }, 4000);

    function addLog(msg, colorClass) {
      const consoleEl = document.getElementById('log-console');
      const now = new Date();
      const timeStr = now.toTimeString().split(' ')[0];
      const logLine = document.createElement('div');
      logLine.innerHTML = `[<span class="text-slate-500">${timeStr}</span>] <span class="${colorClass}">${msg}</span>`;
      consoleEl.prepend(logLine);
    }

    function clearLogs() {
      document.getElementById('log-console').innerHTML = '<div class="text-slate-500 italic">[Consola de auditoría reiniciada]</div>';
    }

    // =========================================================================
    // ENTORNO 4D ULTRA REALISTA CON THREE.JS
    // =========================================================================
    let scene, camera, renderer, controls;
    let racksMesh = [], doorGlassMesh, laserBeamMesh, strobeLight, neuralCloud;
    let smokeParticles = [], fireParticles = [], coldMistParticles = [], cyberShieldMesh;
    let ceilingLights = [], emergencyLightStrips = [], physicalCctvCameras = [];
    let hvacFans = [], hvacLeds = [], intruderMesh, fireLight;
    let currentAlarm = 'normal';
    let showNeural3D = false;
    let showColdMist = true;
    let isTourRunning = false;
    let tourTime = 0;

    let isTransitioning = false;
    let targetCamPos = new THREE.Vector3(0, 1.65, 3.2);
    let targetCamLook = new THREE.Vector3(0, 1.5, 0);
    const keysPressed = {};

    // Sistema Inteligente Anti-Clic Accidental (Detecta arrastre vs clic)
    let pointerDownPos = { x: 0, y: 0 };
    const raycaster = new THREE.Raycaster();
    const mouse = new THREE.Vector2();

    function init3D() {
      const container = document.getElementById('canvas-container');
      const w = container.clientWidth;
      const h = container.clientHeight;

      scene = new THREE.Scene();
      scene.background = new THREE.Color(0x030712);
      scene.fog = new THREE.FogExp2(0x030712, 0.028);

      camera = new THREE.PerspectiveCamera(45, w / h, 0.1, 100);
      camera.position.set(targetCamPos.x, targetCamPos.y, targetCamPos.z);

      renderer = new THREE.WebGLRenderer({ antialias: true, powerPreference: "high-performance" });
      renderer.setSize(w, h);
      renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
      renderer.shadowMap.enabled = true;
      renderer.shadowMap.type = THREE.PCFSoftShadowMap;
      container.appendChild(renderer.domElement);

      // CONTROLES DE RATÓN 360° TOTALMENTE LIBRES
      controls = new THREE.OrbitControls(camera, renderer.domElement);
      controls.enableDamping = true;
      controls.dampingFactor = 0.06;
      controls.maxPolarAngle = Math.PI / 2 - 0.02;
      controls.minDistance = 0.5;
      controls.maxDistance = 22;
      controls.target.set(targetCamLook.x, targetCamLook.y, targetCamLook.z);

      controls.addEventListener('start', () => {
        isTransitioning = false;
        isTourRunning = false;
      });

      // Iluminación Profesional y Difusa (Sin Manchas Duras)
      const ambient = new THREE.AmbientLight(0x0A2540, 0.65);
      scene.add(ambient);

      // Luz Difusa Cenital Superior
      const ceilingAisleLight = new THREE.PointLight(0xBAE6FD, 1.1, 16, 2.0);
      ceilingAisleLight.position.set(0, 4.2, 0);
      scene.add(ceilingAisleLight);
      ceilingLights.push(ceilingAisleLight);

      // Luz Direccional de Relleno Suave
      const mainLight = new THREE.DirectionalLight(0xE0F2FE, 0.7);
      mainLight.position.set(5, 10, 6);
      mainLight.castShadow = true;
      scene.add(mainLight);
      ceilingLights.push(mainLight);

      // Luz Estroboscópica de Alarma
      strobeLight = new THREE.PointLight(0xFF0000, 0, 22);
      strobeLight.position.set(0, 4.2, 0);
      scene.add(strobeLight);

      // Luz de Fuego Parpadeante
      fireLight = new THREE.PointLight(0xFF5500, 0, 8);
      fireLight.position.set(-1.85, 1.4, 0);
      scene.add(fireLight);

      // Elementos del Mundo 3D
      createRoomEnvironment();
      createProfessionalCableTrays();
      createDetailedRacks();
      createMantrapEntrance();
      createProfessionalWallCameras();
      createRealisticHVACUnits();
      createCryogenicMistParticles();
      createSpecialFX();
      createNeuralNetworkMesh3D();

      // Sistema Anti-Clic Accidental: Registra posición inicial de arrastre
      container.addEventListener('pointerdown', (e) => {
        pointerDownPos.x = e.clientX;
        pointerDownPos.y = e.clientY;
      });

      container.addEventListener('pointerup', (e) => {
        // Si el usuario movió el ratón más de 5 píxeles, fue un giro de cámara, NO un clic
        const dist = Math.hypot(e.clientX - pointerDownPos.x, e.clientY - pointerDownPos.y);
        if (dist > 5) return;
        handleCleanRackClick(e);
      });

      // Teclado para caminar WASD
      window.addEventListener('keydown', (e) => {
        keysPressed[e.key.toLowerCase()] = true;
        isTourRunning = false;
        isTransitioning = false;
      });
      window.addEventListener('keyup', (e) => {
        keysPressed[e.key.toLowerCase()] = false;
      });

      window.addEventListener('resize', onResize);
      animate();
    }

    function createServerTexture(isDatabase = false) {
      const canvas = document.createElement('canvas');
      canvas.width = 512;
      canvas.height = 512;
      const ctx = canvas.getContext('2d');

      ctx.fillStyle = isDatabase ? '#091322' : '#0B1120';
      ctx.fillRect(0, 0, 512, 512);

      // Título en la parte superior del rack
      ctx.fillStyle = isDatabase ? '#0284C7' : '#1E293B';
      ctx.fillRect(10, 8, 492, 28);
      ctx.fillStyle = '#FFFFFF';
      ctx.font = 'bold 16px monospace';
      ctx.fillText(isDatabase ? 'FINANSUR DB SAN CLUSTER' : 'SERVER BLADE ARRAY TIER III', 24, 28);

      for (let y = 44; y < 500; y += 42) {
        ctx.fillStyle = '#162238';
        ctx.fillRect(15, y, 482, 36);
        ctx.strokeStyle = isDatabase ? '#0369A1' : '#334155';
        ctx.lineWidth = 1.5;
        ctx.strokeRect(15, y, 482, 36);

        for (let x = 30; x < 380; x += 32) {
          ctx.fillStyle = '#060B14';
          ctx.fillRect(x, y + 6, 26, 24);
          ctx.fillStyle = isDatabase ? '#38BDF8' : (Math.random() > 0.3 ? '#10B981' : '#06B6D4');
          ctx.fillRect(x + 20, y + 8, 3, 3);
        }

        ctx.fillStyle = '#000000';
        ctx.fillRect(395, y + 6, 90, 24);

        ctx.fillStyle = '#38BDF8';
        ctx.beginPath();
        ctx.arc(415, y + 18, 2.5, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = '#10B981';
        ctx.beginPath();
        ctx.arc(435, y + 18, 2.5, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = '#E2E8F0';
        ctx.font = '9px monospace';
        ctx.fillText(isDatabase ? 'NVMe' : '100G', 452, y + 21);
      }

      return new THREE.CanvasTexture(canvas);
    }

    function createRoomEnvironment() {
      // Suelo Técnico Elevado Perforado
      const floor = new THREE.Mesh(
        new THREE.PlaneGeometry(18, 18),
        new THREE.MeshStandardMaterial({ color: 0x080E1C, roughness: 0.3, metalness: 0.85 })
      );
      floor.rotation.x = -Math.PI / 2;
      floor.receiveShadow = true;
      scene.add(floor);

      const grid = new THREE.GridHelper(18, 36, 0x0284C7, 0x1E293B);
      grid.position.y = 0.01;
      scene.add(grid);

      // Tiras LED de Emergencia en el Suelo
      const cableMat = new THREE.MeshBasicMaterial({ color: 0x06B6D4 });
      const cableL = new THREE.Mesh(new THREE.BoxGeometry(0.04, 0.02, 13), cableMat);
      cableL.position.set(-1.3, 0.02, 0);
      scene.add(cableL);
      emergencyLightStrips.push(cableL);

      const cableR = new THREE.Mesh(new THREE.BoxGeometry(0.04, 0.02, 13), cableMat);
      cableR.position.set(1.3, 0.02, 0);
      scene.add(cableR);
      emergencyLightStrips.push(cableR);

      // Paredes
      const wallMat = new THREE.MeshStandardMaterial({ color: 0x060913, roughness: 0.6 });
      const backWall = new THREE.Mesh(new THREE.PlaneGeometry(18, 5.5), wallMat);
      backWall.position.set(0, 2.75, -6.5);
      scene.add(backWall);

      const leftWall = new THREE.Mesh(new THREE.PlaneGeometry(18, 5.5), wallMat);
      leftWall.position.set(-7, 2.75, 0);
      leftWall.rotation.y = Math.PI / 2;
      scene.add(leftWall);

      const rightWall = new THREE.Mesh(new THREE.PlaneGeometry(18, 5.5), wallMat);
      rightWall.position.set(7, 2.75, 0);
      rightWall.rotation.y = -Math.PI / 2;
      scene.add(rightWall);

      // Techo
      const ceiling = new THREE.Mesh(new THREE.PlaneGeometry(18, 18), new THREE.MeshStandardMaterial({ color: 0x020617 }));
      ceiling.position.y = 4.8;
      ceiling.rotation.x = Math.PI / 2;
      scene.add(ceiling);

      // Paneles LED de Techo (Troffers Emisivos Suaves)
      const ledMat = new THREE.MeshBasicMaterial({ color: 0xBAE6FD });
      for (let z = -4; z <= 4; z += 2.5) {
        const ledStrip = new THREE.Mesh(new THREE.BoxGeometry(1.6, 0.03, 0.3), ledMat);
        ledStrip.position.set(0, 4.78, z);
        scene.add(ledStrip);
        ceilingLights.push(ledStrip);
      }

      // Tubería de Gas Limpio y VESDA (Rojo Incendio)
      const vesdaPipe = new THREE.Mesh(
        new THREE.CylinderGeometry(0.06, 0.06, 14, 16),
        new THREE.MeshStandardMaterial({ color: 0xDC2626, metalness: 0.6 })
      );
      vesdaPipe.rotation.x = Math.PI / 2;
      vesdaPipe.position.set(0, 4.2, 0);
      scene.add(vesdaPipe);

      // Boquillas de Descarga Novec 1230
      for (let i = -4.5; i <= 4.5; i += 2.2) {
        const nozzle = new THREE.Mesh(
          new THREE.ConeGeometry(0.08, 0.15, 8),
          new THREE.MeshStandardMaterial({ color: 0xE2E8F0, metalness: 0.9 })
        );
        nozzle.position.set(0, 4.1, i);
        scene.add(nozzle);
      }
    }

    // 1. ESCALERILLAS PASACABLES PROFESIONALES (Estructura de Malla Metálica Realista)
    function createProfessionalCableTrays() {
      const traySteel = new THREE.MeshStandardMaterial({ color: 0x475569, metalness: 0.85, roughness: 0.25 });
      const hangerSteel = new THREE.MeshStandardMaterial({ color: 0x64748B, metalness: 0.9, roughness: 0.2 });
      const fiberMatCyan = new THREE.MeshBasicMaterial({ color: 0x06B6D4 });
      const fiberMatOrange = new THREE.MeshBasicMaterial({ color: 0xF97316 });
      const fiberMatYellow = new THREE.MeshBasicMaterial({ color: 0xEAB308 });

      [-1.85, 1.85].forEach(xPos => {
        const trayGroup = new THREE.Group();

        // Rieles laterales delgados
        const railL = new THREE.Mesh(new THREE.BoxGeometry(0.03, 0.08, 10.5), traySteel);
        railL.position.set(-0.25, 0, 0);
        trayGroup.add(railL);

        const railR = new THREE.Mesh(new THREE.BoxGeometry(0.03, 0.08, 10.5), traySteel);
        railR.position.set(0.25, 0, 0);
        trayGroup.add(railR);

        // Travesaños / Peldaños de la escalerilla
        for (let z = -5.0; z <= 5.0; z += 0.4) {
          const rung = new THREE.Mesh(new THREE.BoxGeometry(0.5, 0.02, 0.03), traySteel);
          rung.position.set(0, -0.03, z);
          trayGroup.add(rung);
        }

        // Varillas de suspensión al techo
        for (let z = -4.0; z <= 4.0; z += 2.6) {
          const rodL = new THREE.Mesh(new THREE.CylinderGeometry(0.012, 0.012, 1.35, 8), hangerSteel);
          rodL.position.set(-0.25, 0.72, z);
          trayGroup.add(rodL);

          const rodR = new THREE.Mesh(new THREE.CylinderGeometry(0.012, 0.012, 1.35, 8), hangerSteel);
          rodR.position.set(0.25, 0.72, z);
          trayGroup.add(rodR);
        }

        // Haces Delgados y Proporcionados de Fibra Óptica
        const f1 = new THREE.Mesh(new THREE.CylinderGeometry(0.014, 0.014, 10.4, 8), fiberMatCyan);
        f1.rotation.x = Math.PI / 2;
        f1.position.set(-0.12, 0.02, 0);
        trayGroup.add(f1);

        const f2 = new THREE.Mesh(new THREE.CylinderGeometry(0.014, 0.014, 10.4, 8), fiberMatOrange);
        f2.rotation.x = Math.PI / 2;
        f2.position.set(0, 0.02, 0);
        trayGroup.add(f2);

        const f3 = new THREE.Mesh(new THREE.CylinderGeometry(0.014, 0.014, 10.4, 8), fiberMatYellow);
        f3.rotation.x = Math.PI / 2;
        f3.position.set(0.12, 0.02, 0);
        trayGroup.add(f3);

        trayGroup.position.set(xPos, 3.25, 0);
        scene.add(trayGroup);
      });
    }

    // 2. VENTILADORES INDUSTRIALES CRAC ULTRA REALISTAS (Turbinas con Rejilla y Nicho)
    function createRealisticHVACUnits() {
      const cabinetMat = new THREE.MeshStandardMaterial({ color: 0x1E293B, metalness: 0.8, roughness: 0.3 });
      const rimMat = new THREE.MeshStandardMaterial({ color: 0x334155, metalness: 0.9, roughness: 0.2 });
      const bladeMat = new THREE.MeshStandardMaterial({ color: 0x0284C7, metalness: 0.85, roughness: 0.2 });
      const grillMat = new THREE.MeshStandardMaterial({ color: 0x64748B, metalness: 0.9, roughness: 0.2 });

      [-4.5, 4.5].forEach(xPos => {
        const hvacGroup = new THREE.Group();

        // 1. Gabinete de Acero Industrial
        const cabinet = new THREE.Mesh(new THREE.BoxGeometry(2.2, 3.8, 1.2), cabinetMat);
        cabinet.position.set(0, 1.9, 0);
        hvacGroup.add(cabinet);

        // 2. Nicho Cilíndrico Empotrado (Túnel de Viento)
        const tunnel = new THREE.Mesh(new THREE.CylinderGeometry(0.72, 0.72, 0.25, 32), new THREE.MeshStandardMaterial({ color: 0x0A0F1D, roughness: 0.9 }));
        tunnel.rotation.x = Math.PI / 2;
        tunnel.position.set(0, 2.5, 0.6);
        hvacGroup.add(tunnel);

        // Anillo Biselado Exterior
        const rim = new THREE.Mesh(new THREE.TorusGeometry(0.74, 0.04, 12, 32), rimMat);
        rim.position.set(0, 2.5, 0.62);
        hvacGroup.add(rim);

        // Anillo LED de Estado (Azul frío en normal, naranja en alerta térmica)
        const ledRing = new THREE.Mesh(new THREE.TorusGeometry(0.70, 0.015, 8, 32), new THREE.MeshBasicMaterial({ color: 0x06B6D4 }));
        ledRing.position.set(0, 2.5, 0.63);
        hvacGroup.add(ledRing);
        hvacLeds.push(ledRing);

        // 3. Turbina Aerodinámica con 6 Aspas Curvadas
        const turbineGroup = new THREE.Group();

        // Spinner / Cono Central
        const cone = new THREE.Mesh(new THREE.ConeGeometry(0.16, 0.22, 16), rimMat);
        cone.rotation.x = Math.PI / 2;
        cone.position.set(0, 0, 0.1);
        turbineGroup.add(cone);

        // 6 Aspas Anguladas
        for (let b = 0; b < 6; b++) {
          const blade = new THREE.Mesh(new THREE.BoxGeometry(0.12, 0.58, 0.02), bladeMat);
          blade.position.y = 0.32;
          blade.rotation.z = (b * Math.PI) / 3;
          blade.rotation.y = 0.35; // Ángulo de ataque de flujo de aire
          turbineGroup.add(blade);
        }

        turbineGroup.position.set(0, 2.5, 0.61);
        hvacGroup.add(turbineGroup);
        hvacFans.push(turbineGroup);

        // 4. Rejilla Protectora de Acero (Anillos Concéntricos y Radios)
        const grillGroup = new THREE.Group();
        [0.25, 0.48, 0.68].forEach(rad => {
          const ring = new THREE.Mesh(new THREE.TorusGeometry(rad, 0.008, 6, 24), grillMat);
          grillGroup.add(ring);
        });
        for (let r = 0; r < 4; r++) {
          const spoke = new THREE.Mesh(new THREE.BoxGeometry(0.01, 1.4, 0.01), grillMat);
          spoke.rotation.z = (r * Math.PI) / 4;
          grillGroup.add(spoke);
        }
        grillGroup.position.set(0, 2.5, 0.72);
        hvacGroup.add(grillGroup);

        // Display Digital de Temperatura del Clima
        const disp = new THREE.Mesh(new THREE.PlaneGeometry(0.7, 0.22), new THREE.MeshBasicMaterial({ color: 0x0284C7 }));
        disp.position.set(0, 3.4, 0.61);
        hvacGroup.add(disp);

        hvacGroup.position.set(xPos, 0, -5.8);
        scene.add(hvacGroup);
      });
    }

    // 3. CÁMARAS PROFESIONALES CCTV (Montadas en Paredes y Techo con Soportes Articulados)
    function createProfessionalWallCameras() {
      const mountLocations = [
        { x: -6.7, y: 4.1, z: -5.8, rotY: 0.8 },   // Esquina Pared Izquierda / Fondo
        { x: 6.7, y: 4.1, z: -5.8, rotY: -0.8 },   // Esquina Pared Derecha / Fondo
        { x: -6.7, y: 4.1, z: 4.5, rotY: 2.3 },    // Esquina Pared Izquierda / Frente
        { x: 6.7, y: 4.1, z: 4.5, rotY: -2.3 }     // Esquina Pared Derecha / Frente
      ];

      const steelMat = new THREE.MeshStandardMaterial({ color: 0x334155, metalness: 0.9, roughness: 0.2 });
      const housingMat = new THREE.MeshStandardMaterial({ color: 0xCBD5E1, roughness: 0.3, metalness: 0.5 }); // Carcasa blanca Hikvision/Axis
      const darkGlass = new THREE.MeshStandardMaterial({ color: 0x0284C7, metalness: 0.9, roughness: 0.1 });

      mountLocations.forEach((loc) => {
        const camRig = new THREE.Group();

        // 1. Placa Base de Anclaje a Pared
        const basePlate = new THREE.Mesh(new THREE.BoxGeometry(0.1, 0.3, 0.3), steelMat);
        camRig.add(basePlate);

        // 2. Brazo Articulado en L
        const armH = new THREE.Mesh(new THREE.CylinderGeometry(0.03, 0.03, 0.45, 12), steelMat);
        armH.rotation.z = Math.PI / 2;
        armH.position.set(0.22, 0, 0);
        camRig.add(armH);

        // 3. Cabezal Giratorio Motorizado (PTZ)
        const ptzHead = new THREE.Group();

        // Carcasa de Cámara Bullet Profesional
        const body = new THREE.Mesh(new THREE.CylinderGeometry(0.12, 0.13, 0.42, 16), housingMat);
        body.rotation.x = Math.PI / 2;
        ptzHead.add(body);

        // Visera Antirreflejo
        const visor = new THREE.Mesh(new THREE.CylinderGeometry(0.14, 0.14, 0.18, 16, 1, true, 0, Math.PI), housingMat);
        visor.rotation.x = Math.PI / 2;
        visor.position.set(0, 0.04, 0.18);
        ptzHead.add(visor);

        // Lente Óptico Oscuro
        const lens = new THREE.Mesh(new THREE.CylinderGeometry(0.08, 0.08, 0.06, 16), darkGlass);
        lens.rotation.x = Math.PI / 2;
        lens.position.set(0, 0, 0.22);
        ptzHead.add(lens);

        // LED Rojo de Grabación Activa
        const recDot = new THREE.Mesh(new THREE.SphereGeometry(0.02, 8, 8), new THREE.MeshBasicMaterial({ color: 0xEF4444 }));
        recDot.position.set(0.08, -0.06, 0.22);
        ptzHead.add(recDot);

        ptzHead.position.set(0.42, -0.08, 0);
        camRig.add(ptzHead);

        camRig.position.set(loc.x, loc.y, loc.z);
        camRig.rotation.y = loc.rotY;
        scene.add(camRig);
        physicalCctvCameras.push(ptzHead);
      });
    }

    function aimPhysicalCameras(targetPos) {
      physicalCctvCameras.forEach(cg => {
        cg.lookAt(targetPos.x, targetPos.y, targetPos.z);
      });
    }

    function createDetailedRacks() {
      const serverTexStandard = createServerTexture(false);
      const serverTexDatabase = createServerTexture(true);

      const rackGeo = new THREE.BoxGeometry(0.95, 2.7, 1.25);
      const sideMat = new THREE.MeshStandardMaterial({ color: 0x090E1A, roughness: 0.3, metalness: 0.8 });
      const sideMatDB = new THREE.MeshStandardMaterial({ color: 0x08152B, roughness: 0.25, metalness: 0.85 });

      const frontMatStandard = new THREE.MeshStandardMaterial({ map: serverTexStandard, roughness: 0.3, metalness: 0.5 });
      const frontMatDatabase = new THREE.MeshStandardMaterial({ map: serverTexDatabase, roughness: 0.3, metalness: 0.5 });

      const rackMaterialsL_Std = [frontMatStandard, sideMat, sideMat, sideMat, sideMat, sideMat];
      const rackMaterialsR_Std = [sideMat, frontMatStandard, sideMat, sideMat, sideMat, sideMat];

      const rackMaterialsL_DB = [frontMatDatabase, sideMatDB, sideMatDB, sideMatDB, sideMatDB, sideMatDB];
      const rackMaterialsR_DB = [sideMatDB, frontMatDatabase, sideMatDB, sideMatDB, sideMatDB, sideMatDB];

      const rackMetadata = [
        { id: "RACK 01 - BASE DE DATOS CORE SAN (ORACLE/POSTGRES)", temp: "19.8 °C", status: "ÓPTIMO FRÍO (REPLICADO ❄️)", isDB: true, icon: "🗄️" },
        { id: "RACK 02 - BACKUP INMUTABLE SAN (WORM 3-2-1)", temp: "20.1 °C", status: "ÓPTIMO FRÍO ❄️", isDB: true, icon: "💾" },
        { id: "RACK 03 - WEB DMZ & REVERSE PROXY", temp: "20.4 °C", status: "ÓPTIMO FRÍO ❄️", isDB: false, icon: "🌐" },
        { id: "RACK 04 - API GATEWAY & MICROSERVICIOS", temp: "20.2 °C", status: "ÓPTIMO FRÍO ❄️", isDB: false, icon: "⚡" },
        { id: "RACK 05 - VPN CORPORATIVA & FIREWALL NGFW", temp: "19.9 °C", status: "ÓPTIMO FRÍO ❄️", isDB: false, icon: "🛡️" },
        { id: "RACK 06 - CLÚSTER TRANSACCIONAL FINANSUR", temp: "20.0 °C", status: "ÓPTIMO FRÍO ❄️", isDB: false, icon: "🏦" },
        { id: "RACK 07 - AUTENTICACIÓN RADIUS / ACTIVE DIRECTORY", temp: "19.7 °C", status: "ÓPTIMO FRÍO ❄️", isDB: false, icon: "🔑" },
        { id: "RACK 08 - SIEM FORENSE & BITÁCORAS DE AUDITORÍA", temp: "19.9 °C", status: "ÓPTIMO FRÍO ❄️", isDB: false, icon: "📋" },
        { id: "RACK 09 - STORAGE MULTI-CLOUD HYBRID", temp: "20.3 °C", status: "ÓPTIMO FRÍO ❄️", isDB: false, icon: "☁️" },
        { id: "RACK 10 - UPS MODULAR TRIFÁSICO & PDU A/B", temp: "21.0 °C", status: "100% CARGA (TIER III)", isDB: false, icon: "🔋" }
      ];

      let idx = 0;
      for (let i = -2; i <= 2; i++) {
        const isDB_L = (i === 0);
        const dataL = rackMetadata[idx++] || { id: "RACK SERVIDOR", temp: "19.8 °C", status: "ÓPTIMO", isDB: false, icon: "🖧" };
        const rackL = new THREE.Mesh(rackGeo, isDB_L ? rackMaterialsL_DB : rackMaterialsL_Std);
        rackL.position.set(-1.85, 1.35, i * 1.6);
        rackL.castShadow = true;
        rackL.userData = dataL;
        scene.add(rackL);
        racksMesh.push(rackL);

        const isDB_R = (i === 1);
        const dataR = rackMetadata[idx++] || { id: "RACK SERVIDOR", temp: "20.1 °C", status: "ÓPTIMO", isDB: false, icon: "🖧" };
        const rackR = new THREE.Mesh(rackGeo, isDB_R ? rackMaterialsR_DB : rackMaterialsR_Std);
        rackR.position.set(1.85, 1.35, i * 1.6);
        rackR.castShadow = true;
        rackR.userData = dataR;
        scene.add(rackR);
        racksMesh.push(rackR);
      }

      // Techo Confinado de Pasillo Frío (Cristal Acrílico Hermético)
      const roofGlass = new THREE.Mesh(
        new THREE.PlaneGeometry(3.7, 8.2),
        new THREE.MeshPhysicalMaterial({
          color: 0x06B6D4,
          transparent: true,
          opacity: 0.30,
          transmission: 0.92,
          roughness: 0.1
        })
      );
      roofGlass.position.set(0, 2.72, 0);
      roofGlass.rotation.x = -Math.PI / 2;
      scene.add(roofGlass);
    }

    function createMantrapEntrance() {
      const frame = new THREE.Mesh(
        new THREE.BoxGeometry(2.8, 3.2, 0.2),
        new THREE.MeshStandardMaterial({ color: 0x334155, metalness: 0.9, roughness: 0.2 })
      );
      frame.position.set(0, 1.6, -5.2);
      scene.add(frame);

      doorGlassMesh = new THREE.Mesh(
        new THREE.BoxGeometry(2.2, 2.8, 0.06),
        new THREE.MeshPhysicalMaterial({
          color: 0x38BDF8,
          transparent: true,
          opacity: 0.55,
          transmission: 0.95
        })
      );
      doorGlassMesh.position.set(0, 1.6, -5.2);
      doorGlassMesh.userData = { id: "ESCLUSA MANTRAP BIOMÉTRICA", temp: "20.0 °C", status: "PUERTA BLOQUEADA SEGURA", icon: "🚪" };
      scene.add(doorGlassMesh);
      racksMesh.push(doorGlassMesh);

      const terminal = new THREE.Mesh(
        new THREE.BoxGeometry(0.3, 0.5, 0.12),
        new THREE.MeshStandardMaterial({ color: 0x10B981, emissive: 0x10B981, emissiveIntensity: 0.8 })
      );
      terminal.position.set(1.65, 1.5, -5.1);
      scene.add(terminal);

      laserBeamMesh = new THREE.Mesh(
        new THREE.CylinderGeometry(0.012, 0.012, 3.7, 8),
        new THREE.MeshBasicMaterial({ color: 0xEF4444, transparent: true, opacity: 0.85 })
      );
      laserBeamMesh.rotation.z = Math.PI / 2;
      laserBeamMesh.position.set(0, 0.8, -4.8);
      scene.add(laserBeamMesh);

      const intruderGeo = new THREE.CylinderGeometry(0.25, 0.25, 1.7, 16);
      const intruderMat = new THREE.MeshBasicMaterial({ color: 0xEF4444, wireframe: true, transparent: true, opacity: 0 });
      intruderMesh = new THREE.Mesh(intruderGeo, intruderMat);
      intruderMesh.position.set(0, 0.85, -5.0);
      scene.add(intruderMesh);
    }

    // 4. NIEBLA FRÍA CON PARTÍCULAS RADIALES SUAVES (Sin Cubos Pixelados)
    function createMistTexture() {
      const canvas = document.createElement('canvas');
      canvas.width = 64;
      canvas.height = 64;
      const ctx = canvas.getContext('2d');
      const grad = ctx.createRadialGradient(32, 32, 0, 32, 32, 32);
      grad.addColorStop(0, 'rgba(103, 232, 249, 0.7)');
      grad.addColorStop(0.4, 'rgba(56, 189, 248, 0.25)');
      grad.addColorStop(1, 'rgba(14, 165, 233, 0)');
      ctx.fillStyle = grad;
      ctx.fillRect(0, 0, 64, 64);
      return new THREE.CanvasTexture(canvas);
    }

    function createCryogenicMistParticles() {
      const mistCount = 200;
      const mistGeo = new THREE.BufferGeometry();
      const mistPos = new Float32Array(mistCount * 3);

      for (let i = 0; i < mistCount * 3; i += 3) {
        mistPos[i] = (Math.random() - 0.5) * 2.4;
        mistPos[i + 1] = 0.08 + Math.random() * 0.45;
        mistPos[i + 2] = (Math.random() - 0.5) * 7.5;
      }

      mistGeo.setAttribute('position', new THREE.BufferAttribute(mistPos, 3));
      const mistMat = new THREE.PointsMaterial({
        size: 0.38,
        map: createMistTexture(),
        transparent: true,
        opacity: 0.45,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });

      coldMistParticles = new THREE.Points(mistGeo, mistMat);
      scene.add(coldMistParticles);
    }

    function toggleColdMist() {
      showColdMist = !showColdMist;
      const btn = document.getElementById('btn-toggle-mist');
      if (showColdMist) {
        coldMistParticles.material.opacity = 0.45;
        btn.innerText = "❄️ Niebla ON";
        btn.className = "px-2.5 py-1 bg-cyan-950 text-cyan-300 border border-cyan-700 text-xs font-bold rounded-lg transition";
      } else {
        coldMistParticles.material.opacity = 0;
        btn.innerText = "❄️ Niebla OFF";
        btn.className = "px-2.5 py-1 bg-slate-800 text-slate-400 border border-slate-700 text-xs font-bold rounded-lg transition";
      }
    }

    function createSpecialFX() {
      const shieldGeo = new THREE.IcosahedronGeometry(1.9, 3);
      const shieldMat = new THREE.MeshBasicMaterial({
        color: 0xA855F7,
        wireframe: true,
        transparent: true,
        opacity: 0
      });
      cyberShieldMesh = new THREE.Mesh(shieldGeo, shieldMat);
      cyberShieldMesh.position.set(-1.85, 1.4, 0);
      scene.add(cyberShieldMesh);

      // Fuego Realista en Rack 03
      const fireCount = 180;
      const fireGeo = new THREE.BufferGeometry();
      const firePos = new Float32Array(fireCount * 3);
      for (let i = 0; i < fireCount * 3; i += 3) {
        firePos[i] = -1.85 + (Math.random() - 0.5) * 0.7;
        firePos[i + 1] = 0.4 + Math.random() * 1.5;
        firePos[i + 2] = (Math.random() - 0.5) * 1.1;
      }
      fireGeo.setAttribute('position', new THREE.BufferAttribute(firePos, 3));
      const fireMat = new THREE.PointsMaterial({
        size: 0.22,
        color: 0xF59E0B,
        transparent: true,
        opacity: 0,
        blending: THREE.AdditiveBlending
      });
      fireParticles = new THREE.Points(fireGeo, fireMat);
      scene.add(fireParticles);

      // Humo Denso
      const smokeCount = 220;
      const smokeGeo = new THREE.BufferGeometry();
      const smokePos = new Float32Array(smokeCount * 3);
      for (let i = 0; i < smokeCount * 3; i += 3) {
        smokePos[i] = -1.85 + (Math.random() - 0.5) * 0.9;
        smokePos[i + 1] = 1.0 + Math.random() * 3.2;
        smokePos[i + 2] = (Math.random() - 0.5) * 1.4;
      }
      smokeGeo.setAttribute('position', new THREE.BufferAttribute(smokePos, 3));
      const smokeMat = new THREE.PointsMaterial({
        size: 0.32,
        color: 0x475569,
        transparent: true,
        opacity: 0
      });
      smokeParticles = new THREE.Points(smokeGeo, smokeMat);
      scene.add(smokeParticles);
    }

    function createNeuralNetworkMesh3D() {
      const nodeCount = 65;
      const geo = new THREE.BufferGeometry();
      const pos = new Float32Array(nodeCount * 3);
      for (let i = 0; i < nodeCount * 3; i += 3) {
        pos[i] = (Math.random() - 0.5) * 8.0;
        pos[i + 1] = 3.2 + Math.random() * 1.4;
        pos[i + 2] = (Math.random() - 0.5) * 8.0;
      }
      geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
      const mat = new THREE.PointsMaterial({
        size: 0.20,
        color: 0x06B6D4,
        transparent: true,
        opacity: 0
      });
      neuralCloud = new THREE.Points(geo, mat);
      scene.add(neuralCloud);
    }

    // 5. MANEJADOR LIMPIO DE CLIC (Sin Modales Invasivos)
    function handleCleanRackClick(event) {
      const container = document.getElementById('canvas-container');
      const rect = container.getBoundingClientRect();
      mouse.x = ((event.clientX - rect.left) / container.clientWidth) * 2 - 1;
      mouse.y = -((event.clientY - rect.top) / container.clientHeight) * 2 + 1;

      raycaster.setFromCamera(mouse, camera);
      const intersects = raycaster.intersectObjects(racksMesh);

      if (intersects.length > 0) {
        const obj = intersects[0].object;
        if (obj.userData && obj.userData.id) {
          playBeep(750, 0.08);
          openRackPanel(obj.userData);
        }
      }
    }

    function openRackPanel(data) {
      document.getElementById('rack-panel-title').innerText = data.id;
      document.getElementById('rack-panel-icon').innerText = data.icon || "🗄️";
      document.getElementById('rack-panel-status').innerText = (Math.random() * 1.0 + 19.4).toFixed(1) + " °C • " + data.status;
      document.getElementById('rack-panel-perf').innerText = (Math.random() * 15 + 10).toFixed(1) + "% CPU • " + (Math.random() * 20 + 35).toFixed(0) + "% RAM";
      document.getElementById('rack-panel-disk').innerText = (Math.random() * 600 + 4400).toFixed(0) + " IOPS • RAID-10";

      document.getElementById('hud-rack-panel').classList.remove('hidden');
      document.getElementById('hint-click').classList.add('hidden');
    }

    function closeRackPanel() {
      document.getElementById('hud-rack-panel').classList.add('hidden');
      document.getElementById('hint-click').classList.remove('hidden');
    }

    function animateCameraTo(newPos, newLook) {
      targetCamPos.set(newPos.x, newPos.y, newPos.z);
      targetCamLook.set(newLook.x, newLook.y, newLook.z);
      isTransitioning = true;
    }

    function movePlayer(dir) {
      isTourRunning = false;
      isTransitioning = false;
      const step = 0.55;
      const forward = new THREE.Vector3();
      camera.getWorldDirection(forward);
      forward.y = 0;
      forward.normalize();
      const side = new THREE.Vector3().crossVectors(camera.up, forward).normalize();

      if (dir === 'forward') {
        camera.position.addScaledVector(forward, step);
        controls.target.addScaledVector(forward, step);
      } else if (dir === 'backward') {
        camera.position.addScaledVector(forward, -step);
        controls.target.addScaledVector(forward, -step);
      } else if (dir === 'left') {
        camera.position.addScaledVector(side, step);
        controls.target.addScaledVector(side, step);
      } else if (dir === 'right') {
        camera.position.addScaledVector(side, -step);
        controls.target.addScaledVector(side, -step);
      }
    }

    function startCinematicTour() {
      isTourRunning = true;
      isTransitioning = false;
      tourTime = 0;
      playBeep(880, 0.1);
    }

    function toggleNeuralNet3D() {
      showNeural3D = !showNeural3D;
      const btn = document.getElementById('btn-toggle-net3d');
      if (showNeural3D) {
        neuralCloud.material.opacity = 0.9;
        btn.className = 'px-2.5 py-1 bg-cyan-600 text-white font-bold rounded-lg border border-cyan-400 transition';
      } else {
        neuralCloud.material.opacity = 0;
        btn.className = 'px-2.5 py-1 bg-indigo-950 text-indigo-300 border border-indigo-700 text-xs font-bold rounded-lg transition';
      }
    }

    function update3DEffects(state) {
      currentAlarm = state;

      smokeParticles.material.opacity = 0;
      fireParticles.material.opacity = 0;
      cyberShieldMesh.material.opacity = 0;
      intruderMesh.material.opacity = 0;
      fireLight.intensity = 0;
      doorGlassMesh.material.color.setHex(0x38BDF8);
      doorGlassMesh.position.x = 0;

      ceilingLights.forEach(cl => {
        if (cl.isPointLight || cl.isDirectionalLight) cl.intensity = 1.0;
        else if (cl.material) cl.material.color.setHex(0xBAE6FD);
      });
      emergencyLightStrips.forEach(els => els.material.color.setHex(0x06B6D4));
      hvacLeds.forEach(hl => hl.material.color.setHex(0x06B6D4));

      if (state === 'normal') {
        strobeLight.intensity = 0;
        if (showColdMist) coldMistParticles.material.opacity = 0.45;
      } else if (state === 'alarm_door') {
        doorGlassMesh.material.color.setHex(0xEF4444);
        strobeLight.color.setHex(0xEF4444);
        doorGlassMesh.position.x = 0.6;
        intruderMesh.material.opacity = 0.85;
      } else if (state === 'alarm_fire') {
        fireParticles.material.opacity = 0.9;
        smokeParticles.material.opacity = 0.85;
        fireLight.intensity = 2.8;
        strobeLight.color.setHex(0xEA580C);
      } else if (state === 'alarm_heat') {
        smokeParticles.material.opacity = 0.35;
        strobeLight.color.setHex(0xF59E0B);
        coldMistParticles.material.opacity = 0.05;
        hvacLeds.forEach(hl => hl.material.color.setHex(0xF59E0B)); // Ventilador en sobrecalentamiento
      } else if (state === 'alarm_net' || state === 'alarm_ransom') {
        cyberShieldMesh.material.opacity = 0.95;
        strobeLight.color.setHex(0xA855F7);
      } else if (state === 'alarm_power') {
        ceilingLights.forEach(cl => {
          if (cl.isPointLight || cl.isDirectionalLight) cl.intensity = 0.05;
          else if (cl.material) cl.material.color.setHex(0x020617);
        });
        emergencyLightStrips.forEach(els => els.material.color.setHex(0xEAB308));
        strobeLight.color.setHex(0xEAB308);
      }
    }

    function onResize() {
      const container = document.getElementById('canvas-container');
      const w = container.clientWidth;
      const h = container.clientHeight;
      camera.aspect = w / h;
      camera.updateProjectionMatrix();
      renderer.setSize(w, h);
    }

    let clock = new THREE.Clock();

    function animate() {
      requestAnimationFrame(animate);
      const delta = clock.getDelta();
      const time = clock.getElapsedTime();

      if (keysPressed['w'] || keysPressed['arrowup']) movePlayer('forward');
      if (keysPressed['s'] || keysPressed['arrowdown']) movePlayer('backward');
      if (keysPressed['a'] || keysPressed['arrowleft']) movePlayer('left');
      if (keysPressed['d'] || keysPressed['arrowright']) movePlayer('right');

      if (isTransitioning) {
        camera.position.lerp(targetCamPos, 0.06);
        controls.target.lerp(targetCamLook, 0.06);
        if (camera.position.distanceTo(targetCamPos) < 0.05) {
          isTransitioning = false;
        }
      }

      if (isTourRunning) {
        tourTime += delta * 0.35;
        const radius = 5.2;
        camera.position.x = Math.sin(tourTime) * radius;
        camera.position.z = Math.cos(tourTime) * radius;
        camera.position.y = 2.0 + Math.sin(tourTime * 2) * 0.45;
        controls.target.set(0, 1.4, 0);
      }

      // Rotación suave y aerodinámica de las aspas del ventilador
      const fanSpeed = (currentAlarm === 'alarm_heat') ? 18 : 5;
      hvacFans.forEach(fg => {
        fg.rotation.z += delta * fanSpeed;
      });

      if (currentAlarm !== 'normal') {
        strobeLight.intensity = Math.sin(time * 14) > 0 ? 5.0 : 0.2;
      } else {
        strobeLight.intensity = 0;
      }

      if (currentAlarm === 'alarm_fire') {
        fireLight.intensity = 2.0 + Math.random() * 2.5;
      }

      if (cyberShieldMesh && cyberShieldMesh.material.opacity > 0) {
        cyberShieldMesh.rotation.y += delta * 1.8;
        cyberShieldMesh.rotation.x += delta * 0.9;
      }

      // Animación suave de niebla criogénica deslizándose por el piso
      if (coldMistParticles && showColdMist && coldMistParticles.material.opacity > 0) {
        const pArray = coldMistParticles.geometry.attributes.position.array;
        for (let i = 0; i < pArray.length; i += 3) {
          pArray[i + 2] += delta * 0.35;
          if (pArray[i + 2] > 3.8) pArray[i + 2] = -3.8;
        }
        coldMistParticles.geometry.attributes.position.needsUpdate = true;
      }

      if (fireParticles && fireParticles.material.opacity > 0) {
        const fPos = fireParticles.geometry.attributes.position.array;
        for (let i = 1; i < fPos.length; i += 3) {
          fPos[i] += delta * 1.5;
          if (fPos[i] > 2.2) fPos[i] = 0.4;
        }
        fireParticles.geometry.attributes.position.needsUpdate = true;
      }

      if (smokeParticles && smokeParticles.material.opacity > 0) {
        const sPos = smokeParticles.geometry.attributes.position.array;
        for (let i = 1; i < sPos.length; i += 3) {
          sPos[i] += delta * 0.85;
          if (sPos[i] > 4.4) sPos[i] = 1.0;
        }
        smokeParticles.geometry.attributes.position.needsUpdate = true;
      }

      if (neuralCloud && showNeural3D) {
        neuralCloud.rotation.y = time * 0.18;
      }

      const now = new Date();
      document.getElementById('cctv-timer').innerText = now.toTimeString().split(' ')[0];

      controls.update();
      renderer.render(scene, camera);
    }

    window.addEventListener('DOMContentLoaded', () => {
      init3D();
    });
  </script>
</body>
</html>
'''

# 1. Guardar en Workspace
target_ws = r"c:\Users\Misael P\Downloads\Trabajo de jaramillo de nuetar soepracibiddes\SIMULADOR_DATA_CENTER_3D.html"
with open(target_ws, "w", encoding="utf-8") as f:
    f.write(html_code)
print(f"[OK] Guardado en Workspace: {target_ws} ({len(html_code)} bytes)")

# 2. Guardar en Brain
target_brain = r"C:\Users\Misael P\.gemini\antigravity\brain\ddf73e8f-6454-4b4e-a910-bf3c3817c189\SIMULADOR_DATA_CENTER_3D.html"
try:
    with open(target_brain, "w", encoding="utf-8") as f:
        f.write(html_code)
    print(f"[OK] Guardado en Brain: {target_brain}")
except Exception as e:
    print(f"[WARN] Error en Brain: {e}")
