#Processamento de dados
def calculo_media(bomba, tarefa):
    media = (bomba[0] + bomba[1] * 2 + bomba[2] * 3 + tarefa) / 7
    return f"A média do aluno é: {media:.2f}"

def conceito(bomba, tarefa):
    media = (bomba[0] + bomba[1] * 2 + bomba[2] * 3 + tarefa) / 7

    if media >= 9.0:
        return "Aluno nota A"
    elif 9 > media >= 7.5:
        return "Aluno nota B"
    elif 7.5 > media >= 6.0:
        return "Aluno nota C"
    elif 6.0 > media >= 4.0:
        return "Aluno nota D"
    elif media < 4.0:
        return "Aluno nota E"

def ceu_ou_inferno(conceito):
    if conceito in ["Aluno nota A","Aluno nota B","Aluno nota C"]:
        return "Conclusão: Aprovado"
    else:
        return "Conclusão: Reprovado"
    
#Programa principal
def main():
    #Lista VAZIA
    trimestre = []

    #Entrada para número de MATRÍCULA
    n_matricula = input("Digite seu número de matrícula: ").strip()
    
    #Entrada para NOTAS
    for i in range(3):
        notas = float(input(f"{i+1}ª nota: ").strip())
        trimestre.append(notas)

    #Entrada para MÉDIA dos EXERCÍCIOS
    media_exercicio = float(input("Média de qualitativo: ").strip())

    #Chamada da função
    resultado_media = calculo_media(trimestre, media_exercicio)
    resultado_conceito = conceito(trimestre, media_exercicio)
    resultado_aprovacao = ceu_ou_inferno(resultado_conceito)

    #Saída condicional
    print(n_matricula)
    print(resultado_media)
    print(resultado_conceito)
    print(resultado_aprovacao)

if __name__ == '__main__':
    main()
        
    
