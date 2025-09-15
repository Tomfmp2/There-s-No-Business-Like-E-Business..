#Login ambos

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
         

            
