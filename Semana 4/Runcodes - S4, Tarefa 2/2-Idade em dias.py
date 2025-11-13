#Determina valores para DIAS, MESES e ANOS, que representam a idade de uma pessoa
anos=int(input("Digite um número de anos: ").strip())
meses=int(input("Agora confirme os meses: ").strip())
dias=int(input("Por fim, os dias: ").strip())

#Conversão para DIAS
anos_em_dias = anos*365
meses_em_dias = meses*30
soma_final = anos_em_dias + meses_em_dias + dias

#Imprime o resultado em DIAS
print(f"Você já viveu {soma_final} dias até agora! Continue assim!")
