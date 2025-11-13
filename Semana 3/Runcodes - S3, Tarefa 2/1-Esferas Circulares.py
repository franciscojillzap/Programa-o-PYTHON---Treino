#Valor de PI
PI=float(3.141592)

#Valor para RAIO
r=float(input("Digite um valor para raio: ").strip())

#Círculo
circunferência=2*PI*r
área_c=PI*r**2

#Esfera
volume=4/3*PI*r**3
área_e=4*PI*r**2

#Imprime os resultados do Comprimento da Circunferência e Área do Círculo
print(f"O comprimento da circunferência é:{circunferência:.6f}")
print(f"A área do círculo é igual a: {área_c:.6f}")

#Imprime os resultados da Área e Volume da Esfera
print(f"A área da esfera é equivalente a:{área_e:.6f}")
print(f"O volume da esfera tem como resultado: {volume:.6f}")




