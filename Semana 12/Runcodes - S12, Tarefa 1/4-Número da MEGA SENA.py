#Processamento de dados
def numero_da_sorte(data):
    #Contém a soma dos digitos da data de nascimento
    total = 0

    #Separa cada um dos números da data individualmente e adiciona ao total
    for digito in str(data):
        total += int(digito)

    return total
#Programa principal
def main():
    #Entrada - Data de nascimento do usuário, formato ddmmaaaaa.
    nascimento = int(input("Digite sua data de nascimento (ddmmaaaa): "))

    #Chamada da função
    sorte = numero_da_sorte(nascimento)

    #Apresenta o número premiado do usuário
    print("Na Mega da Virada, aposte no número",sorte)

if __name__ == '__main__':
    main()
