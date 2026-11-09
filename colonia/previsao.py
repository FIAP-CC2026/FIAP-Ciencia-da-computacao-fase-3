# previsao com regressao linear
from math import isfinite


def validar_medida(valor, nome):
    if (isinstance(valor, bool) or not isinstance(valor, (int, float))
            or not isfinite(valor) or valor < 0):
        raise ValueError(f"{nome} deve ser um número finito maior ou igual a zero.")


def ajustar_reta(x, y):
    if len(x) != len(y):
        raise ValueError("As listas de vento e energia devem ter o mesmo tamanho.")
    if len(x) < 2:
        raise ValueError("São necessárias pelo menos duas observações históricas.")
    for vento, energia in zip(x, y):
        validar_medida(vento, "Vento histórico")
        validar_medida(energia, "Energia histórica")

    media_x = sum(x) / len(x)
    media_y = sum(y) / len(y)
    cima = 0
    baixo = 0
    for i in range(len(x)):
        cima = cima + (x[i] - media_x) * (y[i] - media_y)
        baixo = baixo + (x[i] - media_x) ** 2
    if baixo == 0:
        raise ValueError("O histórico deve conter pelo menos dois valores de vento diferentes.")
    a = cima / baixo
    b = media_y - a * media_x
    return a, b


def prever(a, b, x):
    validar_medida(x, "Vento previsto")
    return a * x + b


def classificar_previsao(energia_prevista, limite=25):
    if energia_prevista >= limite:
        return "favoravel"
    else:
        return "desfavoravel"
