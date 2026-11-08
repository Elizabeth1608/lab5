import os

source = "source_folder"
os.makedirs(source, exist_ok=True)

# Создаём несколько файлов с другим содержимым
files = {
    "file1.txt": "Это первый тестовый файл.",
    "file2.txt": "Содержимое второго файла.",
    "subfolder/inner.txt": "Файл внутри вложенной папки.",
    "subfolder/deep/deeper.txt": "Файл на самом дне структуры.",
}

for path, content in files.items():
    full_path = os.path.join(source, path)
    # Создаём папку, если её нет
    parent_dir = os.path.dirname(full_path)
    if parent_dir:
        os.makedirs(parent_dir, exist_ok=True)
    
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Создан тестовый каталог: {source}")
print("Файлы:")
for path in files:
    print(f"  - {path}")