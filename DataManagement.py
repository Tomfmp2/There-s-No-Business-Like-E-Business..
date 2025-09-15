import os
import Modules.js as js
def clear (): # Limpiar pantalla
    os.system('cls' if os.name == 'nt' else 'clear')
def precionar(): # Pausa o espera para seguir con la ejecucion
    input("\nPresione Enter para continuar...")

def InicarJsons(): # Funcion para iniciar los archivos json
    js.WriteJson(js.JSON_CUENTAS, {})

# funcion para registrar nombre
def RegistrarNombre():
   while True:
      clear()
      try:   
         Nombre=str(input("Ingrese su nombre: "))
         if not Nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
            Oprimir()
         elif not Nombre.replace(" ", "").isalpha():
            raise ValueError("El nombre solo puede contener letras.")
         else:
            return Nombre
      except ValueError as e:
         print(f"Error: {e}. Intente de nuevo.")
         precionar()
# funcion para registrar nombre de usuario
def RegistrarUser():
    while True:
        clear()
        RegistroUser = str(input("Ingrese su nombre de usuario: "))
        Datos = js.ReadJson(js.JSON_CUENTAS)
        if RegistroUser in Datos:
            clear()
            print("El nombre de usuario ya existe. Por favor, elija otro.")
            precionar()
        elif not RegistroUser.strip():
            clear()
            print("El nombre de usuario no puede estar vacío.")
            precionar()
        else:
            return RegistroUser

# funcion para registrar edad
def RegistrarEdad ():
    while True:
        clear()
        try:
            edad = int(input("Ingrese su edad: "))
            if edad < 0:
                clear()
                print("La edad debe ser un numero positivo")
                precionar()
            elif 0 <= edad < 18:
                clear()
                print("Debes ser mayor de edad para registrarse")
                precionar()
            else:
                return edad
        except ValueError:
            print("Por favot Solo ingrese numeros")
            precionar()

# funcion para registrar telefono
def RegistrarTelefono ():
    while True: 
        clear()
        try: 
            print("""
|-------------------------------|
|       Tipos de telefono       |
|                               |
|   1. Celular                  |
|   2. Fijo                     |
|-------------------------------|
""")
            TipoTelefono = int(input("Ingrese el tipo de telefono (1 o 2): "))
            match TipoTelefono:
                case 1: 
                    while True:
                        try:
                            numero = input("Ingrese su numero de celular (10 digitos): ")
                            if len(numero) == 10 and numero.isdigit():
                                return numero
                            else:
                                clear()
                                print("El numero de celular solamente debe tener 10 digitos")
                                presionar()
                        except ValueError:
                            clear()
                            print("Por favor solo ingrese numeros")
                            presionar()
                case 2:
                    while True:
                        try:
                            numero = input("Ingrese su numero de telefono fijo (7 digitos): ")
                            if len(numero) == 7 and numero.isdigit():
                                return numero
                            else:   
                                clear()
                                print("El numero de telefono fijo solamente debe tener 7 digitos")
                                presionar()
                        except ValueError:
                            clear()
                            print("Por favor solo ingrese numeros")
                            presionar() 
                case _:
                    clear()
                    print("Opcion no valida, ingrese 1 o 2")
                    presionar()
        except ValueError:
            print("Por favor solo ingrese numeros")
            presionar()
# funcion para registrar direccion
def RegistrarDireccion():
    while True:
        clear()
        try:
            Direccion = str(input("Ingrese su direccion: "))
            if not Direccion.strip():
                raise ValueError("La direccion no puede estar vacia.")
                precionar()
            else:
                return Direccion
        except ValueError as e:
            print(f"Error: {e}. Intente de nuevo.")
            precionar()

# funcion para registrar usuario
def RegistrarCuentaUsuario():
    diccionario ={
        RegistrarUser: {
        "NOMBRE": RegistrarNombre(),
        "EDAD": RegistrarEdad(),
        "TELEFONO": RegistrarTelefono(),
        "DIRECCION": RegistrarDireccion(), 
        "PRODUCTOS": []
                  }
    }
    js.UpdateJson(js.JSON_CUENTAS, diccionario)

# funcion para registrar cuneta de vendedor
def RegistrarVendedor():
    diccionario ={
        RegistrarUser: {
        "NOMBRE": RegistrarNombre(),
        "EDAD": RegistrarEdad(),
        "TELEFONO": RegistrarTelefono(),
        "D": RegistrarDireccion(), 
        "PRODUCTOS": []
                  }
    }
    js.UpdateJson(js.JSON_CUENTAS, diccionario)
