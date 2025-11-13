#Processamento de dados
def soma(lista):
    return sum(lista)

#Programa principal
def main():
    lista = []

    while True:
        numero = int(input("Digite um número: "))

        if numero == 0: break

        lista.append(numero)
    
    print('A soma desses números é:', soma(lista))

if __name__ == '__main__':
    main()
    
