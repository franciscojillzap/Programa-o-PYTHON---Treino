#Processamento de dados
def alcance_a_tartaruga(avante_T):
    #Distância percorrida pela lebre em METROS
    avante_L = 0

    #A velocidade dos dois animais medida em METROS/MINUTOS
    velocidade_T = 1
    velocidade_L = 10

    #Contagem de tempo até que a lebre alcance a tartaruga
    minutos = 0

    #Repetição com teste no início
    while avante_L < avante_T:
        avante_T += velocidade_T
        avante_L += velocidade_L
        minutos += 1

    return minutos
        
#Programa principal
def main():
    #Entrada - Distância percorrida pela tartaruga em METROS
    avante_T = int(input("A Tartaruga aproveita e avança um total de metros igual a: "))

    #Chamada da função
    chegada = alcance_a_tartaruga(avante_T)
    
    #Imprime o tempo levado pela lebre até alcançar a tartaruga
    print(f"A lebre levará {chegada} minutos, para chegar a tartaruga. Apresse-se!")

if __name__ == '__main__':
    main()
