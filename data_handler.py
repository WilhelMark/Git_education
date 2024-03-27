from data_storage import PhonebookDataStorage

class PhonebookDataHandler:
    def __init__(self):
        self.data_storage = PhonebookDataStorage()

    def add_contact(self, contact):
        # Добавление нового контакта
        self.data_storage.add_contact(contact)

    def delete_contact(self, contact_id):
        # Удаление контакта
        self.data_storage.delete_contact(contact_id)

    def get_all_contacts(self):
        # Получение всех контактов
        return self.data_storage.get_all_contacts()

    def update_contact(self, contact_id, updated_contact):
        # Обновление контакта
        self.data_storage.update_contact(contact_id, updated_contact)

    def merge_contacts(self, contact1, contact2):
        # Слияние двух контактов
        return self.data_storage.merge_contacts(contact1, contact2)
