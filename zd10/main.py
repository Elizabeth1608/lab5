import argparse


def format_text_block(frame_height, frame_width, file_name):
    """Форматирует текст из файла в блок заданного размера."""
    try:
        with open(file_name, "r", encoding="utf-8-sig") as f:
            text = f.read()
    except Exception as e:
        return f"{type(e).__name__}: {e}"
    
    result_lines = []
    
    for line in text.split("\n"):
        line = line.rstrip("\r")  
        if not line.strip():
            continue
        
        # Разбиваем по символам
        while line:
            result_lines.append(line[:frame_width])
            line = line[frame_width:]
    
    result_lines = result_lines[:frame_height]
    return "\n".join(result_lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--frame-height", type=int, default=10)
    parser.add_argument("--frame-width", type=int, default=30)
    parser.add_argument("file_name")
    args = parser.parse_args()
    
    print(format_text_block(args.frame_height, args.frame_width, args.file_name))


if __name__ == "__main__":
    main()