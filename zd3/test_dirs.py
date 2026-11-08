import os

base = "test_dir"
os.makedirs(base, exist_ok=True)

# Создаем папки разного размера
sizes = {
    "folder_1KB": 1_000,
    "folder_10KB": 10_000,
    "folder_100KB": 100_000,
    "folder_500KB": 500_000,
    "folder_1MB": 1_000_000,
    "folder_5MB": 5_000_000,
    "folder_10MB": 10_000_000,
    "folder_20MB": 20_000_000,
    "folder_50MB": 50_000_000,
}

for name, size in sizes.items():
    path = os.path.join(base, name)
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, "data.bin"), "wb") as f:
        f.write(b"\0" * size)

print("Тестовая папка test_dir создана!")