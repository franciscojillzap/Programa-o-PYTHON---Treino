#Cria uma lista vazia para receber as notas
trimestre=[]
#Cria uma lista com o peso de cada nota
pesos=[2,3,5]

#Variável com valor inicial zerado
soma_ponderada = 0
#Realiza a soma dos pesos
soma_pesos = sum(pesos)

#Através da leitura do total de pesos, repete o input esse número de vezes
for i in range(len(pesos)):
    notas=float(input(f"Digite a {i+1}ª nota: ").strip())
    #Adiciona as notas na lista vazia
    trimestre.append(notas)
    #Atribui-se o resultado da soma dos produtos entre as notas e pesos a variavel vazia
    soma_ponderada += notas * pesos[i]

#Realiza o cálculo da média ponderada
media_ponderada = soma_ponderada / soma_pesos

#Imprime o resultado final
print(f"A média dessas notas é: {media_ponderada}!")
    
