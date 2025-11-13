#Atribui um valor para A e B
a=float(input("Digite o primeiro valor: ").strip())
b=int(input("Digite o segundo valor: ").strip())

#Adição
soma=a+b
#Concatenação
concat=str(a)+ str(b)
#Multiplicação
produto=a*b
#Multiplicação de String
mult_str=str(a)*b
#Divisão
divisao=a/b
#Divisão inteira
div_int=a//b
#Exponenciação
potencia=a**b
#Módulo
resto=a%b

#Imprime os resultados
print(f"A soma desses números é {soma}!")
print(f"A junção desses valores como string é {concat}!")
print(f"Esses números tem como produto {produto}!")
print(f"A multiplicação como string termina em {mult_str}!")
print(f"A divisão resulta em {divisao}!")
print(f"O resultado inteiro dessa divisão é {div_int}!")
print(f"O primeiro valor elevado ao segundo tem como resposta {potencia}!")
print(f"O que sobra da divisão: {resto}.")
