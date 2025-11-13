#Processamento de dados
def por_extenso(digito):
    #Separar número em UNIDADE, DEZENA & CENTENA
    uni = digito % 10
    dez = (digito // 10) % 10
    cen = (digito // 100) % 10

    #Garantir PLURAL & SINGULAR
    cen_PS = "centena" if cen == 1 else "centenas"
    dez_PS = "dezena" if dez == 1 else "dezenas"
    uni_PS = "unidade" if uni == 1 else "unidades"

    #Formatar por EXTENSO
    cen_str = "Uma" if cen == 1 else "Duas" if cen == 2 else "Três" if cen == 3 else "Quatro" if cen == 4 else "Cinco" if cen == 5 else "Seis" if cen == 6 else "Sete" if cen == 7 else "Oito" if cen == 8 else "Nove"
    dez_str = "uma" if dez == 1 else "duas" if dez == 2 else "três" if dez == 3 else "quatro" if dez == 4 else "cinco" if dez == 5 else "seis" if dez == 6 else "sete" if dez == 7 else "oito" if dez == 8 else "nove"
    uni_str = "uma" if uni == 1 else "duas" if uni == 2 else "três" if uni == 3 else "quatro" if uni == 4 else "cinco" if uni == 5 else "seis" if uni == 6 else "sete" if uni == 7 else "oito" if uni == 8 else "nove"

    #Entrega condicional
    if dez == 0 and uni == 0:
        return f"{cen_str} {cen_PS}."
    if cen == 0 and uni == 0:
        return f"{dez_str} {dez_PS}."
    if cen == 0 and dez == 0:
        return f"{uni_str} {uni_PS}."
    elif cen == 0:
        return f"{dez_str} {dez_PS} e {uni_str} {uni_PS}."
    elif dez == 0:
        return f"{cen_str} {cen_PS} e {uni_str} {uni_PS}."
    elif uni == 0:
        return f"{cen_str} {cen_PS} e {dez_str} {dez_PS}."
    else:
        return f"{cen_str} {cen_PS}, {dez_str} {dez_PS} e {uni_str} {uni_PS}."
            
#Programa principal
def main():
    #Entrada
    numero = int(input("Digite um número inteiro de até 3 algarismos: ").strip())

    #Saída
    print(por_extenso(numero))

if __name__ == '__main__':
    main()
