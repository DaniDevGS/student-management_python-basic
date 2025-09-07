UDO = {
    "nombre": "Universidad de Oriente (UDO) - Núcleo Monagas",
    "ubicacion": "Av. Universidad, Sector Jusepín, Maturín, estado Monagas",
    "carreras": {
        "Ingenierías": [
            {"name": "Ingeniería Agronómica", "id": 1},
            {"name": "Ingeniería de Petróleo", "id": 2},
            {"name": "Ingeniería de Gas", "id": 3},
            {"name": "Ingeniería Geológica", "id": 4},
            {"name": "Ingeniería Geofísica", "id": 5},
            {"name": "Ingeniería de Mantenimiento Mecánico", "id": 6},
            {"name": "Ingeniería Eléctrica", "id": 7},
            {"name": "Ingeniería Electrónica", "id": 8},
            {"name": "Ingeniería en Sistemas", "id": 9},
            {"name": "Ingeniería Informatica", "id": 10}
        ],
        "Otros": [
            {"name": "Medicina", "id": 1},
            {"name": "Enfermería", "id": 2},
            {"name": "Bioanálisis", "id": 3},
            {"name": "Salud Pública", "id": 4},
            {"name": "Administración", "id": 5},
            {"name": "Contaduría Pública", "id": 6},
            {"name": "Estudios Internacionales", "id": 7},
            {"name": "Relaciones Industriales", "id": 8},
            {"name": "Turismo", "id": 9}
        ]
    }
}




UNEFA = {
    "nombre": "Universidad Nacional Experimental Politécnica de la Fuerza Armada Nacional Bolivariana (UNEFA) - Núcleo Monagas",
    "ubicacion": "Av. Raúl Leoni, Sector Los Guaritos, Maturín, estado Monagas",
    "carreras": {
        "Ingenierías": [
            {"name":"Ingeniería de Sistemas", "id": 1},{"name":"Ingeniería Electrónica", "id": 2},{"name":"Ingeniería Mecánica", "id": 3},{"name":"Ingeniería Civil", "id": 4},{"name":"Ingeniería de Petróleo", "id": 5}
        ],
        "Licenciaturas": [
            {"name":"Licenciatura en Administración", "id": 1},
            {"name":"Licenciatura en Contaduría Pública", "id": 2}
        ]
    }
}


IUTIRLA = {
    "nombre": "Instituto Universitario de Tecnología Industrial Rodolfo Loero Arismendi (IUTIRLA) - Núcleo Maturín",
    "ubicacion": "Avenida Bolívar, Sector Los Guaritos, Maturín, Estado Monagas",
    "carreras": {
        "Ingeniería": [
            {"name": "Ingeniería Eléctrica", "id": 1},
            {"name": "Ingeniería Electrónica", "id": 2},
            {"name": "Ingeniería Mecánica", "id": 3}
        ],
        "Tecnico Superior Universitario": [
            {"name": "Informatica", "id": 1},
            {"name": "Diseño Grafico", "id": 2},
            {"name": "Administracion de Empresas", "id": 3},
            {"name": "Turismo", "id": 4}
        ],
        
    }
}

UNES = {
    "nombre": "Universidad Nacional Experimental de la Seguridad (UNES) - Sede Maturín",
    "ubicacion": "Calle Cumaná con Calle Caicara, frente a la Redoma El Indio, Parroquia Alto de los Godos, Maturín",
    "carreras": {
        "Otros":[
            {"name": "Formación para Oficiales de Seguridad", "id": 1},
            {"name": "Investigación Penal", "id": 2},
            {"name": "Prevención y Gestión de Riesgos", "id": 3}
        ]
    }
}

"""
    Funciones
"""

#Funciones Gets
def obtener_universidades():
    """Obtiene la lista de todas las universidades disponibles en el sistema.
    
    Retorna un listado con los diccionarios que contienen la información completa
    de cada universidad registrada, incluyendo UDO, UNEFA, IUTIRLA y UNES.

    Returns:
        list: Lista de diccionarios con la información de las universidades.
            Cada diccionario contiene las claves: 'nombre', 'ubicacion' y 'carreras'

    """
    return [UDO, UNEFA, IUTIRLA, UNES]


def obtener_tipos_carreras(universidad):
    """Obtiene los tipos o categorías de carreras disponibles en una universidad.
    
    Cada universidad organiza sus carreras en categorías como "Ingenierías", 
    "Licenciaturas" y "Otros" Esta función devuelve las categorías
    disponibles para la universidad especificada.

    Args:
        universidad (dict): Diccionario que representa una universidad, debe contener
                la clave 'carreras' con un diccionario de categorías.

    Returns:
        list: Lista de strings con los nombres de las categorías de carreras.
    """
    return list(universidad['carreras'].keys())


def obtener_carreras_por_tipo(universidad, tipo):
    """Obtiene la lista de carreras de una categoría específica en una universidad.
    
    Devuelve todas las carreras pertenecientes a un tipo específico (categoría)
    dentro de una universidad determinada.

    Args:
        universidad (dict): Diccionario que representa una universidad.
        tipo (str): Tipo o categoría de carreras a consultar (ej: "Ingenierías", "Otros")

    Returns:
        list: Lista de diccionarios con las carreras del tipo especificado.
            Cada diccionario contiene las claves: 'name' y 'id'
            Retorna lista vacía si el tipo no existe.

    """
    return universidad['carreras'].get(tipo, [])

