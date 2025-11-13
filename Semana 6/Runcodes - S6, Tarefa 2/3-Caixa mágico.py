#Processamento de dados
def total_a_pagar(preco1, preco2):
    return 3*preco1 + 2*preco2

#Programa principal
def main():
    #Entrada
    maca = float(input("Qual o preço da maçã? "))
    banana = float(input("Qual o preço da banana? "))
    #Saída
    print(f'Deu R${total_a_pagar(maca, banana):.2f} no total. A forma de pagamento será no crédito ou no débito?')

if __name__ == '__main__':
    main()
