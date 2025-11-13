#Processamento de dados
def soma_se_impopa(variavel):
    if variavel % 2 == 0:
        return f"Esse número é par, somando-o a 5, fica: {variavel + 5}"
    else:
        return f"Esse número é ímpar, somando-o a 8, fica: {variavel + 8}"

#Programa principal
def main():
    #Entrada
    numero = int(input("Digite um número: ").strip())

    #Chamada de função
    resultado = soma_se_impopa(numero)

    #Saída condicional
    print(resultado)

if __name__ == '__main__':
    main()
