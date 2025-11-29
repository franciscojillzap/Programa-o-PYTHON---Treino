#Processamento de dados
def criptografar(msg, key):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    mensagem_criptografada = ''

    for char in msg:
        if char in alfabeto:
            posicao = alfabeto.find(char)
            nova_posicao = (posicao + key) % 26

            mensagem_criptografada += alfabeto[nova_posicao]

        else:
            mensagem_criptografada += char

    return mensagem_criptografada

def descriptografar(msg, key):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    mensagem_descriptografada = ''

    for char in msg:
        if char in alfabeto:
            posicao = alfabeto.find(char)
            nova_posicao = (posicao - key) % 26

            mensagem_descriptografada += alfabeto[nova_posicao]

        else:
            mensagem_descriptografada += char

    return mensagem_descriptografada

def main():
    while True:
        print('''\nOPÇÃO:\n
1 - CRIPTOGRAFAR
2 - DESCRIPTOGRAFAR
3 - SAIR
''')
        try:
            resposta = int(input('O que deseja? '))
        except ValueError:
            print('Apenas números, gênio.')
            continue

        if resposta == 1:
            mensagem = input('\nDigite a mensagem a ser criptografada: ').upper()
            chave = int(input('Sua chave codificadora é: '))

            print('\nA mensagem modificada é:', criptografar(mensagem, chave))

        if resposta == 2:
            mensagem = input('Digite a mensagem a ser descriptografada: ').upper()
            chave = int(input('Sua chave codificadora é: '))

            print('A mensagem original é:', descriptografar(mensagem, chave))

        if resposta == 3:
            print('Até um outro dia.')
            break

        else:
            print('\nVocê tem apenas 3 opções disponíveis.')

    print('\nYROJ CDQJLHI, FDPSHÃR VXSHU-SHQD!')
    print('Chave = Quantas vitórias Wally tinha antes de lutar com Ippo?')
if __name__ == '__main__':
    main()
                    

            
