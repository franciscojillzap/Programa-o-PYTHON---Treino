#Processamento de dados
def lista_A():
    A = []
    
    for i in range(2):
        letras = input()
        A.append(letras)

def lista_B():
    B = []
    
    for i in range(2):
        letras = input()
        B.append(letras)

def lista_C():
    C = []
    
    for item_A, item_B in zip(lista_A, lista_B):
        C.append(item_A)
        C.append(item_B)
        
#Programa principal
def main():
    print(lista_C)

if __name__ == '__main__':
    main()
