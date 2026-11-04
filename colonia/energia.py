# analise de energia
def somar_valores(dicionario):
    return sum(dicionario.values())


def calcular_saldo(geracao, consumo):
    return geracao - consumo


def analisar_energia(geracao, consumo):
    if consumo > geracao:
        return "ALERTA: consumo maior que geração"
    elif geracao > consumo:
        return "SUGESTÃO: armazenar energia excedente"
    else:
        return "OK: geração e consumo equilibrados"


def participacao_fontes(fontes):
    total = somar_valores(fontes)
    participacao = {}
    for nome, valor in fontes.items():
        if total == 0:
            participacao[nome] = 0
        else:
            participacao[nome] = round(valor / total * 100, 1)
    return participacao
