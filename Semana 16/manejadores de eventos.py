import tkinter as tk
from tkinter import ttk, messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas Pendientes")

        self.tasks = []
        self.task_var = tk.StringVar(value=self.tasks)

        # Campo de entrada para nuevas tareas
        self.entry_new_task = ttk.Entry(self.root, width=40)
        self.entry_new_task.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.entry_new_task.bind("<Return>", self.add_task_keyboard)

        # Botones de acción
        self.btn_add = ttk.Button(self.root, text="Añadir Tarea", command=self.add_task)
        self.btn_add.grid(row=0, column=1, padx=5, pady=10)

        self.btn_complete = ttk.Button(self.root, text="Completar", command=self.complete_task)
        self.btn_complete.grid(row=1, column=1, padx=5, pady=5)

        self.btn_delete = ttk.Button(self.root, text="Eliminar", command=self.delete_task)
        self.btn_delete.grid(row=2, column=1, padx=5, pady=5)

        # Lista de tareas
        self.listbox_tasks = tk.Listbox(self.root, listvariable=self.task_var, selectmode=tk.SINGLE, height=10)
        self.listbox_tasks.grid(row=1, column=0, rowspan=3, padx=10, pady=5, sticky="nsew")

        # Atajos de teclado
        self.root.bind("<Escape>", self.close_app)
        self.root.bind("c", self.complete_task_keyboard)
        self.root.bind("<Delete>", self.delete_task_keyboard)
        self.root.bind("d", self.delete_task_keyboard) # Atajo alternativo para eliminar

        # Configuración de pesos para el grid (para que la lista se expanda)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(3, weight=1)

        self.update_task_list()

    def add_task(self):
        new_task = self.entry_new_task.get().strip()
        if new_task:
            self.tasks.append({"text": new_task, "completed": False})
            self.update_task_list()
            self.entry_new_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, introduce una tarea.")

    def add_task_keyboard(self, event):
        self.add_task()

    def complete_task(self):
        selected_index = self.listbox_tasks.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.update_task_list()

    def complete_task_keyboard(self, event):
        self.complete_task()

    def delete_task(self):
        selected_index = self.listbox_tasks.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.update_task_list()

    def delete_task_keyboard(self, event):
        self.delete_task()

    def update_task_list(self):
        display_tasks = []
        for task in self.tasks:
            if task["completed"]:
                display_tasks.append(f"[Completada] {task['text']}")
            else:
                display_tasks.append(task["text"])
        self.task_var.set(display_tasks)
        self._apply_visual_feedback()

    def _apply_visual_feedback(self):
        self.listbox_tasks.tag_delete("completed")
        self.listbox_tasks.tag_config("completed", foreground="gray", strikethrough=True)
        for i, task in enumerate(self.tasks):
            if task["completed"]:
                self.listbox_tasks.itemconfig(i, tags=("completed",))
            else:
                self.listbox_tasks.itemconfig(i, tags=())

    def close_app(self, event):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()