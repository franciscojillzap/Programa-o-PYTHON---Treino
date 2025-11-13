#Processamento de Dados
def a_vista(valor):
    desconto = valor - (valor * 9 / 100)
    return f'{desconto:.2f}'

def prazo_5(valor):
    parcela = valor / 5
    return f'{parcela:.2f}'

def prazo_10(valor):
    preco_juros = valor + (valor * 17 / 100)
    parcela = preco_juros / 10
    return f'{parcela:.2f}'

#Programa Principal
def main():
    #Entrada
    preco = float(input("Digite o total da compra: "))
    #Saída
    print(f"Se pagar à vista, receberá 9% de desconto e pagará apenas R${a_vista(preco)}!")
    print(f"A parcela em até 5 vezes ficará por R${prazo_5(preco)}.")
    print(f"O valor da prestação em 10 vezes custa R${prazo_10(preco)} com de 17% de juros aplicado!")

if __name__ == '__main__':
    main()
