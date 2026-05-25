# Bloc de notas

Editor de texto de escritorio hecho con **Python** y **Tkinter**. Permite abrir y guardar archivos `.txt`, editar con cortar/copiar/pegar y avisar si hay cambios sin guardar al salir.

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-2E7D32)](https://docs.python.org/3/library/tkinter.html)

## Características

- Abrir, guardar y guardar como (UTF-8)
- Confirmación al salir o abrir otro archivo si el documento fue modificado
- Menú Editar: cortar, copiar y pegar
- Atajos de teclado: `Ctrl+O`, `Ctrl+S`, `Ctrl+X`, `Ctrl+C`, `Ctrl+V`
- Interfaz en español

## Requisitos

- Python 3.8 o superior
- Tkinter (incluido en Windows; en Linux: `sudo apt install python3-tk`)

No requiere instalar paquetes con pip.

## Uso

```bash
git clone https://github.com/Adonai24/bloc-de-notas.git
cd bloc-de-notas
python notas.py
```

También se puede ejecutar abriendo `notas.py` directamente en Windows.

## Menús

| Archivo | Editar |
|---------|--------|
| Abrir (`Ctrl+O`) | Cortar (`Ctrl+X`) |
| Guardar (`Ctrl+S`) | Copiar (`Ctrl+C`) |
| Guardar como... | Pegar (`Ctrl+V`) |
| Salir | |

## Estructura

```
bloc-de-notas/
├── notas.py
└── README.md
```

## Autor

Desarrollado por **[Adonai24](https://github.com/Adonai24)**.
