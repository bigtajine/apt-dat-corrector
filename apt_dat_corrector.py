"""Console entry point for the X-Plane Airport Data Corrector."""

import os
import sys
from apt_corrector_core import load_airport_map_xlsx, scan_and_process, find_backups, restore_backups

for stream in (sys.stdout, sys.stderr):
    if hasattr(stream, "reconfigure"):
        stream.reconfigure(encoding="utf-8", errors="replace")

LOCALAPPDATA = os.environ.get("LOCALAPPDATA", "")


def detect_xplane_scenery():
    """Look for X-Plane 12/11 install-location marker files and return the Custom Scenery path."""
    for version in ("12", "11"):
        marker = os.path.join(LOCALAPPDATA, f"x-plane_install_{version}.txt")
        if not os.path.isfile(marker):
            continue
        try:
            with open(marker, "r", encoding="utf-8", errors="replace") as f:
                install_path = f.read().strip()
        except Exception:
            continue
        scenery = os.path.join(install_path, "Custom Scenery")
        if os.path.isdir(scenery):
            return scenery
    return None


def find_spreadsheet():
    """Look for airports.xlsx (or .csv) next to this script/exe."""
    base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    for name in ("airports.xlsx", "airports.csv"):
        candidate = os.path.join(base_dir, name)
        if os.path.isfile(candidate):
            return candidate
    return None


def ask_path(prompt):
    while True:
        value = input(prompt).strip().strip('"')
        if os.path.exists(value):
            return value
        print("  That path doesn't exist, try again.")


def print_summary(changes):
    print("\n" + "=" * 60)
    print("AIRPORTS CHANGED")
    print("=" * 60)
    if not changes:
        print("  (none)")
    else:
        for icao, old_name, new_name in changes:
            print(f"  {icao}: {old_name} -> {new_name}")
    print("=" * 60 + "\n")


def main():
    print("X-Plane Airport Data Corrector\n")

    scenery_path = detect_xplane_scenery()
    if scenery_path:
        print(f"Found X-Plane Custom Scenery: {scenery_path}")
    else:
        scenery_path = ask_path("Could not auto-detect X-Plane install. Enter path to your Custom Scenery folder: ")

    backups = find_backups(scenery_path)
    if backups:
        print(f"\nFound {len(backups)} backup(s) from a previous run (original apt.dat files this tool changed).")
        answer = input("Undo those changes and restore the originals? [y/N]: ").strip().lower()
        if answer == "y":
            restored = restore_backups(scenery_path, log_fn=print)
            print(f"\nRestored {restored} file(s).")
            input("\nPress Enter to exit...")
            return
        print("Keeping current files. New changes will still be backed up separately.\n")

    xlsx_path = find_spreadsheet()
    if xlsx_path:
        print(f"Found spreadsheet: {xlsx_path}")
    else:
        xlsx_path = ask_path("No airports.xlsx/.csv found next to this program. Enter path to it: ")

    airport_map = load_airport_map_xlsx(xlsx_path, log_fn=print)
    if not airport_map:
        print("No airport data loaded, stopping.")
        input("\nPress Enter to exit...")
        return

    print("\n--- Dry run (no files will be changed) ---\n")
    dry_stats = scan_and_process(scenery_path, airport_map, dry_run=True, log_fn=print)
    print_summary(dry_stats["changes"])

    if dry_stats["changed"] == 0:
        print("Nothing to change.")
        input("\nPress Enter to exit...")
        return

    answer = input(
        f"Apply these {dry_stats['changed']} changes? "
        "A backup of each original apt.dat is kept, run this program again to undo. [y/N]: "
    ).strip().lower()
    if answer != "y":
        print("No changes applied.")
        input("\nPress Enter to exit...")
        return

    print("\n--- Applying changes ---\n")
    live_stats = scan_and_process(scenery_path, airport_map, dry_run=False, log_fn=print)
    print_summary(live_stats["changes"])

    input("Press Enter to exit...")


if __name__ == "__main__":
    main()
