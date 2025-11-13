#Processamento de Dados
def leitor_código(caractere):
    #Lê o código númerico de UM caractere por vez.
    return ord(caractere)

#Programa Principal
def main():
    #Entrada
    c = input()
    #Saída
    print(leitor_código(c))

if __name__ == '__main__':
    main()
