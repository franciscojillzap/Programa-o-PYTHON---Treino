from random import *

def gerador_de_insultos(nome):
    adjetivos = ['retardado', 'maria-mole', 'mendigo', 'frango', 'boneco de olinda']
    hobbie = ['joga yu-gi-OH!', 'anda de bicicleta', 'come', 'levanta peso na academia', 'dança']
    
    return f'\n{nome}, você parece um {choice(adjetivos)} quando {choice(hobbie)}.'
    
def main():
    print('Gerador de INSULTOS & OFENSAS')
    print(f"{'-'*29}")
    
    nome = input('Digite seu nome, seu animal! ')
    print('Aqui está seus cumprimentos, cabeção!')

    while True:
        print(gerador_de_insultos(nome))

        while True:
            resposta = input('E aí? Quer continuar? (S/N) ').upper()

            if resposta in ('S', 'N'):
                break
            print('\nDigite uma resposta válida')

        if resposta == 'N':
            break
    
    print(f'\nO quê? Não fique zangado por tão pouco!')
    

if __name__ == '__main__':
    main()
