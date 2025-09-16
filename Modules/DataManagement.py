import os
import Modules.js as js
import time as t
# Variables globales
usr = ""

def clear (): # Limpiar pantalla
    os.system('cls' if os.name == 'nt' else 'clear')

def presionar(): # Pausa o espera para seguir con la ejecucion
    input("\nPresione Enter para continuar...")

def InicarJsons(): # Funcion para iniciar los archivos json
    js.InitJson(js.JSON_CUENTAS, {})
    js.InitJson(js.JSON_TIENDAS, {})

# funcion para registrar nombre
def RegistrarNombre():
   while True:
      clear()
      try:   
         Nombre=str(input("Ingrese su nombre: ")).strip().upper()
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
        RegistroUser = str(input("Ingrese su nombre de usuario: ")).strip().upper()
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
        Contraseña = str(input("Ingrese su contraseña: ")).strip().upper()
        ConfirmarContraseña = str(input("Confirme su contraseña: ")).strip().upper()
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
        "CONTRASENA": RegistrarContraseña(),
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
        "CONTRASENA": RegistrarContraseña(),
        "PRODUCTOS": {}
                  }
    }
    js.UpdateJson(js.JSON_TIENDAS, diccionario)

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
            if db[usr]["CONTRASENA"] == ContraseñaRegistrada: 
                return
            else:
                print("Contraseña incorrecta")
                presionar()
                clear()
      else: 
         print("Usuario no encontrado")

         presionar()
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
            if db[usr]["CONTRASENA"] == ContraseñaRegistrada: 
                return
            else:
                print("Contraseña incorrecta")
                presionar()
                clear()
      else: 
         print("Usuario no encontrado")
         presionar()
         clear()

def AgregarOtravez ():
    clear()
    while True: 
        volverAgregar = input('¿Desea volver a agregar otro producto? (s/n):').strip().upper()
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
        volverAgregar = input('¿Desea volver a eliminar otro producto? (s/n):').strip().upper()
        match volverAgregar:
            case "S":
                return "S"
            case "N":
                return 
            case _:
                clear()
                print('Opcion invalida.. ')
                presionar()


def CantidadProducto():
    while True:
        clear()
        try:
            cantidad = int(input('Ingrese la cantidad del producto: '))
            if cantidad <= 0:
                clear()
                print('La cantidad debe ser un numero positivo')
                presionar()
            else:
                return cantidad
        except ValueError:
            clear()
            print('Solo se pueden ingesar numeros..')
            presionar()

# Esta funcion agrega los productos a la tienda del vendedor 
def AgregarProductoTienda():
    db = js.ReadJson(js.JSON_TIENDAS)
    global usr
    while True:
        nombreProducto = input('Ingrese el nombre del producto a Agregar:').strip().upper()
        if nombreProducto in db[usr]["PRODUCTOS"]: 
            clear()
            print('Nombre de producto ya registrado.. intente otra vez')
            presionar()
        else:
            clear()
            
            while True:
                try:
                    precio = int(input(f'Ingrese el Precio del producto {nombreProducto}: '))
                    cantidad = CantidadProducto()
                    producto =  {nombreProducto:{
                            "PRECIO": precio,
                            "CANTIDAD": cantidad
                            }
                        }
                    js.UpdateJson(js.JSON_TIENDAS, producto, [usr,"PRODUCTOS"])
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
    db2=js.ReadJson(js.JSON_TIENDAS)
    while True:
       clear()
       for g, i in db2[usr]["PRODUCTOS"].items():
                            print(f"""
========================
--------Producto--------
========================
    Nombre: {g}
    Precio: {i["PRECIO"]}
    Cantidad: {i["CANTIDAD"]}
========================
                                """) 
       while True:  
            producto=input("Porfavor ingrese el nombre del producto que desea eliminar: ").strip().upper()
            if producto in db2[usr]["PRODUCTOS"].keys():
                del db2[usr]["PRODUCTOS"][producto]
                js.UpdateJson(js.JSON_TIENDAS, db2)
                print(f"Producto {producto} eliminado correctamente")
                presionar()
                op=ElminiarOtraVez()
                if op == "S":
                    break
                else:
                    return
            else:
                clear()
                print("El producto que ha ingresado no se encuentra en su tienda")
                slr = input("Desea intentarlo de nuevo? (S/N): ").strip().upper()
                match slr:
                    case "S":
                        break
                    case "N":
                        return
                    case _:
                        print("Opcion no valida")   
                        presionar()  
                presionar()      

