import tkinter as tk
from tkinter import filedialog
import os
import pdfToMp3Convert as convert

# Create a function to handle the file selection
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        if file_path.endswith(".pdf"):
            selected_file.set(file_path)
            convert.convertPdfToMp3(selected_file.get())
        else:
            selected_file.set("Selected file is not a PDF")
    else:
        selected_file.set("No file selected")

# Create the main window
root = tk.Tk()
root.title("PDF File Selector")

# Create a StringVar to store the selected file path
selected_file = tk.StringVar()

# Create a label to display the selected file path
file_label = tk.Label(root, textvariable=selected_file)
file_label.pack()

# Create a button to open the file dialog
select_button = tk.Button(root, text="Select PDF File", command=select_file)
select_button.pack()

# Start the main event loop
root.mainloop()
