#Processamento de Dados
def maior(n):
    #Analisa os números e retorna aquele que for o MAIOR.
    maior_numero = max(n)
    return maior_numero

def menor(n):
    #Analisa os números e retorna aquele que for o MENOR.
    menor_numero = min(n)
    return menor_numero

def media(n):
    #Realiza o cálculo da MÉDIA.
    media = sum(n) / len(n)
    return media

#Programa Principal
def main():
    #Cria uma lista VAZIA.
    lista = []
    #Repete o INPUT.
    for i in range(5):
        #Entrada
        numeros = int(input(f"Digite o {i+1}º número: "))
        #Adiciona os valores da variável na lista vazia.
        lista.append(numeros)
    #Saída    
    print(f'Dentre os números digitados, o maior certamente é {maior(lista)}!')
    print(f'O menor número dentre os digitados sem dúvida é {menor(lista)}!')
    print(f'A média entre esses números é {media(lista)}')
        
if __name__ == '__main__':
    main()
