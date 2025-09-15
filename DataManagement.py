import os
import Modules.js as js
def clear (): # Limpiar pantalla
    os.system('cls' if os.name == 'nt' else 'clear')
def presionar(): # Pausa o espera para seguir con la ejecucion
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
         presionar()
# funcion para registrar nombre de usuario
def RegistrarUser():
    while True:
        clear()
        RegistroUser = str(input("Ingrese su nombre de usuario: "))
        Datos = js.ReadJson(js.JSON_CUENTAS)
        if RegistroUser in Datos:
            clear()
            print("El nombre de usuario ya existe. Por favor, elija otro.")
            presionar()
        elif not RegistroUser.strip():
            clear()
            print("El nombre de usuario no puede estar vacío.")
            presionar()
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
                presionar()
            elif 0 <= edad < 18:
                clear()
                print("Debes ser mayor de edad para registrarse")
                presionar()
            else:
                return edad
        except ValueError:
            print("Por favot Solo ingrese numeros")
            presionar()

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
            presionar()

def RegistrarContraseña():
    while True:
        clear()
        Contraseña = str(input("Ingrese su contraseña: "))
        ConfirmarContraseña = str(input("Confirme su contraseña: "))
        if Contraseña != ConfirmarContraseña:
            clear()
            print("Las contraseñas no coinciden. Intente de nuevo.")
            presionar()
        elif not Contraseña.strip():
            clear()
            print("La contraseña no puede estar vacía.")
            presionar()
        else:
            return Contraseña
        
# funcion para registrar usuario
def RegistrarCuentaUsuario():
    diccionario ={
        RegistrarUser(): {
        "NOMBRE": RegistrarNombre(),
        "EDAD": RegistrarEdad(),
        "TELEFONO": RegistrarTelefono(),
        "DIRECCION": RegistrarDireccion(), 
        "CONTRASEÑA": RegistrarContraseña(),
                  }
    }
    js.UpdateJson(js.JSON_CUENTAS, diccionario)

# funcion para registrar cuneta de vendedor
def RegistrarVendedor():
    diccionario ={
        RegistrarUser(): {
        "NOMBRE": RegistrarNombre(),
        "EDAD": RegistrarEdad(),
        "TELEFONO": RegistrarTelefono(),
        "DIRECCION": RegistrarDireccion(),
        "CONTRASEÑA": RegistrarContraseña(),
        "PRODUCTOS": []
                  }
    }
    js.UpdateJson(js.JSON_CUENTAS, diccionario)

def Login(Op : int):
 # Esta funcion permite iniciar sesion en la aplicacion
 match Op:

  case 2:
   clear()
   db=js.ReadJson(js.JSON_TIENDAS)
   while True:
             
      print("""
            -----------------------------------
            |        Bienvenido Dueño       |
            -----------------------------------
            """)
      usrDue=input("Porfavor ingrese su usuario: ").upper().strip()
      if usrDue in db:
        while True: 
            print(f"""
            -----------------------------------
            |        Bienvenido {usuario}     |
            -----------------------------------
            """)
            ContraseñaRegistrada=input('Ingrese la contraseña de su cuenta: ').upper().strip()
            if db[usrDue]["CONTRASEÑA"] == ContraseñaRegistrada: 
                return
            else:
                print("Contraseña incorrecta")
                clear()
      else: 
         print("Usuario no encontrado")
         clear()  

  case 1:
   db=js.ReadJson(js.JSON_CUENTAS)
   while True:
             
      print("""
            -----------------------------------
            |        Bienvenido Usuario       |
            -----------------------------------
            """)
      usuario=input("Porfavor ingrese su usuario: ").upper().strip()
      if usuario in db:
        while True: 
            ContraseñaRegistrada=input('Ingrese la contraseña de su cuenta: ').upper().strip()
            if db[usuario]["CONTRASEÑA"] == ContraseñaRegistrada: 
                return
            else:
                print("Contraseña incorrecta")
                clear()
      else: 
         print("Usuario no encontrado")
         clear()
         