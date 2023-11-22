def suma_numeros():
    numeros = []

    try:
        for _ in range(5):
            entrada = input("Introduce un número (o 'q' para salir): ")

            if entrada.lower() == 'q':
                break

            if '.' in entrada:
                numero = float(entrada)
            else:
                numero = int(entrada)

            numeros.append(numero)

        if len(numeros) == 5:
            print("Se alcanzó el máximo de 5 números permitidos.")

    except ValueError:
        print("Error: Por favor, introduce solo números.")
    except KeyboardInterrupt:
        print("\nOperación interrumpida por el usuario.")
    except Exception as e:
        print(f"Error inesperado: {e}")

    if numeros:
        print("Números introducidos:")
        for num in numeros:
            print(num, end=' ')

        suma_total = sum(numeros)
        print(f"\nLa suma de todos los números introducidos es: {suma_total}")
    else:
        print("No se introdujeron números.")

suma_numeros()
