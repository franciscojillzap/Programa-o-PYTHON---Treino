from random import *

continuar = True

#Instruções do jogo
print('''
Porta da FORTUNA!

Uma dessas três portas guarda um tesouro maior que o ONE PIECE!
Seu trabalho é adivinhar em qual porta ele está.
Faça suas apostas...e leve o prêmio para casa!

    _______     _______     _______    
   |       |   |       |   |       |
   |  [1]  |   |  [2]  |   |  [3]  |
   |      o|   |      o|   |      o|
   |       |   |       |   |       |
   |_______|   |_______|   |_______|
''')

#Contador de acertos
acertos = 0

#O jogo continua por tempo indeterminado, até o jogador encher o saco
while continuar == True:    
    print("\nQual porta deseja abrir? 1, 2 ou 3?")

    #Transforme a porta escolhida em número inteiro
    escolha_porta = int(input())

    #Escolha a porta certa aleatoriamente
    porta_premiada = randint(1,3)

    #Mostre a porta escolhida pelo usuário e a porta certa
    print("Sua escolha foi a porta...", escolha_porta)
    print("A porta que guarda o tesouro é a...", porta_premiada)

    #Entre a glória e a humilhação
    if escolha_porta == porta_premiada:
        print("Eita, bicho de SORTE!")
        #Mais um ponto toda vez que acerta!
        acertos += 1
    else:
        print("Eita, azar dos INFERNOS!")
        #Pega todos os pontos ganhos e os joga no lixo toda vez que erra!
        acertos = 0

    #Decidindo se o jogo continua
    print("\nVai desistir? (S/N)")
    decidir_rumo = input().lower()

    if decidir_rumo in ["s", "sim"]:
        continuar = False

#Total de acertos
print(f"\nVocê acertou a porta correta um total de {acertos} vezes!")
#Despedida
print("Adeus! Sei pode fazer melhor do que isso.")

    
