#Processamento de dados
def conversao(t, e):
    pass

#Programa principal
def main():
    dados = []

    for i in range(2):
        temperatura = float(input(f'Digite a {i+1}ª temperatura: '))
        dados.append(temperatura)
        escala = input('A escala é classificada em: ').upper()[0]
        dados.append(escala)

    tupla = tuple(dados)

    print(tupla)

if __name__ == '__main__':
    main()


