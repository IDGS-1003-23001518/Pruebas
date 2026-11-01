import pytest
from tienda import calcular_envio

@pytest.mark.parametrize(
    "subtotal,envio_esperado",
    [
        (300, 80),
        (499, 80),
        (500, 0),
        (600, 0),
    ]
)
def test_reglas_de_envio(subtotal, envio_esperado):
    assert calcular_envio(subtotal) == envio_esperado

def test_subtotal_negativo():
    with pytest.raises(ValueError):
        calcular_envio(-100)