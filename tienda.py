def calcular_envio(subtotal):
    if subtotal < 0:
        raise ValueError("Subtotal invalido")

    if subtotal >= 500:
        return 0

    return 80

def validar_descuento(descuento):
    if not 0 <= descuento <= 100:
        raise ValueError("Descuento invalido")


def calcular_precio(precio, descuento):
    validar_descuento(descuento)
    if descuento == 0:
        return precio
    if descuento == 100:
        return 0
    return precio - (precio * descuento / 100)