#Processamento de dados
def calculo_IMC(massa, tamanho):
    #Cálculo do Índice de Massa Corporal
    IMC = massa / tamanho**2
    return f"\nSeu Índice de Massa Corporal é {IMC:.2f}"

def classe_peso(massa, tamanho):
    IMC = massa / tamanho**2

    #Classificação
    if IMC < 18.5:
        return "Abaixo do peso"
    elif IMC < 25:
        return "Peso normal"
    elif IMC < 30:
        return "Sobrepeso"
    elif IMC < 35:
        return "Obeso leve"
    elif IMC < 40:
        return "Obeso moderado"
    elif IMC >= 40:
        return "Obeso mórbido"    

#Programa principal
def main():
    #Entrada
    peso = float(input("Digite seu peso: ").strip())
    altura = float(input("Digite sua altura: ").strip())

    #Chamada de função
    seu_indice = calculo_IMC(peso, altura)
    sua_classificacao = classe_peso(peso, altura)

    #Saída
    print(seu_indice)
    print(f"Você é classificado como: {sua_classificacao}")

if __name__ == '__main__':
    main()
