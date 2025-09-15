import js as js
import json
import os
from typing import Dict, List

JSON_TIENDAS = "data/JsonTiendas.json"

def vistaprincipal():

    print("""
    -----------------------------------
    -------Bienvenido al sistema-------
    -----------------------------------""")

    opcion = int(input(
        
        """
        -------------------------
        ____Elige una opcion:____
        -------------------------

        _________________________
                                 *
        --1 Resgistrarme         *
        --2 Iniciar sesion       *
        _________________________*


        """))

            match opcion:
                case 1:
                    pass

            match opcion:
                case 2:
                    pass
        


def vistaCuentaCreada():

    print("""
    _________________________

    -----¡Bienvenido!--------
    _________________________
    
    """)


def mostrar_productos():

    data = ReadJson(JSON_TIENDAS)

    if not data:
        print("No hay tiendas registradas.")
        return
    
    print("\nProductos disponibles:\n")

    for tienda, info in data.items():
        print(f" Tienda: {tienda}")
        productos: List[Dict] = info.get("productos", [])
        if not productos:
            print("   (Sin productos)\n")
            continue
        
        for producto in productos:

            print(f"   🔹 ID: {producto['id']}")
            print(f"      Nombre: {producto['nombre']}")
            print(f"      Precio: ${producto['precio']:,}")
            print(f"      Stock: {producto['stock']}\n")

    print(" ------Fin de lista-------.\n")

    







