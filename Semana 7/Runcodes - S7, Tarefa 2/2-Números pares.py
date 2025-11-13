#Processamento de dados
def quantos_pares(digitos):        
    #Divide o número em partes.
    centena = dezena = unidade = 0
    #Caso o número tenha 3 algarismos
    if len(str(digitos)) == 3:
        centena = digitos // 100
        dezena = (digitos // 10) % 10
        unidade = digitos % 10
    #Caso o número tenha 2 algarismos
    elif len(str(digitos)) == 2:
        dezena = digitos // 10
        unidade = digitos % 10
    #Se só houver um algarismo
    else:
        unidade = digitos
    
    score = 0

    #Distribuição de pontos
    if centena % 2 == 0 and len(str(digitos)) == 3:
        score += 1
    if dezena % 2 == 0 and len(str(digitos)) >= 2:
        score += 1
    if unidade % 2 == 0:
        score += 1
    
    #Retorna o total de dígitos pares
    return score

#Programa principal
def main():
    #Entrada
    numero = int(input("Digite um número de 0 à 999: ").strip())

    #Chamada da função
    total = quantos_pares(numero)

    #Saída condicional
    print(f"O número {numero} tem {total} dígito(s) pares.")

if __name__ == '__main__':
    main()
    
