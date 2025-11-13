#Processamento de dados
def atencao_ao_sinal(s):
    if s == "VERDE":
        return "Está verde! Vamos adiante!"
    elif s == "AMARELO":
        return "Amarelo, vamos aguardar, então."
    elif s == "VERMELHO":
        return "Vermelho. Droga! Anda logo!!"
    else:
        return "Você não prestou atenção ao sinal, atravessou, e foi atropelado por um caminhão."
    
#Programa principal
def main():
    #Entrada
    sinal = input("Preciso atravessar a rua, o sinal está: ").upper()

    #Chamada da função
    o_que_fazer = atencao_ao_sinal(sinal)

    #Saída Condicional
    print(o_que_fazer)
    
if __name__ == '__main__':
    main()
    
