from datetime import datetime

def calcular_total_producto(unidades, precio_unitario, aplicar_descuento):
    subtotal_producto = unidades * precio_unitario

    total_con_descuento = aplicar_descuento(subtotal_producto)

    return total_con_descuento

def preguntar_dia():
    respuesta = input("¿Es hoy anterior al 15 del mes? (responde 'si' o 'no'): ")
    return respuesta.lower() == 'si'

def procesar_factura():
    try:
        productos = []
        total_factura = 0

        while True:
            unidades = int(input("Introduce la cantidad de unidades del producto (o '0' para finalizar): "))

            if unidades == 0:
                break

            precio_unitario = float(input("Introduce el precio unitario del producto: "))

            if unidades < 0 or precio_unitario < 0:
                raise ValueError("Error: Las unidades y el precio deben ser valores positivos.")

            aplicar_descuento = lambda subtotal: subtotal * 0.95 if preguntar_dia() else subtotal

            total_producto = calcular_total_producto(unidades, precio_unitario, aplicar_descuento)
            productos.append((unidades, precio_unitario, total_producto))

            total_factura += total_producto

        print("\nDetalle de la Factura:")
        for i, (unidades, precio_unitario, total_producto) in enumerate(productos, start=1):
            print(f"Producto {i}: {unidades} unidades x ${precio_unitario:.2f} = ${total_producto:.2f}")

        print(f"\nTotal de la factura: ${total_factura:.2f}")

    except ValueError as ve:
        print(ve)
    except KeyboardInterrupt:
        print("\nOperación interrumpida por el usuario.")
    except Exception as e:
        print(f"Error inesperado: {e}")

procesar_factura()
