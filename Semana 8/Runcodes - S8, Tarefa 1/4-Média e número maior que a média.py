#Processamento de dados
def media(numeros):
    media = sum(numeros)/len(numeros)
    maior_que_media = [n for n in numeros if n > media]
    return media, maior_que_media

def main():
    #Lista vazia
    lista = []

    #Entrada
    for i in range(5):
        numero = int(input(f"Digite o {i+1}º número: ").strip())
        #Adicionar variável a LISTA
        lista.append(numero)

    #Chamada da função
    valor_media, supera_media = media(lista)

    #Saída
    print(f"\nA média entre os números é: {valor_media:.2f}")
    print("\nDentre os valores digitados, os que superam a média são: ")
    for n in supera_media:
        print(f"{n:.2f}")

if __name__ == '__main__':
    main()
