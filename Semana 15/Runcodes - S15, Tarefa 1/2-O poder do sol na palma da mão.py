#Processamento de dados
def fahrenheit_em_celcius(t):
    return (t - 32) * (5/9)

def celcius_em_fahrenheit(t):
    return (t * (9/5)) + 32

def temperatura_maxima(t):
    #TEMPERATURAS
    temp1 = t[0]
    temp2 = t[2]

    #ESCALAS
    esc1 = t[1]
    esc2 = t[3]

    #Quando as escalas são IGUAIS
    if esc1 == esc2:
        total_temp = temp1 + temp2
        return total_temp, esc1
    
    #Quando as escalas são DIFERENTES
    elif esc1 != esc2:
        if esc2 == 'C':
            #Converte a primeira temperatura para CELCIUS
            temp1_cel = fahrenheit_em_celcius(temp1)

            total_temp = temp1_cel + temp2
            return f'{total_temp:.4f}', esc2

        elif esc2 == 'F':
            #Converte a primeira temperatura para FAHRENHEIT
            temp1_fah = celcius_em_fahrenheit(temp1)
            
            total_temp = temp1_fah + temp2
            return f'{total_temp:.4f}', esc2

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
    print(temperatura_maxima(tupla))

if __name__ == '__main__':
    main()
                            
