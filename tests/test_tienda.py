import pytest

from devops_tienda.tienda import calcular_iva, calcular_precio


def test_precio_con_descuento():
    assert calcular_precio(200, 25) == pytest.approx(150)


def test_precio_sin_descuento():
    assert calcular_precio(500, 0) == pytest.approx(500)


def test_precio_con_iva():
    assert calcular_iva(100) == pytest.approx(116)


def test_precio_negativo():
    with pytest.raises(ValueError, match="Precio invalido"):
        calcular_precio(-1, 0)


def test_descuento_invalido():
    with pytest.raises(ValueError, match="Descuento invalido"):
        calcular_precio(500, 150)

