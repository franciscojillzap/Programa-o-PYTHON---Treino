#Processamento de dados
def fahrenheit(c):
    return (c * (9/5)) + 32

#Programa principal
def main():
    #Entrada
    celcius = float(input("Que friaca dos infernos! Qual a temperatura atual em graus celcius? "))
    #Saída
    print(f'Isso equivale a {fahrenheit(celcius):.2f}° em graus fahrenheit...Não que isso resolva esse frio.')

if __name__ == '__main__':
    main()
