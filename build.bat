@echo off
REM Build script for Airport Data Corrector
REM This script builds the standalone .exe executable

echo.
echo ============================================================
echo   AIRPORT DATA CORRECTOR - BUILD
echo ============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

REM Run the build script
echo Running build process...
echo.

python build.py

if %errorlevel% equ 0 (
    echo.
    echo ============================================================
    echo   BUILD COMPLETE!
    echo ============================================================
    echo.
    echo The executable is ready at: dist\AirportCorrector.exe
    echo.
    pause
) else (
    echo.
    echo BUILD FAILED! Check error messages above.
    echo.
    pause
    exit /b 1
)
