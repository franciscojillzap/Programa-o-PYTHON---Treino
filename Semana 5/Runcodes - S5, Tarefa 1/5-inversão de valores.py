#PROCESSAMENTO de DADOS
def numero_invertido(valor):
    #Inverte o valor do número
    return str(valor)[::-1]

#PROGRAMA PRINCIPAL
def main():
    #Entrada
    original = int(input("Digite um valor entre 1000 e 9999: "))

    #Saída
    print(f"Ao invertê-lo, ele ficará assim: {numero_invertido(original)}!")

if __name__ == '__main__':
    main()
