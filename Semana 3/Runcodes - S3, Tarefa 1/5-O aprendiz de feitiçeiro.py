print("O mestre me pediu para ir atrás dos ingredientes para uma poção. Vejamos...")

#Porção desejada para o ingrediente PÓ DE LUA ESTELAR
pó_estelar=int(input("Vamos precisar de Pó de Lua Estelar. A quantidade deve ser: ").strip())

#Porção desejada para o ingrediente ESSÊNCIA DRACÔNICA
essência_dracônica=int(input("Essência Dracônica também! Que eu lembre, vamos precisar de: ").strip())

#Porção desejada para o ingrediente LÁGRIMA DE FÊNIX
lágrima_fênix=int(input("E por último, Lágrima de Fênix: ").strip())

#Total a pagar
dinheiro=(5*pó_estelar)+(3*essência_dracônica)+(8*lágrima_fênix)

#Revela a quantidade necessária de moedas de ouro para a compra dos materiais
print(f"Parece que vou ter que desembolsar {dinheiro} moedas de ouro pra pagar tudo isso.")

