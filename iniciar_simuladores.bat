@echo off
chcp 65001 > nul
title Suite de Simuladores - I.E.S.T.P. Hermanos Cárcamo
echo =========================================================================
echo    SUITE DE SIMULADORES TECNOLÓGICOS - PROF. JARAMILLO
echo    I.E.S.T.P. Hermanos Cárcamo - Paita
echo    Sistemas de Transporte de Información (STI) & ISO/IEC 27001
echo =========================================================================
echo.
echo [1/3] Iniciando Portal Maestro Hub (portal.html)...
start "" "%~dp0portal.html"
timeout /t 1 /nobreak > nul

echo [2/3] Iniciando Simulador 3D Data Center II Pro (datacenter.html)...
start "" "%~dp0datacenter.html"
timeout /t 1 /nobreak > nul

echo [3/3] Iniciando Centro de Ciberdefensa SOC ISO 27001 (ciberdefensa.html)...
start "" "%~dp0ciberdefensa.html"

echo.
echo =========================================================================
echo    ¡Todos los simuladores han sido cargados con éxito en tu navegador!
echo =========================================================================
pause
