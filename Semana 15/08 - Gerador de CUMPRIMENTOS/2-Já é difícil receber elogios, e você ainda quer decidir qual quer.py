from random import *

def excesso_de_bajulacao(CPF):
    adjetivos = ['maravilhoso', 'acima da média', 'excelente']
    hobbies = ['andar de bicicleta', 'programar', 'fazer chá']

    while True:
        escolha = input('\nEscolha uma opção: ').strip().upper()

        if escolha == '1':
            print('\nAqui está seu cumprimento:')
            print(f'{CPF}, você é {choice(adjetivos)} em {choice(hobbies)}!')

        elif escolha == '2':
            add_hobby = input('Adicione o hobby desejado: ')

            if add_hobby not in hobbies:
                hobbies.append(add_hobby)
            else:
                print(f'\nEste hobby já existe! Você gosta tanto assim de {add_hobby}?')

        elif escolha == '3':
            del_hobby = input('Insira o hobby a ser removido: ')

            if del_hobby in hobbies:
                hobbies.remove(del_hobby)
            else:
                print(f'\n{del_hobby} ainda não faz parte da sua árvore de habilidades.')

        elif escolha == '4':
            print('\nSeus hobbies são:\n')
            for i, hobby in enumerate(hobbies, start = 1):
                print(f'{i} - {hobby}')

        elif escolha == '5':
            print('\nAté um outro dia.')
            break

        elif escolha == 'A':
            add_elogio = input('Adicione o elogio desejado: ')

            if add_elogio not in adjetivos:
                adjetivos.append(add_elogio)
            else:
                print(f'\nEste elogio já existe! Você se acha tão {add_elogio} assim?')

        elif escolha == 'B':
            print('''\nEsses são os elogios que decidiu atribuir a si mesmo...
mas suponho que não passam de hipérboles e falácias:\n''')
            for i, elogio in enumerate(adjetivos, start = 1):
                print(f'{i} - {elogio}')

        elif escolha == 'C':
            print()
            for elogio in adjetivos:
                print(f'{CPF} é {elogio}!')

            print('\nMe recuso a continuar babando seu ovo...')
            break

        else:
            print('Você pode escolher apenas as opções disponíveis.')

def main():
    print('Gerador de Cumprimentos')
    print('-'*23)

    nome = input('Qual é o seu nome? ')
    print('''
Menu
    Principal:
    1 - OBTER cumprimento
    2 - ADICIONAR hobby
    3 - REMOVER hobby
    4 - IMPRIMIR hobbies
    5 - SAIR
    Extra:
    A - ADICIONAR  elogios
    B - IMPRIMIR elogios
    C - APENAS elogios''')

    excesso_de_bajulacao(nome)

if __name__ == '__main__':
    main()
