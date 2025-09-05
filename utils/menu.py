from .components.universitys import obtener_universidades, obtener_tipos_carreras, obtener_carreras_por_tipo
from colorama import Fore, Style, init
import time

# Inicializa colorama (necesario para Windows)
init()

DELAY = 1

#Funciones para el menu
def mostrar_menu_universidades():
    """Muestra el menú principal de selección de universidades.
    
    Presenta una interfaz interactiva que permite al usuario seleccionar
    entre las universidades disponibles o salir del programa. Navega
    a través de los submenús de tipos de carrera y carreras específicas.

    Returns:
        str or None: Nombre de la carrera seleccionada por el usuario.
                Retorna None si el usuario elige salir o cancela la selección.
    """

    universidades = obtener_universidades()
    
    while True:
        print(Fore.YELLOW + "\n\t\tMenú de Universidades" + Style.RESET_ALL)
        for i, uni in enumerate(universidades, 1):
            print(f"\t{i}. {uni['nombre']}")
        print(Fore.RED + "\t5. Salir" + Style.RESET_ALL)
        
        try:
            opcion = int(input("\nSeleccione una universidad: "))
            if opcion == 5:
                print("Programa finalizada.")
                return None
            elif 1 <= opcion <= 4:
                universidad_seleccionada = universidades[opcion-1]
                carrera_seleccionada = mostrar_menu_tipos_carreras(universidad_seleccionada)
                if carrera_seleccionada:
                    return carrera_seleccionada
            else:
                print("Opción inválida. Intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")



def mostrar_menu_tipos_carreras(universidad):
    """Muestra el menú de tipos de carrera para una universidad específica.
    
    Presenta las categorías de carreras disponibles en la universidad
    seleccionada y permite navegar al menú de carreras específicas.

    Args:
        universidad (dict): Diccionario con la información de la universidad
                    seleccionada. Debe contener las claves 'nombre' y 'carreras'.

    Returns:
        str or None: Nombre de la carrera seleccionada por el usuario.
                    Retorna None si el usuario elige volver al menú anterior.
    """

    tipos_carrera = obtener_tipos_carreras(universidad)

    time.sleep(DELAY) 
    
    while True:
        print(f"\n--- Tipos de Carrera en {universidad['nombre']} ---")
        for i, tipo in enumerate(tipos_carrera, 1):
            print(f"{i}. {tipo}")
        print(f"{len(tipos_carrera)+1}. Volver al menú anterior")
        
        try:
            opcion = int(input("\nSeleccione un tipo de carrera: "))
            if opcion == len(tipos_carrera)+1:
                return None
            elif 1 <= opcion <= len(tipos_carrera):
                tipo_seleccionado = tipos_carrera[opcion-1]
                carrera_seleccionada = mostrar_carreras(universidad, tipo_seleccionado)
                if carrera_seleccionada:
                    return carrera_seleccionada
            else:
                print("Opción inválida. Intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")



def mostrar_carreras(universidad, tipo_carrera):
    """Muestra la lista de carreras específicas de un tipo en una universidad.
    
    Presenta todas las carreras disponibles dentro de una categoría específica
    y permite al usuario seleccionar una por su ID.

    Args:
        universidad (dict): Diccionario con la información de la universidad.
        tipo_carrera (str): Tipo o categoría de carreras a mostrar.

    Returns:
        str or None: Nombre de la carrera seleccionada por el usuario.
                    Retorna None si el usuario elige volver al menú anterior.

    """

    time.sleep(DELAY) 


    carreras = obtener_carreras_por_tipo(universidad, tipo_carrera)
    
    print(f"\n--- {tipo_carrera} en {universidad['nombre']} ---")
    for carrera in carreras:
        print(f"{carrera['id']}: {carrera['name']}")
    
    while True:
        try:
            opcion = int(input("\nIngrese el ID de la carrera que desea seleccionar (0 para volver): "))
            if opcion == 0:
                return None
            for carrera in carreras:
                if carrera['id'] == opcion:
                    print(f"La carrera seleccionada es: {carrera["name"]}")
                    carrera_estudiante = carrera["name"] 
                    return carrera_estudiante
                    
            print("ID no encontrado. Intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
