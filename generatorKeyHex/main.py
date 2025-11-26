
# Ajuste del path para permitir ejecutar este archivo directamente
import os
import sys

# Si se ejecuta como script directo, asegurar que la carpeta raíz esté en sys.path
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root not in sys.path:
    sys.path.insert(0, root)

# Importacion archivos
from menu.menu import mostrar_banner, mostrar_menu



# =========================================================================================================================== #
#                                     INIT PROGRAMA BASE DE MENU INTERACTIVO                                                  #
# =========================================================================================================================== #   
if __name__ == "__main__":
    mostrar_banner() 
    mostrar_menu()

