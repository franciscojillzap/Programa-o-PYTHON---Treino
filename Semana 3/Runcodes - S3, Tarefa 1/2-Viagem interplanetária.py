#É determinado um número que representará a distância de um planeta em KM
distância=int(input("Capitão! Qual a distância do nosso objetivo? ").strip())

#Escala-se um número que represente a velocidade de uma nave em KM/H
nave=int(input("Quantos KM/H nossa nave é capaz de percorrer? ").strip())

#Tempo que levará para chegar ao destino
tempo=distância//nave

#Converte o tempo em dias de viagem
dias=tempo//24

#O tempo restante em horas
horas=tempo%24

#Mostra o resultado final
print(f"{dias} dias e {horas} horas ainda nos separam de nosso destino!")




