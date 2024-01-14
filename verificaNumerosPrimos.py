import math


def eh_primo(entrada):
    resultado = True
    raiz = int(math.sqrt(entrada))
    if raiz > 1:
        for i in range(2, raiz + 1):
            if entrada % i == 0:
                resultado = False
                break
            else:
                if i >= raiz:
                    resultado = True
    else:
        resultado = True
    return resultado


def getStringPrimo(entrada):
    if eh_primo(entrada):
        StringPrimoAux = " eh primo"
    else:
        StringPrimoAux = " nao eh primo"
    print(str(entrada) + StringPrimoAux)


if __name__ == '__main__':
    n = int(input())
    for j in range(0, n):
        entrada = int(input())
        getStringPrimo(entrada)
