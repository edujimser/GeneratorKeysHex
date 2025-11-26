import os
import sys

# Si se ejecuta como script directo, asegurar que la carpeta raíz esté en sys.path
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root not in sys.path:
    sys.path.insert(0, root)

# Importacion archivos
import config.config as config

# ============================================================================================================================ #
#                                     Importar variables desde el paquete de configuración (config)                            # ============================================================================================================
# ============================================================================================================================ #
try:
    # Import directo (cuando se ejecuta desde la raíz del proyecto)
    from config.config import output_folder, output_file_name, input_folder, input_file_name
except Exception:
    # Fallback: añadir la carpeta raíz al sys.path para poder importar cuando se ejecuta el módulo directamente
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if root not in sys.path:
        sys.path.insert(0, root)
        
# Importacion archivos        
from osDef.osDef import borrarCarpeta

# ============================================================================================================================ #
#                                                   BORRAR POR RUTA                                                            # ============================================================================================================
# ============================================================================================================================ #
def BorrarCarpetaSalida(folder):
    # Revisamos si la carpeta ya existe antes de crearla
    if os.path.exists(folder):
        print("⚠️  Atención: La carpeta de salida ya existe en la ruta:" + folder + "\n")
        try:
            borrarCarpeta(folder)
        except PermissionError:
            print(f"⛔ No tienes permisos para borrar la carpeta: {folder}")
        except Exception as e:
            print(f"⚠️ Error inesperado al borrar {folder}: {e}")
            
            

# ============================================================================================================================ #
#                                                   Configuracion                                                              # ============================================================================================================
# ============================================================================================================================ #
def configuracionCarpetaSalida():
    # ───────────────────────────────────────────────────────────── #
    #                   🎛️ CONFIGURACIÓN DE GENERACIÓN              #
    # ───────────────────────────────────────────────────────────── #

    print("\n\033[96m" + "═" * 60)
    print("🎛️  CONFIGURACIÓN DE CLAVES MIFARE CLASSIC".center(60))
    print("═" * 60 + "\033[0m")

    # ── 🔢 RANGO DE CLAVES ──────────────────────────────────────── #
    while True:
        try:
            Number_Items_Inicio_VIRTUAL = (input("🔢 Clave inicial (ej. 0): ".rjust(40)))
            Number_Items_Fin_VIRTUAL = (input("🔢 Clave final   (ej. 999): ".rjust(40)))

            #FILTRADO DE ERRORES
            if (
                not Number_Items_Inicio_VIRTUAL.isdigit()
                or not Number_Items_Fin_VIRTUAL.isdigit()
                or int(Number_Items_Inicio_VIRTUAL) > int(Number_Items_Fin_VIRTUAL)
                or int(Number_Items_Inicio_VIRTUAL) == int(Number_Items_Fin_VIRTUAL)
            ):
                print("❌ Introduce números enteros válidos y asegúrate de que el inicial sea menor al final.\n")
                continue
            
            #VALIDACION CORRECTA
            config.Number_Items_Inicio = int(Number_Items_Inicio_VIRTUAL)
            config.Number_Items_Fin = int(Number_Items_Fin_VIRTUAL)
            break
        
        except ValueError:
            #RESET DE VALORES
            config.Number_Items_Inicio = 0
            config.Number_Items_Fin = 0
            print("❌ Introduce números enteros válidos.\n")

    # ── 📁 NÚMERO DE ARCHIVOS ───────────────────────────────────── #
    while True:
        try:
            num_archivos_VIRTUAL = input(
                f"📁 ¿Cuántos archivos quieres? (mínimo {config.claves_por_archivo_min} claves por archivo)\n"
                f"{'Introduce un número entero:'.rjust(40)} "
            )

            #FILTRADO DE ERRORES
            if int(num_archivos_VIRTUAL) < 1 or not num_archivos_VIRTUAL.isdigit():
                print("❌ Debe ser al menos 1 archivo.\n")
                continue
            
             #VALIDACION CORRECTA
            config.num_archivos = int(num_archivos_VIRTUAL)
            break
        
        except ValueError:
            num_archivos_VIRTUAL = 0
            print("❌ Introduce un número entero válido.\n")

    # ── 📊 CÁLCULOS DE DISTRIBUCIÓN ─────────────────────────────── #
    config.total_claves       = config.Number_Items_Fin - config.Number_Items_Inicio 
    config.claves_por_archivo = config.total_claves // config.num_archivos
    config.resto              = config.total_claves % config.num_archivos


    # ── ✅ RESUMEN FINAL ────────────────────────────────────────── #
    print("\n\033[92m" + "═" * 60)
    print("✅ CONFIGURACIÓN COMPLETA".center(60))
    print("═" * 60 + "\033[0m")
    print(f"🔐 Total de claves:     {config.total_claves}")
    print(f"📂 Archivos a generar:  {config.num_archivos}")
    print(f"📄 Claves por archivo:  {config.claves_por_archivo} (+{config.resto} extra en el último) \n")
    
            
            
            
# ============================================================================================================================ #
#                                                   CREAR CARPETA SALIDA                                                       # ============================================================================================================
# ============================================================================================================================ #



