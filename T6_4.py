def parse_input(user_input: str) -> tuple[str, list[str]]:
    """Розбирає введений рядок на команду та аргументи."""
    if not user_input.strip():
        return "invalid", []
    
    # Використовуємо split(), cmd отримує перше слово, args — решту
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    """Додає новий контакт або перезаписує існуючий."""
    if len(args) < 2:
        return "Error: Give me name and phone please."
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    """Оновлює номер телефону для існуючого контакту."""
    if len(args) < 2:
        return "Error: Give me name and phone please."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return f"Error: Contact '{name}' not found."


def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    """Виводить номер телефону за ім'ям."""
    if len(args) < 1:
        return "Error: Enter user name."
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return f"Error: Contact '{name}' not found."


def show_all(contacts: dict[str, str]) -> str:
    """Виводить усі збережені контакти."""
    if not contacts:
        return "No contacts stored."
    
    # Створюємо список рядків для виводу
    contact_list: list[str] = [f"{name}: {phone}" for name, phone in contacts.items()]
    return "\n".join(contact_list)


def main() -> None:
    """Основний цикл управління ботом."""
    # Ініціалізуємо порожній словник з анотацією типів
    contacts: dict[str, str] = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input: str = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
