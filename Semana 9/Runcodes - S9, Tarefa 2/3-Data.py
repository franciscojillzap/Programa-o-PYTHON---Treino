#Processamento de dados
def data_valida(tempo):
    #Dividir data em DIA, MÊS & ANO
    dia = int(tempo[:2])
    mes = int(tempo[2:4])
    ano = int(tempo[4:])

    #Verifica se um ano é BISSEXTO
    bissexto = (ano % 4 == 0) or (ano % 400 == 0)

    #Define o número de dias em um mês
    dia_mes = 31 if mes in [1, 3, 5, 7, 8, 10, 12] else 30 if mes in [4, 6, 9, 11] else 29 if bissexto else 28

    #Verifica se a data é VÁLIDA
    if (dia <= dia_mes) and (mes <= 12) and (ano >= 1):
        return "Data válida"
    else:
        return "Data inválida"

#Programa principal
def main():
    #Entrada
    data = input("Digite uma data (formato - DDMMAAAA): ").strip()

    #Saída
    print(data_valida(data))

if __name__ == '__main__':
    main()
    
