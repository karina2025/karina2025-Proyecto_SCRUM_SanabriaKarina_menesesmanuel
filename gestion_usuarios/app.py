import usuarios
import json

def main():
    while True:
        print("\nOpciones:")
        print("1. Agregar un nuevo dato")
        print("2. Salir")
        
        opcion = input("Elige una opción (1/2): ")
        
        if opcion == '1':
            agregar_dato()
        elif opcion == '2':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == '__main__':
    main()