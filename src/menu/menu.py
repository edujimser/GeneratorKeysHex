import os
import sys

# Importacion archivos
from config.config import VERSION, colors
from generatorKeyHex.FolderDocument import BorrarCarpetaSalida, CrearCarpetaSalida, configuracionCarpetaSalida
from generatorKeyHex.formatOutput import create_key_hex_output
from config.config import output_folder, output_file_name, input_folder, input_file_name, num_archivos

# ============================================================================================================================ #
#                                               Banner del Menú generador de contraseñas                                       # ============================================================================================================
# ============================================================================================================================ #
def mostrar_banner():
    os.system("cls" if os.name == "nt" else "clear")
    # Banner grande: GENERADOR DE CONTRASEÑAS
    print(colors["YELLOW"] + colors["BOLD"] + r"""
    ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ██████╗  ██████╗ ██████╗     ██████╗ ███████╗    ██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗ 
    ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔═══██╗██╔══██╗    ██╔══██╗██╔════╝    ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗
    ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║██║  ██║██║   ██║██████╔╝    ██║  ██║█████╗      ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║
    ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║██║  ██║██║   ██║██╔══██╗    ██║  ██║██╔══╝      ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║
    ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║██████╔╝╚██████╔╝██║  ██║    ██████╔╝███████╗    ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝
    ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚═════╝ ╚══════╝    ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝
        """ + colors["RESET"])
    # Subtítulo
    print(colors["WHITE"] + colors["BOLD"] + "Hexadecimal para tarjetas MIFARE CLASSIC 1K" + colors["RESET"])
    # Autor
    print(colors["WHITE"] + "Autor: EduJimSer" + colors["RESET"])
    # Versión
    print(colors["WHITE"] + "Versión: "+ VERSION + colors["RESET"])
    print("\n")




# ============================================================================================================================ #
#                                               Banner del Menú generador de contraseñas                                       # ============================================================================================================
# ============================================================================================================================ #
def mostrar_menu():
    # Caja del menú
    print(colors["BLUE"] + "╔══════════════════════════════════════════════╗" + colors["RESET"])
    print(colors["BLUE"] + "║" + colors["RESET"] + colors["BOLD"] + colors["YELLOW"] + "                 MENÚ PRINCIPAL               " + colors["RESET"] + colors["BLUE"] + "║" + colors["RESET"])
    print(colors["BLUE"] + "╠══════════════════════════════════════════════╣" + colors["RESET"])
    print(colors["BLUE"] + "║" + colors["RESET"] + " 1. 📂 Generacion de password                 " + colors["BLUE"] + "║" + colors["RESET"])
    print(colors["BLUE"] + "╠══════════════════════════════════════════════╣" + colors["RESET"])
    print(colors["BLUE"] + "║" + colors["RESET"] + " 0. ❌ Salir del programa                     " + colors["BLUE"] + "║" + colors["RESET"])
    print(colors["BLUE"] + "╚══════════════════════════════════════════════╝" + colors["RESET"])
    print()  # Espacio debajo
    
    while True:
        opcion = input(colors["GREEN"] + "👉  Selecciona una opción: " + colors["RESET"] + "\n")

        if opcion == "1":
            mostrar_menu_create_output_folder() #Menú secundario
        elif opcion == "0":
            print(colors["RED"] + "❌ Saliendo del programa..." + colors["RESET"] + "\n")
            sys.exit(0)  # 0 = salida correcta
            break
        else:
            print(colors["RED"] + "⚠️ Opción no válida, intenta de nuevo." + colors["RESET"] + "\n")

        input("\nPresiona ENTER para continuar...")

    
# ============================================================================================================================ #
#                                              mostrar_menu_create_output_folder                                               # ============================================================================================================
# ============================================================================================================================ #
def mostrar_menu_create_output_folder():
    print(colors["BLUE"] + "╔══════════════════════════════════════════════╗" + colors["RESET"])
    print(colors["BLUE"] + "║" + colors["RESET"] + colors["BOLD"] + colors["YELLOW"] + "          CREAR CARPETA DE SALIDA             " + colors["RESET"] + colors["BLUE"] + "║" + colors["RESET"])
    print(colors["BLUE"] + "╠══════════════════════════════════════════════╣" + colors["RESET"])
    print(colors["BLUE"] + "║" + colors["RESET"] + " 1. 📂 CONFIGURACION                          " + colors["BLUE"] + "║" + colors["RESET"])
    print(colors["BLUE"] + "║" + colors["RESET"] + " 2. 📂 GENERAR PASSWORDS                      " + colors["BLUE"] + "║" + colors["RESET"])
    print(colors["BLUE"] + "║" + colors["RESET"] + " 0. ❌ VOLVER AL MENÚ PRINCIPAL               " + colors["BLUE"] + "║" + colors["RESET"])
    print(colors["BLUE"] + "╚══════════════════════════════════════════════╝" + colors["RESET"])
    print()  # Espacio debajo
   
    while True:
        opcion = input(colors["GREEN"] + "👉  Selecciona una opción: " + colors["RESET"] + "\n")

        if opcion == "1":
            BorrarCarpetaSalida(output_folder) #Borrar carpeta de salida si existe
            configuracionCarpetaSalida()
            CrearCarpetaSalida(output_folder,output_file_name) #Crear carpeta de salida
            mostrar_menu_create_output_folder() #Volver al menú secundario
        elif opcion == "2":
            create_key_hex_output() #Crear el archivo keysForced.h
            mostrar_menu_create_output_folder() #Volver al menú secundario
        elif opcion == "0":
            mostrar_menu()
        else:
            print(colors["RED"] + "⚠️ Opción no válida, intenta de nuevo." + colors["RESET"] + "\n")
