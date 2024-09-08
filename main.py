import os
import pandas as pd
from datetime import datetime

# Direktori utama yang berisikan folder dengan gambar dan video
root_directory = 'C:\\Users\\adity\\Documents\\Foto'

# Template CSV sesuai format Shutterstock
columns = ['filename', 'title', 'description', 'keywords', 'Editorial', 'Mature Content', 'Illustration', 'Categories']
data = []

# Ekstensi file yang ingin diambil (gambar dan video)
valid_extensions = ['.jpg', '.png', '.mp4', '.avi', '.mov']

# Tanggal editorial yang akan digunakan dalam deskripsi
editorial_date = datetime.now().strftime('%Y-%m-%d')

# Loop melalui setiap folder di dalam root_directory
for folder_name in os.listdir(root_directory):
    folder_path = os.path.join(root_directory, folder_name)
    
    if os.path.isdir(folder_path):
        # Loop melalui setiap file di dalam folder
        for filename in os.listdir(folder_path):
            if any(filename.endswith(ext) for ext in valid_extensions):
                # Extract nama file tanpa ekstensi untuk title dan description
                name = os.path.splitext(filename)[0]
                
                # Buat title, description, dan keywords berdasarkan nama folder
                title = f"{folder_name.capitalize()} in Japan"
                description = f"Editorial use only. This image shows {folder_name} in Japan, taken on {editorial_date}."
                keywords = f'{folder_name}, Japan, editorial, {folder_name} in Japan'
                editorial = 'Yes'
                mature_content = 'No'
                illustration = 'No'
                categories = folder_name.capitalize()
                
                # Tambahkan data ke list
                data.append([filename, title, description, keywords, editorial, mature_content, illustration, categories])

# Buat DataFrame dan simpan ke CSV
df = pd.DataFrame(data, columns=columns)
df.to_csv('shutterstock_metadata.csv', index=False)

print("CSV berhasil dibuat dan diisi secara otomatis.")
