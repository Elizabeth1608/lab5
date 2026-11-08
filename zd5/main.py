import schedule
import time
from datetime import datetime


def ku():
    """Выводит 'Ку' столько раз, сколько сейчас часов (1-12)."""
    hour = datetime.now().hour
    
    # Преобразуем в 12-часовой формат (1-12)
    hour_12 = hour % 12
    if hour_12 == 0:
        hour_12 = 12
    
    # Выводим "Ку" нужное количество раз
    result = " ".join(["Ку"] * hour_12)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {result}")


def main():
    # 1. Вызываем функцию сразу при запуске (для проверки)
    print("Тестовый вызов функции:")
    ku()
    
    # 2. Планируем задачу: каждый час в 00 минут
    schedule.every().hour.at(":00").do(ku)
    
    print("\nПрограмма запущена. Задача выполнится каждый час в :00")
    print("Для остановки нажмите Ctrl+C\n")
    
    # Бесконечный цикл проверки расписания
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()