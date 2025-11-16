def sera_primo(n):
    if n <= 1:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True

def quantos_primos(n_1, n_2):
    inicio = min(n_1, n_2)
    fim = max(n_1, n_2)

    for n in range(inicio, fim + 1):
        if sera_primo(n):
            print(n)

def main():
    x = int(input())
    y = int(input())

    quantos_primos(x, y)
    
if __name__ == '__main__':
    main()

    
