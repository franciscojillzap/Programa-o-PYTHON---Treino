#Processamento de dados
def quadrado_ou_retangulo(b, h):
    
    #Cálculo do PERÍMETRO e ÁREA de um RETÂNGULO
    perimetro = 2 * (b + h)
    area = b * h
    #Quadrado possui todos os seus lados iguais
    if b == h:
        return "Os valores iguais indicam que este retângulo na verdade é um QUADRADO!"
    #Retângulo possui base e altura distintas
    else:
        return f"PERÍMETRO: {perimetro} - ÁREA: {area}"

#Programa principal
def main():
    #Entrada
    base = int(input("Digite a base do retângulo: ").strip())
    altura = int(input("Digite a altura do retângulo: ").strip())

    #Chamada de função
    resultado = quadrado_ou_retangulo(base, altura)

    #Saída condicional
    print(resultado)

if __name__ == '__main__':
    main()
