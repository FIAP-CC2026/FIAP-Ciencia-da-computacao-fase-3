from colonia.dados import colonia, obter, total_geracao, total_consumo, listar_alertas
from colonia.regras import decidir, sistemas_a_desligar
from colonia.previsao import ajustar_reta, prever, classificar_previsao, validar_medida
from colonia.energia import somar_valores, calcular_saldo, analisar_energia, participacao_fontes
from colonia.cenarios import CENARIOS


# exibicao
def listar_kw(dicionario):
    partes = []
    for nome, valor in dicionario.items():
        partes.append(f"{nome} {valor} kW")
    return ", ".join(partes)


def mostrar_colonia():
    print("\n=== SITUAÇÃO ATUAL DA COLÔNIA ===")
    print(f"Geração total: {total_geracao(colonia)} kW")
    print(f"Consumo total: {total_consumo(colonia)} kW")
    print(f"Reserva: {obter(colonia, 'energia', 'reserva')} kWh")
    print(f"Vento agora: {obter(colonia, 'clima', 'vento')} m/s")
    alertas = listar_alertas(colonia)
    if alertas:
        print("Alertas:", ", ".join(alertas))
    else:
        print("Alertas: nenhum")


def rodar_cenario(cenario, a, b):
    print(f"\n=== CENÁRIO: {cenario['nome']} ===")
    print("ENTRADA")
    print(f"  Geração por fonte: {listar_kw(cenario['geracao'])}")
    print(f"  Consumo por sistema: {listar_kw(cenario['consumo'])}")
    print(f"  Vento previsto: {cenario['vento_previsto']} m/s")

    geracao = somar_valores(cenario["geracao"])
    consumo = somar_valores(cenario["consumo"])
    saldo = calcular_saldo(geracao, consumo)
    fontes = participacao_fontes(cenario["geracao"])
    eolica_prevista = prever(a, b, cenario["vento_previsto"])
    previsao = classificar_previsao(eolica_prevista)
    analise = analisar_energia(geracao, consumo)
    decisao = decidir(geracao, consumo, previsao)

    print("SAÍDA")
    print(f"  Geração: {geracao} kW | Consumo: {consumo} kW | Saldo: {saldo} kW")
    for nome, porcentagem in fontes.items():
        print(f"  Fonte {nome}: {porcentagem}% da geração")
    print(f"  Energia eólica prevista: {eolica_prevista:.1f} kW ({previsao})")
    print(f"  Análise de energia: {analise}")
    print(f"  Decisão: {decisao}")
    if "ECONOMIA" in decisao:
        desligar = sistemas_a_desligar(cenario["consumo"])
        print(f"  Desligar nesta ordem: {', '.join(desligar)}")


# entrada de dados
def ler_numero(mensagem):
    while True:
        texto = input(mensagem).replace(",", ".")
        try:
            numero = float(texto)
            validar_medida(numero, "Valor")
            return numero
        except ValueError:
            pass
        print("Digite um número finito maior ou igual a zero.")


def digitar_cenario():
    print("\nDigite os valores (em kW):")
    geracao = {
        "solar": ler_numero("  Geração solar: "),
        "eolico": ler_numero("  Geração eólica: "),
    }
    consumo = {}
    for sistema in colonia["consumo"]:
        consumo[sistema] = ler_numero(f"  Consumo de {sistema}: ")
    vento = ler_numero("  Vento previsto (m/s): ")
    return {"nome": "Digitado pelo usuário", "geracao": geracao,
            "consumo": consumo, "vento_previsto": vento}


# programa principal
def main():
    print("Colônia Aurora Siger - Sistema de energia")
    mostrar_colonia()

    vento = obter(colonia, "historico", "vento")
    energia = obter(colonia, "historico", "energia_eolica")
    a, b = ajustar_reta(vento, energia)
    print(f"\nReta da previsão: energia = {a:.2f} x vento + {b:.2f}")

    while True:
        print("\nEscolha um cenário:")
        for numero, cenario in enumerate(CENARIOS, start=1):
            print(f"  {numero} - {cenario['nome']}")
        print("  T - Rodar todos")
        print("  D - Digitar meus valores")
        print("  P - Prever energia eólica a partir do vento")
        print("  S - Sair")
        opcao = input("Opção: ").strip().upper()

        if opcao == "S":
            print("Encerrando o sistema.")
            break
        elif opcao == "T":
            for cenario in CENARIOS:
                rodar_cenario(cenario, a, b)
        elif opcao == "D":
            rodar_cenario(digitar_cenario(), a, b)
        elif opcao == "P":
            vento_previsto = ler_numero("Vento previsto (m/s): ")
            energia_prevista = prever(a, b, vento_previsto)
            print(f"Energia eólica prevista: {energia_prevista:.1f} kW "
                  f"({classificar_previsao(energia_prevista)})")
            historico_vento = obter(colonia, "historico", "vento")
            if vento_previsto < min(historico_vento) or vento_previsto > max(historico_vento):
                print("Estimativa fora da faixa do histórico; a previsão tem maior incerteza.")
        elif opcao.isdigit() and 1 <= int(opcao) <= len(CENARIOS):
            rodar_cenario(CENARIOS[int(opcao) - 1], a, b)
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
