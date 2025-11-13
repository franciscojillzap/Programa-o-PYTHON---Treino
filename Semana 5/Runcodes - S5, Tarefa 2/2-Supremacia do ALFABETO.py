#Processamento de dados
def eh_alfabeto(letra):
    #Retorna True se houver caracteres pertencentes ao ALFABETO.
    return letra.isalpha()

#Programa principal
def main():
    #Entrada
    l = input("Digite algo: ")
    #Saída
    print(f'O caractere "{l}" faz parte do alfabeto? {eh_alfabeto(l)}')

if __name__ == '__main__':
    main()
