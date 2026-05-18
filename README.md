# X-Plane Airport Name Fixer

A Python tool that updates airport names in X-Plane Custom Scenery `apt.dat` files using an ICAO-based Excel reference list.

## What it does

- Scans all `apt.dat` files in X-Plane Custom Scenery
- Reads ICAO codes and airport names from an Excel file
- Matches ICAO codes and replaces outdated names
- Prints all changes to the console
- Supports dry-run mode before applying edits

## Requirements

- Python 3.10+
- openpyxl

## Install:

```bash
pip install openpyxl


## Configuration

Edit in script:

```python
CUSTOM_SCENERY = r"C:\Path\To\X-Plane 12\Custom Scenery"
XLSX_PATH = r"C:\Path\To\airports.xlsx"
DRY_RUN = True
VERBOSE = True
```

## Excel format

* Column B → ICAO code
* Column C → Airport name

Example:

| B    | C                        |
| ---- | ------------------------ |
| KABQ | Albuquerque Intl Sunport |

## How it works

Reads line 4 of each `apt.dat`:

```
1 5354 1 0 KABQ Albuquerque International Sunport
```

Then:

* Extracts ICAO code
* Looks up correct name in Excel
* Replaces name if different

## Output example

```
KABQ Albuquerque International Sunport -> KABQ Albuquerque Intl Sunport
EGLL London Heathrow Airport -> EGLL London Heathrow
```

## Safety

* DRY_RUN = True → preview only
* DRY_RUN = False → writes changes

## Notes

* Only processes `apt.dat` files
* Assumes ICAO is on line 4
* Automatically strips accented characters

## Warning

This modifies scenery files directly. Always test with DRY_RUN first.
