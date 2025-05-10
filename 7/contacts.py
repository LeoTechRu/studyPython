import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    """Загружает контакты из файла JSON."""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_contacts(contacts):
    """Сохраняет контакты в файл JSON."""
    with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=4)

def show_all_contacts(contacts):
    """Выводит все контакты."""
    if not contacts:
        print("Телефонный справочник пуст.")
        return
    for contact in contacts:
        print(f"ID: {contact['id']}, Имя: {contact['name']}, "
              f"Телефон: {contact['phone']}, Комментарий: {contact['comment']}")

def create_contact(contacts):
    """Создает новый контакт."""
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    comment = input("Введите комментарий: ")
    new_id = max((c["id"] for c in contacts), default=0) + 1
    contacts.append({
        "id": new_id,
        "name": name,
        "phone": phone,
        "comment": comment
    })
    print("Контакт добавлен.")

def find_contact(contacts):
    """Ищет контакт по ключевому слову (имя, телефон или комментарий)."""
    query = input("Введите поисковое слово: ").lower()
    results = [c for c in contacts if any(query in str(v).lower() for v in c.values())]
    if results:
        show_all_contacts(results)
    else:
        print("Контакты не найдены.")

def edit_contact(contacts):
    """Изменяет существующий контакт."""
    try:
        contact_id = int(input("Введите ID контакта для изменения: "))
        for contact in contacts:
            if contact["id"] == contact_id:
                contact["name"] = input(f"Новое имя ({contact['name']}): ") or contact["name"]
                contact["phone"] = input(f"Новый телефон ({contact['phone']}): ") or contact["phone"]
                contact["comment"] = input(f"Новый комментарий ({contact['comment']}): ") or contact["comment"]
                print("Контакт обновлен.")
                return
        print("Контакт с таким ID не найден.")
    except ValueError:
        print("Некорректный ввод ID.")

def delete_contact(contacts):
    """Удаляет контакт по ID."""
    try:
        contact_id = int(input("Введите ID контакта для удаления: "))
        for i, contact in enumerate(contacts):
            if contact["id"] == contact_id:
                contacts.pop(i)
                print("Контакт удален.")
                return
        print("Контакт с таким ID не найден.")
    except ValueError:
        print("Некорректный ввод ID.")

def main():
    contacts = load_contacts()
    while True:
        print("\nМеню телефонного справочника:")
        print("1. Показать все контакты")
        print("2. Добавить контакт")
        print("3. Найти контакт")
        print("4. Изменить контакт")
        print("5. Удалить контакт")
        print("6. Сохранить изменения")
        print("7. Выйти")
        choice = input("Выберите действие (1-7): ")

        if choice == "1":
            show_all_contacts(contacts)
        elif choice == "2":
            create_contact(contacts)
        elif choice == "3":
            find_contact(contacts)
        elif choice == "4":
            edit_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            save_contacts(contacts)
            print("Изменения сохранены.")
        elif choice == "7":
            if input("Сохранить изменения перед выходом? (y/n): ").lower() == "y":
                save_contacts(contacts)
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()