#Processamento de dados
def listas():
    lista_completa = []
    lista_pares = []
    lista_impares = []

    for i in range(20):
        numeros = int(input())
        lista_completa.append(numeros)

    for n in lista_completa:
        if n % 2 == 0: lista_pares.append(n)
        elif n % 2 != 0: lista_impares.append(n)

    return lista_completa, lista_pares, lista_impares

#Programa principal
def main():
    completa, pares, impares = listas()
    
    print(completa)
    print(pares)
    print(impares)

if __name__ == '__main__':
    main()
