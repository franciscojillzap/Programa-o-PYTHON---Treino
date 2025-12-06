def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:

        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            resultado.append((uf, int(ibge), nome, int(dia), int(mes), int(pop)))

    return resultado

def nome_dos_meses(M):
    meses = ['', 'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
             'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

    return meses[M]

def cidades_aniversarigrandes(M, POP):
    MES = nome_dos_meses(M).upper()
    lista_meganiver = []
    
    print(f'\nCIDADES COM MAIS DE {POP} HABITANTES E ANIVERSÁRIO EM {MES}:\n')

    for uf, ibge, nome, dia, mes, pop in carrega_cidades():
        if mes == M and pop > POP:
            lista_meganiver.append((f'{nome}({uf})', pop, dia, mes))

    return lista_meganiver
    
def main():
    mesversario = int(input('Digite um valor referente a um MÊS: '))
    populacao = int(input('Valor populacional de comparação: '))
    
    for cidade, teto_pop, dia, mes in cidades_aniversarigrandes(mesversario, populacao):
        print(f'{cidade} tem {teto_pop} habitantes e faz aniversário em {dia} de {nome_dos_meses(mes)}.')

if __name__ == '__main__':
    main()
                
