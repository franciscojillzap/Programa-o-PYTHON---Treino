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

def cidades_aniversariantes(D, M):
    DIA = D
    MES = nome_dos_meses(M).upper()
    lista_aniversario = []
    
    print(f'\nCIDADES QUE FAZEM ANIVERSÁRIO EM {DIA} DE {MES}:')

    for uf, ibge, nome, dia, mes, pop in carrega_cidades():
        if dia == D and mes == M:
            lista_aniversario.append(f'{nome}({uf})')

    return lista_aniversario
    
def main():
    data = input('Digite uma data (formato - DD/MM): ')

    #Divide a data em duas partes utilizando '/' como ponto de referência
    dia, mes = map(int, data.split('/'))
    
    for cidades in cidades_aniversariantes(dia, mes):
        print(cidades)

if __name__ == '__main__':
    main()
                
