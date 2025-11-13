#Programa principal
def main():
    #Digita-se um número, por enquanto em formato de string
    numero = input("Digite um número: ")

    #Inverte essa string
    invertido = numero[::-1]

    #Converte para número inteiro
    numero_trocado = int(invertido)
    
    #Imprime o número invertido
    print(f"Este é o número invertido {numero_trocado}")

if __name__ == '__main__':
    main()