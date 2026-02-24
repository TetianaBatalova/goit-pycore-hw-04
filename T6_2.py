from pathlib import Path


def get_cats_info(path: str) -> list[dict[str, str]]:
    """
    Читає текстовий файл із даними про котів і повертає список словників.

    Аргументи:
        path (str): Шлях до файлу.

    Повертає:
        list[dict[str, str]]: Список словників з ключами id, name, age.
    """
    cats_list = []

    try:
        file_path = Path(path)

        # Перевіряємо, чи існує файл
        if not file_path.exists():
            print(f"Помилка: Файл '{path}' не знайдено.")
            return []

        # Відкриваємо файл для читання
        with open(file_path, mode="r", encoding="utf-8") as file:
            for line in file:
                # Очищуємо рядок від зайвих пробілів та переносу \n
                line = line.strip()
                if not line:
                    continue

                try:
                    # Розділяємо дані по комі
                    cat_id, name, age = line.split(",")

                    # Створюємо словник для поточного кота
                    cat_dict = {
                        "id": cat_id,
                        "name": name,
                        "age": age
                    }

                    # Додаємо словник до загального списку
                    cats_list.append(cat_dict)

                except ValueError:
                    print(f"Попередження: Некоректний формат рядка: '{line}'")
                    continue

        return cats_list

    except Exception as e:
        print(f"Сталася помилка при обробці файлу: {e}")
        return []


if __name__ == "__main__":
    # Тестовий блок
    filename = "cats_file.txt"

    # Створюємо тестовий файл
    content = (
        "60b90c1c13067a15887e1ae1,Tayson,3\n"
        "60b90c2413067a15887e1ae2,Vika,1\n"
        "60b90c2e13067a15887e1ae3,Barsik,2\n"
        "60b90c3b13067a15887e1ae4,Simon,12\n"
        "60b90c4613067a15887e1ae5,Tessi,5"
    )

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    # Виклик функції
    cats_info = get_cats_info(filename)

    # Вивід результату
    import pprint
    pprint.pprint(cats_info, sort_dicts=False)
