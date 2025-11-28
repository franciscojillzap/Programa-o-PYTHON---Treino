#Processamento de dados
def lista_A():
    A = []
    
    for i in range(2):
        letras = int(input())
        A.append(letras)
    
    return A

def lista_B():
    B = []
    
    for i in range(2):
        letras = int(input())
        B.append(letras)
    
    return B

def lista_C():
    A = lista_A()
    B = lista_B()
    C = []
    
    for item_A, item_B in zip(A, B):
        C.append(item_A)
        C.append(item_B)
    
    return C
        
#Programa principal
def main():
    print(lista_C())

if __name__ == '__main__':
    main()