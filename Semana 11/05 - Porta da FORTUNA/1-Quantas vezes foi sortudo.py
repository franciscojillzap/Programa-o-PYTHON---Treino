from random import *

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

#São permitidos apenas 3 tentativas
for attempt in range(3):    
    print("\nQual porta deseja abrir? 1, 2 ou 3?")

    #Transforme a porta escolhida em número inteiro
    escolha_porta = int(input())

    #Escolha a porta certa aleatoriamente
    porta_premiada = randint(1,3)

    #Mostre a porta escolhida pelo usuário e a porta certa
    print("Sua escolha foi a porta...",escolha_porta)
    print("A porta que guarda o tesouro é a...",porta_premiada)

    #Entre a glória e a humilhação
    if escolha_porta == porta_premiada:
        print("Eita, bicho de SORTE!")
        acertos += 1
    else:
        print("Eita, azar dos INFERNOS!")

#Total de acertos
print(f"\nVocê acertou a porta correta um total de {acertos} vezes!")

    
