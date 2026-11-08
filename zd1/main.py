import os


def get_readable_size(size_bytes):
    """Переводит размер в байтах в человекочитаемый вид."""
    if size_bytes == 0:
        return "0Б"
    
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    size = size_bytes
    unit_index = 0
    
    while size > 1023 and unit_index < len(units) - 1:
        size /= 1023
        unit_index += 1
    
    return f"{round(size)}{units[unit_index]}"


def get_files_info():
    """Возвращает строку с файлами и их размерами из текущей папки."""
    lines = []
    
    for name in sorted(os.listdir(".")):
        if os.path.isfile(name):
            size = os.path.getsize(name)
            readable = get_readable_size(size)
            lines.append(f"{name} {readable}")
    
    return "\n".join(lines)


if __name__ == "__main__":
    print(get_files_info())