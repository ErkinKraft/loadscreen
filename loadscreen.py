import time
import sys

def loading_screen(duration, start=0, end=100, message="Загрузка"):
    # Проверяем входные параметры на корректность
    if not (0 <= start <= 100) or not (0 <= end <= 100) or start > end:
        raise ValueError("Неправильные параметры start и end")

    if not (0 < duration < 100):
        raise ValueError("Продолжительность должна быть в диапазоне (0, 100)")

    # Вычисляем шаг
    step = (end - start) / duration

    for i in range(start, end + 1):
        sys.stdout.write(f"\r{message}... [{i}%]")
        sys.stdout.flush()
        time.sleep(0.1 / step)

    sys.stdout.write("\n")

if __name__ == "__main__":
    # Пример использования библиотеки
    loading_screen(duration=5, start=0, end=50, message="Инициализация")