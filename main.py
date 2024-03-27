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

    # Создание файла "contacts.txt" по умолчанию, если он отсутствует
    create_default_contacts_file()

    # Загрузка контактов из файла при запуске программы
    imported_contacts = import_export_manager.import_contacts("contacts.txt")
    if imported_contacts is not None:
        for contact in imported_contacts:
            data_handler.add_contact(contact)

    # Обновление списка контактов в GUI
    update_contact_list(gui, data_handler)

    root.config(menu=gui.menu_bar)  # Добавление меню в графический интерфейс

    root.mainloop()

def create_default_contacts_file():
    # Создание файла "contacts.txt" по умолчанию, если он отсутствует
    try:
        with open("contacts.txt", "x"):
            pass
    except FileExistsError:
        pass

def update_contact_list(gui, data_handler):
    # Обновление списка контактов в GUI
    gui.contact_listbox.delete(0, tk.END)
    contacts = data_handler.get_all_contacts()
    for contact in contacts:
        gui.contact_listbox.insert(tk.END, contact)

if __name__ == "__main__":
    main()
