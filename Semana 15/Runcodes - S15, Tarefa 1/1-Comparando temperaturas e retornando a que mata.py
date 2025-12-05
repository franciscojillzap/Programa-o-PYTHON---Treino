#Processamento de dados
def fahrenheit_em_celcius(t):
    return (t - 32) * (5/9)

def celcius_em_fahrenheit(t):
    return (t * (9/5)) + 32

def maior_temperatura(t):
    #TEMPERATURAS
    temp1 = t[0]
    temp2 = t[2]

    #ESCALAS
    esc1 = t[1]
    esc2 = t[3]

    #Quando as escalas são IGUAIS
    if esc1 == esc2:
        if temp1 > temp2:
            return t[ : 2]
        else:
            return t[2 : 4]

    #Quando as escalas são DIFERENTES
    elif esc1 != esc2:
        if esc1 == 'C':
            #Converte a segunda temperatura para CELCIUS
            temp2_cel = fahrenheit_em_celcius(temp2)
            if temp1 > temp2_cel:
                return t[ : 2]
            else:
                return t[2 : 4]

        elif esc1 == 'F':
            #Converte a segunda temperatura para FAHRENHEIT
            temp2_fah = celcius_em_fahrenheit(temp2)
            if temp1 > temp2_fah:
                return t[ : 2]
            else:
                return t[2 : 4]

#Programa principal
def main():
    lista = []

    for i in range(2):
        temperatura = float(input(f'\nDigite a {i+1}ª temperatura: '))
        lista.append(temperatura)

        escala = input('A escala correspondente é: ').upper()[0]
        lista.append(escala)

    tupla = tuple(lista)

    print(f'\n{tupla}')
    print(maior_temperatura(tupla))

if __name__ == '__main__':
    main()
                            
