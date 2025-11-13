#Processamento de dados
def qual_maior(digitos):
    return max(digitos)
        
#Programa principal
def main():
    #Lista VAZIA
    lista = []

    #Entrada
    for i in range(100):
        numeros = int(input(f"Digite o {i+1}º número: ").strip())
        lista.append(numeros)

    #Saída
    print(f"Apresento-lhe o maior número dos 100 digitados: {qual_maior(lista)}!")

if __name__ == '__main__':
    main()
