# Создаём файлы разного размера для теста
sizes = {
    "tiny.txt": 100,              # 100 байт
    "small.txt": 2048,            # 2 КБ
    "medium.bin": 100_000,        # ~98 КБ
    "large.bin": 5_000_000,       # ~5 МБ
    "huge.bin": 50_000_000,       # ~48 МБ
    "empty.txt": 0,               # 0 байт
}

for name, size in sizes.items():
    with open(name, "wb") as f:
        f.write(b"\0" * size)
    print(f"Создан: {name} ({size} байт)")