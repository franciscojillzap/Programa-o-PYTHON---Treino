#Programa principal
def main():
    #Lista VAZIA
    lista = []

    #Entrada
    for i in range(3):
        numeros = int(input(f"Digite o {i+1}º número: ").strip())
        lista.append(numeros)

    #Organiza a lista de forma ordenada, disposta em ordem CRESCENTE.
    ordem_crescente = sorted(lista)

    print("A ordem crescente desses números:")

    #Saída com números em ordem crescente.
    for numeros in ordem_crescente:
        print(numeros)

    #Lista ORIGINAL, o método ".sorted()" não altera seu conteúdo.
    print(f"Lista original:", lista)

    #Organiza a lista de forma ordenada, disposta em ordem DECRESCENTE.
    ordem_decrescente = sorted(lista, reverse=True)

    print("A ordem decrescente desses números:")

    #Saída com números em ordem decrescente.
    for numeros in ordem_decrescente:
        print(numeros)

    #Mesmo propósito de ".sorted()", mas altera lista original permanentemente.
    lista.sort()

    print(f"Lista original modificada (CRESCENTE):", lista)

    #Pode-se reverter a ordem da lista para decrescente também
    lista.sort(reverse=True)

    print(f"Lista original modificada (DECRESCENTE):", lista)
    

if __name__ == '__main__':
    main()
    
