#Processamento de dados
def media_de_100(digitos):
    #Cálculo da MÉDIA
    return sum(digitos) / len(digitos)

#Programa principal
def main():
    #Lista VAZIA
    conjunto_100 = []

    #Entrada
    for i in range(100):
        numeros = int(input(f"Digite o {i+1}º número: ").strip())
        conjunto_100.append(numeros)

    #Chamada da função
    resultado = media_de_100(conjunto_100)

    #Saída
    print(f"A média aritmética desse conjunto de 100 NÚMEROS é: {resultado:.2f}")

if __name__ == '__main__':
    main()
