#Processamento de Dados
def quantas_letras(palavra):
    #Lê quantidade de caracteres de uma palavra.
    return len(palavra)

#Programa Principal
def main():
    #Entrada
    p = input("Digite uma palavra: ")
    #Saída
    print(f'A palavra "{p}" tem {quantas_letras(p)} letras no total!')

if __name__ == '__main__':
    main()
