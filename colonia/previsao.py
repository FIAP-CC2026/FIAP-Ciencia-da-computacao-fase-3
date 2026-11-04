# previsao com regressao linear
def ajustar_reta(x, y):
    media_x = sum(x) / len(x)
    media_y = sum(y) / len(y)
    cima = 0
    baixo = 0
    for i in range(len(x)):
        cima = cima + (x[i] - media_x) * (y[i] - media_y)
        baixo = baixo + (x[i] - media_x) ** 2
    a = cima / baixo
    b = media_y - a * media_x
    return a, b


def prever(a, b, x):
    return a * x + b


def classificar_previsao(energia_prevista, limite=25):
    if energia_prevista >= limite:
        return "favoravel"
    else:
        return "desfavoravel"
