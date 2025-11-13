#Processamento de dados
def determinar_signo(D, M):
    #Em caso de erro:

    #Se o MÊS não for número -
    if not str(M).isdigit():
        return "Digite o número correspondente ao mês de seu nascimento"
    else:
        M = int(M)

    #Se o DIA for maior que 31 e mês maior que 12, ou ambos forem menores que 1 -
    if D > 31 or M > 12 or D < 1 or M < 1:
        return "Algo de errado, não está certo...Tem certeza que digitou os dias e os meses corretamente?"
        

    #De acordo com a data de nascimento, retorna o signo correspondente
    if (D >= 21 and M == 3) or (D <= 19 and M == 4):
        return "Seu signo é Áries. EXTINÇÃO ESTELAR!!!"
    elif (D >= 20 and M == 4) or (D <= 20 and M == 5):
        return "Seu signo é Touro. GRANDE CHIFRE!!!"
    elif (D >= 21 and M == 5) or (D <= 21 and M == 6):
        return "Seu signo é Gêmeos. EXPLOSÃO GALÁTICA!!!"
    elif (D >= 22 and M == 6) or (D <= 22 and M == 7):
        return "Seu signo é Câncer. ONDAS DO INFERNO!!!"
    elif (D >= 23 and M == 7) or (D <= 22 and M == 8):
        return "Seu signo é Leão. RELÂMPAGO DE PLASMA!!!"
    elif (D >= 23 and M == 8) or (D <= 22 and M == 9):
        return "Seu signo é Virgem. TESOURO DO CÉU!!!"
    elif (D >= 23 and M == 9) or (D <= 22 and M == 10):
        return "Seu signo é Libra. CÓLERA DOS CEM DRAGÕES!!!"
    elif (D >= 23 and M == 10) or (D <= 21 and M == 11):
        return "Seu signo é Escorpião. AGULHA ESCARLATE!!!"
    elif (D >= 22 and M == 11) or (D <= 21 and M == 12):
        return "Seu signo é Sagitário. METEORO DE PÉGASO!!!"
    elif (D >= 22 and M == 12) or (D <= 19 and M == 1):
        return "Seu signo é Capricórnio. EXCALIBUR!!!"
    elif (D >= 20 and M == 1) or (D <= 18 and M == 2):
        return "Seu signo é Aquário. EXECUÇÃO AURORA!!!"
    elif (D >= 19 and M == 2) or (D <= 20 and M == 3):
        return "Seu signo é Peixes. ROSAS DIABÓLICAS REAIS!!!"
    

#Programa principal
def main():
    #Entrada
    dia = int(input("Digite o dia de seu nascimento: ").strip())
    mes = input("Digite o mês de seu nascimento: ").strip()
        
    #Chamada da função
    signo = determinar_signo(dia, mes)

    #Saída condicional
    print(signo)

if __name__ == '__main__':
    main()
