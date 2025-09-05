from utils.menu import *
from utils.database.json import cargar_datos, guardar_datos
from colorama import Fore, Style, init
import time

#CONSTANTES
EDADMINIMA = 13
EDADMAXIMA = 25
DELAY = 1

# Inicializa colorama (necesario para Windows)
init()

estudiantes = {
        "Nombre": ...,
        "Edad": 0,
        "Notas": [],
        "Cedula": 0,
    }

lista_materias = ["Biologia", "Castellano", "Fisica", "Ingles", "Matematicas", "Quimica", "GHC", "Ciencias de la Tierra", "Premilitar"]

lista_estudiantes = cargar_datos()

def main():
    """Funcion principal que se encarga de la toda la logia del programa

    """

    global lista_estudiantes

    print(Fore.LIGHTYELLOW_EX +"\n\t\tPrograma de ingresos de estudiantes\n" + Style.RESET_ALL)
    print(Fore.CYAN + "\t\t\tMenú de Ingresos\n" + Style.RESET_ALL)
    print("\t\t 1. Estudiante")
    print("\t\t 2. Administador")

    opcion = int(input("\nSeleccione una opcion: "))

    #===================================Menu de Opciones=====================================================
    """Ejecuta la opcion de estudiante, crear un estudiante con los datos del datos"""
    if opcion == 1:

        time.sleep(DELAY)
        print(Fore.CYAN + "\n\tColoque sus datos\n" + Style.RESET_ALL)

        #Crea una copia del diccionario 
        estudiante_actual = estudiantes.copy()

        estudiante_actual["Nombre"] = input("Hola usuario porfavor coloque su nombre: ")

        #Verificacion de la edad del usuario sin que el programa termine
        while True:
            try:
                edad = int(input("Ahora porfavor coloque su edad: "))
                verificar_edad(edad)
                estudiante_actual["Edad"] = edad
                break
            except (ValueError, TypeError, Exception) as e:
                print(Fore.RED + f"\nError: {e}")

        estudiantes["Cedula"] = input("Por favor coloque su cédula: ")

        #Verificacion de las notas del usuario sin que el programa termine
        for materia in lista_materias:
            while True:
                try:
                    nota = int(input(f"\nColoque la nota de {materia}: "))
                    verificar_notas(nota)
                    estudiantes["Notas"].append(nota)
                    break
                except (ValueError, TypeError, Exception) as e:
                    print(Fore.RED + f"\nError: {e}" + Style.RESET_ALL)

        #Nota final del estudiante
        nota_final = calcular_nota(estudiante_actual["Notas"])

        time.sleep(DELAY)  
        carrera_estudiante = mostrar_menu_universidades()

        #===================================Imprimir datos====================================================
        #Datos del estudiante
        print("")
        print(Fore.CYAN + "\t\tDatos del Estudiante" + Style.RESET_ALL )

        for clave, valor in estudiantes.items():
            #Imprime la lista de notas como un STR(string)
            if isinstance(valor, list):
                valor_str = ', '.join(map(str, valor))
                print(Fore.BLUE + f"{clave}: " + Fore.GREEN + f"{valor_str}")
            else:
                print(Fore.BLUE + f"{clave}: " + Fore.GREEN + f"{valor}" + Style.RESET_ALL)
        print(Fore.BLUE + f"Nota Global:" + Fore.GREEN + f"{nota_final:.2f}" + Style.RESET_ALL)
        print(Fore.BLUE + f"Carrera seleccionada:" + Fore.GREEN + f"{carrera_estudiante}" + Style.RESET_ALL)


        #Guardar
        estudiante_actual["Nota Global"] = nota_final
        estudiante_actual["Carrera"] = carrera_estudiante
        lista_estudiantes.append(estudiante_actual)
        guardar_datos(lista_estudiantes) #Guardar al JSON

    #===================================Opcion dos sistema de Administracion=================================
    elif opcion ==2:

        lista_estudiantes = cargar_datos()
        
        print("\n\tMenú de Administracion\n")
        print("\t1. Ver la lista de estudiantes.")
        estudiantes_registrados(lista_estudiantes)
        opcion_admin = int(input("\nSeleccione una opcion: "))

        if opcion_admin == 1:
            #Muestra los datos del
            mostrar_lista_estudiantes(lista_estudiantes)
        else: 
            print(Fore.RED + "Opcion no valida" + Style.RESET_ALL)

    #===================================ELSE=====================================================
    else:
        print("Opcion no valida")


"""
    FUNCIONES
"""
#Funciones de verificacion
def verificar_edad(edad: int):
    """Verifica que la edad cumpla con los requisitos establecidos.
    
    Valida que la edad esté dentro del rango permitido (13-19 años) y que sea
    del tipo de dato correcto (entero).

    Args:
        edad (int): Edad del estudiante a validar

    Raises:
        ValueError: Si la edad está fuera del rango permitido (13-19)
        TypeError: Si el tipo de dato no es entero
    """

    if edad < EDADMINIMA or edad > EDADMAXIMA:
        raise ValueError("La edad no puede ser menor a 13 o mayor a 19. Porfavor intente de nuevo.\n" + Style.RESET_ALL)
    if isinstance(edad, str):
            raise TypeError("La edad no pueden ser texto\n" + Style.RESET_ALL)
    

def verificar_notas(nota: int):
    """Verifica que la nota cumpla con los requisitos establecidos.
    
    Valida que la nota esté dentro del rango permitido (0-20) y que sea
    del tipo de dato correcto (entero).

    Args:
        nota (int): Nota del estudiante a validar

    Raises:
        ValueError: Si la nota está fuera del rango permitido (0-20)
        TypeError: Si el tipo de dato no es entero
    """
    if nota < 0 or nota > 20:
        raise ValueError("Las notas deben estar entre 0 y 20.\n" + Style.RESET_ALL)
        
    if isinstance(nota, str):
        raise TypeError("Las notas no pueden ser texto\n" + Style.RESET_ALL)
    
def calcular_nota(notas: list) -> float:
    """Calcula el promedio de una lista de notas del estudiante.
    
    Toma una lista de notas numéricas y devuelve el promedio en decimales.

    Args:
        notas (list): Lista de notas numéricas

    Returns:
        float: Promedio de las notas con precisión decimal

    """
    
    return sum(notas) / len(notas)

def mostrar_lista_estudiantes(estudiantes: list):
    """Muestra en pantalla la lista de estudiantes registrados.
    
    Presenta de forma ordenada la información de todos los estudiantes
    en el formato: nombre, edad, cédula y nota global.

    Args:
        estudiantes (list): Lista de diccionarios con información de estudiantes.
                            Cada diccionario debe contener las claves:
                            'Nombre', 'Cedula', 'Edad', 'Nota Global'
    """

    print("\nLista de estudiantes:")
    for i, estudiante in enumerate(estudiantes, 1):
        print(f"\n{i}. {estudiante['Nombre']} - Cédula: {estudiante['Cedula']} - Nota Global: {estudiante['Nota Global']:.2f}")


def estudiantes_registrados(lista_estudiantes: list):
    """Muestra el total de estudiantes registrados.
    
    Presenta el conteo total de estudiantes en color amarillo.

    Args:
        lista_estudiantes (list): Lista de estudiantes registrados
    """

    print(Fore.YELLOW + f"\tTotal de estudiantes registrados: {len(lista_estudiantes)}" + Style.RESET_ALL)


if __name__ == '__main__':
    main()
