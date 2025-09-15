import Modules.DataManagement as dm
import Modules.menus as mn

if __name__ == "__main__":
    dm.InicarJsons()
    while True:
        dm.clear()
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            idioma =  "es"
            break
        elif opcion == "2":
            idioma = "en"
            break
        else:
            print("⚠️ Opción no válida")
            dm.presionar()
            dm.clear()
    
    mn.menu_principal()