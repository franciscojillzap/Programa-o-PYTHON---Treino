#Programa principal
def main():
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    print('Que segredos a mensagem "OMQEMD" esconde? Tente descobrir!')

    resposta = ''
    
    for i in range(6):
        letra = input('\nDigite a letra criptografada: ').upper()
        
        chave = 12

        #FIND() - Determina a posição do caractere/letra
        posicao = alfabeto.find(letra)
        nova_posicao = (posicao - chave) % 26

        #Utiliza a nova_posicao como índice e procura a letra correspondente
        letra_verdadeira = alfabeto[nova_posicao]
        resposta += letra_verdadeira
        
        print(f'Descriptografando..."{letra}" corresponde a:', letra_verdadeira)

    print(f'\nA palavra original escondida era: {resposta}!')
    print('Um viva a JÚLIO CÉSAR!!')

if __name__ == '__main__':
    main()

    
    
