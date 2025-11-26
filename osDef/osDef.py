import os
import shutil


# ============================================================================================================================ #
#                                                    Borrar carpeta de un directorio                                           #
# ============================================================================================================================ #
def borrarCarpeta(ruta: str):
    try:
        if os.path.exists(ruta):
            shutil.rmtree(ruta)  # elimina carpeta y contenido
            print(f"🗑️ Carpeta eliminada correctamente: {ruta}")
        else:
            print(f"⚠️ La carpeta no existe: {ruta}")
    except PermissionError:
        print(f"⛔ No tienes permisos para borrar la carpeta: {ruta}")
    except Exception as e:
        print(f"⚠️ Error inesperado al borrar {ruta}: {e}")
