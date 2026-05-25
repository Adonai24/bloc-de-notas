import tkinter as tk
from tkinter import filedialog, messagebox


class EditorNotas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Editor de Notas")
        self.geometry("600x400")

        self.ruta_actual = None
        self.hay_cambios = False

        self.text_area = tk.Text(self)
        self.text_area.pack(expand=True, fill=tk.BOTH)
        self.text_area.bind("<<Modified>>", self._al_modificar_texto)

        self.crear_menu()
        self.protocol("WM_DELETE_WINDOW", self.salir)

    def _al_modificar_texto(self, _event=None):
        if self.text_area.edit_modified():
            self.hay_cambios = True
            self.text_area.edit_modified(False)

    def crear_menu(self):
        menubar = tk.Menu(self)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Abrir", command=self.abrir_archivo, accelerator="Ctrl+O")
        filemenu.add_command(label="Guardar", command=self.guardar_archivo, accelerator="Ctrl+S")
        filemenu.add_command(label="Guardar como...", command=self.guardar_como)
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=self.salir)
        menubar.add_cascade(label="Archivo", menu=filemenu)

        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Cortar", command=self.cortar, accelerator="Ctrl+X")
        editmenu.add_command(label="Copiar", command=self.copiar, accelerator="Ctrl+C")
        editmenu.add_command(label="Pegar", command=self.pegar, accelerator="Ctrl+V")
        menubar.add_cascade(label="Editar", menu=editmenu)

        self.config(menu=menubar)
        self.bind_all("<Control-o>", lambda e: self.abrir_archivo())
        self.bind_all("<Control-s>", lambda e: self.guardar_archivo())

    def cortar(self):
        try:
            self.text_area.event_generate("<<Cut>>")
        except tk.TclError:
            pass

    def copiar(self):
        try:
            self.text_area.event_generate("<<Copy>>")
        except tk.TclError:
            pass

    def pegar(self):
        try:
            self.text_area.event_generate("<<Paste>>")
        except tk.TclError:
            pass

    def _preguntar_guardar_si_hay_cambios(self):
        if not self.hay_cambios:
            return True
        respuesta = messagebox.askyesnocancel(
            "Guardar cambios",
            "¿Desea guardar los cambios antes de continuar?",
        )
        if respuesta is None:
            return False
        if respuesta:
            return self.guardar_archivo()
        return True

    def abrir_archivo(self):
        if not self._preguntar_guardar_si_hay_cambios():
            return
        filepath = filedialog.askopenfilename(
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
        )
        if not filepath:
            return
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                contenido = file.read()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, contenido)
            self.text_area.edit_modified(False)
            self.ruta_actual = filepath
            self.hay_cambios = False
            self.title(f"Editor de Notas — {filepath}")
        except OSError as e:
            messagebox.showerror("Error", f"No se pudo abrir el archivo:\n{e}")

    def guardar_archivo(self):
        if self.ruta_actual:
            return self._escribir_archivo(self.ruta_actual)
        return self.guardar_como()

    def guardar_como(self):
        filepath = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")],
        )
        if not filepath:
            return False
        if self._escribir_archivo(filepath):
            self.ruta_actual = filepath
            self.title(f"Editor de Notas — {filepath}")
            return True
        return False

    def _escribir_archivo(self, filepath):
        try:
            contenido = self.text_area.get(1.0, tk.END)
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(contenido)
            self.text_area.edit_modified(False)
            self.hay_cambios = False
            return True
        except OSError as e:
            messagebox.showerror("Error", f"No se pudo guardar el archivo:\n{e}")
            return False

    def salir(self):
        if not self._preguntar_guardar_si_hay_cambios():
            return
        self.destroy()


if __name__ == "__main__":
    app = EditorNotas()
    app.mainloop()
