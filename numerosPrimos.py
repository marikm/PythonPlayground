def eh_primo_2(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print("nao e primo")
                break
            else:
                print("e primo")
                break
        if num == 2:
            print("numero 2 e primo")
    else:
        if num == 1:
            print("voce digitou 1, nao e primo")
        elif num == 0:
            print("voce digitou 0, nao e primo")

if __name__ == '__main__':
    n = int(input())
    for j in range(0, n):
        x = int(input())
        eh_primo_2(x)
