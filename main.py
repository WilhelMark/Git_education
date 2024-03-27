# main.py

import tkinter as tk
from gui import PhonebookGUI # Модуль для создания графического интерфейса.
from data_handler import PhonebookDataHandler # Модуль для работы с данными (CRUD операции)

def main():
    root = tk.Tk()
    root.title("Phonebook App")

    data_handler = PhonebookDataHandler()
    gui = PhonebookGUI(root, data_handler)

    gui.pack()
    root.mainloop()

if __name__ == "__main__":
    main()
