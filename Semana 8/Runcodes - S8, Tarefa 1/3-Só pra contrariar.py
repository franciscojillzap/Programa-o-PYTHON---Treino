#Processamento de dados
def maior(numeros):
    return max(numeros)

def menor(numeros):
    return min(numeros)

#Programa principal
def main():
    #Lista vazia
    lista = []

    #Entrada
    for i in range(5):
        numero = int(input().strip())
        #Adicionar variável a LISTA
        lista.append(numero)

    #Chamada da função
    maior_numero = maior(lista)
    menor_numero = menor(lista)
    
    #Saída
    print(maior_numero)
    print(menor_numero)

if __name__ == '__main__':
    main()

    
        
