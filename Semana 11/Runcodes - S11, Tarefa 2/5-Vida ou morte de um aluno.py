#Processamento de dados
def conceito(n):
    #Retorna um conceito dependendo da nota.
    if n >= 8.5:
        return "A"
    elif n >= 7.0:
        return "B"
    elif n >= 5.0:
        return "C"
    elif n >= 4.0:
        return "D"
    elif n >= 0:
        return "E"
    
#Programa principal
def main():
    while True:
        #Digita-se uma nota
        nota = float(input().strip())

        #Interrompe a repetição se a nota estiver entre 0 e 10
        if 0 <= nota <= 10: break
        #A repetição continua até que uma nota válida seja digitada.
        else: print("Nota inválida.")

    #Imprime o conceito correspondente a nota.
    print(conceito(nota))

if __name__ == '__main__':
    main()
