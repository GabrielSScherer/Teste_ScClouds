#recursivo
def verificar_primo(numero, divisor=2):
    if numero < 2:
        return False
    if divisor * divisor > numero:
        return True
    if numero % divisor == 0:
        return False
    return verificar_primo(numero, divisor + 1)


def listar_primos(n, atual=2):
    if atual > n:
        return []
    if verificar_primo(atual):
        return [atual] + listar_primos(n, atual + 1)
    return listar_primos(n, atual + 1)


# Entrada do usuário
try:
    n = int(input("Digite um número inteiro maior que 1 para listar os números primos até ele: "))
    if n <= 1:
        print("Por favor, insira um número maior que 1.")
    else:
        print(f"Números primos até {n}: {listar_primos(n)}")
except ValueError:
    print("Entrada inválida! Insira um número inteiro.")

#Linear

def encontrar_primos(n):
    primos = []
    for num in range(2, n + 1):
        eh_primo = True
        for divisor in range(2, num):
            if num % divisor == 0:
                eh_primo = False
                break
        if eh_primo:
            primos.append(num)
    return primos


# Entrada do usuário e exibição de resultados
n = int(input("Digite um número inteiro maior que 1: "))
if n <= 1:
    print("O número deve ser maior que 1.")
else:
    print("Números primos até", n, "são:", encontrar_primos(n))
