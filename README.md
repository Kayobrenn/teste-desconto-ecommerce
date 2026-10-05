# Testes Unitários - Cálculo de Desconto

Atividade prática de Qualidade de Software utilizando Python e Pytest.

## Objetivo

Validar a função `calcular_desconto`, responsável por calcular descontos progressivos de acordo com o valor da compra e o tipo de cliente.

## Regras de negócio

- Compras abaixo de R$ 100,00 não recebem desconto base.
- Compras entre R$ 100,00 e R$ 499,99 recebem 10% de desconto.
- Compras a partir de R$ 500,00 recebem 20% de desconto.
- Clientes VIP recebem 5% adicionais.
- O tipo VIP deve ser reconhecido independentemente de letras maiúsculas ou minúsculas.
- O desconto máximo permitido é de R$ 200,00.

## Cenários testados

Foram criados testes para:

- Compras abaixo de R$ 100,00.
- Valor limite de R$ 100,00.
- Valores entre R$ 100,00 e R$ 500,00.
- Valor limite de R$ 500,00.
- Clientes comuns.
- Clientes VIP.
- VIP escrito em diferentes combinações de maiúsculas e minúsculas.
- Aplicação do teto máximo de R$ 200,00.

## Bugs encontrados

Durante a execução dos testes foram identificados dois problemas no código original:

1. O valor de R$ 100,00 não recebia o desconto de 10%, pois a condição utilizava `> 100` em vez de `>= 100`.

2. O cliente VIP era reconhecido apenas quando escrito exatamente como `"VIP"`, não atendendo ao requisito de aceitar letras maiúsculas e minúsculas.

## Correções realizadas

A condição:

```python
valor_compra > 100