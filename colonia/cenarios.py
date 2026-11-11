# cenarios prontos
CENARIOS = [
    {
        "nome": "Pouca energia e consumo alto",
        "geracao": {"solar": 25, "eolico": 15},
        "consumo": {"suporte_vida": 30, "habitacao": 15, "laboratorio": 15, "comunicacao": 10},
        "vento_previsto": 11,
    },
    {
        "nome": "Sobra de energia",
        "geracao": {"solar": 55, "eolico": 25},
        "consumo": {"suporte_vida": 20, "habitacao": 10},
        "vento_previsto": 12,
    },
    {
        "nome": "Pouca energia, consumo alto e pouco vento",
        "geracao": {"solar": 25, "eolico": 15},
        "consumo": {"suporte_vida": 30, "habitacao": 15, "laboratorio": 15, "comunicacao": 10},
        "vento_previsto": 8,
    },
    {
        "nome": "Geração e consumo iguais",
        "geracao": {"solar": 35, "eolico": 25},
        "consumo": {"suporte_vida": 30, "habitacao": 20, "comunicacao": 10},
        "vento_previsto": 10,
    },
    {
        "nome": "Tempestade de poeira",
        "geracao": {"solar": 5, "eolico": 10},
        "consumo": {"suporte_vida": 30, "habitacao": 15, "laboratorio": 10, "comunicacao": 5},
        "vento_previsto": 8,
    },
]
