# regras de decisao
ORDEM_PRIORIDADE = ["suporte_vida", "habitacao", "comunicacao", "laboratorio"]
ESSENCIAIS = {"suporte_vida", "habitacao"}


def decidir(energia, consumo, previsao="favoravel"):
    if energia < 50 and consumo > 60 and previsao == "desfavoravel":
        return "MODO ECONOMIA: desligar sistemas não essenciais"
    elif energia < 50:
        return "ALERTA: reduzir consumo"
    else:
        return "NORMAL: manter sistemas ligados"


def sistemas_a_desligar(consumo):
    desligar = []
    for nome in reversed(ORDEM_PRIORIDADE):
        if nome in consumo and nome not in ESSENCIAIS:
            desligar.append(nome)
    return desligar
