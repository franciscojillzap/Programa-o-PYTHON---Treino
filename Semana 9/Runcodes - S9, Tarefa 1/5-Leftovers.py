#Processamento de dados
def resto(valor):
    
    #Resto da divisão por 5
    resto = valor % 5

    #Resto condicional
    if resto == 0:
        return 9 * valor + 7
    elif resto == 2:
        return 5 * (valor ** 2) - (3 * valor) + 42
    elif resto == 3:
        return valor // 10
    elif resto == 4:
        return valor ** 2
    elif resto == 1 and (valor % 2 == 0):
        return "Este número é PAR!"
    else:
        return "Este número é ÍMPAR!"

#Programa principal
def main():
    
    #PEQUENA explicação do programa ao usuário
    print('''Este programa lê um número inteiro e realiza uma operação diferente
dependendo do resto de sua divisão por 5 -

Se resto = 0,
    calcula: 9 * (número digitado) + 7
Se resto = 1,
    analisa se o valor digitado é PAR ou ÍMPAR
Se resto = 2,
    calcula: 5 * (número **2) - (3 * número) + 42
Se resto = 3,
    calcula: número // 10
Se resto = 4,
    calcula: número **2
''')
    
    #Entrada
    numero = int(input("Digite um número: ").strip())

    #Saída
    print(resto(numero))

if __name__ == "__main__":
    main()
