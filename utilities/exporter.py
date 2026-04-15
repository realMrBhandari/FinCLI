import csv
from tkinter import Tk, filedialog


def get_save_file_path(default_name="export.csv"):
    root = Tk()
    root.withdraw()

    file_path = filedialog.asksaveasfilename(
        defaultextension=".csv",
        initialfile=default_name,
        filetypes=[("CSV files", "*.csv")],
        title="Save File",
    )

    root.destroy()
    return file_path


def export_to_csv(data, headers, default_name="export.csv"):
    file_path = get_save_file_path(default_name)

    if not file_path:
        return False  # user cancelled

    with open(file_path, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)
        writer.writerows(data)

    return True
