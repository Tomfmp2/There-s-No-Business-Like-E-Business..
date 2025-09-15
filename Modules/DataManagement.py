import os
import Modules.js as js
# Variables globales
usr = ""

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
        "CARRITO":{}
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
        "PRODUCTOS": {}
                  }
    }
    js.UpdateJson(js.JSON_CUENTAS, diccionario)

def Login(Op : int):
 # Esta funcion permite iniciar sesion en la aplicacion
 match Op:

  case 2:
   clear()
   global usr
   db=js.ReadJson(js.JSON_TIENDAS)
   while True:
             
      print("""
            -----------------------------------
            |        Bienvenido Dueño       |
            -----------------------------------
            """)
      usr = input("Porfavor ingrese su usuario: ").upper().strip()
      if usr in db:
        while True: 
            print(f"""
            -----------------------------------
            |        Bienvenido {usr}     |
            -----------------------------------
            """)
            ContraseñaRegistrada=input('Ingrese la contraseña de su cuenta: ').upper().strip()
            if db[usr]["CONTRASEÑA"] == ContraseñaRegistrada: 
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
      usr=input("Porfavor ingrese su usuario: ").upper().strip()
      if usr in db:
        while True: 
            ContraseñaRegistrada=input('Ingrese la contraseña de su cuenta: ').upper().strip()
            if db[usr]["CONTRASEÑA"] == ContraseñaRegistrada: 
                return
            else:
                print("Contraseña incorrecta")
                clear()
      else: 
         print("Usuario no encontrado")
         clear()

def AgregarOtravez ():
    clear()
    while True: 
        volverAgregar = input('¿Desea volver a agregar otro producto? (s/n):').upper()
        match volverAgregar:
            case "S":
                return "S"
            case "N":
                return 
            case _:
                clear()
                print('Opcion invalida.. ')
                presionar()

def ElminiarOtraVez():
    clear()
    while True: 
        volverAgregar = input('¿Desea volver a eliminar otro producto? (s/n):').upper()
        match volverAgregar:
            case "S":
                return "S"
            case "N":
                return 
            case _:
                clear()
                print('Opcion invalida.. ')
                presionar()

# Esta funcion agrega los productos a la tienda del vendedor 
def AgregarProductoTienda():
    db = js.ReadJson(js.JSON_TIENDAS)
    global usr
    while True:
        nombreProducto = input('Ingrese el nombre del producto a Agregar:')
        if nombreProducto in db: 
            clear()
            print('Nombre de producto ya registrado.. intente otra vez')
            presionar()
        else:
            clear()
            
            while True:
                try:
                    precio = int(input(f'Ingrese el Precio del producto {nombreProducto}:\n'))
                    producto =  {nombreProducto:precio}
                    
                    js.UpdateJson(js.JSON_TIENDAS, producto, [usr]["PRODUCTOS"])
                    opcion=AgregarOtravez()
                    if opcion == "S":
                        break
                    else:                            
                        return
                except ValueError:
                    clear()
                    print('Solo se pueden ingesar numeros..')
                    presionar()

def EliminarProductoTienda():
    global usr
    db2=js.ReadJson(js.JSON_CUENTAS)
    while True:
       for g, i in db2[usr]["PRODUCTOS"].keys():
                            print(f"""
                                --------Producto--------
                                Nombre: {g}
                                Precio: {[usr]["PRODUCTOS"][g]["PRECIO"]}
                                Cantidad: {[usr]["PRODUCTOS"][g]["CANTIDAD"]}
                                """) 
       while True:  
            producto=input("Porfavor ingrese el nombre del producto que desea eliminar: ")
            if producto in db2[usr]["PRODUCTOS"].keys():
                del db2[usr]["PRODUCTOS"][producto]
                print(f"Producto {producto} eliminado correctamente")
                presionar()
                op=ElminiarOtraVez()
                if op == "S":
                    break
                else:
                    return      
        


