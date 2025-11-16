#Processamento de dados
def aumento_populacional(a, b):
    #Total de ANOS até superar o país A
    anos = 0

    #Repetição com teste no final
    while True:
        a += (a * 2/100)
        b += (b * 3/100)
        anos += 1

        #Se o país B supera A, finaliza a repetição
        if b > a:
            break

    return anos

#Programa principal
def main():
    #Entrada - População dos países A e B
    A = int(input("Digite a população total do país A: "))
    B = int(input("Digite a população total do país B: "))

    #Se A maior que B, as variáveis mantêm seus valores
    if A > B:
        pais_A = A
        pais_B = B
    #Se A menor que B, as variáveis trocam de valores
    else:
        pais_A = B
        pais_B = A

    #Chamada de função
    tempo = aumento_populacional(pais_A, pais_B)

    #Imprime os anos necessários para que seja possível ao país B
    #superar o país vizinho.
    print("O país B ainda tem",tempo,"anos para alcançar o país A em número populacional.")

if __name__ == '__main__':
    main()
