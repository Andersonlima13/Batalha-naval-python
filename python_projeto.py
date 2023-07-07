# Bibliotecas usadas:
# Randint - obtida da random = Será usada para sortear a célula que o navio estará;
# Sleep - obtida da time = Será usada para obter delays quando requisitado;

from random import randint
from time import sleep 

# A seguir temos a ordem das funções:
# Caso queira ir direto, pesquise:
# Por exemplo: "1ª função" ou "7ª função" ou pelo nome de cada uma;

# 1 - configurarJogo;
# 2 - criarTabuleiro;
# 3 - ataque;
# 4 - analisarLetra;
# 5 - resultadoTiro;
# 6 - levarParaImpressao;
# 7 - impressao;
# 8 - letrasParaCabecalho;
# 9 - imprimirSeparacao;
# 10 - mostrarPontuacao;

# # # # Funções # # # #

#passar as variaveis globais como parametro

#----- 1ª função -----#

# Anderson lima
'''' SUGESTAO : remover as variaveis globais, ao inves disso passar a necessidade de criar os tabuleiros ocultos e nao ocultos para a funçao
criar tabuleiro, que vai ficar dependente do nome dos jogadores e da ordem ja definida'''
# Configuração inicial do jogo




def configurarJogo():
    # Definir as variáveis importantes como globais
    global ordem, nomeJogador1, nomeJogador2, quantidadeDeNavios, tabuleiroJogador1, tabOculto1, pontuacaoDoJogador1,tabuleiroJogador2, pontuacaoDoJogador2, tabOculto2

    ordem = 8
    pontuacaoDoJogador1 = pontuacaoDoJogador2 = 0

    # O programa será iniciado e mostrado na tela a partir deste ponto // apenas a primeira impressao
    
    print('-'*38)
    print('🚢 Bem-vindo ao jogo BATALHA NAVAL 🚢')
    print('-'*38)
    sleep(1)
    global arq
    arq = open('jogadas2','w')
    
    # Pede-se o nome de cada jogador

    
    while True:
        nomeJogador1 = str(input('🔘 NOME DO PRIMEIRO JOGADOR: ')).upper().strip()
        sleep(0.5)
        nomeJogador2 = str(input('🔘 NOME DO SEGUNDO JOGADOR: ')).upper().strip()
        sleep(0.5)
        nome_jogadores = "NOME DO JOGADOR 1 :" + nomeJogador1+"|" + '\n' + "|" + "NOME DO JOGADOR 2 :" + nomeJogador2 + '\n'
        arq.write(nome_jogadores)
        print('\nArquivo gerado com sucesso.')
        

    # Escolher a quantidade de navios que cada jogador possuirá, enquanto a funçao é executada
        while True:
            quantidadeDeNavios = int(input('🚢 Número de navios de cada jogador 🚢 [máximo = 6]: '))
            if quantidadeDeNavios <= 6 and quantidadeDeNavios >= 1:
                break
        sleep(0.5)

    # Tabuleiros ocultos
        tabOculto1 = [['-']* ordem for i in range(ordem)]
        tabOculto2 = [['-']* ordem for i in range(ordem)]
    

    # Tabuleiros que mostram as frota, vamos chamar a função criarTabuleiro, apos receber o numero de navios como parametro
    
        tabuleiroJogador1 = criarTabuleiro(quantidadeDeNavios)
        tabuleiroJogador2 = criarTabuleiro(quantidadeDeNavios) 
        tab = tabuleiroJogador1
        tab2 = tabuleiroJogador2
        string1 = str(tab).replace("[]","|") + '\n'
        string2 = str(tab2).replace("[]","|") + '\n'
        arq.write(string1)
        arq.write(string2)
         

    # Vamos definir se os usuários querem que mostre a frota de navio no tabuleiro ou não durante o jogo
    # Anderson lima : transformar (mostratabuleiro em uma funçao dependente da 2 função)
        global mostrarTabuleiro
        while True:
            mostrarTabuleiro = int(input('Mostrar FROTA no tabuleiro?\n[Selencione "1" para NÃO MOSTRAR a FROTA]\n[Selencione "2" para MOSTRAR a FROTA]\n'))
        
        # NÃO MOSTRAR AS FROTAS DE NAVIOS DE CADA JOGADOR, DURANTE A PARTIDA
            if mostrarTabuleiro == 1:
                levarParaImpressao(tabuleiroJogador1, 1, None, None, None)
                sleep(1)
                levarParaImpressao(tabOculto1, 1, None, None, None)
                sleep(1)
                '''levarParaImpressao(tabuleiroJogador2, 2, None, None, None)
                sleep(1)
                levarParaImpressao(tabOculto2, 2, None, None, None)     
                sleep(1)'''
                break

        # MOSTRAR AS FROTAS DE NAVIOS DE CADA JOGADOR, DURANTE A PARTIDA
            elif mostrarTabuleiro == 2:
                levarParaImpressao(tabuleiroJogador1, 1, None, None, None)     
                sleep(1)
                # levarParaImpressao(tabuleiroJogador2, 2, None, None, None)     
                # sleep(1)
                break

            # USUÁRIO DIGITOU ALGUMA VALOR INVÁLIDO
            else:
                print('⚠️ Digite uma opção válida! [Opção 1 ou Opção 2] ⚠️\n')
            
    
        break

   
    # Como temos uma função para imprimir todas as matrizes em todas as possibilidades, passamos parâmetros do tipo "None", pois não será usados nessa declaração. Porém, não podemos ocultar os 3 últimos, tendo em vista que mesmo essa função recebe 5 parâmetros formais, usados por outras funções;

    

