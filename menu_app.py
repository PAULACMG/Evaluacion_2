compras =[]
def agregarCompra():
    compra = input("Ingresa una compra: ")
    compras.append(int(compra))
    print("La compra se ha agregado correctamente")

def mostrarCompra():
    if len(compras) == 0:
        print("No hay compras registradas.")
    else:
        print("Compras realizadas:")
        for i, compra in enumerate(compras):
            print(f"Compra {i + 1}: ${compra}")


def mostrar_total():
    total = sum(compras)
    print(f"Total gastado: ${total:.2f}")

def main():
    while True:
        print("\n--- MENÚ ---")
        print("1. Opción 1: Agregar compra")
        print("2. Opción 2: Mostrar compras")
        print("3. Opción 3: Mostrar total gastado")
        print("4. Opción 4: Salir")
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            agregarCompra()
        if opcion == 2:
            mostrarCompra()
        if opcion == 3:
            mostrar_total()
        if opcion == 4:
            print("¡Hasta luego!")
            exit()

main()


