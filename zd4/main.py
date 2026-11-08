import os
import zipfile
from datetime import datetime


def make_reserve_arc(source, dest):
    """Создаёт резервный архив каталога source в каталоге dest.
    
    Имя архива содержит дату и время с точностью до секунды.
    """
    # Проверяем, что source — существующий каталог
    if not os.path.isdir(source):
        print(f"Ошибка: {source} — не каталог или не существует")
        return
    
    # Создаём папку dest, если её нет
    os.makedirs(dest, exist_ok=True)
    
    # Получаем имя исходной папки
    source_name = os.path.basename(os.path.normpath(source))
    
    # Формируем имя архива с датой и временем до секунды
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    archive_name = f"{source_name}_{timestamp}.zip"
    archive_path = os.path.join(dest, archive_name)
    
    # Создаём ZIP-архив
    with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(source):
            for file in files:
                full_path = os.path.join(root, file)
                arcname = os.path.relpath(full_path, source)
                zf.write(full_path, arcname)
    
    print(f"Архив создан: {archive_path}")
    return archive_path


if __name__ == "__main__":
    source = "source_folder"
    dest = "backups"
    make_reserve_arc(source, dest)