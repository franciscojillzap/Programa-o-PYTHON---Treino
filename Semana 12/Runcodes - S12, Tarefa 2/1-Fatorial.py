#Processamento de dados
def fatorial(n):
    #Recebe o valor do fatorial
    fatorial = 1

    #Se número igual 0, imprime 1
    if n == 0: return 1

    while n > 1:
        #Calcula o fatorial
        fatorial *= n
        #Subtrai o número digitado e adiciona a parte ao fatorial
        n -= 1

    return fatorial        
        
#Programa principal
def main():
    #Entrada - Número inteiro para cálculo do FATORIAL
    numero = int(input("Digite um número: "))

    #Imprime o fatorial do número inserido
    print(f"O fatorial do número lido é:",fatorial(numero))

if __name__ == '__main__':
    main()
