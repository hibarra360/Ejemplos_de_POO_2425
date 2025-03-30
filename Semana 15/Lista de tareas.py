import tkinter as tk
from tkinter import ttk, messagebox

class Tarea:
    def __init__(self, texto):
        self.texto = texto
        self.completada = False

class ListaTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")

        self.tareas = []

        self.tarea_entry = ttk.Entry(self.root)
        self.tarea_entry.pack(padx=10, pady=5, fill=tk.X)
        self.tarea_entry.bind("<Return>", self.agregar_tarea_enter)

        self.botones_frame = ttk.Frame(self.root)
        self.botones_frame.pack(pady=5)

        self.agregar_button = ttk.Button(self.botones_frame, text="Añadir Tarea", command=self.agregar_tarea)
        self.agregar_button.pack(side=tk.LEFT, padx=5)

        self.completar_button = ttk.Button(self.botones_frame, text="Marcar como Completada", command=self.marcar_completada)
        self.completar_button.pack(side=tk.LEFT, padx=5)

        self.eliminar_button = ttk.Button(self.botones_frame, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.eliminar_button.pack(side=tk.LEFT, padx=5)

        self.tareas_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.tareas_listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.actualizar_lista()

        # Evento opcional: doble clic para marcar como completada
        self.tareas_listbox.bind("<Double-Button-1>", self.marcar_completada_doble_click)

    def agregar_tarea(self):
        texto_tarea = self.tarea_entry.get().strip()
        if texto_tarea:
            nueva_tarea = Tarea(texto_tarea)
            self.tareas.append(nueva_tarea)
            self.actualizar_lista()
            self.tarea_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Por favor, introduce una tarea.")

    def agregar_tarea_enter(self, event):
        self.agregar_tarea()

    def marcar_completada(self):
        seleccion = self.tareas_listbox.curselection()
        if seleccion:
            indice = seleccion[0]
            if 0 <= indice < len(self.tareas):
                self.tareas[indice].completada = not self.tareas[indice].completada
                self.actualizar_lista()

    def marcar_completada_doble_click(self, event):
        self.marcar_completada()

    def eliminar_tarea(self):
        seleccion = self.tareas_listbox.curselection()
        if seleccion:
            indice = seleccion[0]
            if messagebox.askyesno("Confirmar", "¿Seguro que quieres eliminar esta tarea?"):
                del self.tareas[indice]
                self.actualizar_lista()

    def actualizar_lista(self):
        self.tareas_listbox.delete(0, tk.END)
        for tarea in self.tareas:
            estado = "[Completada]" if tarea.completada else "[Pendiente]"
            self.tareas_listbox.insert(tk.END, f"{tarea.texto} {estado}")
            if tarea.completada:
                self.tareas_listbox.itemconfig(tk.END, fg="gray")
            else:
                self.tareas_listbox.itemconfig(tk.END, fg="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaTareasApp(root)
    root.mainloop()