import sys
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізація colorama для підтримки Windows та автоматичного скидання кольорів
init(autoreset=True)

# Додано -> None, оскільки функція тільки друкує в консоль
def visualize_directory_structure(path: Path, indent: str = "") -> None:
    """
    Рекурсивно обходить директорію та виводить її структуру з кольоровим маркуванням.
    """
    try:
        # Анотація для списку елементів (необов'язково, але корисно)
        items: list[Path] = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
        
        for i, item in enumerate(items):
            # Визначаємо, чи це останній елемент у списку
            is_last: bool = (i == len(items) - 1)
            symbol: str = "┗ " if is_last else "┣ "
            next_indent: str = indent + ("  " if is_last else "┃ ")

            if item.is_dir():
                # Виводимо папку синім кольором
                print(f"{indent}{symbol}📂 {Fore.BLUE}{item.name}{Style.RESET_ALL}")
                # Рекурсивно заходимо всередину папки
                visualize_directory_structure(item, next_indent)
            else:
                # Виводимо файл зеленим кольором
                print(f"{indent}{symbol}📜 {Fore.GREEN}{item.name}{Style.RESET_ALL}")
                
    except PermissionError:
        print(f"{indent}┗ {Fore.RED}[Відмовлено в доступі]{Style.RESET_ALL}")

# Додано -> None
def main() -> None:
    # Перевіряємо, чи передано аргумент шляху
    if len(sys.argv) < 2:
        print(f"{Fore.YELLOW}Використання: python hw03.py /шлях/до/директорії{Style.RESET_ALL}")
        return

    # Отримуємо шлях з аргументів командного рядка
    input_path: Path = Path(sys.argv[1])

    # Перевірка на існування та чи є це директорією
    if not input_path.exists():
        print(f"{Fore.RED}Помилка: Шлях '{input_path}' не існує.{Style.RESET_ALL}")
        return
    
    if not input_path.is_dir():
        print(f"{Fore.RED}Помилка: Шлях '{input_path}' не є директорією.{Style.RESET_ALL}")
        return

    # Початок виводу
    print(f"📦 {Fore.CYAN}{input_path.name}{Style.RESET_ALL}")
    visualize_directory_structure(input_path)

if __name__ == "__main__":
    main()
