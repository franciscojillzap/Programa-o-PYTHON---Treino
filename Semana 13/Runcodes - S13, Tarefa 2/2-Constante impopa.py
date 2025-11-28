#Processamento de dados
def multiplica_constante(L):
    lista_final = sorted(L)

    for i in range(len(lista_final)):
        if i % 2 == 0:
            lista_final[i] *= 3
        else:
            lista_final[i] *= 5
        
    return lista_final

#Programa principal
def main():
    lista = []

    for i in range(100):
        numeros = int(input())
        lista.append(numeros)
    
    print(multiplica_constante(lista))

if __name__ == '__main__':
    main()
