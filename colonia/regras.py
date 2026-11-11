# regras de decisao
LIMITE_ENERGIA = 50
CONSUMO_ALTO = 60
ENERGIA_CRITICA = 20

# do mais importante para o menos importante
ORDEM_PRIORIDADE = ["suporte_vida", "habitacao", "comunicacao", "laboratorio"]
ESSENCIAIS = {"suporte_vida", "habitacao"}


def decidir(energia, consumo, previsao="favoravel"):
    # condicoes simples
    energia_baixa = energia < LIMITE_ENERGIA
    consumo_alto = consumo > CONSUMO_ALTO
    previsao_ruim = previsao == "desfavoravel"

    if energia < ENERGIA_CRITICA:
        return "MODO ECONOMIA CRÍTICO: manter apenas sistemas essenciais"
    elif energia_baixa and consumo_alto and previsao_ruim:
        return "MODO ECONOMIA: desligar sistemas não essenciais"
    elif energia_baixa or consumo > energia:
        return "ALERTA: reduzir consumo"
    else:
        return "NORMAL: manter sistemas ligados"


def sistemas_a_desligar(consumo):
    desligar = []
    for nome in reversed(ORDEM_PRIORIDADE):
        if nome in consumo and nome not in ESSENCIAIS:
            desligar.append(nome)
    return desligar
