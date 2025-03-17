import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
from datetime import datetime
import csv
import json
import pickle
import os

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.filename = "agenda_eventos.pkl"  # Nombre del archivo para guardar los eventos
        self.eventos = self.cargar_eventos()  # Cargar eventos al iniciar la aplicación

        # --- Contenedores ---
        self.frame_visualizacion = ttk.LabelFrame(root, text="Eventos Programados")
        self.frame_visualizacion.pack(padx=10, pady=10, fill="both", expand=True)

        self.frame_entrada = ttk.LabelFrame(root, text="Nuevo Evento")
        self.frame_entrada.pack(padx=10, pady=5, fill="x")

        self.frame_acciones = ttk.Frame(root)
        self.frame_acciones.pack(padx=10, pady=5, fill="x")

        # --- Componentes de Visualización ---
        self.tree = ttk.Treeview(self.frame_visualizacion, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha", command=lambda: self.ordenar_eventos("Fecha"))
        self.tree.heading("Hora", text="Hora", command=lambda: self.ordenar_eventos("Hora"))
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(fill="both", expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.seleccionar_evento)

        # --- Componentes de Entrada ---
        ttk.Label(self.frame_entrada, text="Fecha (YYYY-MM-DD):").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.fecha_entry = ttk.Entry(self.frame_entrada, width=15)
        self.fecha_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.fecha_button = ttk.Button(self.frame_entrada, text="Seleccionar Fecha", command=self.abrir_calendario)
        self.fecha_button.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

        ttk.Label(self.frame_entrada, text="Hora (HH:MM):").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.hora_entry = ttk.Entry(self.frame_entrada, width=10)
        self.hora_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(self.frame_entrada, text="Descripción:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.descripcion_entry = ttk.Entry(self.frame_entrada)
        self.descripcion_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky="ew")

        # --- Botones de Acción ---
        self.agregar_button = ttk.Button(self.frame_acciones, text="Agregar Evento", command=self.agregar_evento)
        self.agregar_button.pack(side="left", padx=5, pady=5)

        self.eliminar_button = ttk.Button(self.frame_acciones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento, state="disabled")
        self.eliminar_button.pack(side="left", padx=5, pady=5)

        self.salir_button = ttk.Button(self.frame_acciones, text="Salir", command=self.cerrar_aplicacion)
        self.salir_button.pack(side="right", padx=5, pady=5)

        # --- DatePicker (Inicialmente oculto) ---
        self.calendario_ventana = None

        # --- Mostrar eventos iniciales ---
        self.actualizar_lista_eventos()

        # --- Protocolo para guardar al cerrar la ventana ---
        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_aplicacion)

    def abrir_calendario(self):
        """Abre una ventana de calendario para seleccionar la fecha."""
        if not self.calendario_ventana:
            self.calendario_ventana = tk.Toplevel(self.root)
            self.calendario_ventana.title("Seleccionar Fecha")
            self.calendario = Calendar(self.calendario_ventana, selectmode='day', date_pattern='yyyy-mm-dd')
            self.calendario.pack(padx=10, pady=10)
            ttk.Button(self.calendario_ventana, text="Aceptar", command=self.seleccionar_fecha_calendario).pack(pady=5)
            self.calendario_ventana.transient(self.root)

    def seleccionar_fecha_calendario(self):
        """Obtiene la fecha seleccionada del calendario y la coloca en el Entry."""
        self.fecha_entry.delete(0, tk.END)
        self.fecha_entry.insert(0, self.calendario.get_date())
        self.calendario_ventana.destroy()
        self.calendario_ventana = None

    def agregar_evento(self):
        """Agrega un nuevo evento a la lista y actualiza la vista."""
        fecha_str = self.fecha_entry.get()
        hora_str = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        if not all([fecha_str, hora_str, descripcion]):
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return

        # Validar formato de fecha
        try:
            datetime.strptime(fecha_str, '%Y-%m-%d')
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha inválido (YYYY-MM-DD).")
            return

        # Validar formato de hora
        try:
            datetime.strptime(hora_str, '%H:%M')
        except ValueError:
            messagebox.showerror("Error", "Formato de hora inválido (HH:MM).")
            return

        evento = {"Fecha": fecha_str, "Hora": hora_str, "Descripción": descripcion}
        self.eventos.append(evento)
        self.ordenar_eventos()  # Ordenar después de agregar
        self.actualizar_lista_eventos()

        # Limpiar los campos de entrada
        self.fecha_entry.delete(0, tk.END)
        self.hora_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)

    def actualizar_lista_eventos(self):
        """Limpia y rellena la Treeview con los eventos actuales."""
        for item in self.tree.get_children():
            self.tree.delete(item)
        for evento in self.eventos:
            self.tree.insert("", tk.END, values=(evento["Fecha"], evento["Hora"], evento["Descripción"]))

    def seleccionar_evento(self, event):
        """Habilita el botón de eliminar cuando se selecciona un evento en la lista."""
        if self.tree.selection():
            self.eliminar_button.config(state="normal")
        else:
            self.eliminar_button.config(state="disabled")

    def eliminar_evento(self):
        """Elimina el evento seleccionado de la lista y actualiza la vista."""
        seleccion = self.tree.selection()
        if not seleccion:
            return

        item_seleccionado = seleccion[0]
        indices = [self.tree.index(item) for item in self.tree.get_children()]
        indice_seleccionado = indices.index(self.tree.index(item_seleccionado))

        if messagebox.askyesno("Confirmar", "¿Seguro que desea eliminar este evento?"):
            del self.eventos[indice_seleccionado]
            self.actualizar_lista_eventos()
            self.eliminar_button.config(state="disabled")

    def ordenar_eventos(self, criterio=None):
        """Ordena la lista de eventos por fecha y luego por hora."""
        def sort_key(evento):
            return (evento['Fecha'], evento['Hora'])

        self.eventos.sort(key=sort_key)
        self.actualizar_lista_eventos()

    def guardar_eventos(self):
        """Guarda los eventos en un archivo usando pickle."""
        try:
            with open(self.filename, 'wb') as f:
                pickle.dump(self.eventos, f)
            print(f"Eventos guardados en {self.filename}")
        except Exception as e:
            messagebox.showerror("Error al guardar", f"Ocurrió un error al guardar los eventos: {e}")

    def cargar_eventos(self):
        """Carga los eventos desde el archivo pickle."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'rb') as f:
                    return pickle.load(f)
            except Exception as e:
                messagebox.showerror("Error al cargar", f"Ocurrió un error al cargar los eventos: {e}")
                return []
        return []

    def cerrar_aplicacion(self):
        """Guarda los eventos antes de cerrar la aplicación."""
        self.guardar_eventos()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()