atual=int(input("Qual volume atual do seu aparelho? ").strip())
desejado=int(input("Deseja que ele esteja em que volume? ").strip())
diferença=desejado-atual

print(f"Para que o volume atinja o valor desejado, falta {diferença}!")
