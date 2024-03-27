class ImportExportManager:
    def __init__(self):
        pass

    def export_contacts(self, filename, contacts):
        # Экспорт контактов в файл
        with open(filename, 'w') as file:
            for contact in contacts:
                file.write(f"{contact}\n")

    def import_contacts(self, filename):
        # Импорт контактов из файла
        imported_contacts = []
        with open(filename, 'r') as file:
            for line in file:
                imported_contacts.append(line.strip())
        return imported_contacts
