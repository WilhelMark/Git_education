import tkinter as tk
from gui import PhonebookGUI 
from data_handler import PhonebookDataHandler 

def main():
    root = tk.Tk()
    root.title("Телефонный справочник")

    data_handler = PhonebookDataHandler()
    gui = PhonebookGUI(root, data_handler)

    gui.pack()
    root.mainloop()

if __name__ == "__main__":
    main()
