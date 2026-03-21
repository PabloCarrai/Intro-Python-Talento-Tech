from colorama import init, Fore, Back
from datetime import datetime
from productos import mostrar_producto, eliminar_producto, cargar_producto, mostrar_menu

init(autoreset=True)


def main():
    mostrar_menu()


if __name__ == "__main__":
    main()
