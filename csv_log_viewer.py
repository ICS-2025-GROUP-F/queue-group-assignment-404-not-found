import tkinter as tk
from tkinter import filedialog, ttk
import csv
import os

class CSVLogViewer:
    def __init__(self, master):
        self.master = master
        self.master.title("📄 Printer Log Viewer")
        self.master.geometry("700x400")

        # Create GUI elements
        self.label = tk.Label(master, text="Select a printer log CSV file:", font=("Arial", 12))
        self.label.pack(pady=10)

        self.button = tk.Button(master, text="Open CSV File", command=self.open_file)
        self.button.pack(pady=5)

        self.tree = ttk.Treeview(master)
        self.tree.pack(expand=True, fill='both', padx=10, pady=10)

    def open_file(self):
        file_path = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Select a CSV File",
            filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*"))
        )

        if not file_path:
            return

        # Clear existing data
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.tree["columns"] = ()
        self.tree["show"] = "headings"

        # Load and display CSV
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            headers = next(reader)
            self.tree["columns"] = headers

            for col in headers:
                self.tree.heading(col, text=col)
                self.tree.column(col, anchor=tk.CENTER, width=120)

            for row in reader:
                self.tree.insert("", "end", values=row)

        self.label.config(text=f"📂 Viewing: {os.path.basename(file_path)}")


# Run the viewer
if __name__ == "__main__":
    root = tk.Tk()
    viewer = CSVLogViewer(root)
    root.mainloop()
