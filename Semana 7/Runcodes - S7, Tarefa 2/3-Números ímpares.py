#Processamento de dados
def quantos_impares(digitos):
    dezena = digitos // 10
    unidade = digitos % 10

    if dezena % 2 == 0 and unidade % 2 != 0 or dezena % 2 != 0 and unidade % 2 == 0:
        return "Apenas um dígito é ímpar."
    elif dezena % 2 != 0 and unidade % 2 != 0:
        return "Os dois dígitos são ímpares."
    else:
        return "Nenhum dígito é ímpar."
        
#Programa principal
def main():
    #Entrada
    numero = int(input("Dígite um número de 10 à 99: ").strip())

    #Chamada da função
    o_numero_tem = quantos_impares(numero)

    #Saída condicional
    print(o_numero_tem)

if __name__ == '__main__':
    main()
    
