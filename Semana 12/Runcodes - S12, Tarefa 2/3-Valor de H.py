#Processamento de dados
def calculo_H(termos):
    H = 0

    for i in range(1, termos + 1):
        H += 1 / i

    return f"{H:.4f}"

#Programa principal
def main():
    #Entrada
    n_termos = int(input())

    #Imprime o resultado
    print(calculo_H(n_termos))

if __name__ == '__main__':
    main()
