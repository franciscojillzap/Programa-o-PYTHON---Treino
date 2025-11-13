#Processamento de dados
def media_indeterminada(lista):
    #Pega os números e realiza a média aritmética entre eles.
    media = sum(lista) / len(lista)
    
    #Retorna o resultado da média
    return f"{media:.2f}"

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

    #Chamada da função
    resultado = media_indeterminada(lista)

    #Imprime o resultado
    print(resultado)

if __name__ == '__main__':
    main()
        
