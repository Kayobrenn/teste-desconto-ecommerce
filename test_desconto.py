import pytest

from desconto import calcular_desconto


@pytest.mark.parametrize(
    "valor_compra, tipo_cliente, esperado",
    [
        # Compra abaixo de R$ 100
        (50, "COMUM", 0),
        (99, "COMUM", 0),

        # Limite de R$ 100
        (100, "COMUM", 10),

        # Entre R$ 100 e R$ 500
        (300, "COMUM", 30),
        (499, "COMUM", 49.90),

        # R$ 500 ou mais
        (500, "COMUM", 100),
        (800, "COMUM", 160),

        # Clientes VIP
        (50, "VIP", 2.50),
        (300, "VIP", 45),
        (500, "VIP", 125),

        # VIP deve funcionar independente de maiúsculas/minúsculas
        (300, "vip", 45),
        (300, "Vip", 45),

        # Regra do teto
        (1000, "VIP", 200),
        (2000, "COMUM", 200),
    ]
)
def test_calcular_desconto(valor_compra, tipo_cliente, esperado):
    resultado = calcular_desconto(valor_compra, tipo_cliente)

    assert resultado == esperado