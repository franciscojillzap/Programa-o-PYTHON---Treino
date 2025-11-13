#Processamento de dados
def e_impopa(n):
    if n % 2 != 0:
        return f"Certamente {n} é um número ímpar. True!"
    else:
        return f"{n} é ímpar? False! Em que diabos de escola você estudou?!"
    
#Programa principal
def main():
    #Entrada
    numero = int(input("Digite um número ímpar: "))

    #Chamada da função
    e_parouimpa = e_impopa(numero)

    #Saída Condicional
    print(e_parouimpa)
    
if __name__ == '__main__':
    main()
