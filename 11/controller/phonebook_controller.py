from model.exceptions import PhoneBookError, ContactNotFoundError
from view.console_view import ConsoleView


class PhoneBookController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        """Запускает основной цикл программы"""
        print("Добро пожаловать в телефонный справочник!")

        while True:
            self.view.show_menu()
            choice = self.view.get_user_choice()

            try:
                if choice == "1":
                    contacts = self.model.get_all()
                    self.view.show_contacts(contacts)

                elif choice == "2":
                    name, phone, comment = self.view.get_contact_input()
                    contact = self.model.add(name, phone, comment)
                    self.view.show_message(f"Контакт добавлен: {contact}")

                elif choice == "3":
                    query = self.view.get_search_query()
                    results = self.model.search(query)
                    self.view.show_message(f"Найдено {len(results)} контактов:")
                    self.view.show_contacts(results)

                elif choice == "4":
                    contact_id = self.view.get_contact_id()
                    contact = self.model.edit(contact_id, *self.view.get_edit_input(contact_id))
                    self.view.show_message(f"Контакт обновлен: {contact}")

                elif choice == "5":
                    contact_id = self.view.get_contact_id()
                    self.model.delete(contact_id)
                    self.view.show_message("Контакт удален")

                elif choice == "6":
                    self.view.show_message("Выход из программы")
                    break

                else:
                    self.view.show_message("Некорректный выбор. Пожалуйста, введите число от 1 до 6.")

            except PhoneBookError as e:
                self.view.show_message(f"Ошибка: {str(e)}")