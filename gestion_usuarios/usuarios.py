import json
import os

usuarios = 'usuarios.json'
def cargar_datos():
    if os.path.exists(usuarios):
        with open(usuarios, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    else:
        return []

def guardar_datos(datos):
    with open(usuarios, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

def agregar_dato():
    
    datos = cargar_datos()
    
    identificacion = input("Ingresa tu identificacion: ")
    nombre = input("Ingresa el nombre: ")
    apellido = input("Ingrese el apellido: ")
    edad = input("Ingresa la edad: ")
    tel = int(input("ingresa tu numero celular: "))
    correo = input("Añade tu correo :D: ")
    contraseña = input("crea tu contraseña: ")


    
    nuevo_dato = {
        "identificacion": identificacion,
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "telefono": tel,
        "correo": correo,
        "contraseña": contraseña
    }
    

    datos.append(nuevo_dato)
    guardar_datos(datos)
    print("Dato agregado exitosamente!")


### rama main (no supe como poner la rama main aparte :c)
def main():
    while True:
        print("""
* * * * * * * * * * * * * * *
*   Bienvenido              *
*    Escoge una opcion      * 
*     1 . Editar Usuario    * 
*     2 . Salir             *
* * * * * * * * * * * * * * *                                                        
""")
        
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            agregar_dato()
        elif opcion == '2':
            print("bye espero verte pronto :D...")
            break
        else:
            print("lo siento pero no puedes registrarte :c : ")

if __name__ == '__main__':
    main()

  
     

        
