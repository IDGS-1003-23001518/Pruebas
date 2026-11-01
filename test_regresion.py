import pytest
from tienda import calcular_precio

@pytest.mark.parametrize(
    "precio,descuento,esperado",
    [
        (200, 25, 150),
        (500, 0, 500),
        (100, 100, 0),
        (300, 10, 270),
    ]
)
def test_descuentos_existentes(precio, descuento, esperado):
    assert calcular_precio(
        precio, descuento
    ) == pytest.approx(esperado)