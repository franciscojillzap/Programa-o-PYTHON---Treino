#Processamento de dados
def so_pares(conjunto):
    #Lista para receber apenas os números pares do conjunto
    lista_pares = []

    for numero in conjunto:
        if numero % 2 == 0:
            lista_pares.append(numero)

    #Retorna quantos números pares existem dentro do conjunto
    return len(lista_pares)

def so_impares(conjunto):
    #Lista para receber apenas os números ímpares do conjunto
    lista_impares = []

    for numero in conjunto:
        if numero % 2 != 0:
            lista_impares.append(numero)

    #Retorna quantos números ímpares existem dentro do conjunto
    return len(lista_impares)
    
#Programa principal
def main():
    #Lista VAZIA
    conjunto_100 = []

    #Entrada - (100 números inteiros? É sério?)
    for i in range(100):
       numeros = int(input(f"Digite o {i+1}º número: ").strip())
       sconjunto_100.append(numeros)
        
    #Saída para PARES
    print(f"Dos números digitados, {so_pares(conjunto_100)} são pares!")

    #Saída para ÍMPARES
    print(f"Dos números digitados, {so_impares(conjunto_100)} são ímpares")

if __name__ == '__main__':
    main()

