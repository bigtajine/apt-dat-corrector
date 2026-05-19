"""
Build script to create standalone .exe using PyInstaller

This script will:
1. Check for PyInstaller installation
2. Build a standalone executable
3. Create a dist/ folder with the .exe

Usage:
    python build.py
"""

import os
import sys
import subprocess
from pathlib import Path


def run_command(cmd, description):
    """Run a command and report status"""
    print(f"\n{'='*60}")
    print(f"  {description}")
    print(f"{'='*60}")
    result = subprocess.run(cmd, shell=True)
    return result.returncode == 0


def main():
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    print("\n" + "="*60)
    print("  AIRPORT DATA CORRECTOR - STANDALONE BUILD")
    print("="*60)
    
    # Step 1: Install PyInstaller if needed
    print("\n[1/4] Checking dependencies...")
    if not run_command("pip install pyinstaller", "Installing PyInstaller"):
        print("✗ Failed to install PyInstaller")
        return False
    
    # Step 2: Install requirements
    print("\n[2/4] Installing requirements...")
    if not run_command("pip install -r requirements.txt", "Installing requirements"):
        print("✗ Failed to install requirements")
        return False
    
    # Step 3: Build executable
    print("\n[3/4] Building executable...")
    build_cmd = (
        "pyinstaller --onefile "
        "--windowed "
        "--name apt_dat_corrector "
        "--icon=NONE "
        "--hidden-import=openpyxl "
        "gui_app.py"
    )
    
    if not run_command(build_cmd, "Running PyInstaller"):
        print("✗ PyInstaller build failed")
        return False
    
    # Step 4: Verify
    print("\n[4/4] Verifying build...")
    exe_path = script_dir / "dist" / "AirportCorrector"
    if exe_path.exists():
        print(f"\n{'='*60}")
        print("  ✓ BUILD SUCCESSFUL")
        print(f"{'='*60}")
        print(f"\nExecutable created at:")
        print(f"  {exe_path}")
        print(f"\nTo run: Double-click AirportCorrector")
        print(f"\nThe executable is standalone and requires no Python installation.")
        return True
    else:
        print(f"\n✗ Executable not found at {exe_path}")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
