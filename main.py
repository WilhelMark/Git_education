import tkinter as tk
from gui import PhonebookGUI
from data_handler import PhonebookDataHandler
from import_export import ImportExportManager

def main():
    root = tk.Tk()
    root.title("Телефонный справочник")

    data_handler = PhonebookDataHandler()
    import_export_manager = ImportExportManager()
    gui = PhonebookGUI(root, data_handler, import_export_manager)

    # Загрузка контактов из файла при запуске программы (предположим, что файл contacts.txt содержит список контактов)
    imported_contacts = import_export_manager.import_contacts("contacts.txt")
    for contact in imported_contacts:
        data_handler.add_contact(contact)

    # Обновление списка контактов в GUI
    update_contact_list(gui, data_handler)

    root.mainloop()

def update_contact_list(gui, data_handler):
    # Обновление списка контактов в GUI
    gui.contact_listbox.delete(0, tk.END)
    contacts = data_handler.get_all_contacts()
    for contact in contacts:
        gui.contact_listbox.insert(tk.END, contact)

if __name__ == "__main__":
    main()
