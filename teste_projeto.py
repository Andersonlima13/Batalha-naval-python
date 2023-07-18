from random import randint
from time import sleep

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

    
    
    nomeJogador1 = str(input('🔘 NOME DO PRIMEIRO JOGADOR: ')).upper().strip()
    sleep(0.5)
    nomeJogador2 = str(input('🔘 NOME DO SEGUNDO JOGADOR: ')).upper().strip()
    sleep(0.5)
    nome_jogadores = "NOME DO JOGADOR 1 :" + nomeJogador1+"|" + '\n' + "|" + "NOME DO JOGADOR 2 :" + nomeJogador2 + '\n'
    arq.write(nome_jogadores)
    print('\nArquivo gerado com sucesso.')
        

    # Escolher a quantidade de navios que cada jogador possuirá, enquanto a funçao é executada
    quantidadeDeNavios = int(input('🚢 Número de navios de cada jogador 🚢 [máximo = 6]: '))      
    sleep(0.5)
    
    tabuleiroJogador1 = criarTabuleiro(quantidadeDeNavios)
    tabuleiroJogador2 = criarTabuleiro(quantidadeDeNavios) 
        
        
            
    
   
    
def criarTabuleiro(quantidadeDeNavios):  
    tabuleiro = [['-']*ordem for i in range(ordem)]
    
    cont = 0

    # Impede que os navios encostem uns nos outros, verificando de há navios adjacentes
    # logo, contador só recebe mais naviis ao passar pelas condicionais
    
    while cont < quantidadeDeNavios:
        linha = randint(0, ordem - 1)
        coluna = randint(0, ordem - 1)
# VALOR N = B5 : adjacentes = A4 , A5, A6 , B4, B6, C4,C5,C6

#ou seja , a logica é B-1 que vai ser == A , e vai verificar se existe um item "n"
#no valor 5 - 1 e 5 + 1,   
# O METODO -> um primeiro laço for vai verificar as matrizes, se houver um valor == "N" , O VALOR DOS INDICES DEVERÃO SER GUARDADOS
# EXEMPLO INDICE 2 , 5 , LOGO , OUTRO FOR ENTRA EM AÇÃO NOS INDICES 2 - 1 ATÉ 5-1 ASSIM COMO 5 - 1 E 5 + 1 E TAMBÉM 2+1 ATÉ 5+1
# LOGO ELE FAZ ESSA VERIFICAÇÃO , COMO SO VÃO EXISTIR VALORES DE '-' , O  N SERÁ ATRIBUIDO, VOLTANDO PRO LAÇO FOR  

        tabuleiro[linha][coluna] = 'N'
        
        
        cont += 1

    return tabuleiro


while True:
    escolha = int(input('😀 Olá, o que você deseja fazer?\n[1 - Iniciar um novo jogo?] ✔️\n[2 - Sair] 👋\n'))
    if escolha == 2:
        break
    sleep(1)
    print('🎉 Vamos começar 🎉')
    sleep(1)
    configurarJogo()
    print(tabuleiroJogador1)
