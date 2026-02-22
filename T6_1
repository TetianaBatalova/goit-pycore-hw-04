from pathlib import Path


def total_salary(path: str) -> tuple[int, int]:
    """
    Аналізує текстовий файл із зарплатами та повертає загальну та середню суму.
    
    Аргументи:
        path (str): Шлях до текстового файлу.
        
    Повертає:
        tuple[int, int]: Кортеж (загальна сума, середня зарплата).
    """
    total = 0
    count = 0
    
    try:
        # Створюємо об'єкт шляху та перевіряємо його
        file_path = Path(path)
        
        if not file_path.exists():
            print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
            return 0, 0

        # Відкриваємо файл 
        with open(file_path, mode="r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:  # Пропускаємо порожні рядки
                    continue
                
                try:
                    # Розділяємо рядок за комою
                    name, salary = line.split(",")
                    total += int(salary)
                    count += 1
                except ValueError:
                    print(f"Попередження: Некоректний формат даних у рядку: '{line}'")
                    continue

        # Розрахунок середньої зарплати 
        average = total // count if count > 0 else 0
        
        return total, average

    except Exception as e:
        print(f"Сталася непередбачувана помилка: {e}")
        return 0, 0


if __name__ == "__main__":
    # --- Тестування ---
    
    # 1. Файл для демонстрації
    test_filename = "salary_file.txt"
    with open(test_filename, "w", encoding="utf-8") as f:
        f.write("Alex Korp,3000\n")
        f.write("Nikita Borisenko,2000\n")
        f.write("Sitarama Raju,1000\n")

    # 2. Викликаємо функцію
    total, average = total_salary(test_filename)
    
    # 3. Виводимо результат
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

  
