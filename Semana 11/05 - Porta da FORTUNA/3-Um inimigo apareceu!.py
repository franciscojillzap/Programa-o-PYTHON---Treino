from random import *

#Instruções do jogo
print('''
Um slime aparece diante de você! Ele possui 21 pontos de HP!
Pegue sua espada e prepare-se para a batalha!

Em quantos turnos você consegue derrotá-lo?
''')

#Dano causado pelo ataque, seja físico ou mágico.
dano_causado = 0

#Número de turnos que levou até o final do combate.
n_turnos = 0

#Pontos de HP totais do Slime
HP_slime = 21

#Pontos de HP totais do Herói
HP_heroi = 21

while dano_causado < 21:
    n_turnos += 1
    
    #Movimentos que podem ser executados durante o turno de ação.
    print("ESCOLHA SUA AÇÃO: (1-Atacar / 2-Magia / 3-Fugir)")

    #Ação do jogador durante seu turno, baseado nos movimentos acima.
    turno = input()

    #Se escolher atacar, usará um golpe básico com a ESPADA.
    if turno == "1":
        atacar = randint(4, 8)
        dano_causado += atacar
        HP_slime = max(0, HP_slime - atacar)
        print(f"Você atinge o slime com sua espada e arranca {atacar} de dano!\nSlime fica com {HP_slime} de HP!\n")

    #Se escolher magia, pode alternar entre magia de ATAQUE ou magia de CURA.
    elif turno == "2":
        magia = input("A magia mais útil no momento é: (A - Ataque / C - Cura)\n").upper()

        if magia == "A":
            magia_ataque = randint(5, 15)
            dano_causado += magia_ataque
            HP_slime = max(0, HP_slime - magia_ataque)
            print(f"Você concentra-se e atinge o slime com uma bola de fogo! causa {magia_ataque} de dano!\nSlime fica com {HP_slime} de HP!\n")

        elif magia == "C":
            magia_cura = randint(8, 12)
            HP_heroi = min(21, HP_heroi + magia_cura)
            print(f"Os céus lhe concedem a benção da cura! Recupera {magia_cura} de HP!\nVocê tem {HP_heroi} pontos de HP.\n")

    #Se decidir fugir...
    elif turno == "3":
        print("Conseguiu escapar por pouco!\n")
        print("Este é o herói que protegerá o mundo da devastação?\nQue unirá as pessoas de nossa nação?\nSó pode ser brincadeira...")
        break

    #Reduziu o inimigo a CINZAS!
    if HP_slime == 0:
        print(f"Slime foi derrotado! Ganhou 5 pontos de experiência!\nNúmero de turnos até a vitória: {n_turnos}!")
        break

    #O inimigo também pode ATACAR!
    print("CUIDADO! TURNO INIMIGO!!!")
    ataque_slime = randint(5, 10)
    HP_heroi = max(0, HP_heroi - ataque_slime)
    print(f"Slime se lança na sua direção e causa {ataque_slime} de dano!\nSeu HP cai para {HP_heroi}!\n")

    #Se o Herói for derrotado...
    if HP_heroi == 0:
        print(f"Você fracassou, sua jornada teve fim, e o mundo continua um lugar perigoso...\nNúmero de turnos que sobreviveu: {n_turnos}.")
        break
        
