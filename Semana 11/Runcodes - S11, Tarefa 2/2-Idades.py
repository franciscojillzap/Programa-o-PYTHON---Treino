#Processamento de dados
def total_pessoas(lista):
    
    return len(lista)

def media_idade(lista):
    media = sum(lista) / len(lista)

    return f'{media:.2f}'

def maior_menor(lista) :
    maior = max(lista)
    menor = min(lista)

    return maior, menor

#Programa principal
def main():
    lista_idade = []

    while True:
        idades = int(input("Digite uma idade: "))

        if idades == 0: break

        lista_idade.append(idades)
    
    v_max, v_min = maior_menor(lista_idade)

    print("Número de pessoas:", total_pessoas(lista_idade))
    print("Média entre as idades:", media_idade(lista_idade))
    print("Maior idade:", v_min)
    print("Menor idade:", v_max)

if __name__ == '__main__':
    main()
    



