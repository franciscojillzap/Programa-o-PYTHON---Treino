#Processamento de dados
def soma_cumulativa(L):
    my_list = []
    soma_termos = 0

    for numero in L:
        soma_termos += numero
        my_list.append(soma_termos)

    return my_list
    
#Programa principal
def main():
    lista = []

    while True:
        numeros = int(input())

        if numeros != 0: lista.append(numeros)
        if numeros == 0: break

    print(soma_cumulativa(lista))

if __name__ == '__main__':
    main()