def VerProductosMiTienda():
    global usr
    db = js.ReadJson(js.JSON_TIENDAS)

    if usr not in db:
        print(f"El usuario '{usr}' no existe en la base de datos")
        return
    
    if "PRODUCTOS" not in db[usr]:
        print(f"El usuario '{usr}' no tiene productos registrados")
        return

    productos = db[usr]["PRODUCTOS"]

    if not productos:
        print("No hay productos para mostrar")
        return

    while True:
        clear()  # limpia la pantalla cada vez que se muestran los productos

        for g, i in productos.items():
            print(f"""
========================
--------Producto--------
========================
    Nombre: {g}
    Precio: {i["PRECIO"]}
    Cantidad: {i["CANTIDAD"]}
========================
            """)

        seguir = input("¿Desea seguir viendo sus productos? (S/N): ").strip().upper()
        if seguir == "S":
            continue  # vuelve al inicio del while y refresca la pantalla
        elif seguir == "N":
            break      # sale del while y termina la función
        else:
            print("Opción no válida")
            presionar()  # pausar antes de reintentar

def VerProductosCarrito():
    clear()
    global usr
    db = js.ReadJson(js.JSON_CUENTAS)
    total = 0
    if not db[usr]["CARRITO"]:
        print("No hay productos en el carrito")
        presionar()
        return
    for g, i in db[usr]["CARRITO"].items():
                            print(f"""
========================
--------Producto--------
======================== 
    Nombre: {g}
    Precio: {i["PRECIO"]}
    Cantidad: {i["CANTIDAD"]}   
========================
                                """)
    total += db[usr]["CARRITO"][g]["PRECIO"]
    print(f"El Valor total del carrito es de {total}")
    while True:
        op = input("¿Desea proceder al pago? (S/N): ").strip().upper()
        match op:
            case "S":
                Pagar()
                return
            case "N":
                return
            case _:
                print("Valor no soportado")
                presionar()
# Esta fincion guarda productos en un apartado llamado CARRITO 
def AgregarProductoCarrito():
    global usr
    db=js.ReadJson(js.JSON_TIENDAS)
    db2=js.ReadJson(js.JSON_CUENTAS)
    while True:
        producto=str(input("Porfavor ingrese el nombre del producto que desea comprar: ")).strip().upper()
        tienda=str(input("Ahora porfavor ingrese el nombre de la tienda que posee ese producto: ")).strip().upper()
        if tienda in db:
            while True:
                if producto in db[tienda]["PRODUCTOS"] and producto not in db2[usr]["CARRITO"]:
                    cantidad=int(input("Porfavor ingrese la cantidad del producto que desea agregar al carrito: "))
                    while True: 
                        if cantidad > 0 and db[tienda]["PRODUCTOS"][producto]["CANTIDAD"] > cantidad:
                            dic={
                                producto: {
                                "CANTIDAD": cantidad,
                                "PRECIO": db[tienda]["PRODUCTOS"][producto]["PRECIO"] * cantidad
                                    }
                                }
                            js.UpdateJson(js.JSON_CUENTAS, dic, [usr, "CARRITO"])
                            ct= db[tienda]["PRODUCTOS"][producto]
                            ct -= cantidad
                            js.UpdateJson(js.JSON_TIENDAS, db)
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
                            break
                elif producto in db2[usr]["CARRITO"]:
                    cantidad=int(input("Porfavor ingrese la cantidad del producto que desea agregar al carrito (Este ya se encuentra en el carrito): "))
                    precio=db2[usr]["CARRITO"][producto]["PRECIO"]
                    precio=db[tienda]["PRODUCTOS"][producto]["PRECIO"] * cantidad
                    cantidadtot=db2[usr]["CARRITO"][producto]["CANTIDAD"] + cantidad
                    dic={
                                producto: {
                                "CANTIDAD": cantidadtot,
                                "PRECIO": precio
                                    }
                                }
                    js.UpdateJson(js.JSON_CUENTAS, dic, [usr, "CARRITO"])
                    db[tienda]["PRODUCTOS"][producto] -= cantidad
                    js.UpdateJson(js.JSON_TIENDAS, db)
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
                    break
        else:
            print("La tienda que ha ingresado no se encuentra registrada")
            presionar()

