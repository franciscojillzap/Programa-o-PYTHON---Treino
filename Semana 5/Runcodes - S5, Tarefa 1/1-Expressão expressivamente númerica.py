#PROCESSAMENTO de DADOS
def calcular(a, b, c):
    #Retorna o resultado da expressão.
    return 2 * a + 5 * b - c

#PROGRAMA PRINCIPAL
def main():
    #Entrada
    A = int(input("Digite o valor de A: "))
    B = int(input("Digite o valor de B: "))
    C = int(input("Digite o valor de C: "))

    #Chama a função
    resultado = calcular(A, B, C)

    #Saída
    print(f"""Substituindo as letras A, B e C por {A}, {B} e {C}
na expressão 2 * A + 5 * B - C, temos como resultado {resultado}!""")

if __name__ == '__main__':
    main()
