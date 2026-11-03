# Diccionario con los productos y sus precios
menu_productos = {
    "Cafe": 1200,
    "Cappuccino": 1700,
    "Latte": 1800,
    "Te": 1300,
    "Queque": 2200,
    "Sandwich": 3200
}

# Lista vacía para almacenar los productos solicitados
pedido = []

# Solicitar el nombre del cliente
nombre_cliente = input("Ingrese su nombre: ")

# Mostrar un saludo personalizado
print(f"\n¡Bienvenido a nuestra cafeteria, {nombre_cliente}!")


# Mostrar el menú de opciones hasta que el cliente decida salir
while True:
    print("\n--- MENU DE LA CAFETERIA ---")
    print("1. Ver menú de productos")
    print("2. Agregar producto al pedido")
    print("3. Ver pedido actual")
    print("4. Finalizar pedido y salir")

    # Solicitar una opción al cliente
    opcion = input("Seleccione una opción del 1 al 4: ")

    # Opción 1: Mostrar los productos y sus precios
    if opcion == "1":
        print("\n--- PRODUCTOS DISPONIBLES ---")
        numero = 1

        for producto, precio in menu_productos.items():
            print(f"{numero}. {producto}: ₡{precio}")
            numero = numero + 1

    
    # Opción 2: Agregar un producto al pedido
    elif opcion == "2":
        nombre_producto = input("Ingrese el nombre del producto: ")

        # Buscar el producto dentro del diccionario
        for producto in menu_productos:

            if nombre_producto.lower() == producto.lower():

                # Solicitar y validar la cantidad
                while True:
                    cantidad_texto = input("Ingrese la cantidad: ")

                    # Verificar que sea un número entero
                    if not cantidad_texto.isdigit():
                        print("Error: ingrese un número entero positivo.")
                        continue

                    cantidad = int(cantidad_texto)

                    # Verificar que sea mayor que cero
                    if cantidad <= 0:
                        print("Error: la cantidad debe ser mayor que cero.")
                        continue

                    # Agregar el producto y su cantidad a la lista
                    pedido.append([producto, cantidad])
                    print(f"Agregaste {cantidad} unidad(es) de {producto}.")
                    break

                break

        # Se ejecuta si el producto no existe
        else:
            print("Error: el producto no existe en el menú.")

    # Opción 3: Mostrar el pedido actual
    elif opcion == "3":

            # Comprobar si el pedido está vacío
            if pedido == []:
                print("Su pedido está vacío.")

            else:
                print("\n--- PEDIDO ACTUAL ---")

                # Variable para acumular el subtotal del pedido
                subtotal_pedido = 0

                # Recorrer los productos que el cliente solicitó
                for producto, cantidad in pedido:

                    # Consultar el precio en el diccionario
                    precio = menu_productos[producto]

                    # Calcular el subtotal de cada producto
                    subtotal = precio * cantidad

                    # Mostrar los detalles del producto
                    print(f"\nProducto: {producto}")
                    print(f"Cantidad: {cantidad}")
                    print(f"Subtotal: ₡{subtotal}")

                    # Acumular los subtotales
                    subtotal_pedido = subtotal_pedido + subtotal

                # Mostrar el subtotal del pedido
                print(f"\nSubtotal del pedido: ₡{subtotal_pedido}")

    # Opción 4: Salir del programa
    elif opcion == "4":
        print(f"Gracias por visitarnos, {nombre_cliente}.")
        break

    # Mostrar error si la opción no existe
    else:
        print("Opción incorrecta. Ingrese un número del 1 al 4.")
