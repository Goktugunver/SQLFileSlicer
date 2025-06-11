import os
from tkinter import Tk, filedialog

def split_sql_file(input_file, chunk_size_mb=50):
    # Klasör seçtir
    root = Tk()
    root.withdraw()  # GUI pencereyi gizle
    output_dir = filedialog.askdirectory(title="Lütfen kayıt edilecek klasörü seçin")
    if not output_dir:
        print("Klasör seçilmedi, işlem iptal edildi.")
        return

    chunk_size = chunk_size_mb * 1024 * 1024
    file_count = 1
    current_size = 0
    output_path = os.path.join(output_dir, f"part_{file_count}.sql")
    output_file = open(output_path, "w", encoding="utf-8")

    with open(input_file, "r", encoding="utf-8") as infile:
        for line in infile:
            current_size += len(line.encode("utf-8"))
            if current_size >= chunk_size:
                output_file.close()
                file_count += 1
                current_size = len(line.encode("utf-8"))
                output_path = os.path.join(output_dir, f"part_{file_count}.sql")
                output_file = open(output_path, "w", encoding="utf-8")
            output_file.write(line)

    output_file.close()
    print(f"{file_count} adet dosya oluşturuldu ve '{output_dir}' klasörüne kaydedildi.")

# Örnek çağrı
split_sql_file("/Users/goktugunver/Downloads/ihopecom_yake-new.sql", chunk_size_mb=120)
