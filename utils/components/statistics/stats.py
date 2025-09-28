from colorama import Fore, Style, init

init()

def main():
    estudiantes = [
        {'Nombre': 'Ana', 'Nota Global': 19.2},
        {'Nombre': 'Beto', 'Nota Global': 20},
        {'Nombre': 'Carlos', 'Nota Global': 13.4},
        {'Nombre': 'Diana', 'Nota Global': 5.65}
    ]
    estudiantes_ordenados = ordenar_notas(estudiantes) 
    imprimir_notas(estudiantes_ordenados)

def ordenar_notas(estudiantes: list) -> list:
    """Ordena una lista de estudiantes (diccionarios) por su 'Nota Global'
    de forma descendente.

    La función espera que cada elemento de la lista 'estudiantes' sea un diccionario
    que contenga la clave 'Nota Global'.

    Args:
        estudiantes (list): Lista de diccionarios, donde cada diccionario
            representa un estudiante y debe contener la clave 'Nota Global'.

    Returns:
        list: Una nueva lista de diccionarios de estudiantes, ordenada
            descendentemente por la 'Nota Global'.
    """
    lista_estudiantes = []

    for estudiante in estudiantes:
        lista_estudiantes.append(estudiante['Nota Global'])

    notas_ordenadas = sorted(estudiantes, key=lambda estudiante: estudiante['Nota Global'], reverse=True)
    return notas_ordenadas

def imprimir_notas(estudiantes_ordenados: list):
    """Imprime una lista de estudiantes ordenada, mostrando su posición numerica,
    nombre y 'Nota Global' con formato.

    Args:
        estudiantes_ordenados (list): Lista de diccionarios de estudiantes
            previamente ordenada, donde cada diccionario debe contener las
            claves 'Nombre' y 'Nota Global'.
    """
    print(Fore.LIGHTYELLOW_EX + "\n\t\tMejores promedios de estudiantes:" + Style.RESET_ALL)
    for i, ordenado in enumerate(estudiantes_ordenados, 1):
        print(Fore.BLUE + f"\n{i}. Nombre: " + Fore.GREEN + f"{ordenado["Nombre"]} " + Fore.BLUE + f"Nota Global: " + Fore.GREEN + f"{ordenado['Nota Global']:.2f}" + Style.RESET_ALL)


if __name__ == "__main__":
    main()