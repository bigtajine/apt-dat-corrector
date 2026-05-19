# Airport Data Corrector (X-Plane)

A small GUI tool that updates airport names inside X-Plane **Custom Scenery** packages using data from an Excel spreadsheet.

This is useful when third-party scenery uses inconsistent or incorrect airport naming.

## What it Does

- Reads ICAO + airport name data from an `.xlsx` file

- Scans X-Plane `Custom Scenery` folders for `apt.dat` files

- Updates airport names based on ICAO matches

- Supports **Dry Run mode** so you can preview changes before writing anything

## Quick Start (Most Users)

1. Download `AirportCorrector.exe` and `airports.xlsx` from the **Releases** page

2. Run `AirportCorrector.exe`

3. Select:
   
   - your `.xlsx` file
   
   - your X-Plane `Custom Scenery` folder

4. Click **Load Excel**

5. Run a **Dry Run** to preview changes

6. Uncheck **Dry Run** and run again to apply edits

## Spreadsheet Format

The tool expects the first worksheet to contain:

- **Column B** → ICAO code

- **Column C** → Airport name

Example:

| B (ICAO) | C (Name)            |
| -------- | ------------------- |
| KJFK     | John F Kennedy Intl |
| EGLL     | London Heathrow     |

## Project Files (Important)

- `gui_app.py` — GUI entry point

- `apt_corrector_core.py` — core processing logic

- `build.py` — build helper for PyInstaller

- `requirements.txt` — Python dependencies

## Developer Setup

### Requirements

- Python 3.8+

- pip

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Locally

```bash
python gui_app.py
```

### Build Windows EXE

```bash
python build.py
```

Output will be in the `dist/` folder.

## Legacy Script (CLI)

This repo also includes an older command-line version:

- `apt_dat_corrector.py` — legacy CLI tool (kept for reference)

To use it:

1. Install dependency:

```bash
pip install openpyxl
```

2. Edit the settings at the top of `apt_dat_corrector.py`:
- `CUSTOM_SCENERY`

- `XLSX_PATH`

- `DRY_RUN`
3. Run:

```bash
python apt_dat_corrector.py
```

⚠️ **Note:** the legacy script does not automatically create backups. Always test with `DRY_RUN = True` first.

## Safety Notes

- Always run a **Dry Run** before applying changes

- Back up your `Custom Scenery` folder if you're editing important scenery packages

- The tool edits airport name lines inside `apt.dat`

## License

MIT