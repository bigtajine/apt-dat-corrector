"""Tkinter GUI for apt.dat corrector - Standalone application"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import os
from apt_corrector_core import load_airport_map_xlsx, scan_and_process


class AptCorrectorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("X-Plane Airport Data Corrector")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        
        # State
        self.excel_path = tk.StringVar()
        self.scenery_path = tk.StringVar()
        self.dry_run_var = tk.BooleanVar(value=True)
        self.airport_map = {}
        self.is_processing = False
        
        self._create_widgets()
        self._center_window()
    
    def _center_window(self):
        """Center window on screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
    
    def _create_widgets(self):
        """Create all GUI widgets"""
        # Style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky="nsew")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(3, weight=1)
        
        # Title
        title = ttk.Label(main_frame, text="X-Plane Airport Data Corrector", 
                         font=("Segoe UI", 14, "bold"))
        title.grid(row=0, column=0, columnspan=3, pady=(0, 15), sticky="w")
        
        # --- FILE SELECTION SECTION ---
        file_frame = ttk.LabelFrame(main_frame, text="Files & Settings", padding="10")
        file_frame.grid(row=1, column=0, sticky="ew", pady=(0, 10))
        file_frame.columnconfigure(1, weight=1)
        
        # Excel file selection
        ttk.Label(file_frame, text="Airport Excel File:").grid(row=0, column=0, sticky="w", pady=5)
        ttk.Entry(file_frame, textvariable=self.excel_path, state="readonly").grid(
            row=0, column=1, sticky="ew", padx=(5, 5))
        ttk.Button(file_frame, text="Browse...", 
                  command=self._select_excel).grid(row=0, column=2, padx=5)
        
        # Scenery directory selection
        ttk.Label(file_frame, text="Custom Scenery Folder:").grid(row=1, column=0, sticky="w", pady=5)
        ttk.Entry(file_frame, textvariable=self.scenery_path, state="readonly").grid(
            row=1, column=1, sticky="ew", padx=(5, 5))
        ttk.Button(file_frame, text="Browse...", 
                  command=self._select_scenery).grid(row=1, column=2, padx=5)
        
        # Dry run checkbox
        ttk.Checkbutton(file_frame, text="Dry Run (preview only, no changes)", 
                       variable=self.dry_run_var).grid(row=2, column=0, columnspan=3, sticky="w", pady=5)
        
        # --- CONTROL BUTTONS ---
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, sticky="ew", pady=10)
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        
        ttk.Button(button_frame, text="Load Excel", command=self._load_excel).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Start Processing", command=self._start_processing, 
                  style="Accent.TButton").pack(side="left", padx=5)
        ttk.Button(button_frame, text="Clear Output", command=self._clear_output).pack(side="left", padx=5)
        
        # --- OUTPUT SECTION ---
        output_label = ttk.Label(main_frame, text="Output Log:", font=("Segoe UI", 10, "bold"))
        output_label.grid(row=3, column=0, sticky="w", pady=(10, 5))
        
        # Text widget with scrollbar
        text_frame = ttk.Frame(main_frame)
        text_frame.grid(row=4, column=0, sticky="nsew", pady=(0, 10))
        text_frame.rowconfigure(0, weight=1)
        text_frame.columnconfigure(0, weight=1)
        
        scrollbar = ttk.Scrollbar(text_frame)
        scrollbar.grid(row=0, column=1, sticky="ns")
        
        self.output_text = tk.Text(text_frame, height=20, width=80, 
                                    yscrollcommand=scrollbar.set, 
                                    font=("Courier", 9), wrap="word")
        self.output_text.grid(row=0, column=0, sticky="nsew")
        scrollbar.config(command=self.output_text.yview)
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief="sunken")
        status_bar.grid(row=5, column=0, sticky="ew", pady=(5, 0))
    
    def _select_excel(self):
        """Select Excel file"""
        path = filedialog.askopenfilename(
            title="Select Airport Excel File",
            filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")]
        )
        if path:
            self.excel_path.set(path)
    
    def _select_scenery(self):
        """Select scenery directory"""
        path = filedialog.askdirectory(title="Select Custom Scenery Folder")
        if path:
            self.scenery_path.set(path)
    
    def _log(self, message):
        """Add message to output"""
        self.output_text.insert("end", message)
        self.output_text.see("end")
        self.output_text.update()
    
    def _clear_output(self):
        """Clear output text"""
        self.output_text.delete("1.0", "end")
    
    def _load_excel(self):
        """Load Excel file"""
        if not self.excel_path.get():
            messagebox.showwarning("Warning", "Please select an Excel file first")
            return
        
        self._clear_output()
        self.status_var.set("Loading Excel...")
        self.root.update()
        
        self.airport_map = load_airport_map_xlsx(self.excel_path.get(), self._log)
        
        if self.airport_map:
            self.status_var.set(f"Ready - {len(self.airport_map)} airports loaded")
        else:
            self.status_var.set("Error loading Excel")
            messagebox.showerror("Error", "Failed to load Excel file")
    
    def _start_processing(self):
        """Start processing in background thread"""
        if not self.excel_path.get():
            messagebox.showwarning("Warning", "Please select an Excel file")
            return
        
        if not self.scenery_path.get():
            messagebox.showwarning("Warning", "Please select a Custom Scenery folder")
            return
        
        if not self.airport_map:
            messagebox.showwarning("Warning", "Please load the Excel file first")
            return
        
        self.is_processing = True
        self._clear_output()
        self.status_var.set("Processing...")
        
        # Run in background thread to keep GUI responsive
        thread = threading.Thread(target=self._process_thread, daemon=True)
        thread.start()
    
    def _process_thread(self):
        """Background thread for processing"""
        try:
            dry_run = self.dry_run_var.get()
            mode = "DRY RUN (Preview Only)" if dry_run else "LIVE (Making Changes)"
            self._log(f"\n{'='*60}\n")
            self._log(f"MODE: {mode}\n")
            self._log(f"{'='*60}\n\n")
            
            stats = scan_and_process(
                self.scenery_path.get(),
                self.airport_map,
                dry_run=dry_run,
                log_fn=self._log
            )
            
            self.status_var.set(f"Complete - {stats['changed']} updated, {stats['skipped']} skipped")
            
        except Exception as e:
            self._log(f"\n✗ ERROR: {str(e)}\n")
            self.status_var.set("Error occurred")
        finally:
            self.is_processing = False


def main():
    root = tk.Tk()
    app = AptCorrectorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
