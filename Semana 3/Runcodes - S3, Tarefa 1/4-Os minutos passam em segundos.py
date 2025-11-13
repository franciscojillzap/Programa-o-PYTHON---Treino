#Insere-se um valor para segundos
segundos=int(input("Digite um total de segundos: ").strip())

#Transforma segundos em minutos
minutos=segundos//60

#Os segundos restantes
resto=segundos%60

#Mostra os segundos convertidos em minutos
print(f"Estes segundos equivalem a {minutos} minutos e {resto} segundos!")
