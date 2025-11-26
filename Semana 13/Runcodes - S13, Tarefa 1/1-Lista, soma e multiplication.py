#Importa a biblioteca matemática do Python
from math import prod

#Processamento de dados
def soma(lista):
    #Realiza a soma de todos os itens da lista
    return sum(lista)

def produto(lista):
    #Realiza a multiplicação de todos os itens da lista
    return prod(lista)

#Programa principal
def main():
    #Lista VAZIA
    lista = []

    #Repetição com final determinado até 10
    for i in range(10):
        numero = int(input(f"Digite o {i+1}º número: "))
        #Adiciona a variável a lista
        lista.append(numero)
    
    #Imprime a lista completa com as variáveis, soma e multiplicação
    print("Esta lista contêm todos os números digitados:", lista)
    print("A soma total desses números é:", soma(lista))
    print("O produto desses números equivale a:", produto(lista))

if __name__ == '__main__':
    main()
