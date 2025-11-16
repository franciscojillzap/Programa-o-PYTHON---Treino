#Processamento de dados
def tempo_ate_comprar(carro):
    
    #Dinheiro depositado no banco
    poupanca = 10000

    #Tempo decorrido em MESES, determina o aumento da poupança,
    #preço do carro e o tempo levado até que possa ser comprado.
    meses = 0

    #Repetição com teste no início
    while poupanca < carro:
        poupanca += (poupanca * 0.7/100)
        carro += (carro * 0.4/100)
        meses += 1

    return meses

#Programa principal
def main():
    #Entrada - Preço do carro
    preco_carro = float(input("Qual o preço do fusca azul? "))

    #Chamada de função
    eternidade = tempo_ate_comprar(preco_carro)

    #Declara o tempo que levará até que se tenha dinheiro suficente para
    #comprar o carro à vista.
    print("Levará uma eternidade equivalente a", eternidade ,"meses...")

if __name__ == '__main__':
    main()
