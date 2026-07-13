# Airport Data Corrector (X-Plane)

Fixes airport names inside X-Plane `Custom Scenery` packages, using an Excel spreadsheet as the source of correct names. Handy when third-party scenery ships with inconsistent or wrong airport naming.

## Usage

1. Download `AirportCorrector.exe` and `airports.xlsx` from the Releases page, and put them in the same folder.
2. Double-click `AirportCorrector.exe`.

A console window opens and does the rest on its own: it finds `airports.xlsx` next to itself, finds your X-Plane 12 (or 11) `Custom Scenery` folder automatically, and runs a dry run showing every change it would make (old name → new name), ending with a summary list.

Then it asks `Apply these changes? [y/N]`. Type `y` and Enter to write them, or just press Enter to leave everything untouched.

If it can't find the spreadsheet or your X-Plane install, it asks you to paste the path instead.

## Undoing changes

Before it overwrites any `apt.dat`, it saves the original next to it as `apt.dat.apt-corrector-bak`. Run the program again and it'll notice those backup files and offer to restore them:

```
Found 3 backup(s) from a previous run (original apt.dat files this tool changed).
Undo those changes and restore the originals? [y/N]:
```

Say `y` and it restores every changed file and deletes the backups. This is the actual undo — there's no separate "make a backup yourself first" step required.

## Spreadsheet format

First worksheet, column B = ICAO code, column C = airport name:

| B (ICAO) | C (Name)             |
|----------|-----------------------|
| KJFK     | John F Kennedy Intl  |
| EGLL     | London Heathrow      |

## Troubleshooting

- **.exe won't run** — try "Run as administrator", or check if your antivirus is blocking it.
- **No airports loaded** — confirm the file is `.xlsx` (not `.xls`) or `.csv`, column B/C are correct, and the file isn't open in Excel.
- **Can't auto-detect X-Plane** — X-Plane writes `%LOCALAPPDATA%\x-plane_install_12.txt` (or `_11.txt`) on install; if that's missing, just paste the `Custom Scenery` path when asked.
- **Want to undo** — run the program again, it'll offer to restore from the `.apt-corrector-bak` files automatically (see above).

## Project files

- `apt_dat_corrector.py` — console entry point
- `apt_corrector_core.py` — core processing logic (load spreadsheet, scan/patch apt.dat, backup/restore)
- `build.py` — PyInstaller build helper

## Developer setup

```bash
pip install -r requirements.txt
python apt_dat_corrector.py   # run
python build.py               # build Windows exe, output in dist/
```

## License

MIT
