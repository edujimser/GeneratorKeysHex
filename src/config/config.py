import os

#Version ---------------------------------------------------------------------------------------------------------------------------------
VERSION = "1.0.0"

#rutas -----------------------------------------------------------------------------------------------------------------------------------
output_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/output'
output_file_name = 'keysForced.h'
input_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/input'
input_file_name = 'keys.txt'

#Colores ----------------------------------------------------------------------------------------------------------------------------------
colors = {
    "RESET": "\033[0m",
    "BOLD": "\033[1m",
    "RED": "\033[91m",
    "GREEN": "\033[92m",
    "YELLOW": "\033[93m",
    "BLUE": "\033[94m",
    "CYAN": "\033[96m",
    "WHITE": "\033[97m"
}

#CARPETA SALIDA ----------------------------------------------------------------------------------------------------------------------------------
Number_File = 0
Number_Items_Inicio = 0
Number_Items_Fin = 0
total_claves = 0
claves_por_archivo = 0
claves_por_archivo_min = 1000
num_archivos = 0
resto = 0