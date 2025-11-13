#Cria uma lista vazia
números=[]

#Repete a mensagem de input quantas vezes quiser
for i in range(3):
    variáveis=int(input(f"Digite o {i+1}º número: ").strip())
    #Armazena as variáveis dentro da lista vazia
    números.append(variáveis)

#SUM soma e LEN conta quantas variáveis estão dentro da lista.
média=sum(números)/len(números)

#Imprime o resultado da média entre as variáveis
print(f"A média entre os valores é: {média:.2f}.")
