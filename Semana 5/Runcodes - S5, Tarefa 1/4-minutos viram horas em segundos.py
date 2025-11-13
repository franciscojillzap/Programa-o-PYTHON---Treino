#PROCESSAMENTO de DADOS
def conversao_minutos(total_minutos):
    #Converte para HORAS e MINUTOS
    hours = total_minutos // 60
    minutes = total_minutos % 60
    return f"{hours}h:{minutes}min"

#PROGRAMA PRINCIPAL
def main():
    #Entrada
    minutos = int(input("Digite um total de minutos: "))

    #Saída
    print(f'Estes minutos equivalem à {conversao_minutos(minutos)}')

if __name__ == '__main__':
    main()