def EliminarDelCarrito():
    global usr
    while True:
        db=js.ReadJson(js.JSON_CUENTAS)
        for g, i in db[usr]["CARRITO"].items():
                            print(f"""
====================================                            
--------------Producto--------------
====================================                                
    Nombre: {g}
    Precio: {i["PRECIO"]}
    Cantidad: {i["CANTIDAD"]}
====================================
""")
        while True:  
            producto=input("Porfavor ingrese el nombre del producto que desea eliminar de su carrito: ").strip().upper()
            if producto in db[usr]["CARRITO"].keys():
                del db[usr]["CARRITO"][producto]
                js.UpdateJson(js.JSON_CUENTAS,db)
                print(f"Producto {producto} eliminado correctamente")
                presionar()
                op=ElminiarOtraVez()
                if op == "S":
                    break
                else:
                    return
            else:
                print("El producto que ha ingresado no se encuentra en su carrito")
                presionar()

def Pagar():
    import time
    clear()
    global usr

    db = js.ReadJson(js.JSON_CUENTAS)

    # Verificar usuario
    if usr not in db:
        print(f"Usuario '{usr}' no encontrado.")
        presionar()
        return

    # Asegurar que CARRITO exista
    carrito = db[usr].get("CARRITO", {})
    if not isinstance(carrito, dict):
        carrito = {}
        db[usr]["CARRITO"] = {}

    # Si está vacío
    if not carrito:
        print("Su carrito está vacío.")
        presionar()
        return

    total = 0
    for nombre, item in carrito.items():
        cantidad = item.get("CANTIDAD", 0)
        precio_total = item.get("PRECIO", 0)

        print(f"""
========================
--------Producto--------
======================== 
    Nombre: {nombre}
    Cantidad: {cantidad}
    Subtotal: {precio_total}
========================
""")
        total += precio_total

    print(f"El valor total del carrito es de {total}")

    op = input("Presione S para continuar con el pago, o N para cancelarlo: ").strip().upper()
    if op == "S":
        MetodoPago()  # Procesar pago

        # Vaciar carrito y guardar
        db[usr]["CARRITO"] = {}
        js.UpdateJson(js.JSON_CUENTAS, db[usr], [usr])

        print("Pago realizado exitosamente. Su carrito ha sido vaciado.")
        presionar()
        return

    elif op == "N":
        print("Saliendo al menú principal...")
        time.sleep(2)
        return

    else:
        print("Valor no soportado")
        presionar()
        return


def MetodoPago():
    while True:
        clear()
        print(""" 
=============================
--💳Elije el metodo de pago--
=============================
    - 1. Tarjeta de credito *
    - 2. Tarjeta debito     *
    - 3. PSE                *
                            *
=============================

        """)
        metodo = str(input("Porfavor ingrese el metodo de pago a usar (Tarjeta|Nequi): ")).strip()
        match metodo:
            case "1":
                numeroTarjeta = int(input("Ingrese el numero de su tarjeta: "))
                fecha = str(input("Ingrese la fecha en la cual fue expedida la tarjeta"))
                # Leer como string para poder usar len()
                ccv = input("Ingrese el CCV de su tarjeta: ").strip()

                # validar que sean dígitos y longitud correcta
                if ccv.isdigit() and len(ccv) == 3:
                    print("Gracias por tu compra todos los elementos de tu carrito han sido pagados")
                    presionar()
                    return 
                else:
                    print("El ccv proporcionado no es valido, abortado el pago")
                    t.sleep(1)
                    break

            case "2":
                # Leer como string para poder usar len()
                codigo = input("Ingrese su clave dinamica: ").strip()

                # validar que sean dígitos y longitud correcta
                if not (codigo.isdigit() and len(codigo) == 6):
                    print("El codigo proporcionado no es valido, abortado el pago")
                    t.sleep(1)
                    break 
                else: 
                    print("Gracias por tu compra todos los elementos de tu carrito han sido pagados")
                    presionar()
                    return

            case _: 
                print("Porfavor elija una de las opciones dadas")
                presionar()


def MostrarProductos():
    clear()
    db = js.ReadJson(js.JSON_TIENDAS)

    for tienda, datos in db.items():
        try:
            productos = datos.get("PRODUCTOS", {})
            for nombre, info in productos.items():
                print(f"""
========================
------- Producto --------
========================
    Nombre: {nombre}
    Precio: {info['PRECIO']}
    Cantidad: {info['CANTIDAD']}
    Tienda: {datos.get('NOM', tienda)}
========================
                """)
        except Exception as e:
            print("Error al mostrar productos:", e)
    presionar()