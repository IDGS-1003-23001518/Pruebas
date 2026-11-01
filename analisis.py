
def calcular_total(precio, descuento):
    resultado = precio - precio * descuento / 100
    return resultado

def obtener_categoria(precio):
    if precio > 1000:
        return "Premium"
    else:
        return "Normal"