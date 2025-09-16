from typing import Dict, List
import os
import Modules.js as js
import Modules.DataManagement as dm

JSON_TIENDAS = "data/JsonTiendas.json"

# Menú de idiomas

def seleccionar_idioma():
    dm.clear()
    print("""
    ====================================
    --------🌍 Seleccione idioma--------
    ====================================
        1. Español
        2. English
    ====================================
    """)

"""
    while True:
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            return "es"
        elif opcion == "2":
            return "en"
        else:
            print("⚠️ Opción no válida")
            dm.presionar()
            dm.clear()
"""
# Menú principal

def menu_principal():
    while True:
        dm.clear()
        print("""
        =============================
        --------🛒 E-Commerce--------
        =============================
            1. Registrarse
            2. Iniciar sesión
            3. Salir
        =============================
        """)
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            dm.clear()
            print("¿Desea registrarse como?\n1. Usuario\n2. Vendedor")
            tipo = input("Seleccione: ")
            if tipo == "1":
                dm.RegistrarCuentaUsuario()
                print("✅ Usuario registrado con éxito")
            elif tipo == "2":
                dm.RegistrarVendedor()
                print("✅ Vendedor registrado con éxito")
            else:
                print("⚠️ Opción inválida")
            dm.presionar()
        elif opcion == "2":
            dm.clear()
            print("¿Desea iniciar sesión como?\n1. Usuario\n2. Dueño/Vendedor")
            tipo = input("Seleccione: ")
            if tipo in ["1", "2"]:
                dm.Login(int(tipo))
                if tipo == "1":
                    menu_usuario()
                else:
                    menu_dueño()
            else:
                print("⚠️ Opción inválida")
                dm.presionar()

        elif opcion == "3":
            dm.clear()
            print("👋 Gracias por usar el sistema")
            break

        else:
            print("⚠️ Opción no válida")
            dm.presionar()


# Menú usuario

def menu_usuario():
    while True:
        dm.clear()
        print("""
===================================
        👤 Menú Usuario
===================================
    1. Ver productos
    2. Ver carrito
    3. Cerrar sesión
===================================
        """)
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            dm.MostrarProductos()
        elif opcion == "2":
            subMenuUsusario()
        elif opcion == "3":
            break   
        else:
            print("⚠️ Opción inválida")
            dm.presionar()

# submenu para agregar o quitar producto

def subMenuUsusario():
    while True:
        dm.clear()
        print("""
        =================================
        -----------🛒 Carrito------------
        =================================
        - 1. Ver productos guardados    :
        - 2. Agregar producto           :
        - 3. Quitar producto            :
        - 4. Pagar                      :
        - 5. Salir                      :
        =================================

        """)
        opcion = input("Ingrese una opcion: ")
        match opcion:
            case "1":
                dm.VerProductosCarrito()
            case "2":
                dm.AgregarProductoCarrito()
            case "3":
                dm.EliminarDelCarrito()  
            case "4":
                dm.Pagar()
                print("Gracias por su compra")
                dm.presionar()
            case "5":
                return
            case _:
                print("⚠️ Opción inválida")
                dm.presionar()



# Menú dueño/vendedor
def menu_dueño():
    while True:
        dm.clear()
        print("""
        ================================
        --------🏪 Menú Vendedor--------
        ================================
            1. Ver productos
            2. Agregar producto
            3. Eliminar producto
            4. Cerrar sesión
        ================================
        """)
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            dm.VerProductosMiTienda()
            dm.presionar()
        elif opcion == "2":
            dm.AgregarProductoTienda()
            dm.presionar()
        elif opcion == "3":
            dm.EliminarProductoTienda()
            dm.presionar()
        elif opcion == "4":
            break
        else:
            print("⚠️ Opción inválida")
            dm.presionar()

# Menú admin            
def vistaAdmin():
    while True:
        dm.clear()
        print("""
=============================
--------🛠️ Menú Admin--------
=============================
    1. Ver productos
    2. Agregar producto
    3. Eliminar producto
    4. Salir
=============================
            """)
        opcion = input("Seleccione una opción: ")
        match opcion:
            case "1":
                dm.MostrarProductos()
                dm.presionar()
            case "2":
                dm.AgregarProductoTienda()
                dm.presionar()
            case "3":
                dm.EliminarProductoTienda()
                dm.presionar()
            case "4":
                break
            case _:
                print("⚠️ Opción inválida")
                dm.presionar()