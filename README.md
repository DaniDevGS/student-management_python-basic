# Gestión de Estudiantes Python Basic

[![Estado](https://img.shields.io/badge/estado-activo-brightgreen)](https://github.com/DaniDevGS/student-management_python-basic)
[![Licencia](https://img.shields.io/badge/licencia-CC_BY--ND_4.0-lightgrey)](https://creativecommons.org/licenses/by-nd/4.0/)
[![Python](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python)](https://python.org)
[![Code Style](https://img.shields.io/badge/code%20style-PEP8-brightgreen)](https://pep8.org)

![Demo](https://images.unsplash.com/photo-1624953587687-daf255b6b80a?fm=jpg&q=60&w=800&h=400&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8cHl0aG9uJTIwcHJvZ3JhbW1pbmd8ZW58MHx8MHx8fDA%3D)


Sistema de gestión académica basica desarrollado en Python que permite a estudiantes registrar sus datos y a administradores visualizar información académica.

## Características

- Interfaz de línea de comandos con colores (usando Colorama)
- Validación de datos integrada
- Persistencia de datos mediante archivos JSON
- Diseño colorido y amigable para terminal
- Gestión de estudiantes y administradores

## Requisitos previos

- Python 3.6 o superior
- pip (gestor de paquetes de Python)

## Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/DaniDevGS/student-management_python-basic
cd student-management_python-basic
```

2. Instala dependencias:
```bash
pip install -r requirements.txt
```

## Ejecucion

1. Abrir terminal:
```bash
python main.py
```

<b>Note:</b> Para acceder a las funciones del menu admin se necesita una contraseña la cual es <strong>admin123</strong>.

## Estructura del proyecto
```bash
student-management_python-basic/
├── utils/
│   ├── components/
│   │   ├──statistics/
│   │   │   ├── __init__.py
│   │   │   └── stats.py
│   │   ├── __init__.py
│   │   └── universitys.py
│   ├── database/
│   │   ├── __init__.py
│   │   └── json.py
│   ├── __init__.py
│   └── menu.py
├── estudiantes.json
├── main.py
├── README.md
└── requirements.txt
```
