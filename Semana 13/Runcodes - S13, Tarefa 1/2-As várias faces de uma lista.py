#Processamento de dados
def lista_A(tt):
    #Lista VAZIA
    A = []
    #Adiciona itens na lista de acordo com o total desejado
    for i in range(tt):
        A.append(i*0)
    #Retorna a lista contendo apenas um conjunto de números ZERO
    return A

def lista_B(tt):
    #Lista VAZIA
    B = []
    #Adiciona itens na lista de acordo com o total desejado
    for i in range(tt):
        B.append(i+1)
    #Retorna a lista contendo os números de 1 até total almejado
    return B

def lista_C(tt):
    #Lista VAZIA
    C = []
    #Adiciona itens na lista de acordo com o total desejado
    for i in range(tt):
        numero = int(input(f"Digite o {i+1}º número: "))
        C.append(numero)
    #Retorna a lista contendo as variáveis digitadas
    return C

def lista_D(tt):
    #Lista VAZIA
    D = []
    #Adiciona itens na lista de acordo com o total desejado
    for i in range(tt):
        numero = int(input(f"Digite o {i+1}º número: "))
        D.append(numero)
    #Os últimos serão os primeiros
    D.reverse()
    #Retorna a lista contendo as variáveis em ordem invertida
    return D

#Programa principal
def main():
    #Determina o número de itens da lista
    total = int(input("Quantos itens cada lista deve ter? "))

    #Imprime as listas
    print("Está lista revela meu saldo bancário:", lista_A(total))
    print(lista_B(total))
    print(lista_C(total))
    print(lista_D(total))

if __name__ == '__main__':
    main()
    
