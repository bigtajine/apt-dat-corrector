# Airport Data Corrector - X-Plane

A standalone GUI application to update airport names in X-Plane custom scenery files using Excel data.

## Features

- **No Python Required**: Standalone `.exe` - works on any Windows PC
- **Visual Interface**: Easy-to-use GUI with file browser dialogs
- **Dry Run Mode**: Preview changes before applying them
- **Live Output**: See exactly what changes are being made
- **Safe Processing**: Automatic backups via dry run, detailed logging

## For Users (Using Pre-Built .exe)

### Quick Start

1. **Download** `AirportCorrector.exe` from the `dist/` folder
2. **Double-click** the executable to run
3. **Select Files**:
   - Click "Browse..." next to "Airport Excel File" and select your `.xlsx` file
   - Click "Browse..." next to "Custom Scenery Folder" and select your X-Plane Custom Scenery directory
4. **Load Data**: Click "Load Excel" to import airport data
5. **Preview**: Keep "Dry Run" checked and click "Start Processing" to preview changes
6. **Apply Changes**: Uncheck "Dry Run" and click "Start Processing" again to make actual changes

### System Requirements

- Windows 7 or later
- No Python installation needed
- ~50-100 MB disk space for the executable

## For Developers (Building from Source)

### Requirements

- Python 3.8+
- pip (comes with Python)

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd apt-dat-corrector
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the GUI

```bash
python gui_app.py
```

### Building Standalone Executable

```bash
python build.py
```

This will:
- Install PyInstaller
- Build a standalone `.exe` in the `dist/` folder
- No Python installation needed to run the `.exe`

## Project Structure

```
apt-dat-corrector/
├── gui_app.py              # Main GUI application
├── apt_corrector_core.py   # Core processing logic
├── apt_dat_corrector.py    # Original script (legacy)
├── airports.csv            # Sample airport data
├── requirements.txt        # Python dependencies
├── build.py               # Build script for .exe
└── dist/                  # Output folder for built .exe
    └── AirportCorrector.exe
```

## How It Works

1. **Loads Excel Data**: Reads airport ICAO codes and corrected names from your Excel file
2. **Scans X-Plane**: Walks through the Custom Scenery directory
3. **Updates apt.dat Files**: For each airport found, updates the airport name line
4. **Dry Run Mode**: Preview mode shows what would be changed without modifying files
5. **Reports Results**: Displays detailed output for each file processed

## Troubleshooting

### Executable won't run
- Make sure you're on Windows
- Try running as Administrator (right-click → Run as administrator)
- Check your antivirus - it might be blocking the .exe

### Excel file not loading
- Make sure the Excel file is in `.xlsx` format
- Verify the Excel has at least 3 columns: (any), ICAO, Airport Name
- Excel file must not be open in another program

### No files found
- Check that the Custom Scenery path is correct
- Verify the folder contains `apt.dat` files
- Path should be: `X-Plane 12/Custom Scenery/` or similar

### Changes not applying
- Make sure "Dry Run" is unchecked
- Verify you have write permissions to the folder
- Manually check file permissions if needed

## File Format Requirements

### Excel File (.xlsx)
Required columns:
- Column A: (ignored)
- Column B: ICAO Code (e.g., KJFK, EGLL, LFPG)
- Column C: Airport Name (e.g., "John F Kennedy Intl", "London Heathrow")

### apt.dat Files
The tool updates line 4 of each `apt.dat` file with the format:
```
1 5354 1 0 ICAO AIRPORT_NAME
```

## License

MIT

## Support

For issues or questions, please check:
1. The output log for detailed error messages
2. File paths are correct and accessible
3. Excel format matches requirements
4. You have proper file permissions
