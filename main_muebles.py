from muebles import Silla, Color

def main():
    try:
        silla_azul = Silla(Color.AZUL, 9.95)

        silla_roja = Silla(Color.ROJO, 12.50)

        print("Información detallada de las sillas:")
        print(silla_azul.obtener_descripcion())
        print(silla_roja.obtener_descripcion())

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Error inesperado: {e}")

# Llamada a la función principal
if __name__ == "__main__":
    main()
