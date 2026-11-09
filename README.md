# Colônia Aurora Siger - Fase 3

Sistema em Python que organiza os dados de energia da colônia em Marte, prevê a geração eólica com regressão linear, compara geração e consumo e decide o que fazer.

## Integrantes

- Gabriel Ferreira da Silva
- Gustavo Rocha Caxias
- José Kauan Medeiros Machado
- Murilo Ribeiro Falconeri

## Como rodar

Requer Python 3, sem bibliotecas externas.

```bash
python3 main.py
```

No menu, escolha um cenário pronto, `T` para rodar todos ou `D` para digitar os valores.

## Regressão linear: previsão de energia eólica

O histórico fica em `colonia/dados.py`, em duas listas correspondentes:

```python
vento = [8, 10, 12]          # velocidade em m/s
energia_eolica = [20, 25, 30]  # geração em kW
```

Cada posição representa uma observação: vento de 8 m/s gerou 20 kW,
vento de 10 m/s gerou 25 kW e vento de 12 m/s gerou 30 kW.

Em `colonia/previsao.py`, a função `ajustar_reta` calcula os coeficientes
da regressão linear simples pelo método dos mínimos quadrados:

```text
a = soma((vento - média_vento) × (energia - média_energia))
    / soma((vento - média_vento)²)
b = média_energia - a × média_vento
energia_prevista = a × vento_previsto + b
```

Com esse histórico, `a = 2,5` e `b = 0`. Para vento de 11 m/s,
a previsão é `2,5 × 11 + 0 = 27,5 kW`.

Para testar, execute `python3 main.py`, escolha **P**, informe **11** e
depois escolha **S** para sair. A saída será:

```text
Vento previsto (m/s): 11
Energia eólica prevista: 27.5 kW (favoravel)
```

A função `prever` aplica a reta a um novo valor de vento.
`classificar_previsao` considera favorável uma previsão de pelo menos 25 kW.
Nos cenários, essa classificação alimenta as regras de decisão existentes:
uma previsão desfavorável, combinada com geração abaixo de 50 kW e consumo
acima de 60 kW, ativa o modo economia. Assim, a previsão ajuda a antecipar
a necessidade de reduzir consumo.

O ajuste exige ao menos duas observações, listas do mesmo tamanho e valores
de vento diferentes. Medidas devem ser números finitos e não negativos.
O modelo é uma aproximação didática: fora da faixa histórica de 8 a 12 m/s,
a estimativa tem maior incerteza e não representa os limites físicos de uma
turbina. Ao escolher **P**, o programa avisa quando isso acontece.

Para executar os testes da regressão, sem instalar bibliotecas:

```bash
python3 -m unittest discover -s tests -v
```

## Arquivos

```text
main.py              Menu e fluxo do programa
colonia/
    dados.py         Dados da colônia
    regras.py        Regras de decisão
    previsao.py      Regressão linear
    energia.py       Geração x consumo
    cenarios.py      Cenários prontos
```

## Exemplo

```text
ENTRADA
  Geração por fonte: solar 25 kW, eolico 15 kW
  Consumo por sistema: suporte_vida 30 kW, habitacao 15 kW, laboratorio 15 kW, comunicacao 10 kW
  Vento previsto: 11 m/s
SAÍDA
  Geração: 40 kW | Consumo: 70 kW | Saldo: -30 kW
  Fonte solar: 62.5% da geração
  Fonte eolico: 37.5% da geração
  Energia eólica prevista: 27.5 kW (favoravel)
  Análise de energia: ALERTA: consumo maior que geração
  Decisão: ALERTA: reduzir consumo
```

## Relatório

O relatório em PDF vai ficar na pasta `docs/`.
