#Processamento de dados
def eh_vogal(letra):
    #Converte para minúsculo e retorna True caso faça parte das VOGAIS.
    return letra.lower() in "aeiou"

#Programa principal
def main():
    #Entrada
    l = input("Digite uma letra: ")
    #Saída
    print(f'Dizer que a letra "{l}" é uma vogal é uma afirmação: {eh_vogal(l)}')

if __name__ == '__main__':
    main()
