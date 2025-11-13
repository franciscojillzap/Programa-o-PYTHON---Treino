#Processamento de dados
def compromisso(name, estado):
    if estado == 1:
        conjuge = input("Nome do cônjuge: ").strip()
        dupla = len(conjuge) + len(name)
        return f"Seus nomes tem juntos {dupla} letras. Cuidado com o chifre!"
    elif estado == 2:
         solo = len(name)
         return f"Seu nome tem {solo} letras. Cadê as namoradinhas?"

#Programa principal
def main():
    #Entrada
    nome = input("Seu nome: ").strip()
    estado_civil = int(input("Estado civil (Digite 1 para Casado, 2 para Solteiro): ").strip())

    #Saída Condicional
    print(compromisso(nome, estado_civil))

if __name__ == '__main__':
    main()
