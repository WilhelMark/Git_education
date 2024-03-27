class PhonebookDataStorage:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        # Добавление нового контакта
        self.contacts.append(contact)

    def delete_contact(self, contact_id):
        # Удаление контакта по ID
        for contact in self.contacts:
            if contact.get("id") == contact_id:
                self.contacts.remove(contact)
                break

    def get_all_contacts(self):
        # Получение всех контактов
        return self.contacts

    def update_contact(self, contact_id, updated_contact):
        # Обновление контакта по ID
        for contact in self.contacts:
            if contact.get("id") == contact_id:
                contact.update(updated_contact)
                break

    def merge_contacts(self, contact1, contact2):
        # Слияние двух контактов
        merged_contact = {**contact1, **contact2}
        return merged_contact
