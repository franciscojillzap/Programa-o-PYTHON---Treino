#Processamento de dados
def menino_ou_menina(genero, identidade):
    if genero == 1:
        return f"Ilmo Sr. {identidade}"
    elif genero == 2:
        return f"Ilma Sra. {identidade}"
    else:
        return f"Sr. {identidade} Geladeira Eletrolux"

#Programa principal
def main():
    #Entrada
    nome = input("Digite seu nome: ")
    sexo = int(input("Sexo (Digite 1 para Masculino, 2 para Feminino): "))

    #Chamada da função
    hora_da_verdade = menino_ou_menina(sexo, nome)

    #Saída Condicional
    print(hora_da_verdade)

    
if __name__ == '__main__':
    main()


    
    
