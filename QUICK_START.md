# Quick Start Guide - For End Users

## What is This?

This is a tool to fix airport names in X-Plane custom scenery files. It reads correct airport names from an Excel file and updates them in your X-Plane installation.

## Getting Started (5 minutes)

### Step 1: Prepare Your Excel File

Make sure you have an Excel file (`.xlsx`) with airport data in this format:

| Column A | Column B | Column C |
|----------|----------|----------|
| (any)    | KJFK     | John F Kennedy Intl |
| (any)    | EGLL     | London Heathrow |
| (any)    | LFPG     | Paris Charles de Gaulle |

Column B must have ICAO codes (airport identifiers).
Column C must have the airport names.

### Step 2: Run the Program

**Double-click** `AirportCorrector.exe`

You should see a window appear with buttons and fields.

### Step 3: Select Your Files

1. Click the **"Browse..."** button next to **"Airport Excel File"**
   - Find and select your `.xlsx` file
   
2. Click the **"Browse..."** button next to **"Custom Scenery Folder"**
   - Navigate to your X-Plane 12 installation
   - Open the **"Custom Scenery"** folder
   - Click "OK"

### Step 4: Load the Data

Click the **"Load Excel"** button

You should see messages appear in the output window below showing how many airports were loaded.

### Step 5: Preview the Changes

Make sure the checkbox **"Dry Run (preview only, no changes)"** is **CHECKED** ✓

Click **"Start Processing"**

The output window will show:
- What airports will be updated
- Old names → New names
- Any airports it skips
- Summary at the end

**This does NOT make any changes yet.** It's just showing what would happen.

### Step 6: Apply the Changes

Once you're happy with the preview:

1. **UNCHECK** the "Dry Run" checkbox (remove the ✓)
2. Click **"Start Processing"** again
3. The tool will now update all the files in your Custom Scenery folder

## What if Something Goes Wrong?

### The .exe won't run
- Right-click it and select "Run as administrator"
- Your antivirus might be blocking it (check antivirus settings)

### No airports loaded from Excel
- Make sure the file is `.xlsx` format (not `.xls` or `.csv`)
- Verify Column B has ICAO codes and Column C has names
- Make sure the Excel file isn't open in another program

### No files found in Custom Scenery
- Check that the path is correct
- Make sure the folder actually contains `apt.dat` files
- Try a subfolder if the main folder is empty

### I want to undo changes
- You made a backup first... right? Always make a backup before using this tool!
- If you made a mistake, restore the files from your backup

## Tips & Best Practices

✓ **DO:**
- Always try Dry Run first to see what will change
- Make a backup of your Custom Scenery folder first
- Use this tool on copies, not originals
- Keep your Excel file organized

✗ **DON'T:**
- Don't modify the file while processing is happening
- Don't close the program while it's working
- Don't leave the Excel file open in Excel

## Getting Help

1. Check the output window for error messages
2. Look at the README.md file for more detailed information
3. Make sure your file paths and formats are correct

## Still Need Help?

Check the detailed README.md file in the same folder - it has more information about troubleshooting and file formats.
