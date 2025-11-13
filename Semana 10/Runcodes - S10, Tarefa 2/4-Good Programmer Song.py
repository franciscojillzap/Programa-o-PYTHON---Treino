#Programa principal
def main():
    #Saída
    # 99 - início da sequência (START) / 250 - fim da sequência (STOP)
    for i in range(99, 0, -11):
        print(f'{i} bugs no software, pegue onze deles e conserte...\nTecle "Ctrl+F5"')

    print("Sem erros no software! Está estabilizado!")

if __name__ == '__main__':
    main()
