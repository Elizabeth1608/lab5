import os
import zipfile

# Создаём ZIP-архив с тестовой структурой
with zipfile.ZipFile("test.zip", "w") as zf:
    # Файлы в корне
    zf.writestr("1", "0" * 100)          # 100 байт
    zf.writestr("2", "0" * 2048)         # 2 КБ
    zf.writestr("3", "0" * 1024)         # 1 КБ
    
    # Папка "files"
    zf.writestr("files/", "")             # маркер папки
    zf.writestr("files/123.txt", "0" * 25600)  # 25 КБ
    
    # Папка "libs"
    zf.writestr("libs/", "")
    zf.writestr("libs/4", "0" * 500)      # 500 байт

print("Архив test.zip создан!")
print(f"Файлов в архиве: {len(zipfile.ZipFile('test.zip').namelist())}")