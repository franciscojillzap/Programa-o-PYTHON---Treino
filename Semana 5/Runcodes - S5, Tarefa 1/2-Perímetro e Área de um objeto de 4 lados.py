#PROCESSAMENTO de DADOS
def area(valor_lado):
    #Retorna o valor correspondente a ÁREA do quadrado.
    return valor_lado ** 2

def perimetro(valor_lado):
    #Retorna o valor correspondente ao PERÍMETRO do quadrado.
    return valor_lado * 4

#PROGRAMA PRINCIPAL
def main():
    #Entrada
    lado = float(input("Digite o valor do lado de um quadrado: "))
    #Saída
    print(f'A área deste quadrado é:{area(lado):10.4f}')
    print(f'O perímetro deste quadrado é:{perimetro(lado):10.4f}')

if __name__ == '__main__':
    main()
