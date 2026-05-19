@echo off
REM Quick run script for testing during development
REM This launches the GUI application directly

python gui_app.py
if %errorlevel% neq 0 (
    echo.
    echo ERROR: Failed to run application
    echo Make sure Python is installed and requirements are installed:
    echo.
    echo   pip install -r requirements.txt
    echo.
    pause
)
