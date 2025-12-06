from random import *

def nomes():
    macho = ['Fred', 'Thor', 'Paçoca', 'Bob']
    femea = ['Pipoca', 'Penélope', 'Amora', 'Mel']

    while True:
        escolha = input('\nEscolha uma opção: ')

        if escolha == '1':
            print(f'Seu animal de estimação pode se chamar {choice(macho)}!')

        elif escolha == '2':
            print(f'Seu animal de estimação pode se chamar {choice(femea)}!')

        elif escolha == '3':
            opcao = input('\nDeseja ADICIONAR (A) ou REMOVER (R) algum nome? ').strip().upper()

            if opcao == 'A':
                add_macho = input('Digite o nome que deseja adicionar: ')
                if add_macho not in macho:
                    macho.append(add_macho)
                else:
                    print('\nEsse nome já existe!')
                    
            elif opcao == 'R':
                del_macho = input('Digite o nome que deseja remover: ')
                if del_macho in macho:
                    macho.remove(del_macho)
                else:
                    print('\nNome não encontrado.')

        elif escolha == '4':
            opcao = input('\nDeseja ADICIONAR (A) ou REMOVER (R) algum nome? ').strip().upper()

            if opcao == 'A':
                add_femea = input('Digite o nome que deseja adicionar: ')
                if add_femea not in femea:
                    femea.append(add_femea)
                else:
                    print('\nEsse nome já existe!')
                    
            elif opcao == 'R':
                del_femea = input('Digite o nome que deseja remover: ')
                if del_femea in femea:
                    femea.remove(del_femea)
                else:
                    print('\nNome não encontrado.')

        elif escolha == '5':
            print('Até um outro dia.')
            break

        else:
            print('Digite uma entrada válida.')
            
def main():
    print('Serviço de escolha de nomes para animais de estimação')
    print('-'*53)

    print('''Menu
    1 - Nomes para animal de estimação MACHO
    2 - Nomes para animal de estimação FÊMEA
    3 - ADICIONAR/REMOVER nomes para MACHO
    4 - ADICIONAR/REMOVER nomes para FÊMEA
    5 - SAIR''')

    nomes()
    
if __name__ == '__main__':
    main()
