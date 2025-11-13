#PROCESSAMENTO de DADOS
def preco_desconto(valor, porcentagem):
    #Retorna o preço com desconto aplicado.
    return valor - (valor * porcentagem / 100)

def preco_acrescimo(valor, porcentagem):
    #Retorna o preço com aumento aplicado.
    return valor + (valor * porcentagem / 100)

#PROGRAMA PRINCIPAL
def main():
    #Entrada
    pr_original = float(input("Digite um preço: "))
    vlr_percentual = float(input("Digite uma porcentagem: "))

    #Saída
    print(f'''
Um produto que custa R${pr_original:.2f} aplicado um aumento de {vlr_percentual}%,
passará a custar R${preco_acrescimo(pr_original, vlr_percentual):.2f}!''')
    print(f'''
Um produto que custa R${pr_original:.2f} aplicado um desconto de {vlr_percentual}%,
passará a custar R${preco_desconto(pr_original, vlr_percentual):.2f}!''')

if __name__ == '__main__':
    main()
