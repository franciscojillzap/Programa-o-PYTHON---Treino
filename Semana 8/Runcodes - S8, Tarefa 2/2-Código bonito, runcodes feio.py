#Processamento de dados
def deus_me_ajude(variavel):
    if (int(variavel) >= 100000) or (int(variavel) < 0):
        return "Este número é igual ou superior à 100.000, ou é um número negativo."
    elif len(variavel) == 1:
        return f"Este número possui apenas um algarismo: {variavel}"
    elif len(variavel) == 2:
        digito_1 = int(variavel[0])
        digito_2 = int(variavel[1])
        return f"Este número possui dois algarismos, a soma entre eles é: {digito_1 + digito_2}"
    elif len(variavel) == 3:
        digito_1 = int(variavel[0])
        digito_2 = int(variavel[1])
        digito_3 = int(variavel[2])
        return f"Este número possui três algarismos, a soma entre eles é: {digito_1 + digito_2 + digito_3}"
    elif len(variavel) == 4:
        digito_1 = int(variavel[0])
        digito_2 = int(variavel[1])
        digito_3 = int(variavel[2])
        digito_4 = int(variavel[3])
        return f"Este número possui quatro algarismos, a soma entre eles é: {digito_1 + digito_2 + digito_3 + digito_4}"
    elif len(variavel) == 5:
        digito_1 = int(variavel[0])
        digito_2 = int(variavel[1])
        digito_3 = int(variavel[2])
        digito_4 = int(variavel[3])
        digito_5 = int(variavel[4])
        return f"Este número possui cinco algarismos, a soma entre eles é: {digito_1 + digito_2 + digito_3 + digito_4 + digito_5}"
    
#Programa principal
def main():
    #Entrada
    numero = input("Digite um número (entre 0 e 100.000): ").strip()

    #Chamada da função
    resultado = deus_me_ajude(numero)

    #Saída
    print(resultado)

if __name__ == '__main__':
    main()
