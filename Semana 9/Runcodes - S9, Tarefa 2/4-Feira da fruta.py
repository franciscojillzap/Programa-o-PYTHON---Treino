#Processamento de dados
def total_a_pagar(fruta1, fruta2):
    #Valor a pagar por cada fruta
    pagar_f1 = fruta1 * 2.50 if fruta1 <= 5 else fruta1 * 2.20
    pagar_f2 = fruta2 * 1.80 if fruta2 <= 5 else fruta2 * 1.50
    #Total da compra
    total = pagar_f1 + pagar_f2
    desconto = total - (total * 10/100)

    if (total > 25) or (fruta1 + fruta2 > 8):
        return f"{desconto:.2f}"
    else:
        return f"{total:.2f}"

#Programa principal
def main():
    #Entrada
    morango_kg = float(input().strip())
    maca_kg = float(input().strip())

    #Chamada da função
    pagamento = total_a_pagar(morango_kg, maca_kg)

    #Saída condicional
    print(pagamento)

if __name__ == '__main__':
    main()
