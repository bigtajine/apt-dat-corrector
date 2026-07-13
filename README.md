# Airport Data Corrector (X-Plane)

Fixes airport names inside X-Plane `Custom Scenery` packages, using an Excel spreadsheet as the source of correct names. Handy when third-party scenery ships with inconsistent or wrong airport naming.

## Usage

1. Download `AirportCorrector.exe` and `airports.xlsx` from the Releases page.
2. Run `AirportCorrector.exe`.
3. Select your `.xlsx` file and your X-Plane `Custom Scenery` folder.
4. Click **Load Excel**.
5. Run with **Dry Run** checked first to preview changes.
6. Uncheck **Dry Run** and run again to apply them.

The output log shows old name → new name for every airport it updates, plus a summary at the end.

## Spreadsheet format

First worksheet, column B = ICAO code, column C = airport name:

| B (ICAO) | C (Name)             |
|----------|-----------------------|
| KJFK     | John F Kennedy Intl  |
| EGLL     | London Heathrow      |

## Troubleshooting

- **.exe won't run** — try "Run as administrator", or check if your antivirus is blocking it.
- **No airports loaded** — confirm the file is `.xlsx` (not `.xls`/`.csv`), column B/C are correct, and the file isn't open in Excel.
- **No files found** — check the Custom Scenery path actually contains `apt.dat` files.
- **Made a mistake** — restore from your backup. Always back up `Custom Scenery` before a live run.

## Project files

- `gui_app.py` — GUI entry point
- `apt_corrector_core.py` — core processing logic
- `apt_dat_corrector.py` — older CLI version, kept for reference
- `build.py` — PyInstaller build helper

## Developer setup

```bash
pip install -r requirements.txt
python gui_app.py       # run
python build.py         # build Windows exe, output in dist/
```

### Legacy CLI

```bash
pip install openpyxl
```

Edit `CUSTOM_SCENERY`, `XLSX_PATH`, and `DRY_RUN` at the top of `apt_dat_corrector.py`, then run it directly. It does not create backups automatically — test with `DRY_RUN = True` first.

## Safety

Always dry-run before applying changes, and back up `Custom Scenery` before editing anything you care about.

## License

MIT
