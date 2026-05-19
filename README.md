# Airport Data Corrector - X-Plane

A compact GUI tool to update airport names in X-Plane custom scenery from an Excel file.

## Quick Start (Users)

- Download AirportCorrector.exe and airports.xlsx from Releases
- Select your `.xlsx` file and the X-Plane Custom Scenery folder
- Click "Load Excel", run a **Dry Run** to preview, then uncheck Dry Run to apply

## Developers

- Requirements: Python 3.8+, `pip`
- Install deps: `pip install -r requirements.txt`
- Run locally: `python gui_app.py`
- Build standalone Windows exe: `python build.py`

## Project (essential files)

- `gui_app.py` — GUI entry point
- `apt_corrector_core.py` — core processing logic
- `build.py` — build helper for PyInstaller
- `requirements.txt` — Python dependencies

## Legacy / Historical

- `apt_dat_corrector.py` — original command-line script (legacy; kept for reference)
- `airports.xlsx` — sample data used by the legacy script

Legacy usage (how to run the original script)

1. Install the minimal dependency if needed:

```bash
pip install openpyxl
```

2. Edit the configuration at the top of `apt_dat_corrector.py` to point to your files and mode:

- `CUSTOM_SCENERY` — full path to your X-Plane `Custom Scenery` folder
- `XLSX_PATH` — full path to your `.xlsx` spreadsheet (first worksheet is used)
- `DRY_RUN` — `True` to preview only, `False` to write changes
- `VERBOSE` — `True` to show progress output

3. Spreadsheet format expected by the legacy script:

- Column B (index 2): ICAO code (e.g., KJFK)
- Column C (index 3): Airport name to apply

4. Run the script (after configuring):

```bash
python apt_dat_corrector.py
```

Notes and cautions

- The legacy script reads the first worksheet and normalizes accents before matching ICAO codes.
- It updates the airport name on line 4 of any `apt.dat` file it finds (format like `1 5354 1 0 ICAO NAME...`).
- There is no automatic backup in the legacy script — keep `DRY_RUN = True` until you're confident, and manually back up folders before setting `DRY_RUN = False`.
- The GUI (`gui_app.py`) and `apt_corrector_core.py` provide a safer, supported workflow; the legacy script is retained for quick, single-file edits and reference.

## How it works (brief)

- Loads airport ICAO and name data from Excel
- Scans Custom Scenery folders for `apt.dat` files
- Updates airport name lines, with an optional Dry Run mode

## Troubleshooting (short)

- Executable doesn't start: try running as Administrator, temporarily disable antivirus
- Excel import fails: ensure `.xlsx` format and required columns (ICAO, Name)
- No files found: confirm the Custom Scenery path and presence of `apt.dat`

## License

MIT

---

For more details, see the source files and `build.py` in the project root.
