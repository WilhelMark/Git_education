import tkinter as tk

class PhonebookGUI(tk.Frame):
    def __init__(self, master, data_handler, import_export_manager):
        super().__init__(master)
        self.master = master
        self.data_handler = data_handler
        self.import_export_manager = import_export_manager

        self.create_widgets()
        self.create_menu()  # Создание меню

    def create_widgets(self):
        # Создание элементов GUI
        self.label = tk.Label(self, text="Телефонный справочник")
        self.label.pack()

        self.contact_listbox = tk.Listbox(self)
        self.contact_listbox.pack()

        self.search_entry = tk.Entry(self)
        self.search_entry.pack()

        self.search_button = tk.Button(self, text="Поиск", command=self.search_contacts)
        self.search_button.pack()

        self.add_button = tk.Button(self, text="Добавить контакт", command=self.show_add_contact_window)
        self.add_button.pack()

        self.edit_button = tk.Button(self, text="Редактировать контакт", command=self.show_edit_contact_window)
        self.edit_button.pack()

        self.delete_button = tk.Button(self, text="Удалить контакт", command=self.delete_contact)
        self.delete_button.pack()

    def create_menu(self):
        # Создание меню
        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)

        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Экспорт контактов", command=self.export_contacts)
        file_menu.add_command(label="Импорт контактов", command=self.import_contacts)
        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=self.master.quit)

        self.menu_bar.add_cascade(label="Файл", menu=file_menu)

        contact_menu = tk.Menu(self.menu_bar, tearoff=0)
        contact_menu.add_command(label="Добавить контакт", command=self.show_add_contact_window)
        contact_menu.add_command(label="Просмотр контактов", command=self.show_contact_view_window)

        self.menu_bar.add_cascade(label="Контакты", menu=contact_menu)

    def export_contacts(self):
        # Логика экспорта контактов
        contacts = self.data_handler.get_all_contacts()
        self.import_export_manager.export_contacts("contacts.txt", contacts)

    def import_contacts(self):
        # Логика импорта контактов
        imported_contacts = self.import_export_manager.import_contacts("contacts.txt")
        for contact in imported_contacts:
            self.data_handler.add_contact(contact)
        self.update_contact_list()

    def search_contacts(self):
        # Логика поиска контактов
        search_term = self.search_entry.get()
        # Реализация логики поиска с использованием data_handler

    def show_add_contact_window(self):
        # Логика отображения окна добавления контакта
        add_window = tk.Toplevel(self.master)
        add_window.title("Добавить контакт")

        # Создание полей для ввода данных контакта
        name_label = tk.Label(add_window, text="Имя:")
        name_label.pack()
        name_entry = tk.Entry(add_window)
        name_entry.pack()

        phone_label = tk.Label(add_window, text="Номер телефона:")
        phone_label.pack()
        phone_entry = tk.Entry(add_window)
        phone_entry.pack()

        email_label = tk.Label(add_window, text="Email:")
        email_label.pack()
        email_entry = tk.Entry(add_window)
        email_entry.pack()

        job_label = tk.Label(add_window, text="Должность:")
        job_label.pack()
        job_entry = tk.Entry(add_window)
        job_entry.pack()

        company_label = tk.Label(add_window, text="Компания:")
        company_label.pack()
        company_entry = tk.Entry(add_window)
        company_entry.pack()

        save_button = tk.Button(add_window, text="Сохранить", command=lambda: self.save_contact(name_entry.get(), phone_entry.get(), email_entry.get(), job_entry.get(), company_entry.get(), add_window))
        save_button.pack()

    def show_edit_contact_window(self):
        # Логика отображения окна редактирования контакта
        selected_contact = self.contact_listbox.get(tk.ACTIVE)  # Получение выбранного контакта
        edit_window = tk.Toplevel(self.master)
        edit_window.title("Редактировать контакт")

        # Отображение данных выбранного контакта для редактирования
        name_label = tk.Label(edit_window, text="Имя:")
        name_label.pack()
        name_entry = tk.Entry(edit_window)
        name_entry.insert(0, selected_contact["name"])
        name_entry.pack()

        phone_label = tk.Label(edit_window, text="Номер телефона:")
        phone_label.pack()
        phone_entry = tk.Entry(edit_window)
        phone_entry.insert(0, selected_contact["phone_number"])
        phone_entry.pack()

        email_label = tk.Label(edit_window, text="Email:")
        email_label.pack()
        email_entry = tk.Entry(edit_window)
        email_entry.insert(0, selected_contact["email"])
        email_entry.pack()

        job_label = tk.Label(edit_window, text="Должность:")
        job_label.pack()
        job_entry = tk.Entry(edit_window)
        job_entry.insert(0, selected_contact["job_title"])
        job_entry.pack()

        company_label = tk.Label(edit_window, text="Компания:")
        company_label.pack()
        company_entry = tk.Entry(edit_window)
        company_entry.insert(0, selected_contact["company"])
        company_entry.pack()

        save_button = tk.Button(edit_window, text="Сохранить", command=lambda: self.save_edited_contact(selected_contact["id"], name_entry.get(), phone_entry.get(), email_entry.get(), job_entry.get(), company_entry.get(), edit_window))
        save_button.pack()

    def delete_contact(self):
        # Логика удаления контакта
        selected_contact = self.contact_listbox.get(tk.ACTIVE)  # Получение выбранного контакта
        contact_id = selected_contact["id"]  # Предполагается, что у контакта есть поле 'id'
        self.data_handler.delete_contact(contact_id)
        # Реализация логики удаления выбранного контакта

    def save_contact(self, name, phone_number, email, job_title, company, add_window):
        # Логика сохранения нового контакта
        new_contact = {"name": name, "phone_number": phone_number, "email": email, "job_title": job_title, "company": company}
        self.data_handler.add_contact(new_contact)
        add_window.destroy()  # Закрыть окно добавления контакта после сохранения
        # Реализация логики сохранения нового контакта

    def save_edited_contact(self, contact_id, name, phone_number, email, job_title, company, edit_window):
        # Логика сохранения отредактированного контакта
        edited_contact = {"name": name, "phone_number": phone_number, "email": email, "job_title": job_title, "company": company}
        self.data_handler.update_contact(contact_id, edited_contact)
        edit_window.destroy()  # Закрыть окно редактирования контакта после сохранения
        # Реализация логики сохранения отредактированного контакта

    def update_contact_list(self):
        # Обновление списка контактов в GUI
        self.contact_listbox.delete(0, tk.END)
        contacts = self.data_handler.get_all_contacts()
        for contact in contacts:
            self.contact_listbox.insert(tk.END, contact)