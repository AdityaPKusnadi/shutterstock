import os
import pandas as pd
from datetime import datetime
from tkinter import Tk, Label, Button, Entry, filedialog, messagebox, OptionMenu, StringVar, Checkbutton, IntVar

# Variabel global untuk menyimpan data CSV
data = []
valid_extensions = ['.jpg', '.png', '.mp4', '.avi', '.mov']
columns = ['filename', 'title', 'description', 'keywords', 'Editorial', 'Mature Content', 'Illustration', 'Categories']

# Daftar kategori
categories = [
    "Abstract", "Animals/Wildlife", "Arts", "Backgrounds/Textures", "Beauty/Fashion",
    "Buildings/Landmarks", "Business/Finance", "Celebrities", "Education", "Food and Drink",
    "Healthcare/Medical", "Holidays", "Industrial", "Interiors", "Miscellaneous",
    "Nature", "Objects", "Parks/Outdoor", "People", "Religion", "Science",
    "Signs/Symbols", "Sports/Recreation", "Technology", "Transportation", "Vintage"
]

# Fungsi untuk memilih folder
def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_entry.delete(0, 'end')
        folder_entry.insert(0, folder_selected)

# Fungsi untuk generate CSV
def generate_csv():
    root_directory = folder_entry.get()
    category = category_var.get()
    description = description_entry.get()
    keywords = keywords_entry.get()
    editorial_value = 'Yes' if editorial_var.get() == 1 else 'No'
    mature_content_value = 'Yes' if mature_content_var.get() == 1 else 'No'
    editorial_date = datetime.now().strftime('%Y-%m-%d')

    if not root_directory or not category or not description or not keywords:
        messagebox.showwarning("Input Error", "Semua field harus diisi!")
        return

    for folder_name in os.listdir(root_directory):
        folder_path = os.path.join(root_directory, folder_name)

        if os.path.isdir(folder_path):
            print(f"Memproses folder: {folder_name}")
            for filename in os.listdir(folder_path):
                if any(filename.lower().endswith(ext) for ext in valid_extensions):
                    print(f"File ditemukan: {filename}")
                    title = f"{category} in Japan"
                    full_description = f"{description}. This image shows {folder_name} in Japan, taken on {editorial_date}."
                    mature_content = mature_content_value
                    illustration = 'No'
                    
                    # Append data
                    data.append([filename, title, full_description, keywords, editorial_value, mature_content, illustration, category])

    # Cek apakah ada data yang ditambahkan
    if data:
        # Buat CSV
        df = pd.DataFrame(data, columns=columns)
        csv_path = os.path.join(os.getcwd(), 'shutterstock_metadata_gui_dynamic.csv')
        df.to_csv(csv_path, index=False)
        messagebox.showinfo("Success", f"CSV berhasil dibuat di: {csv_path}")
    else:
        messagebox.showwarning("No Files", "Tidak ada file gambar atau video yang ditemukan di folder yang dipilih.")

# GUI Setup
root = Tk()
root.title("Shutterstock Metadata Generator")

# Setting UI
Label(root, text="Folder Utama").grid(row=0, column=0, padx=10, pady=5)
folder_entry = Entry(root, width=50)
folder_entry.grid(row=0, column=1, padx=10, pady=5)
Button(root, text="Browse", command=browse_folder).grid(row=0, column=2, padx=10, pady=5)

Label(root, text="Kategori").grid(row=1, column=0, padx=10, pady=5)
category_var = StringVar(root)
category_var.set(categories[0])  # default value
OptionMenu(root, category_var, *categories).grid(row=1, column=1, padx=10, pady=5)

Label(root, text="Deskripsi").grid(row=2, column=0, padx=10, pady=5)
description_entry = Entry(root, width=50)
description_entry.grid(row=2, column=1, padx=10, pady=5)

Label(root, text="Kata Kunci").grid(row=3, column=0, padx=10, pady=5)
keywords_entry = Entry(root, width=50)
keywords_entry.grid(row=3, column=1, padx=10, pady=5)

# Editorial Checkbox
editorial_var = IntVar()
Checkbutton(root, text="Editorial", variable=editorial_var).grid(row=4, column=1, sticky='W', padx=10, pady=5)

# Mature Content Checkbox
mature_content_var = IntVar()
Checkbutton(root, text="Mature Content", variable=mature_content_var).grid(row=5, column=1, sticky='W', padx=10, pady=5)

# Button to generate CSV
Button(root, text="Generate CSV", command=generate_csv).grid(row=6, column=1, padx=10, pady=20)

root.mainloop()
