#Programa principal
def main():
    while True:
        print('OPÇÕES:')
        print('1 - SAUDAÇÃO')
        print('2 - BRONCA')
        print('3 - FELICITAÇÃO')
        print('0 - FIM')

        escolha = int(input())

        if escolha == 1:
            print("1 - Olá. Como vai?")
        elif escolha == 2:
            print("2 - Vamos estudar mais.")
        elif escolha == 3:
            print("3 - Meus parabéns!")
        elif escolha > 3:
            print("Opção inválida.")
        if escolha == 0:
            print("0 - Fim de serviço.")
            break

if __name__ == '__main__':
    main()