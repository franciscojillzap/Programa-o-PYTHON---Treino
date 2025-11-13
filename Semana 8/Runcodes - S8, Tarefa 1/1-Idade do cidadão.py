#Processamento de Dados
def calculo_idade(tempo_presente, tempo_mais_que_perfeito):
    #Tratando possíveis exceções
    if "/" not in tempo_presente or "/" not in tempo_mais_que_perfeito:
        return "Tente digitar as datas no formato DD/MM/AAAA"
    
    #Dividindo as respectivas datas em DIA / MÊS / ANO
    try:
        dia_atual, mes_atual, ano_atual = map(int, tempo_presente.split("/"))
        nascido_dia, nascido_mes, nascido_ano = map(int, tempo_mais_que_perfeito.split("/"))
    except ValueError:
        return "Digite apenas números."
        
    
    #Descobrir IDADE
    idade = ano_atual - nascido_ano

    #Controle condicional da IDADE
    if (mes_atual < nascido_mes) or (dia_atual < nascido_dia):
        idade -= 1
        
    #Retornar IDADE
    return idade

#Programa Principal
def main():
    #Entrada para DATA ATUAL
    data_atual = input("Qual a data de hoje? ").strip()
    
    #Entrada para DATA de NASCIMENTO
    data_nascimento = input("Qual a data de seu nascimento? ").strip()
    
    #Chamada da função
    voce_tem = calculo_idade(data_atual, data_nascimento)

    #Saída
    if isinstance(voce_tem, int):
        print(f'\nVocê atingiu a idade de {voce_tem} anos! Parábens!')
    else:
        print(f"\n{voce_tem}")

if __name__ == '__main__':
    main()
    
    
