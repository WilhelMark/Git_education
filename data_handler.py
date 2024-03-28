class PhonebookDataHandler:
    def __init__(self):
        self.contacts = []

    def get_all_contacts(self):
        return self.contacts

    def add_contact(self, contact):
        self.contacts.append(contact)

    def delete_contact(self, contact_id):
        for contact in self.contacts:
            if contact.get("id") == contact_id:
                self.contacts.remove(contact)
                break

    def update_contact(self, contact_id, updated_contact):
        for contact in self.contacts:
            if contact.get("id") == contact_id:
                contact.update(updated_contact)
                break