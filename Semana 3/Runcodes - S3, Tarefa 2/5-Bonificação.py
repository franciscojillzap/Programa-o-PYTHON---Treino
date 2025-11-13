#São digitados valores correspondentes ao tempo de serviço e o bônus anual ganho por um trabalhador
tempo_serviço=float(input("Insira o tempo de serviço: ").strip())
bônus_anual=float(input("Insira o valor do bônus anual: ").strip())

#Esses valores são multiplicados para gerar uma bonificação
bonificação=tempo_serviço*bônus_anual

#O que este trabalhador receberá em dinheiro
print(f"Você tem direito a R${bonificação:.2f}")
