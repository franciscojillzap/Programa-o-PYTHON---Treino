#Processamento de dados
def diferenca(valores):
    
    #A função ABS retorna a diferença real entre dois números.
    #Não retorna números NEGATIVOS
    dif_1 = abs(valores[0] - valores[1])
    dif_2 = abs(valores[0] - valores[2])
    #Qual o número mais próximo do primeiro valor digitado?
    if dif_1 < dif_2:
        return f"O segundo número é o mais próximo do primeiro, e a diferença entre eles é: {dif_1}"
    else:
        return f"O terceiro número é o mais próximo do primeiro, e a diferença entre eles é: {dif_2}"

#Programa principal
def main():
    #Lista VAZIA
    numeros = []

    #Entrada
    for i in range(3):
        n = int(input(f"Digite o {i+1}º número: ").strip())
        numeros.append(n)

    #Saída
    print(diferenca(numeros))

if __name__ == '__main__':
    main()
