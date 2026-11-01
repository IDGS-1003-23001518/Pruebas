"""Interfaz de consola para calcular el total de una compra."""

from .tienda import calcular_iva, calcular_precio


def main() -> None:
    print("=== TIENDA DEVOPS ===")
    try:
        precio = float(input("Precio: "))
        descuento = float(input("Descuento (%): "))
        subtotal = calcular_precio(precio, descuento)
        total = calcular_iva(subtotal)
        print(f"Total con IVA: ${total:.2f}")
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()

