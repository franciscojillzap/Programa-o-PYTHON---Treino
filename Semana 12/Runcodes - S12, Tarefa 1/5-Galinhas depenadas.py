#Processamento de dados
def levantamento_passaro_dodo(p_inicial):
    #A amostra correspondente a população que resta a cada ano.
    p_restante = p_inicial

    #Ano que inicia o processo de extinção
    anos = 1599

    #Continua a repetição enquanto a população restante
    #é maior que 10% da população inicial
    while p_restante >= p_inicial * 10/100:
        nascidos = p_restante * 1/100
        mortos = p_restante * 6/100
        p_restante -= mortos - nascidos
        anos += 1

        #Retorna um valor arredondado ao resultado com round
        print(f'{anos},{round(nascidos)},{round(mortos)},{round(p_restante)}')
    

#Programa principal
def main():
    #Entrada - População inicial dos pobres Dodôs
    p_inicial = int(input())

    #Chamada da função
    perdas = levantamento_passaro_dodo(p_inicial)

    #Imprime o ANO, nº de MORTOS, NASCIDOS e POPULAÇÃO SOBREVIVENTE
    perdas

if __name__ == '__main__':
    main()