# Esta fincion guarda productos en un apartado llamado CARRITO 
def AgregarProductoCarrito():
    global usr
    db=js.ReadJson(js.JSON_TIENDAS)
    db2=js.ReadJson(js.JSON_CUENTAS)
    while True:
        producto=str(input("Porfavor ingrese el nombre del producto que desea comprar: "))
        tienda=str(input("Ahora porfavor ingrese el nombre de la tienda que posee ese producto: "))
        if tienda in db:
            while True:
                if producto in db[tienda]["PRODUCTOS"] and producto not in db2[usr]["CARRITO"]:
                    cantidad=int(input("Porfavor ingrese la cantidad del producto que desea agregar al carrito: "))
                    while True: 
                        if cantidad > 0 and db[tienda]["PRODUCTOS"][producto]["CANTIDAD"] > cantidad:
                            dic={
                                producto: {
                                "CANTIDAD": cantidad,
                                "PRECIO": db[tienda]["PRODUCTOS"][producto]["VALOR"]
                                    }
                                }
                            js.UpdateJson(js.JSON_CUENTAS, dic, [usr]["CARRITO"])
                            print(f"El producto {producto} de la tienda {tienda} a sido agregado correctamente a su carrito")
                            presionar()
                            opcion=AgregarOtravez()
                            if opcion == "S":
                                break
                            else:
                               return
                        else:
                            print("El valor ingresado no es soportado, intente de nuevo porfavor")
                            presionar()
                elif producto in db2[usr]["CARRITO"]:
                    cantidad=int(input("Porfavor ingrese la cantidad del producto que desea agregar al carrito (Este ya se encuentra en el carrito): "))
                    precio=db2[usr]["CARRITO"][producto]["PRECIO"]
                    precio=db[tienda]["PRODUCTOS"][producto]["VALOR"] * cantidad
                    cantidadtot=db2[usr]["CARRITO"][producto]["CANTIDAD"] + cantidad
                    dic={
                                producto: {
                                "CANTIDAD": cantidadtot,
                                "PRECIO": precio
                                    }
                                }
                    js.UpdateJson(js.JSON_CUENTAS, dic, [usr]["CARRITO"])
                    print(f"El producto {producto} de la tienda {tienda} a sido agregado correctamente a su carrito")
                    presionar()
                    opcion=AgregarOtravez()
                    if opcion == "S":
                        break
                    else:
                        return            
                else:
                    print("El producto que ha ingresado no se encuentra en la tienda mencionada")
                    presionar()
        else:
            print("La tienda que ha ingresado no se encuentra registrada")
            presionar()

def EliminarDelCarrito():
    global usr
    while True:
        db=js.ReadJson(js.JSON_CUENTAS)
        for g, i in db[usr]["CARRITO"].keys():
                            print(f"""
                                --------Producto--------
                                Nombre: {g}
                                Precio: {[usr]["CARRITO"][g]["PRECIO"]}
                                Cantidad: {[usr]["CARRITO"][g]["CANTIDAD"]}
                                """)
        while True:  
            producto=input("Porfavor ingrese el nombre del producto que desea eliminar de su carrito: ")
            if producto in db[usr]["CARRITO"].keys():
                del db[usr]["CARRITO"][producto]
                print(f"Producto {producto} eliminado correctamente")
                presionar()
                op=ElminiarOtraVez()
                if op == "S":
                    break
                else:
                    return

def Pagar():
    clear()
    global usr
    while True:
        db=js.ReadJson(js.JSON_CUENTAS)
        for g, i in db[usr]["CARRITO"].keys():
                            print(f"""
                                --------Producto--------
                                Nombre: {g}
                                Precio: {[usr]["CARRITO"][g]["PRECIO"]}
                                Cantidad: {[usr]["CARRITO"][g]["CANTIDAD"]}
                                """)
                            total += [usr]["CARRITO"][g]["PRECIO"]
        
        print(f"El Valor total del carrito es de")
        
    
    
    pass        
def MostrarProductos():
    clear()
    db = js.ReadJson(js.JSON_TIENDAS)
    for x,i in db.items():
        try:
            for t in i:
                if t == "PRODUCTOS":
                    for g in i["r"].keys():
                        prodcuto = g
                        print(f"""
                            --------Producto--------
                            Producto: {prodcuto}
                            Precio: {i["r"][g]}
                            Tienda: {i["NOM"]}
                            """)
        except:
            pass