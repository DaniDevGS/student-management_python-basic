# Gestión de Estudiantes Python Basic

[![Estado](https://img.shields.io/badge/estado-activo-brightgreen)](https://github.com/DaniDevGS/student-management_python-basic)
[![Licencia](https://img.shields.io/badge/licencia-CC_BY--ND_4.0-lightgrey)](https://creativecommons.org/licenses/by-nd/4.0/)


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

## Estructura del proyecto
```bash
student-management_python-basic/
├── utils/
│   ├── components/
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
