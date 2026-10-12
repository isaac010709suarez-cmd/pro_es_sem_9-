# Pila simple en Python
pila = []

def mostrar_menu():
    print("\n=== MENÚ DE PILA ===")
    print("1. Agregar elemento (Push)")
    print("2. Quitar elemento (Pop)")
    print("3. Ver el tope (Peek)")
    print("4. Mostrar pila")
    print("5. Salir")

# Pedimos el tamaño inicial
tamano = int(input("¿De qué tamaño máximo será la pila?: "))

while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-5): ")
    
    if opcion == "1":
        if len(pila) < tamano:
            elemento = input("Ingresa el valor: ")
            pila.append(elemento)
            print("¡Elemento agregado con éxito!")
        else:
            print("¡Error: La pila está llena!")
            
    elif opcion == "2":
        if len(pila) > 0:
            eliminado = pila.pop()
            print(f"Elemento eliminado: {eliminado}")
        else:
            print("¡Error: La pila está vacía!")
            
    elif opcion == "3":
        if len(pila) > 0:
            print(f"El elemento en el tope es: {pila[-1]}")
        else:
            print("¡La pila está vacía!")
            
    elif opcion == "4":
        if len(pila) > 0:
            print("\nEstado de la pila (del tope hacia abajo):")
            for item in reversed(pila):
                print(f"| {item} |")
        else:
            print("¡La pila está vacía!")
            
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Elige un número del 1 al 5.")