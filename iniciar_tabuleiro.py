# MODULARIZAÇÃO DA FUNÇÃO CRIAR TABULEIRO  // INICIAR TABULEIRO

''' ESSA FUNÇÃO FICA DOS PARAMETROS DE ORDEM E QUANTIDADE DE NAVIOS, PARA A IMPRESSÃO DOS TABULEIROS.
    É RESPONSABILIDADE DESSA FUNÇÃO :  
    ! Imprimir os tabuleriros ocultos e com navios, fazer a verificação os lados adjacentes da matriz, imprimir aleatoriamente 
'''

from random import randint


''' TABULEIRO VAI CRIAR UMA MATRIZ DE ORDEM A SER DEFINIDA PELOS USUARIOS, 
    NOSSA MISSÃO É FAZER COM QUE OS ELEMENTOS (QUE INICIALMENTE SERÃO "-")
    TROQUEM PARA ELEMENTOS QUE CONTÉM A LETRA "N", ISSO DE MANEIRA ALEATORIA
    '''



def Iniciar_Tabuleiro(Quantidade_Navios,Ordem):
    if Quantidade_Navios <= 6 and Quantidade_Navios >= 1:
        Tabuleiro = [[None] * Ordem for i in range(Ordem)]
        for Linha in range(Ordem):
            for Coluna in range(Ordem):
                print(Tabuleiro)
       
    else:
        '''DEVERÁ CHAMAR A FUNÇÃO DE INSERIR A QUANTIDADE DE NAVIOS NOVAMENTE'''
        print(" INSIRA UMA QUANTIDADE DE NAVIOS VÁLIDA (ENTRE 1 À 6)")
   
def Destribuir_Navios():
    Iniciar_Tabuleiro(Navios, Ordem)
    Atribuir_Navios = 0       
   

Navios = 6 #int(input("DIGITE A QUANTIDADE DE NAVIOS (NO MAXIMO = 6 , NO MINIMO = 1)"))
Ordem =  8#int(input("DIGITE A ESCALA DO TABULEIRO (NO MAXIMO = 8)")) 
Configurar_Tabuleiro = Iniciar_Tabuleiro(Navios,Ordem)