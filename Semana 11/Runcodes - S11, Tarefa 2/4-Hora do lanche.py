#Programa principal
def main():
    #Variável auxiliar que recebe os lanches escolhidos pelo usuário.
    lanche_completo = 0
    
    while True:
        #Cardápio da lanchonete
        print('''CÓDIGO  PRODUTO         PREÇO (R$)
H       Hamburger       5,50
C       Cheeseburger    6,80
M       Misto Quente    4,50
A       Americano       7,00
Q       Queijo Prato    4,00
X       PARA TOTAL DA CONTA''')

        #Lê a escolha de lanche feita pelo usuário
        pedido = input("Qual lanche gostaria, senhor? ").upper()[0]

        #Adiciona o pedido a lista e soma o valor total a ser pago.
        if pedido == "H":
            lanche_completo += 5.50
        elif pedido == "C":
            lanche_completo += 6.80
        elif pedido == "M":
            lanche_completo += 4.50
        elif pedido == "A":
            lanche_completo += 7.00
        elif pedido == "Q":
            lanche_completo += 4.00

        #Encerra o pedido do usuário
        if pedido == 'X':
            break

        #Retorna inválido para qualquer coisa fora das opções do cardápio
        else:
            if pedido not in ["H","C","M","A","Q","X"]:
                print("Opção inválida.")

    #Imprime o valor que deverá ser pago pelo usuário
    print(f'Deu R${lanche_completo:.2f}, senhor! Vai pagar no PIX?')

if __name__ == '__main__':
    main()
        
