#Números que representarão respectivamente ALTURA, COMPRIMENTO e LARGURA
h=int(input("Digite a altura: ").strip())
c=int(input("Digite o comprimento: ").strip())
l=int(input("Digite a largura: ").strip())

#Cálculo da Área do Piso
área_piso = l * c
#Cálculo do Volume da Sala
volume_sala = l * c * h
#Cálculo da Área das Paredes da Sala
área_parede = 2*h * l + 2*h * c

#Imprime o resultado dos cálculos
print(f"A área do piso é {área_piso} m\u00b2.")
print(f"O volume da sala é {volume_sala} m\u00b3.")
print(f"A área da parede é {área_parede} m\u00b2.")
