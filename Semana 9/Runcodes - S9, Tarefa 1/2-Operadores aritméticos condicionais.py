#Processamento de dados
def operacoes_aritmeticas(valores, calculo):
    
    if calculo == 1:
        return f"A soma desses números é: {sum(valores)}"
    elif calculo == 2:
        subtracao = valores[0] - valores[1]
        return f"O resultado da diferença entre esses números é: {subtracao}"
    elif calculo == 3:
        multiplicacao = valores[0] * valores[1]
        return f"O resultado da multiplicação entre esse números é: {multiplicacao}"
    elif calculo == 4:
        divisao = valores[0] / valores[1]
        return f"A divisão entre esses números é: {divisao:.2f}"
    
#Programa principal
def main():
    #Lista VAZIA
    numeros = []

    #Entrada
    for i in range(2):
        n = int(input(f"Digite o {i+1}º número: ").strip())
        numeros.append(n)

    operacao = int(input('''Escolha a operação que deseja realizar -
1 - ADIÇÃO
2 - SUBTRAÇÃO
3 - MULTIPLICAÇÃO
4 - DIVISÃO
''').strip())

    #Chamada da função
    resultado = operacoes_aritmeticas(numeros, operacao)

    #Saída condicional
    print(resultado)

if __name__ == '__main__':
    main() 
