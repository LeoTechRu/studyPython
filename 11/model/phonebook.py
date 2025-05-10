import json
import os
from model.contact import Contact
from model.exceptions import FileReadError, FileWriteError, ContactNotFoundError

CONTACTS_FILE = "contacts.json"


class PhoneBook:
    def __init__(self):
        self.contacts = self._load_contacts()

    def _load_contacts(self):
        """Загружает контакты из файла JSON"""
        try:
            if os.path.exists(CONTACTS_FILE):
                with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
                    content = f.read().strip()
                    if content:
                        data = json.loads(content)
                        return [Contact.from_dict(contact) for contact in data]
            return []
        except (json.JSONDecodeError, FileNotFoundError) as e:
            raise FileReadError(f"Ошибка чтения файла: {str(e)}")

    def _save_contacts(self):
        """Сохраняет контакты в файл JSON"""
        try:
            with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
                data = [contact.to_dict() for contact in self.contacts]
                json.dump(data, f, ensure_ascii=False, indent=4)
            return True
        except IOError as e:
            raise FileWriteError(f"Ошибка записи в файл: {str(e)}")

    def get_all(self):
        """Возвращает все контакты"""
        return self.contacts

    def add(self, name, phone, comment):
        """Добавляет новый контакт"""
        if not name or not phone:
            raise InvalidContactDataError("Имя и телефон обязательны для заполнения")

        new_id = max((c.id for c in self.contacts), default=0) + 1
        contact = Contact(new_id, name, phone, comment)
        self.contacts.append(contact)
        self._save_contacts()
        return contact

    def edit(self, contact_id, name=None, phone=None, comment=None):
        """Редактирует контакт"""
        for contact in self.contacts:
            if contact.id == contact_id:
                contact.name = name.strip() if name else contact.name
                contact.phone = phone.strip() if phone else contact.phone
                contact.comment = comment.strip() if comment else contact.comment
                self._save_contacts()
                return contact
        raise ContactNotFoundError(contact_id)

    def delete(self, contact_id):
        """Удаляет контакт"""
        for i, contact in enumerate(self.contacts):
            if contact.id == contact_id:
                del self.contacts[i]
                self._save_contacts()
                return True
        raise ContactNotFoundError(contact_id)

    def search(self, query):
        """Ищет контакты по запросу"""
        query = query.lower().strip()
        return [
            contact for contact in self.contacts
            if any(query in str(value).lower() for value in contact.__dict__.values())
        ]