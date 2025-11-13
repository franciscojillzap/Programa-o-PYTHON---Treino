#Processamento de dados
def peso_ideal(tamanho, genero):
    if genero == 1:
        peso_homem = (72.7 * tamanho) - 58
        return f"Como homem, seu peso ideal é: {peso_homem:.2f}"
    elif genero == 2:
        peso_mulher = (62.1 * tamanho) - 44.7
        return f"Como mulher, seu peso ideal é: {peso_mulher:.2f}"

#Programa principal
def main():
    #Entrada
    altura = float(input("Digite sua altura: ").strip())
    sexo = int(input("Gênero[1 - Masculino / 2 - Feminino]: ").strip())
    
    #Saída Condicional
    print(peso_ideal(altura, sexo))

if __name__ == '__main__':
    main()
