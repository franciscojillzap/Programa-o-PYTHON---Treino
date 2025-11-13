#Processamento de dados
def inocente_ou_culpado(p1, p2, p3, p4, p5):
    #Armazena as respostas
    respostas = [p1, p2, p3, p4, p5]

    #Contagem de pontos
    #O método count() conta quantas vezes o termo aparece dentro de um conjunto
    pontos = respostas.count("S")
    
    #Nível de envolvimento no crime hipotético 
    if (pontos == 0) or (pontos == 1):
        return "Inocente"
    elif pontos == 2:
        return "Suspeito"
    elif (pontos == 3) or (pontos == 4):
        return "Cúmplice"
    elif pontos == 5:
        return "Assassino"        

#Programa principal
def main():
    #Próposito do questionário
    print("Estamos investigando um homicídio, responda apenas com S(sim) ou N(não) \n")
    #Entrada
    a = input("Telefonou para a vítima? ").strip().upper()
    b = input("Esteve no local do crime? ").strip().upper()
    c = input("Mora perto da vítima? ").strip().upper()
    d = input("Devia para a vítima? ").strip().upper()
    e = input("Já trabalhou com a vítima? ").strip().upper()

    #Chamada da função
    resultado = inocente_ou_culpado(a, b, c, d, e)
    
    #Saída condicional
    print(resultado)

if __name__ == '__main__':
    main()
    
    
