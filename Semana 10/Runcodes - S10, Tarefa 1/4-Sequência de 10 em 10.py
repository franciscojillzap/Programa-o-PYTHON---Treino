#Programa principal
def main():
    # list - Cria uma lista
    # range - gera uma sequência de números. Possui 3 argumentos:
        # START - indica o primeiro número da sequência.
        # STOP - indica o último número da sequência.
        # STEP - indica o andar da sequência, de 2 em 2, de 5 em 5, etc.
    lista_10x10 = list(range(10, 1001, 10))

    # join - junta elementos de uma sequência em uma única string.
        # Usa um string para separar os elementos, como ", " ou " - " e etc.
        # Funciona apenas com string, necessário converter números e afins.
    sequencia = ", ".join(map(str, lista_10x10))

    #Saída com ponto final
    print(sequencia + ".")

    

if __name__ == '__main__':
    main()