def CrearCarpetaSalida(folder_path, base_file_name):

    # ── 📁 CREAR CARPETA DE SALIDA ───────────────────────────────────────── #
    if not os.path.exists(folder_path):
        print("\n📂 Creando carpeta de salida...")
        print(f"   Ruta: {folder_path}")
       
        try:
            os.makedirs(folder_path, exist_ok=True)
        except PermissionError:
            print(f"❌ Permiso denegado para crear carpeta: {folder_path}\n")
            sys.exit(1)
        except OSError as e:
            print(f"❌ Error inesperado al crear la carpeta: {e}\n")
            sys.exit(1)
    else:
        print(f"\n📂 Carpeta ya existe en ruta: {folder_path}")

    # ── 📄 CREAR ARCHIVOS VACÍOS ─────────────────────────────────────────── #
    print("\n🛠️  Preparando archivos de salida...\n")

    for i in range(1, config.num_archivos + 1):
        file_name = f"{base_file_name}_{i:03}.h"
        file_path = os.path.join(folder_path, file_name)

        if not os.path.exists(file_path):
            print(f"📝 Creando archivo vacío → {file_name}")
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    pass  # archivo vacío
            except PermissionError:
                print(f"❌ Permiso denegado para crear archivo: {file_path}")
                sys.exit(1)
            except OSError as e:
                print(f"❌ Error inesperado al crear el archivo: {e}")
                sys.exit(1)
        else:
            print(f"📄 Archivo ya existe → {os.path.abspath(file_path)}")

    # ── ✅ RESUMEN FINAL ─────────────────────────────────────────────────── #
    print("\n" + "═" * 60)
    print("✅ ARCHIVOS DE SALIDA LISTOS".center(60))
    print("═" * 60)
    print(f"📁 Carpeta:         {folder_path}")
    print(f"📄 Archivos creados: {config.num_archivos}")
    print(f"📌 Formato:         {base_file_name}_NNN.h\n")




# ============================================================================================================================ #
#                                                  Comprobación configuracion                                                  # ============================================================================================================
# ============================================================================================================================ #

def comprobarConfiguracion():

    print("\n\033[96m" + "═" * 50)
    print("📦 ESTADO ACTUAL DE VARIABLES".center(50))
    print("═" * 50 + "\033[0m")

    print(f"📁 Número de archivo         ➜ {config.Number_File}")
    print(f"🔢 Ítems inicio              ➜ {config.Number_Items_Inicio}")
    print(f"🔢 Ítems fin                 ➜ {config.Number_Items_Fin}")
    print(f"🔐 Total de claves           ➜ {config.total_claves}")
    print(f"📄 Claves por archivo        ➜ {config.claves_por_archivo}")
    print(f"📉 Mínimo por archivo        ➜ {config.claves_por_archivo_min}")
    print(f"🧮 Número de archivos        ➜ {config.num_archivos}")
    print(f"➕ Resto (último archivo)    ➜ {config.resto}")

    print("\033[92m" + "═" * 50 + "\033[0m\n")


    if (
        config.num_archivos == 0
        or config.Number_Items_Inicio <= 0
        or config.Number_Items_Fin <= 0
    ):
        print("⚠️  Configuración incompleta: debes definir el número de claves y archivos antes de continuar.")
        from menu.menu import mostrar_menu_create_output_folder
        mostrar_menu_create_output_folder()

    else:
        return #Vuelve al flujo normal del programa para generar las claves













# ============================================================================================================================ #
#                                     Crear la carpeta y el archivo de entrada vacíos                                          # ============================================================================================================
# ============================================================================================================================ #

def create_input_folder():
    folder_path = input_folder
    file_name = input_file_name
    file_path = os.path.join(folder_path, file_name)

    
    # Crear carpeta si no existe
    if not os.path.exists(folder_path):
        print("Creando carpeta... Ruta:", folder_path)
        try:
            os.makedirs(folder_path, exist_ok=True)
        except PermissionError:
            print("❌ Permiso denegado para crear carpeta:", folder_path)
            sys.exit(1)
        except OSError as e:
            print(f"❌ Error inesperado al crear la carpeta: {e}")
            sys.exit(1)
    else:
        print("Carpeta ya existe en ruta:", folder_path)


    # Eliminar archivo si existe
    if os.path.exists(file_path):
        try:
            print("Archivo ya existe en ruta:", os.path.abspath(file_path))
            os.remove(file_path)
            print("✅   Archivo eliminado:", file_path)
        except PermissionError:
            print("❌   No tienes permisos para eliminar el archivo:", file_path)
        except OSError as e:
            print(f"❌   Error inesperado: {e}")
        else:
            print("⚠️   El archivo no existe:", file_path)

        
    
    # Crear archivo vacío si no existe
    if not os.path.exists(file_path):
        print("Creando archivo... Ruta:", file_path)
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                pass  # archivo vacío
        except PermissionError:
            print("❌ Permiso denegado para crear archivo:", file_path)
            sys.exit(1)
        except OSError as e:
            print(f"❌ Error inesperado al crear el archivo: {e}")
            sys.exit(1)
    else:
        print("Archivo ya existe en ruta:", os.path.abspath(file_path))

