@echo off
REM Inicia o servidor Flask
start python C:\Apache24\htdocs\PI\app.py

REM Aguarda alguns segundos para garantir que o Flask esteja em execução
timeout /t 5 /nobreak
