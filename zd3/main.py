import os


def get_readable_size(size_bytes):
    """Переводит байты в человекочитаемый вид (КБ, МБ...)."""
    if size_bytes == 0:
        return "0Б"
    
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    i = 0
    while size_bytes > 1023 and i < 4:
        size_bytes /= 1023
        i += 1
        
    return f"{round(size_bytes)}{units[i]}"


def get_dir_size(path):
    """Считает суммарный размер всех файлов в папке (рекурсивно)."""
    total = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            total += os.path.getsize(os.path.join(root, file))
    return total


def main():
    target = "test_dir" 
    
    # Получаем список подпапок и их размеры
    dirs = []
    for name in os.listdir(target):
        full_path = os.path.join(target, name)
        if os.path.isdir(full_path):
            size = get_dir_size(full_path)
            dirs.append((name, size))
    
    # Сортируем по убыванию размера 
    dirs.sort(key=lambda x: x[1], reverse=True)
    
    for name, size in dirs[:10]:
        print(f"{name} - {get_readable_size(size)}")


if __name__ == "__main__":
    main()