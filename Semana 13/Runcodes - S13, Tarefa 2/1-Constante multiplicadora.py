#Processamento de dados
def multiplica_constante(L, C):
    lista_constante = []

    for numero in L:
        n = numero * C
        lista_constante.append(n)
    
    return lista_constante

#Programa principal
def main():
    lista = []

    while True:
        numeros = int(input('Digite um número: '))
        
        if numeros != 0:
            lista.append(numeros)
        
        if numeros == 0: break
    
    constante = int(input('Digite o valor da constante multiplicadora: '))
    
    print(multiplica_constante(lista, constante))
if __name__ == '__main__':
    main()
