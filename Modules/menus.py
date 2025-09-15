from typing import Dict, List
import os
import Modules.js as js

JSON_TIENDAS = "data/JsonTiendas.json"

def clear():
    os.system('cls')

def presionar():
    input("\nPresione Enter para continuar...")


# Menú de idiomas

def seleccionar_idioma():
    clear()
    print("""
    ===================================
            🌍 Seleccione idioma
    ===================================
    1. Español
    2. English
    """)
    while True:
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            return "es"
        elif opcion == "2":
            return "en"
        else:
            print("⚠️ Opción no válida")
            presionar()
            clear()

# Menú principal

def menu_principal():
    while True:
        clear()
        print("""
        ===================================
                🛒 E-Commerce
        ===================================
        1. Registrarse
        2. Iniciar sesión
        3. Salir
        """)
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            clear()
            print("¿Desea registrarse como?\n1. Usuario\n2. Vendedor")
            tipo = input("Seleccione: ")
            if tipo == "1":
                RegistrarCuentaUsuario()
                print("✅ Usuario registrado con éxito")
            elif tipo == "2":
                RegistrarVendedor()
                print("✅ Vendedor registrado con éxito")
            else:
                print("⚠️ Opción inválida")
            presionar()

        elif opcion == "2":
            clear()
            print("¿Desea iniciar sesión como?\n1. Usuario\n2. Dueño/Vendedor")
            tipo = input("Seleccione: ")
            if tipo in ["1", "2"]:
                Login(int(tipo))
                if tipo == "1":
                    menu_usuario()
                else:
                    menu_dueno()
            else:
                print("⚠️ Opción inválida")
                presionar()

        elif opcion == "3":
            clear()
            print("👋 Gracias por usar el sistema")
            break

        else:
            print("⚠️ Opción no válida")
            presionar()


# Menú usuario

def menu_usuario():
    while True:
        clear()
        print("""
        ===================================
                👤 Menú Usuario
        ===================================
        1. Ver productos
        2. Comprar
        3. Cerrar sesión
        """)
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            MostrarProductos()
            subMenuUsusario()
            presionar()
        elif opcion == "2":
            metodoPago()  #Falta funcionnnnn
            presionar()
        elif opcion == "3":
            break
        else:
            print("⚠️ Opción inválida")
            presionar()

# submenu para agregar o quitar producto

def subMenuUsusario():
    while True
        clear()
        print("""
        =========================
        ---❓Que deseas hacer---
        =========================
        - 1. Agregar producto   :
        - 2. Quitar producto    :
        - 3. Salir              :
        =========================

        """)
        if opcion == 1:
            AgregarProductoCarrito()
        elif opcion == 2:
            pass # Pendiente funcion
        else:
            break



# Menú dueño/vendedor

def menu_dueno():
    while True:
        clear()
        print("""
        ===================================
            🏪 Menú Vendedor
        ===================================
        1. Ver productos
        2. Agregar producto
        3. Eliminar producto
        4. Cerrar sesión
        """)
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            MostrarProductos()
            presionar()
        elif opcion == "2":
            AgregarProductoTienda()
            AgregarOtravez ()
            presionar()
        elif opcion == "3":
            print("Pendiente funcion")  #pendiente funcionn
            presionar()
        elif opcion == "4":
            break
        else:
            print("⚠️ Opción inválida")
            presionar()

def metodoPago():
    while True
        clear()
            print(""" 
            =============================
            --💳Elije el metodo de pago--
            =============================
            - 1. Tarjeta de credito     *
            - 2. Tarjeta debito         *
            - 3. PSE                    *
            - 4. Salir                  *
            ____________________________*

            """)
            opcion = int(input('Ingrese una opcion: '))
                if opcion == 1:
                    pass 
                elif opcion == 2:
                    pass
                elif opcion == 3:
                    pass
                else:
                    print('Ingrese una opcion valida')
                    return
                









