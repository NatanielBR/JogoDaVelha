# Metodo para criar o mapa
def criar_mapa(mapa):
    for eixoY in range(0, 3):
        linha = []
        for eixoX in range(0, 3):
            linha.append(0)
        mapa.append(linha)


def dar_nomes_aos_jogadores(jogadores: dict):
    for jogador in range(1, 3):
        jogadores[jogador] = input("Escreva o nome do jogador " + str(jogador) + ":")


# Metodo para desenhar o mapa
def desenhar_mapa(mapa):
    desenho = ''  # o mapa desenhado
    for items in mapa:
        linha = ''  # cada linha do jogo da velha
        for item in items:
            # situações do item
            if item == 0:
                linha += ' '  # espaco em branco
            elif item == 1:
                linha += 'X'  # jogador 1
            elif item == 2:
                linha += 'O'  # jogador 2
            linha += '|'  # separador de item
        linha = linha[0:len(linha) - 1]  # apagar ultima |
        desenho += linha  # adiciona a linha
        desenho += "\n"  # pula pra proxima linha
        desenho += "-+-+-"  # adiciona o detalhe da linha
        desenho += "\n"  # pula pra proxima linha
    desenho = desenho[0:len(desenho) - 7]  # apagar ultimo '-+-+-' e a quebra de linha
    print(desenho)  # só printar o mapa desenhado


# metodo para verificar a vitoria
def verificar_vitoria(mapa: list):
    ganhou = False
    for jogador in range(1, 3):
        # linhas horizontais
        for linha in mapa:
            # calcular a media
            if min(linha) == 0:
                ganhou = False
            elif (sum(linha) / 3) == jogador:
                ganhou = True
                break
        if ganhou:
            return jogador

        # linhas verticais
        for coluna in range(0, 3):
            vertical = []
            for linha in mapa:
                vertical.append(linha[coluna])

            if min(vertical) == 0:
                ganhou = False
            elif (sum(vertical) / 3) == jogador:
                ganhou = True
                break
        if ganhou:
            return jogador

        # diagonal 1,3 até 3,1
        if mapa[0][2] == jogador and mapa[1][1] == jogador and mapa[2][0] == jogador:
            return jogador

        # diagonal 1,3 até 3,1
        if mapa[0][0] == jogador and mapa[1][1] == jogador and mapa[2][2] == jogador:
            return jogador

    return False


mapa = [] # lista, quase a mesma coisa que array
jogadores = {} # dicionario
dar_nomes_aos_jogadores(jogadores)
criar_mapa(mapa)
ganhou = False
jogador_atual = 1

while not ganhou:
    print("Vez do jogador ", jogadores[jogador_atual], "")
    posicoes = input("coloque a posicão: (Exemplo: 1,1)")
    if mapa[int(posicoes[0:1]) - 1][int(posicoes[2:3]) - 1] != 0:
        print("Local já esta em uso!")
        continue

    mapa[int(posicoes[0:1]) - 1][int(posicoes[2:3]) - 1] = jogador_atual
    desenhar_mapa(mapa)
    vitoria = verificar_vitoria(mapa)
    if vitoria:
        print("O jogador ", jogadores[vitoria], " ganhou!!")
        ganhou = True
    else:
        if jogador_atual == 1:
            jogador_atual = 2
        else:
            jogador_atual = 1