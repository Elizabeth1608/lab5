import zipfile


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


def print_zip_structure(zip_path):
    """Выводит структуру ZIP-архива с отступами и размерами."""
    with zipfile.ZipFile(zip_path, "r") as zf:
        for item in zf.infolist():
            name = item.filename.rstrip("/")
            if not name:
                continue
            
            level = name.count("/")
            indent = "  " * level
            file_name = name.split("/")[-1]
            
            if item.filename.endswith("/"):
                print(f"{indent}{file_name}")
            else:
                print(f"{indent}{file_name} {get_readable_size(item.file_size)}")

print_zip_structure("test.zip")