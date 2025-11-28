#Processamento de dados
def lista_A():
    A = []
    
    for i in range(25):
        letras = int(input(f'Digite o {i+1}º número da lista A: '))
        A.append(letras)
    
    return A

def lista_B():
    B = []
    
    for i in range(25):
        letras = int(input(f'Digite o {i+1}º número da lista B: '))
        B.append(letras)
    
    return B

def lista_C(a, b):
    C = []
    
    for item_A, item_B in zip(a, b):
        C.append(item_A)
        C.append(item_B)
    
    return C
        
#Programa principal
def main():
    A = lista_A()
    B = lista_B()
    C = lista_C(A, B)

    print('Eis a lista A:', A)
    print('Eis a lista B:', B)
    print('Eis a lista C, a intercalação das listas A e B:', C)

if __name__ == '__main__':
    main()