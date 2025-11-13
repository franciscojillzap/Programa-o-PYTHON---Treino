#Processamento de dados
def juros_acumulado(valor, taxa):
    #Guardará os anos que levaram para o depósito atingir o dobro.
    anos = 0
    #Armazena o valor original do depósito.
    valor_inicial = valor

    #Repete as instruções enquanto o valor for menor que o dobro do valor inicial
    while valor < valor_inicial * 2:
        #Cálculo dos juros
        valor += (valor * taxa / 100)
        #Adiciona mais um ano até que seja atingido o dobro.
        anos += 1
    return anos

#Programa principal
def main():
    #Pergunta-se o valor inicial de um depósito de dinheiro.
    d_inicial = float(input("Indique o valor do seu depósito inicial: "))
    #Pergunta-se  o valor da taxa anual que será aplicada ao depósito.
    t_anual = float(input("Indique a porcentagem anual de juros que será aplicada a esse valor: "))

    #Chamada da função
    anos_totais = juros_acumulado(d_inicial, t_anual)

    #Imprime o tempo decorrido até o depósito atingir o dobro do seu valor
    print(f"Levará {anos_totais} anos até que seu depósito atinja o dobro do valor.")

if __name__ == '__main__':
    main()
    
