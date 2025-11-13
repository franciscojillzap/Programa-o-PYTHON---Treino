#Processamento de Dados
def data_mais_recente(primeira, segunda):
    #Divindo a data em DIA / MÊS / ANO
    d1, m1, a1 = map(int, primeira.split("/"))
    d2, m2, a2 = map(int, segunda.split("/"))

    #Análise da data mais recente
    if (d1, m1, a1) > (d2, m2, a2):
        return f"\nA data {d1:02d}/{m1:02d}/{a1} é mais recente!"
    elif (d1, m1, a1) < (d2, m2, a2):
        return f"\nA data {d2:02d}/{m2:02d}/{a2} é mais recente!"
    else:
        return "\nAs duas datas são iguais!"

#Programa Principal
def main():
    #Entrada - 1ª Data
    data_1 = input("Digite a primeira data (formato: DD/MM/AAAA): ").strip()
    
    #Entrada - 2ª Data
    data_2 = input("Digite a segunda data (formato: DD/MM/AAAA): ").strip()
    
    #Chamada da função
    data_recente = data_mais_recente(data_1, data_2)

    #Saída Condicional
    print(data_recente)

if __name__ == '__main__':
    main()
