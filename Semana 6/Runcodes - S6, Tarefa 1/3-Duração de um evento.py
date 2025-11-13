#Processamento de Dados
def conversao(total_seg):
    horas = total_seg // 3600
    resto = total_seg % 3600
    minutos = resto // 60
    segundos = resto % 60
    return f'{horas} horas, {minutos} minutos e {segundos} segundos'

#Programa Principal
def main():
    #Entrada
    seg = int(input("O tempo de duração de um evento em segundos é: "))
    #Saída
    print(f'Esse evento durará exatamente {conversao(seg)}.')

if __name__ == '__main__':
    main()
    
    
