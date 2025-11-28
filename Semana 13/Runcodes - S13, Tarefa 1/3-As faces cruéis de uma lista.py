#Processamento de dados
def lista_inversa(n):
    lista = []

    for i in range(n):
        numeros = float(input(f'Digite o {i+1}º número: '))
        lista.append(numeros)

    lista.reverse()

    return lista

def lista_notas(n):
    lista = []

    for i in range(n):
        notas = float(input(f'Digite a {i+1}ª nota: '))
        lista.append(notas)
    
    if n > 0: return lista, sum(lista) / len(lista)
    else: return [], None

def quantas_vogais(n):
    lista = []

    vogais = 'aeiou'
    consoantes = 'bcdfghjklmnpqrstvwxyz'

    total_vogais = 0
    lista_consoantes = []
    
    for i in range(n):
        letras = input(f'Digite a {i+1}ª letra: ')[0]
        lista.append(letras)

    for letra in lista:
        if letra.lower() in vogais: total_vogais += 1
        if letra.lower() in consoantes: lista_consoantes.append(letra)

    return total_vogais, lista_consoantes
        
#Programa principal
def main():
    itens = int(input('Quantos itens a lista possuirá? '))

    inversa_lista = lista_inversa(itens)
    notas, media = lista_notas(itens)
    vogais, consoantes = quantas_vogais(itens)

    print(inversa_lista)
    print(notas)
    if media is None: print('SEM NOTAS')
    else: print(f'{media:.1f}')
    print(vogais)
    print(consoantes)
    
if __name__ == '__main__':
    main()
