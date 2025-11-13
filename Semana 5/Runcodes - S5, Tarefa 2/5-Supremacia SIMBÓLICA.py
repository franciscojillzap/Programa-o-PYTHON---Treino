#Processamento de dados
def eh_simbolo(s):
    return s.isalnum()

#Programa principal
def main():
    #Entrada
    simbolo = input("Digite um símbolo: ")
    #Saída que retorna True para o caractere que não for nem letra nem número.
    print(f'"{simbolo}" é um símbolo {not eh_simbolo(simbolo)}!')

if __name__ == '__main__':
    main()
