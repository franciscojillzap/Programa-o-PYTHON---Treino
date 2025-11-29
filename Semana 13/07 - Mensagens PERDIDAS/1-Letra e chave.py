#Programa principal
def main():
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while True:
        letra = input('\nDigite a letra que deseja criptografar: ').upper()
        
        if letra == 'D':
            chave = 7
        elif letra == 'X':
            chave = 4
        else:
            chave = int(input('A chave codificadora é: '))

        #FIND() - Determina a posição do caractere/letra
        posicao = alfabeto.find(letra)
        nova_posicao = (posicao + chave) % 26

        #Utiliza a nova_posicao como índice e procura a letra correspondente
        letra_criptografada = alfabeto[nova_posicao]
        print(f'A letra criptografada correspondente é:', letra_criptografada)

        parada = int(input('\nDeseja continuar? (1 - SIM / 2 - NÃO) '))

        if parada == 2: break

    print('Até logo.')

if __name__ == '__main__':
    main()

    
    
