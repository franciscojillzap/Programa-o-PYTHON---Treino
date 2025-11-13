#Processamento de dados
def arredondar(numero):
    return round(numero)

#Programa principal
def main():
    #Entrada
    dinheiro = float(input("Digite um valor monetário: ").strip())
    #Saída
    print(f"Este valor arredondado é igual a R${arredondar(dinheiro):.2f}")

if __name__ == '__main__':
    main()
