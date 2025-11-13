#Processamento de dados
def determinar_signo(data):
     #Verifica se a data contém o barra "/"
    if "/" not in data:
        return "Digite sua data de nascimento no formato dia/mês, ex: 05/12."
        
        #Indica que o código a seguir pode apresentar erro.
        try:
            # .split() usa "/" como caractere separador para dividir a string em duas partes.
            # map(int ...) pega as strings e aplica a função int, transformando-as em número inteiro.
            # "dia" recebe o primeiro valor, "mes" recebe o segundo valor.
            dia, mes = map(int, data.split("/"))
        #Caso ocorra erro de um determinado tipo, abre-se uma exceção.    
        except ValueError:
            #Para evitar que o programa quebre, retorna uma mensagem ao usuário para concertar alguma ação que tenha levado ao erro.    
            return "Ocorreu um problema. Tente digitar apenas números!"

    #Em caso de erro
    if dia > 31 or mes > 12 or dia < 1 or mes < 1:
        return "Algo de errado, não está certo..."

    #De acordo com a data de nascimento, retorna o signo correspondente
    if (dia >= 21 and mes == 3) or (dia <= 19 and mes == 4):
        return "Áries"
    elif (dia >= 20 and mes == 4) or (dia <= 20 and mes == 5):
        return "Touro"
    elif (dia >= 21 and mes == 5) or (dia <= 21 and mes == 6):
        return "Gêmeos"
    elif (dia >= 22 and mes == 6) or (dia <= 22 and mes == 7):
        return "Câncer"
    elif (dia >= 23 and mes == 7) or (dia <= 22 and mes == 8):
        return "Leão"
    elif (dia >= 23 and mes == 8) or (dia <= 22 and mes == 9):
        return "Virgem"
    elif (dia >= 23 and mes == 9) or (dia <= 22 and mes == 10):
        return "Libra"
    elif (dia >= 23 and mes == 10) or (dia <= 21 and mes == 11):
        return "Escorpião"
    elif (dia >= 22 and mes == 11) or (dia <= 21 and mes == 12):
        return "Sagitário"
    elif (dia >= 22 and mes == 12) or (dia <= 19 and mes == 1):
        return "Capricórnio"
    elif (dia >= 20 and mes == 1) or (dia <= 18 and mes == 2):
        return "Aquário"
    elif (dia >= 19 and mes == 2) or (dia <= 20 and mes == 3):
        return "Peixes"
    

#Programa principal
def main():
    #Entrada
    nascimento = input().strip()

    #Chamada da função
    signo = determinar_signo(nascimento)

    #Saída condicional
    print(signo)

if __name__ == '__main__':
    main()
