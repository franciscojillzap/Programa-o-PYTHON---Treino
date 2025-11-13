#Processamento de dados
def analise(variavel):
    #A função SET armazena dentro de um lista apenas números únicos, sem repetições.
    analise = set(variavel)
    #Se ao percorrer a lista, ela contiver apenas DOIS números, significa que dos três números digitados, um é REPETIDO.
    if len(analise) == 2:
        return "Existem dois valores iguais e um diferente"
    #Se ao percorrer a lista, ela contiver apenas UM número, significa que os três números digitados são IGUAIS.
    elif len(analise) == 1:
        return "Todos os valores são iguais"
    else:
        #Se ao percorrer a lista, ela contiver TRÊS números, significa que os três números digitados são DIFERENTES.
        if len(analise) == 3:
            return "Todos os valores são diferentes"

#Programa principal
def main():
    #Lista VAZIA
    numeros = []

    #Entrada
    for i in range(3):
        n = int(input(f"Digite o {i+1}º número: ").strip())
        numeros.append(n)

    #Saída condicional
    print(analise(numeros))

if __name__ == '__main__':
    main()
