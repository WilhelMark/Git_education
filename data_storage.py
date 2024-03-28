import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
                                id INTEGER PRIMARY KEY,
                                name TEXT,
                                phone_number TEXT,
                                email TEXT,
                                job_title TEXT,
                                company TEXT
                                )''')
        self.connection.commit()

    def add_contact(self, contact):
        self.cursor.execute('''INSERT INTO contacts (name, phone_number, email, job_title, company)
                               VALUES (?, ?, ?, ?, ?)''', (contact['name'], contact['phone_number'], contact['email'], contact['job_title'], contact['company']))
        self.connection.commit()

    def get_all_contacts(self):
        self.cursor.execute('''SELECT * FROM contacts''')
        return self.cursor.fetchall()

    def delete_contact(self, contact_id):
        self.cursor.execute('''DELETE FROM contacts WHERE id = ?''', (contact_id,))
        self.connection.commit()

    def update_contact(self, contact_id, updated_contact):
        self.cursor.execute('''UPDATE contacts SET name = ?, phone_number = ?, email = ?, job_title = ?, company = ?
                               WHERE id = ?''', (updated_contact['name'], updated_contact['phone_number'], updated_contact['email'], updated_contact['job_title'], updated_contact['company'], contact_id))
        self.connection.commit()

    def save_contacts(self, contacts):
        for contact in contacts:
            self.add_contact(contact)

    def close_connection(self):
        self.connection.close()