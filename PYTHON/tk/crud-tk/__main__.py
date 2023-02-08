import tkinter as tk

class CRUDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CRUD Application")

        self.label = tk.Label(text="Lista de elementos")
        self.label.pack()

        self.listbox = tk.Listbox()
        self.listbox.pack()

        self.create_button = tk.Button(text="Crear", command=self.create)
        self.create_button.pack()

        self.read_button = tk.Button(text="Leer", command=self.read)
        self.read_button.pack()

        self.update_button = tk.Button(text="Actualizar", command=self.update)
        self.update_button.pack()

        self.delete_button = tk.Button(text="Borrar", command=self.delete)
        self.delete_button.pack()

    def create(self):
        # Código para crear un nuevo elemento
        pass

    def read(self):
        # Código para leer los elementos existentes
        pass

    def update(self):
        # Código para actualizar un elemento existente
        pass

    def delete(self):
        # Código para borrar un elemento existente
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = CRUDApp(root)
    root.mainloop()
