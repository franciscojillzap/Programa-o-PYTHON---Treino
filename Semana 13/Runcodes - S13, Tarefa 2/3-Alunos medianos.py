#Processamento de dados
def alunos_medianos(L):
    lista_alunos = []

    #ENUMERATE() - captura o iterável(nota) e seu índice(i)
    for i, nota in enumerate(L):
        if nota >= 6: lista_alunos.append(i)
        
    return lista_alunos

#Programa principal
def main():
    lista = []

    for i in range(5):
        notas = float(input(f'Digite a {i+1}º nota: '))
        lista.append(notas)

    print('Eis os alunos que atingiram uma nota média:', alunos_medianos(lista))

if __name__ == '__main__':
    main()
