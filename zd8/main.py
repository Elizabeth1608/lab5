import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("params", nargs="*", help="Параметры для сложения")
    
    args = parser.parse_args()
    params = args.params
    
    try:
        # Проверка количества параметров
        if len(params) == 0:
            print("NO PARAMS")
            return
        if len(params) == 1:
            print("TOO FEW PARAMS")
            return
        if len(params) > 2:
            print("TOO MANY PARAMS")
            return
        
        a = int(params[0])
        b = int(params[1])
        
        print(a + b)
    
    except Exception as e:
         print(type(e).__name__)


if __name__ == "__main__":
    main()