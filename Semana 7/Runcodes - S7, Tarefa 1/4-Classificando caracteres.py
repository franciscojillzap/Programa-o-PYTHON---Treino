#Processamento de dados
def oque_e_oque_e(c):
    if c.lower() in "aeiou":
        return f"{c} é vogal."
    elif c.isalpha():
        return f"{c} é consoante."
    elif c.isdigit():
        return f"{c} é número."
    else:
        return f"{c} é símbolo."

#Programa principal
def main():
    #Entrada
    caractere = input("Digite qualquer caractere: ")

    #Chamada da função
    resultado = oque_e_oque_e(caractere)

    #Saída Condicional
    print(resultado)

if __name__ == '__main__':
    main()
