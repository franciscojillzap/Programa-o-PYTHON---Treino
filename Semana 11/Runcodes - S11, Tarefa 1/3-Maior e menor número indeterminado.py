#Processamento de dados
def maior(lista):
    return max(lista)

def menor(lista):
    return min(lista)

#Programa principal
def main():
    #Lista vazia para receber números
    lista = []
    while True:
        #Continuará pedindo novos números até que o próxima seja 0.
        numero = int(input())        

        #Se o próximo número for 0, a iteração é interrompida.
        if numero == 0: break

        #Cada novo número será adicionado a lista.
        lista.append(numero)    

    #Imprime o resultado
    print(maior(lista))
    print(menor(lista))

if __name__ == '__main__':
    main()
        
