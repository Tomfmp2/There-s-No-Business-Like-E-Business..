from typing import Dict, List
import os
import Modules.js as js

JSON_TIENDAS = "data/JsonTiendas.json"

def clear():
    os.system('cls')

def presionar():
    input("\nPresione Enter para continuar...")

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

                    print(""" 
                    ______________________________

                    Como deseas registrarte:
                    1 como usuario
                    2 como venderdor
                    ______________________________
                    
                    """)

                    int(input('Ingresa una opcion: '))

                    if opcion == 1:
                        RegistrarCuentaUsuario()
                    elif:
                        RegistrarVendedor()
                    return

            match opcion:
                case 2:
                    Login(Op : int)
        


def vistaCuentaCreada():

    print("""
    _________________________

    -----¡Bienvenido!--------
    _________________________
    
    """)



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
            presionar()
        elif opcion == "2":
            print("Pendiente funcion")
            presionar()
        elif opcion == "3":
            break
        else:
            print("⚠️ Opción inválida")
            presionar()

# ---------------------------
# Menú dueño/vendedor
# ---------------------------
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
            print("Pendiente funcion")
            presionar()
        elif opcion == "3":
            print("Pendiente funcion")
            presionar()
        elif opcion == "4":
            break
        else:
            print("⚠️ Opción inválida")
            presionar()












