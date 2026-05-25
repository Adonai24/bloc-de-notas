# Bloc de notas

Editor de texto de escritorio con interfaz gráfica en **Python** y **Tkinter**. Proyecto de aprendizaje: menús, archivos, portapapeles y aviso al salir si hay cambios sin guardar.

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-2E7D32)](https://docs.python.org/3/library/tkinter.html)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**Repositorio:** [github.com/Adonai24/bloc-de-notas](https://github.com/Adonai24/bloc-de-notas)

---

## Capturas

<!-- Sustituye la URL cuando subas una imagen a la carpeta del repo, por ejemplo docs/captura.png -->
<!-- ![Ventana principal](docs/captura.png) -->

*Puedes añadir una captura en `docs/` y enlazarla aquí.*

---

## Características

- Abrir, guardar y **guardar como** archivos de texto (UTF-8)
- Aviso **«¿Desea guardar los cambios antes de continuar?»** al salir, cerrar la ventana o abrir otro archivo
- Menú **Editar**: cortar, copiar y pegar
- Atajos: `Ctrl+O`, `Ctrl+S`, `Ctrl+X`, `Ctrl+C`, `Ctrl+V`
- Interfaz y mensajes en **español**

---

## Requisitos

| Requisito | Notas |
|-----------|--------|
| Python 3.8+ | [Descargar Python](https://www.python.org/downloads/) |
| Tkinter | Incluido en Windows/macOS; en Linux: `sudo apt install python3-tk` |

No hace falta `pip install`: solo biblioteca estándar.

---

## Instalación y uso

### Clonar el repositorio

```bash
git clone https://github.com/Adonai24/bloc-de-notas.git
cd bloc-de-notas
```

### Ejecutar

```bash
python notas.py
```

En Windows también puedes abrir `notas.py` con doble clic si `.py` está asociado a Python.

---

## Menús y atajos

### Archivo

| Acción | Atajo |
|--------|--------|
| Abrir | `Ctrl+O` |
| Guardar | `Ctrl+S` |
| Guardar como... | — |
| Salir | — |

**Guardar** escribe en el archivo actual si ya existe ruta; si no, abre el diálogo de guardar. **Guardar como...** siempre pide una ruta nueva.

### Editar

| Acción | Atajo |
|--------|--------|
| Cortar | `Ctrl+X` |
| Copiar | `Ctrl+C` |
| Pegar | `Ctrl+V` |

---

## Estructura del proyecto

```
bloc-de-notas/
├── notas.py      # Aplicación principal
└── README.md
```

---

## Detalles técnicos

- Clase `EditorNotas` (`tk.Tk`)
- Flag `hay_cambios` con evento `<<Modified>>` del widget `Text`
- Cierre controlado con `protocol("WM_DELETE_WINDOW", ...)`

---

## Roadmap (ideas futuras)

- [ ] Numeración de líneas
- [ ] Cambio de fuente y tamaño
- [ ] Barra de estado (ruta, cursor)
- [ ] Ayuda con redacción vía API (experimental)

---

## Autor

**[Adonai24](https://github.com/Adonai24)** — [bloc-de-notas](https://github.com/Adonai24/bloc-de-notas)

Si te sirve el proyecto, puedes darle una estrella en GitHub.

---

## Licencia

Este proyecto es de código abierto para aprendizaje y uso libre. Si añades un archivo `LICENSE` (por ejemplo MIT), enlázalo aquí.
