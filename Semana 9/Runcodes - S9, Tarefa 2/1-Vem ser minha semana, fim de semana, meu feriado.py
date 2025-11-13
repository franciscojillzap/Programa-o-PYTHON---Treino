#Processamento de dados
def definir_dia_da_semana(digito):

    if digito == "1":
        return "Domingo"
    elif digito == "2":
        return "Segunda-feira"
    elif digito == "3":
        return "Terça-feira"
    elif digito == "4":
        return "Quarta-feira"
    elif digito == "5":
        return "Quinta-feira"
    elif digito == "6":
        return "Sexta-feira"
    elif digito == "7":
        return "Sábado"
    else:
        return "Valor inválido"

#Programa principal
def main():
    #Entrada
    dia = input("Digite um número que corresponda a um dia da semana: ").strip()

    #Saída
    print(definir_dia_da_semana(dia))

if __name__ == '__main__':
    main()
