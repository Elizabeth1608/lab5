import argparse


def main():
    parser = argparse.ArgumentParser()
    
    # Флаг --sort
    parser.add_argument("--sort", action="store_true", help="Сортировать по ключу")
    
    # Позиционные аргументы (ключ=значение) 
    parser.add_argument("pairs", nargs="*", help="Аргументы вида ключ=значение")
    
    # Разбираем
    args = parser.parse_args()
    
    # Обрабатываем пары
    items = []
    for arg in args.pairs:
        if "=" in arg:
            key, value = arg.split("=", 1)
            items.append((key, value))
    
    if args.sort:
        items.sort(key=lambda x: x[0])
    
    for key, value in items:
        print(f"Key: {key} Value: {value}")


if __name__ == "__main__":
    main()