#Processamento de dados
def data_da_morte(sal, div):
    #Mês e ano em que foi adquirido a dívida, e de onde deve ser começado a contar.
    mes = 10
    ano = 2016

    #Repete as instruções indeterminadamente, até que atenda-se uma condição
    while True:
        #Acrescenta mais um mês
        mes += 1

        #Se 12º mês é atingido, retorna ao 1º mês e passa-se 1 ano
        if mes > 12:
            mes = 1
            ano += 1

        #Calcula-se o valor crescente da dívida, que aumenta 15% a cada mês
        div += (div * 15 / 100)

        #O salário de paulo terá um aumento de 5% apenas quando for atingido o 3º mês do ano
        if mes == 3:
            sal += (sal * 5 / 100)

        #O programa sai da repetição quando a dívida superar o salário            
        if div > sal: break

    #Retorna MÊS e ANO desse acontecimento
    return f'{mes}/{ano}' 
#Programa principal
def main():
    #Valor do salário de Paulo
    salario = float(input("Qual o salário de Paulo? "))

    #Valor da dívida que ele adquiriu
    divida = float(input("Qual o valor de sua dívida? "))

    #Chamada da função
    dia_D = data_da_morte(salario, divida)

    print(f"A dívida atingirá um valor superior ao salário do pobre infeliz quando atingir {dia_D}")

    #{sal:.2f}, {div:.2f},
  
if __name__ == '__main__':
    main()