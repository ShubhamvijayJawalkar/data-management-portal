@echo off
cd /d "%~dp0"

call venv\Scripts\activate

start "" pythonw app.py

timeout /t 3 >nul
start http://127.0.0.1:5000
