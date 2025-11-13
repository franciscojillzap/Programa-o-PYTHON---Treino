#Processamento de dados
def eh_alfa_numero(caractere):
    #Retorna True se for um dígito de 0 à 9 ou pertencer ao alfabeto.
    return caractere.isalnum()

#Programa principal
def main():
    #Entrada
    c = input("Digite algo: ")
    #Saída
    print(f'"{c}" faz parte do conjunto alfanúmerico? {eh_alfa_numero(c)}')

if __name__ == '__main__':
    main()
