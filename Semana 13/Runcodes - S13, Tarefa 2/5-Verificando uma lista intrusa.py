#Processamento de dados
def esta_ordenado(lista_original):
    lista_ordenada = sorted(lista_original)

    if lista_original == lista_ordenada:
        return 'LISTA ORDENADA'
    else:
        return 'LISTA NÃO ORDENADA'

#Programa principal
def main():
    lista = []
    
    n = int(input())

    for i in range(n):
        termo = float(input())
        lista.append(termo)

    print(esta_ordenado(lista))

if __name__ == '__main__':
    main()
