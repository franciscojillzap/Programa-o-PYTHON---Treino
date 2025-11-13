#Diz-se aqui a quantidade de doces fabricados pela doceria
doces=int(input("Digite o número de doces fabricados: ").strip())

#Afirma-se o número de pacotes disponíveis para armazenar esses doces
pacotes=int(input("Quantos pacotes estão disponíveis para receber esses doces? ").strip())

#Dividi-se igualmente os doces entre os pacotes
unidade=doces//pacotes

#Mostra o resultado final com o total de doces por pacote
print(f"Há {unidade} doces em cada pacote")
