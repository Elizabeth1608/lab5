import sys


def main():
    # sys.argv[0] - имя скрипта
    # sys.argv[1:] - аргументы
    args = sys.argv[1:]
    
    # Флаг сортировки
    do_sort = "--sort" in args
    
    # Убираем --sort из списка аргументов
    args = [a for a in args if a != "--sort"]
    
    # Разбираем "ключ=значение"
    pairs = []
    for arg in args:
        if "=" in arg:
            key, value = arg.split("=", 1)  # split по первому "="
            pairs.append((key, value))
    
    if do_sort:
        pairs.sort(key=lambda x: x[0])
    
    for key, value in pairs:
        print(f"Key: {key} Value: {value}")


if __name__ == "__main__":
    main()