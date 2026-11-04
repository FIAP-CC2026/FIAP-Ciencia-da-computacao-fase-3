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
python main.py
```

No menu, escolha um cenário pronto, `T` para rodar todos ou `D` para digitar os valores.

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
