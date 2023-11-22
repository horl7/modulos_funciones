def generar_lista_numeros(inicial, final, mostrar_pares=True):
    try:
        inicial = int(inicial)
        final = int(final)

        if inicial > final:
            raise ValueError("El número inicial debe ser menor o igual al número final.")

        filtro_numeros = lambda x: x % 2 == 0 if mostrar_pares else x % 2 != 0
        lista_numeros = list(filter(filtro_numeros, range(inicial, final + 1)))

        return lista_numeros

    except ValueError as ve:
        print(f"Error: {ve}")
        return []

def obtener_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Error: Por favor, introduce un número entero válido.")

def obtener_opcion():
    while True:
        opcion = input("¿Quieres ver solo números pares? (responde 'si' o 'no'): ")
        if opcion.lower() in ['si', 'no']:
            return opcion.lower() == 'si'
        else:
            print("Respuesta no válida. Por favor, responde 'si' o 'no'.")

def main():
    try:
        numero_inicial = obtener_numero("Introduce el número inicial: ")

        numero_final = obtener_numero("Introduce el número final: ")

        mostrar_pares = obtener_opcion()

        lista_numeros = generar_lista_numeros(numero_inicial, numero_final, mostrar_pares)

        if lista_numeros:
            tipo_numeros = "pares" if mostrar_pares else "impares"
            print(f"Lista de números {tipo_numeros} entre {numero_inicial} y {numero_final}:")
            print(lista_numeros)
        else:
            print("No se pudo generar la lista de números.")

    except KeyboardInterrupt:
        print("\nOperación interrumpida por el usuario.")
    except Exception as e:
        print(f"Error inesperado: {e}")

main()
