#Processamento de dados
def lista_A(L):
    L.insert(0, 0)
    return L

def lista_B(L):
    L.insert(0, 1)
    return L

def lista_C(L):
    return L

def lista_D(L):
    return L.reverse()

#Programa principal
def main():
    #Dita o número de variáveis que a lista receberá
    n_itens = int(input("Quantos itens? "))

    #Lista VAZIA
    lista = []

    for i in range(n_itens):
        numero = int(input("Digite um número: "))
        lista.append(numero)
    
    #Imprime as listas
    print(lista_A(lista))
    print(lista_B(lista))
    print(lista_C(lista))
    print(lista_D(lista))

if __name__ == '__main__':
    main()