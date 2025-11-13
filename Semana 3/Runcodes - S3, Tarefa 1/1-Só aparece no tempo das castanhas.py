#Determina o número de fatias de pizza
fatias=int(input("Pizza? Maravilha! Em quantas fatias ela foi dividida? ").strip())

#Determina o número de pessoas que dividirá a pizza
amigos=int(input("Amigos? Nessa hora todo mundo aparece...Quantos vieram? ").strip())

#Divisão para descobrir quantas fatias de pizza cada amigo vai receber.
divisão=fatias//amigos

#Diz o número de pizzas restantes depois da divisão
resto=fatias%amigos

#Mostra os resultados
print(f"Cada amigo vai receber {divisão} pedaço(s) de pizza...")
print(f"E vai sobrar {resto} fatia(s)!")
