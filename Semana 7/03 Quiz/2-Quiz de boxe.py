score = 0

print("Bem-vindo a este Quiz de conhecimentos gerais sobre BOXE! Vamos às perguntas!")
print('''
1 - A postura SOUTHPAW é adotada por qual tipo de lutador?
a) Destro.
b) Canhoto.
c) Ambidresto.
''')
resposta_1 = input("A resposta correta é a letra...").lower()

if resposta_1 == "a":
    print("Vou supor que você ainda está aquecendo.")
elif resposta_1 == "b":
    print("Afirmação correta! Muito bem! ;)")
    score += 10    
elif resposta_1 == "c":
    print("Passou longe, hein?")
else:
    print("Não sabe? Tudo bem, vamos para a próxima.")

print('''
2 - Um lutador que pode ALTERNAR entre as posturas Ortodoxa e Southpaw só pode ser:
a)Destro.
b)Ambidresto.
c)O Randy Boy Jr.
''')

resposta_2 = input("A única resposta correta é a letra...").lower()

if resposta_2 == "a":
    print("O quê? Está díficil demais pra você?")
elif resposta_2 == "b":
    print("Está no caminho certo. Continue assim!")
    score += 10
elif resposta_2 == "c":
    print("Lê Hajime no Ippo? Não te conheço, mas já te considero pacas!")
    score += 20
else:
    print("Qual é! Faça um esforço pelo menos!")

print('''
3 - Qual a principal diferença entre lutadores IN-FIGHTERS & OUT-BOXERS?
a) O Out-boxer busca combate a curta distância.
b) O intenção do In-fighter é aplicar pressão, atacando seu oponente diretamente.
c) Não há diferença entre os estilos.
''')

resposta_3 = input("A afirmação correta está na letra...").lower()

if resposta_3 == "a":
    print("Na verdade é o exato oposto.")
elif resposta_3 == "b":
    print("Você tem uma ótima intuição! Párabens!")
    score += 10
elif resposta_3 == "c":
    print("IN é dentro, OUT é fora, existe uma clara diferença.")
else:
    print("Vamos lá,cara! Mesmo que não marque um gol, você tem a obrigação de chutar!")

print('''
4 - Quem popularizou o estilo de boxe conhecido como PEEK-A-BOO?
a)Kamogawa Genji
b)Muhammad Ali
c)Mike Tyson
''')

resposta_4 = input("De todas, a única opção só pode ser a letra...").lower()

if resposta_4 == "a":
    print("Errou, mas se sabe quem é, merece pontos.")
    score += 5
elif resposta_4 == "b":
    print("Já estamos na penúltima questão, não acha que está hora de começar a acertar algumas?")
elif resposta_4 == "c":
    print("Preciso como o próprio Tyson na hora de colocar seu adversário pra mimir. Mirou, matou!")
    score += 10
else:
    print("Até onde acha que consegue chegar desse jeito?")

print('''
5 - Agora, a pergunta matadora! Na sua opinião, quem será o futuro campeão de boxe?
a) Eu (você).
b) Você (eu, criador do quiz).
c) Makunouchi Ippo.
''')

resposta_5 = input("Sem dúvida, letra...").lower()

if resposta_5 == "a":
    print("Gosto de você! Perde a questão, mas não perde a piada!")
elif resposta_5 == "b":
    print("Concordo com você.")
    score += 10
elif resposta_5 == "c":
    print("Merece mais do que eu.")
    score += 50
else:
    print("Te falta iniciativa.")

print('''
E este é o fim do Quiz! Hora de analisar sua pontuação!
''')

if score == 100:
    print(f"{score} pontos! Quer tomar meu cinturão?? SÓ POR CIMA DO MEU CADÁVER!!")
elif score >= 20:
    print(f"{score} pontos! Nada mal, consegue dar trabalho pra mim no ringue, mas só um pouco.")
elif score <= 15:
    print(f"{score} pontos! HORRÍVEL!! Em uma academia de boxe, você sem dúvida seria o SACO DE PANCADAS!")



    