#----- 2ª função -----#

# 
# Função da criação do tabuleiro com espaços vazios e navios
def criarTabuleiro(quantidadeDeNavios):  
    tabuleiro = [['-']*ordem for i in range(ordem)]
    
    cont = 0

    # Impede que os navios encostem uns nos outros, verificando de há navios adjacentes
    # logo, contador só recebe mais naviis ao passar pelas condicionais
    while cont < quantidadeDeNavios:
        linha = randint(0, ordem - 1)
        coluna = randint(0, ordem - 1)

        # Verificação para o N na diagonal superior  esquerda
        if linha > 0 and coluna > 0 and tabuleiro[linha-1][coluna-1] == 'N':
            continue #faz o loop voltar para o início identado.
        if linha > 0 and tabuleiro[linha-1][coluna] == 'N': #verificação para o N adjascente acima
            continue
        if linha > 0 and coluna < (ordem - 1) and tabuleiro[linha-1][coluna+1] == 'N': #verificação para o N diagonal superior direita 
            continue
        if coluna > 0 and tabuleiro[linha][coluna-1] == 'N': #verificação para o N adjascente ao lado esquerdo
            continue
        if tabuleiro[linha][coluna] == 'N': #verificação para o N na mesma coordenada 
            continue
        if coluna < (ordem - 1) and tabuleiro[linha][coluna+1] == 'N': #verificação para o N adjascente ao lado direito
            continue
        if linha < (ordem - 1) and coluna > 0 and tabuleiro[linha+1][coluna-1] == 'N': #verificação para o N diagonal inferior esquerda
            continue
        if linha < (ordem - 1) and tabuleiro[linha+1][coluna] == 'N': #verificação para o N adjascente abaixo
            continue
        if linha < (ordem - 1) and coluna < (ordem - 1) and tabuleiro[linha+1][coluna+1] == 'N': #verificação para o N diagonal inferior direita 
            continue
        tabuleiro[linha][coluna] = 'N'
        cont += 1

    return tabuleiro


#----- 3ª função -----#

# anderson lima
# Função de ataque. Aqui será pedido a letra e o número, representando, respectivamente, a linha e a coluna de ataque.
def ataque(tabuleiro, identidade):
    while True:
        sleep(0.5)
        # Escolher qual será a unidade de célula atacada
        bombardear = str(input('🎯 Digite a posição que você quer atacar. 🎯 Ex: D8: ')).upper().strip()
        # Converter as escolhas para números inteiros. Ex: A == 1; B == 2;
        letra = analisarLetra(bombardear[0])
        numero = int(bombardear[1:])
        imprimirSeparacao()
        salvar_arquivo = int(input("Deseja continuar om o jogo ? | 1 para [SIM] e 2 para [Não] |"))
        if salvar_arquivo == 2:
            arq.close()
            break
        else:
            return resultadoTiro(tabuleiro, identidade, letra, numero)
    


#----- 4ª função -----#

# 
# Escolher unidade para ser atacada; O contador, cada vez que passar para a próxima letra vai contar e isso fará com que as letras virem números inteiros. Ex: A == 1; B == 2;
# [Essa função será chamada na função "ataque"]
def analisarLetra(letra):
    contador = 0
    for i in 'ABCDEFGH':
        contador += 1
        if i == letra:
            return contador


#----- 5ª função -----#

# 
# O parâmetro "tabuleiro" é auto explicativo, irá receberá o tabuleiro
# Já o parâmetro "identidade" irá definir de qume é o tabuleiro [1 - refere ao primeiro jogador; 2 - refere ao segundo jogador]
# Os parâmetros "linha" e "coluna" definirá a "linha" e a "coluna" que o jogador mirou no adversário
# O último parâmetro representam a consequência: 0 (Sem consequência); 1 (Fogo); 2 (Água);

