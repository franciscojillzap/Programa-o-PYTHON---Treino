#Processamento de dados
def eh_consoante(letra):
    #Retorna True caso seja CONSOANTE, False se VOGAL.
    return letra.isalpha() and letra.lower() not in "aeiou"

#Programa principal    
def main():
    #Entrada
    l = input("Digite uma letra: ")
    #Saída
    print(f'É uma afirmação {eh_consoante(l)} dizer que "{l}" é uma consoante.')

if __name__ == '__main__':
    main()

    
