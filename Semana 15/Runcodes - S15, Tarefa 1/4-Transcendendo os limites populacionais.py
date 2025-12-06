def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:

        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            resultado.append((uf, int(ibge), nome, int(dia), int(mes), int(pop)))

    return resultado

def cidades_metropolitanas(limite):
    lista_megalopes = []
    
    print(f'CIDADES COM MAIS DE {limite} HABITANTES:')

    for uf, ibge, nome, dia, mes, pop in carrega_cidades():
        if pop > limite:
            lista_megalopes.append((ibge, f'{nome}({uf})', pop))           

    return lista_megalopes
    
def main():
    populacao = int(input('Digite um valor referente ao total populacional de uma cidade: '))
    
    for codigo, cidade, teto_pop in cidades_metropolitanas(populacao):
        print(f'IBGE: {codigo} - {cidade} - POPULAÇÃO: {teto_pop}')

if __name__ == '__main__':
    main()
                
