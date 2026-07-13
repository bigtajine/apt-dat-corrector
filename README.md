# Airport Data Corrector (X-Plane)

Corrects airport names in X-Plane `Custom Scenery` `apt.dat` files against a reference spreadsheet.

## Overview

Third-party X-Plane scenery frequently ships with inconsistent or wrong airport names in `apt.dat` (e.g. `KJFK` labeled something other than "John F Kennedy Intl"). This tool walks a `Custom Scenery` folder, matches each `apt.dat`'s ICAO code against a reference spreadsheet, and rewrites the name field where it differs.

## How it works

Row 4 of every `apt.dat` (the airport header line) has the form:

```
1   <elevation> <deprecated> <deprecated> <ICAO> <name>
```

The script reads the ICAO code from that line, looks it up in the spreadsheet (column B = ICAO, column C = name), and if the name differs, rewrites the line with the spreadsheet's version. Nothing is written until a dry run has shown the changes and been confirmed.

## Usage

Download `AirportCorrector.exe` and `airports.xlsx` from the Releases page, put them in the same folder, and run the exe — no Python required.

To run from source instead:

```
python apt_dat_corrector.py
```

Either way, it auto-detects the X-Plane 12/11 install path (from `%LOCALAPPDATA%\x-plane_install_12.txt` / `_11.txt`) and looks for `airports.xlsx` or `airports.csv` next to itself; if either can't be found it prompts for a path.

It always runs a dry run first, prints every change (`ICAO: old name -> new name`), then asks for confirmation before writing anything.

## Notes

This repository contains the patcher, its Excel/CSV reference data, and documentation. No X-Plane or third-party scenery files are included.
