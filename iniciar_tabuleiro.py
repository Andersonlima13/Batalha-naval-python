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
    
    # Pede-se o nome de cada jogador

    
  
        

    # Escolher a quantidade de navios que cada jogador possuirá, enquanto a funçao é executada
    while True:
        quantidadeDeNavios = int(input('🚢 Número de navios de cada jogador 🚢 [máximo = 6]: '))
        if quantidadeDeNavios <= 6 and quantidadeDeNavios >= 1:
            break
        sleep(0.5)
        tabuleiroJogador1 = criarTabuleiro(quantidadeDeNavios)

    

    # Tabuleiros que mostram as frota, vamos chamar a função criarTabuleiro, apos receber o numero de navios como parametro
    
        

         

    # Vamos definir se os usuários querem que mostre a frota de navio no tabuleiro ou não durante o jogo
    # Anderson lima : transformar (mostratabuleiro em uma funçao dependente da 2 função)
      

   
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
        
    print(tabuleiro)

imprimir = criarTabuleiro(6)
variavel = configurarJogo()