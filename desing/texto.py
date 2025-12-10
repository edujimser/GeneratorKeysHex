import os
import sys

# Si se ejecuta como script directo, asegurar que la carpeta raíz esté en sys.path
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root not in sys.path:
    sys.path.insert(0, root)
    
    
"""
Funciones de texto.py

    1. cabezera de texto --> cabezera_texto() -----------------------------------------------------------------------------
    
    ════════════════════════════════════════════════════════════
    🎛️  CONFIGURACIÓN DE CARPETA PARA CLAVES MIFARE CLASSIC   
    ════════════════════════════════════════════════════════════
    
"""

def cabezera_texto(texto, color, color_reset):
    print("\n" + color + "═" * 60 + color_reset)
    prefijo = "🎛️  "
    print(color + prefijo + str(texto).center(60 - len(prefijo)) + color_reset)
    print(color + "═" * 60 + color_reset)

