from colorama import Fore, Back, Style, init

# Inicializa colorama (necesario para Windows)
init()

print(Fore.RED + 'Texto en rojo')
print(Back.GREEN + 'Fondo verde' + Style.RESET_ALL)
print(Fore.BLUE  + 'Texto azul con fondo amarillo' + Style.RESET_ALL)
print(Fore.RED + 'Texto en rojo')