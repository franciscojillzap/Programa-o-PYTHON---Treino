#Processamento de dados
def contagem(texto):
    return len(texto)

#Programa principal
def main():
    #Entrada
    frase = input("Digite uma frase: ").strip()
    #Saída
    print(f'A frase "{frase}" tem exatamente {contagem(frase)} caracteres!')

if __name__== '__main__':
    main()
    
