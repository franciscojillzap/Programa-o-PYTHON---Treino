print("Essa loja é ótima! Tem os produtos da melhor qualidade!")

#Determina o preço de um produto
preço=float(input("Veja só isso! Justamente o que precisava! Qual é o preço? ").strip())

#O preço sofre 10% de desconto, aqui se descobre esse desconto em reais
desconto=preço*0.10

#Aplica-se o desconto no valor original
preço_final=preço-desconto

#Revela o preço com desconto aplicado
print(f"Graças a um desconto de 10%, paguei apenas R${preço_final:.2f}!")
