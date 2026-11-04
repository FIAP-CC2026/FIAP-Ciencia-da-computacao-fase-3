# dados da colonia
colonia = {
    "energia": {"solar": 40, "eolico": 25, "reserva": 30},
    "consumo": {"suporte_vida": 30, "habitacao": 15, "laboratorio": 15, "comunicacao": 10},
    "clima": {"vento": 11, "tempestade": False},
    "equipamentos": {"bateria": {"carga": 15}},
    "historico": {"vento": [8, 10, 12], "energia_eolica": [20, 25, 30]},
}


def obter(colonia, *caminho):
    atual = colonia
    for chave in caminho:
        atual = atual[chave]
    return atual


def total_geracao(colonia):
    return colonia["energia"]["solar"] + colonia["energia"]["eolico"]


def total_consumo(colonia):
    return sum(colonia["consumo"].values())


def listar_alertas(colonia):
    alertas = []
    if colonia["equipamentos"]["bateria"]["carga"] < 20:
        alertas.append("bateria")
    return alertas
