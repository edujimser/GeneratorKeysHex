# Ajuste del path para permitir ejecutar este archivo directamente
import os
import sys
import time
from tqdm import tqdm


# =========================================================================================================================== #
#                                     Configura el archivo de OutPut keysForced.h                                             #
# =========================================================================================================================== #   
def create_key_hex_output():
    start = time.time()
    #ruta del archivo de salida
    rutaArchivo = os.path.join(output_folder, output_file_name)
    
    contenido = f"""\
    /*******************************************************
    * keys.h - Diccionario de claves MIFARE Classic
    * Generado automáticamente con Python
    * Rango: {Number_Items_Min} hasta {Number_Items_max}
    *******************************************************/

    #ifndef KEYS_H
    #define KEYS_H

    #include <Arduino.h>

    const byte knownKeys[][6] PROGMEM = {{
    """

    # Generar claves con barra de progreso
    for i in tqdm(range(Number_Items_Min, Number_Items_max + 1), desc="Generando claves", unit="clave"):
        clave = [(i >> (8 * j)) & 0xFF for j in reversed(range(6))]
        linea = "    {" + ", ".join(f"0x{b:02X}" for b in clave) + f"}}, // Key {i}\n"
        contenido += linea

    # Cierre del array y guardas

    contenido += """\
    };
    const int numKeys = sizeof(knownKeys) / sizeof(knownKeys[0]);

    #endif // KEYS_H
    """


    # Escribir la cabezera en el archivo
    with open(rutaArchivo, "w", encoding="utf-8") as f:
        f.write(contenido)
    
    
    end = time.time()
    total = Number_Items_max - Number_Items_Min + 1
    print(f"\n✅ Archivo generado con {total} claves en {end - start:.2f} segundos.")

# =========================================================================================================================== #
#                                     Generador de contraseñas para keysForced.h                                              #
# =========================================================================================================================== # 
def generar_clave_ordenada(i):
    """
    Convierte un número entero en una clave de 6 bytes (big endian).
    Ejemplo: 1 -> 00 00 00 00 00 01
             255 -> 00 00 00 00 00 FF
             256 -> 00 00 00 00 01 00
    """
    return [(i >> (8 * j)) & 0xFF for j in reversed(range(6))]
