#Processamento de dados
def media_ajustada(prova):
    media = sum(prova) / len(prova)
    if prova[2] > 8:
        media += 1
    if media > 10:
        media = 10
    return media

#Programa principal
def main():
    #Lista VAZIA
    trimestre = []
    #Entrada
    for i in range(3):
        notas = float(input(f"Digite a {i+1}ª nota: "))
        trimestre.append(notas)
    #Saída
    print(f"A média do aluno é {media_ajustada(trimestre):.2f}.")

if __name__ == '__main__':
    main()
        
    
