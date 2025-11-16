#Processamento de dados
def fibonacci(termos):
    t_anterior = 0
    t_sucessor = 1
    contador = 0
    #Lista para receber a sequência de fibonacci
    sequencia = []

    #Realiza a repetição enquanto o contador não atingir o valor dos n termos
    while contador < termos:
        #Adiciona os termos a lista
        sequencia.append(t_anterior)
        
        #Decide o termo seguinte somando o anterior e o sucessor
        t_seguinte = t_anterior + t_sucessor
        
        #Substitui o termo anterior pelo sucessor
        t_anterior = t_sucessor
        
        #Substitui o termo sucessor pelo seguinte
        t_sucessor = t_seguinte
        
        #Faz a contagem do número de termos
        contador += 1
        
    return ', '.join(str(x) for x in sequencia)

#Programa principal
def main():
    #Entrada -
    #Determina o número de termos a serem exibidos da sequência fibonacci
    n_termos = int(input("Digite o nº de termos da sequência fibonacci que deseja ver: "))

    #Imprime uma lista com os termos de fibonacci
    print(fibonacci(n_termos))

if __name__ == '__main__':
    main()
