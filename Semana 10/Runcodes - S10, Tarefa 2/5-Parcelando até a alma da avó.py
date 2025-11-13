#Processamento de dados
def parcelar(valor):
    for i in range(1, 25):
        divisao = valor / i
        print(f"{i}x de R$ {divisao:.2f}")
    
#Programa principal
def main():
    #Entrada
    preco = float(input("Digite um preço: ").strip())

    #Saída
    parcelar(preco)

if __name__ == '__main__':
    main()