def resultadoTiro(tabuleiro, identidade, linha, coluna):
    # QUANDO O JOGADOR ACERTAR ALGUM NAVIO;
    # Irá imprimir os dois tabuleiros; O de quem atacou e o de quem foi atacado, este com o símbolo de 'F' onde foi atingido;
    # Ao retornar True; simboliza que o jogador acertou o navio e continuará jogando;
    
    if tabuleiro[linha-1][coluna-1] == 'N':
        tabuleiro[linha-1][coluna-1] = 'F'
        if identidade == 1:
            if mostrarTabuleiro == 1: # NÃO MOSTRAR A FROTA DE NAVIOS
                levarParaImpressao(tabOculto2, 2, linha, coluna, 1)
            else:
                levarParaImpressao(tabuleiroJogador2, 2, linha, coluna, 0)
        else:
            if mostrarTabuleiro == 2: # NÃO MOSTRAR A FROTA DE NAVIOS
                levarParaImpressao(tabOculto1, 1, linha, coluna, 1)
            else:
                levarParaImpressao(tabuleiroJogador2, 2, linha, coluna, 0)
        print(f'\n💥 Você ACERTOU, {nomeJogador1}, é FOGO! 💥 \n')
        print('😀 JOGUE NOVAMENTE! 😀')
        imprimirSeparacao()
        return True

    # QUANDO O JOGADOR ACERTAR ALGUMA COORDENADA ONDE TERIA UM NAVIO, PORÉM, QUE JÁ FOI ATINGIDA;
    # Irá imprimir os dois tabuleiros como estariam anteriormente;
    # Ao retornar False; simboliza que o jogador atirou novamente algum lugar já acertado; Agora a vez irá ser a do adversário;

    elif tabuleiro[linha-1][coluna-1] == 'F':
        print('\n😞 Você acertou um lugar já BOMBARDEADO! 😞')
        imprimirSeparacao()
        return False

    # QUANDO ERRAR O TIRO - FOR NA ÁGUA
    # Irá imprimir os dois tabuleiros; O de quem atacou e o de quem foi atacado, este com o símbolo de 'A' onde foi atingido;
    # Ao retornar False; simboliza que o jogador errou o navio; Agora a vez irá ser a do adversário;
    
    else:
        tabuleiro[linha-1][coluna-1] = 'A'
        if identidade == 1:
            if mostrarTabuleiro == 1: # NÃO MOSTRAR A FROTA DE NAVIOS
                levarParaImpressao(tabOculto2, 2, linha, coluna, 2)
            else:
                levarParaImpressao(tabuleiroJogador1, 1, linha, coluna, 0)
        else:
            if mostrarTabuleiro == 1: # NÃO MOSTRAR A FROTA DE NAVIOS
                levarParaImpressao(tabOculto1, 1, linha, coluna, 2)
            else:
                levarParaImpressao(tabuleiroJogador2, 2, linha, coluna, 0)
        print('\n💧 Você ERROU, é ÁGUA! 💧')
        print('👋 VOCÊ PERDEU A VEZ! 👋')
        imprimirSeparacao()
        return False


#----- 6ª função -----#

# 
# Essa função prepara os tabuleiros com os F de fogo e A de água para levar à impressão
def levarParaImpressao(tabuleiroBase, identidade, linha, coluna, consequencia):
    # Identidade == 1 significa que o tabuleiro pertence ao primeiro jogador.
    if identidade == 1:
        if consequencia == 1:
            tabuleiroBase[linha-1][coluna-1] = 'F'
        elif consequencia == 2:
            tabuleiroBase[linha-1][coluna-1] = 'A'
        impressao(tabuleiroBase)

    # Identidade == 2 significa que o tabuleiro pertence ao segundo jogador.
    elif identidade == 2:
        if consequencia == 1:
            tabuleiroBase[linha-1][coluna-1] = 'F'
        elif consequencia == 2:
            tabuleiroBase[linha-1][coluna-1] = 'A'
        impressao(tabuleiroBase)


#----- 7ª função -----#


