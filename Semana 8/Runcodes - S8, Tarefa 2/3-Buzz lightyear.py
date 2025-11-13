#Processamento de dados
def mensagem(variavel):
    if (variavel % 3 == 0) and (variavel % 5 == 0):
        return "FIZZBUZZ - Este número é divisível por 3 e 5 ao mesmo tempo!"
    elif variavel % 3 == 0:
        return "FIZZ - Este número é divisível por 3!"
    elif variavel % 5 == 0:
        return "BUZZ - Este número é divísivel por 5!"
    else:
        if not (variavel % 3 == 0) or (variavel % 5 == 0):
            return "Este número não é nem divísivel por 3, nem por 5..."

#Programa principal
def main():
    #Entrada
    numero = int(input("Digite um número: ").strip())

    #Saída
    print(mensagem(numero))

if __name__ == '__main__':
    main()
