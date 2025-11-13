dividendo=float(input("Digite um número, ele será o dividendo: ").strip())
divisor=float(input("Digite mais um número, este será o divisor: ").strip())

quociente=dividendo//divisor
resto=dividendo%divisor

print(f"O resultado da divisão entre esses números é: {quociente:.4f}!")
print(f"E tem como resto: {resto:.4f}!")
