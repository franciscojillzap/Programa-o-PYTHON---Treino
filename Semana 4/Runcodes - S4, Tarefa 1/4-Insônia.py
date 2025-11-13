#Determina valores para HORAS, MINUTOS e SEGUNDOS
hora=int(input("Que horas são agora? ").strip())
minutos=int(input("Quantos minutos? ").strip())
segundos=int(input("E segundo? ").strip())

#Transforma HORAS em SEGUNDOS (1 hora = 3600 segundos)
hr_em_seg = hora * 3600
#Converte MINUTOS em SEGUNDOS (1 minuto = 60 segundos
min_em_seg = minutos * 60
#Realiza a soma para descobrir o total de segundos
soma_final= hr_em_seg + min_em_seg + segundos

#Revela os segundos passados desde a meia-noite
print(f"Desde a meia-noite, já se passaram {soma_final} segundos!")
print("Acho melhor ir dormir...")


