"""Reglas de precio de la tienda."""


def calcular_precio(precio: float, descuento: float) -> float:
    """Aplica un descuento porcentual después de validar sus límites."""
    if precio < 0:
        raise ValueError("Precio invalido")
    if not 0 <= descuento <= 100:
        raise ValueError("Descuento invalido")
    return precio * (1 - descuento / 100)


def calcular_iva(precio: float) -> float:
    """Agrega IVA del 16 por ciento al precio recibido."""
    return precio * 1.16