# Essa função será para imprimir os tabuleiros um ao lado do outro, com cabeçalho e os demais enfeites;
def impressao(tabuleiroBase):
    if tabuleiroBase == tabuleiroJogador1 or tabuleiroBase == tabuleiroJogador2:
        tabuleiroImpresso1 = tabuleiroJogador1
        tabuleiroImpresso2 = tabuleiroJogador2

    elif tabuleiroBase == tabOculto1 or tabuleiroBase == tabOculto2:
        tabuleiroImpresso1 = tabOculto1
        tabuleiroImpresso2 = tabOculto2
    
    print(f'\n🔴 Tabuleiro da(o) {nomeJogador1}', end=' '*(36-len(nomeJogador1)))
    print(f'🔴 Tabuleiro da(o) {nomeJogador2}\n')

    print('🚢', end=' '*4)
    for i in range(ordem):
        if i > 8:
            print(f'{i+1}', end=' '*2)
        else:
            print(f'{i+1}', end=' '*3)
        if i == ordem-1:
            print(' '*3, end='')
            print('🚢', end=' '*5)
            for i in range(ordem):
                if i > 9:
                    print(f'{i+1}', end=' '*2)
                else:
                    print(f'{i+1}', end=' '*3)
    print()

    for i in range(ordem):
        print(f'{letrasParaCabecalho(i-1):3}', end='|  ')
        for j in range(ordem):
            print(f'{tabuleiroImpresso1[i][j]:4}', end='')
        print(f'   {letrasParaCabecalho(i-1):3}', end='|')
        for k in range(ordem):
            if k == 0:
                print(' '*3, end='')
            print(f'{tabuleiroImpresso2[i][k]:4}', end='')
        print()
    print()



print('\nArquivo gerado com sucesso.')

#----- 8ª função -----#

# Anderson lima
# Definir letra de cada linha no cabeçalho [essa função será chamada na função "impressao"]
def letrasParaCabecalho(contador):
    l = 'ABCDEFGH'
    contador += 1
    return l[contador]


#----- 9ª função -----#

# 
# Essa função serve apenas para imprimir uma separação entre alguns pontos específicos, quando ela for chamada;
def imprimirSeparacao():
    print()
    print('= '*28)
    print()

#----- 10ª função -----#

# 
# Função para mostrar a pontuação de cada jogador, quando for solicitada;
def mostrarPontuacao():
    print('🟨 TABELA DA PONTUAÇÃO DOS JOGADORES 🟨\n')
    print(f'Pontuação do jogador {nomeJogador1}: {pontuacaoDoJogador1}')
    print(f'Pontuação do jogador {nomeJogador2}: {pontuacaoDoJogador2}')

    pontos1 = pontuacaoDoJogador1
    pontos2 = pontuacaoDoJogador2
    
    arqpontos1 = "\n" + f"PONTUAÇÃO DO JOGADOR 1 : " + "\n" + str(pontos1) 
    arqpontos2 = "\n" + f"PONTUAÇÃO DO JOGADOR 2 : " +  "\n" + str(pontos2) 
    arq.write(arqpontos1)
    arq.write(arqpontos2)
        
    

    
    imprimirSeparacao()
        

# # # # #  Programa principal  # # # # #


while True:
    escolha = int(input('😀 Olá, o que você deseja fazer?\n[1 - Iniciar um novo jogo?] ✔️\n[2 - Sair] 👋\n'))
    if escolha == 2:
        break
    sleep(1)
    print('🎉 Vamos começar 🎉')
    sleep(1)
    configurarJogo()
    while True:
        
        # o programa continua ate a pontuaçao ser igual ao n de navios
        while True:
            print(f'\n👉 Agora é a vez do jogador {nomeJogador1} atacar o jogador {nomeJogador2}\n')
            resultadoDoAtaque = ataque(tabuleiroJogador2, 1)
            if resultadoDoAtaque == True:
                pontuacaoDoJogador1 += 1
                mostrarPontuacao()
                if pontuacaoDoJogador1 == quantidadeDeNavios:
                    sleep(1)
                    print('Espereeem.... alguém ganhou...\n')
                    sleep(2)
                    print(f'\n👏 PARABÉNS! {nomeJogador1} GANHOU! 👏\n')
                    
                    break
            else:
                mostrarPontuacao()
                break

        if pontuacaoDoJogador1 == quantidadeDeNavios:
            break

        while True:
            print(f'👉 Agora é a vez do jogador {nomeJogador2} atacar o jogador {nomeJogador1}\n')
            resultadoDoAtaque = ataque(tabuleiroJogador1, 2)
            if resultadoDoAtaque == True:
                pontuacaoDoJogador2 += 1
                mostrarPontuacao()
                if pontuacaoDoJogador2 == quantidadeDeNavios:
                    sleep(1)
                    print('Espereeem.... alguém ganhou...\n')
                    sleep(2)
                    print(f'\n👏 PARABÉNS! {nomeJogador2} GANHOU! 👏\n')
                    break 
            else:
                mostrarPontuacao()
                break
        if pontuacaoDoJogador2 == quantidadeDeNavios:
            break
print('\n😀 Foi um prazer ter esse momento com você. 👏 Volte sempre! 👋\n')