#Processamento de dados
def anos_espaciais(anos):
    return int(anos*0.5)

#Programa principal
def main():
    #Entrada
    anos_terrestres = int(input("Informe sua idade, terráqueo: "))
    #Saída
    print(f"De acordo com Zob, você tem {anos_espaciais(anos_terrestres)} anos em anos espaciais.")

if __name__ == '__main__':
    main()
