def sera_primo(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

        return True

def main():
    numero = int(input("Digite um maldito número: "))

    print(f'Será que é par?',sera_primo(numero))

if __name__ == '__main__':
    main()

    
