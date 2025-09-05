import json

#CONSTANTES
ARCHIVO_JSON = 'estudiantes.json'

# Cargar datos existentes al iniciar
def cargar_datos():
    """
    Carga los datos de estudiantes desde el archivo JSON.
    
    Intenta leer el archivo especificado en la variable ARCHIVO_JSON. Si el archivo
    no existe, retorna una lista vacía para inicializar los datos.
    
    Returns:
        list: Una lista de diccionarios con los datos de los estudiantes cargados desde el archivo JSON. Retorna una lista vacía si el archivo no existe.
        
    """
    try:
        with open(ARCHIVO_JSON, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []
    
# Guardar datos en el archivo JSON
def guardar_datos(datos):
    """
    Guarda los datos de estudiantes en el archivo JSON.
    
    Escribe los datos proporcionados en el archivo especificado en la variable ARCHIVO_JSON
    con formato indentado para mejor legibilidad.
    
    Args:
        datos (list): Lista de diccionarios con los datos de estudiantes a guardar.
        
    
    """

    with open(ARCHIVO_JSON, 'w') as archivo:
        json.dump(datos, archivo, indent=4)