import argparse


def main():
    # Создаём парсер без description
    parser = argparse.ArgumentParser()
    
    parser.add_argument("args", nargs="*", help="Позиционные аргументы")
    
    parsed = parser.parse_args()
    
    # Если нет аргументов выводим "no args"
    if not parsed.args:
        print("no args")
    else:
        for arg in parsed.args:
            print(arg)


if __name__ == "__main__":
    main()