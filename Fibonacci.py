# recursivo
def fibonacci_recursivo(n):
    # quando n for zero retorna zero
    if n == 0:
        return 0
    # quando n for 1 retorna 1
    if n == 1:
        return 1
    # faz calculo de forma recursiva somando as funções e diminuindo n - 1 de uma e n -2 de outra
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


# Enquanto for verdadeiro ele fica no loop
while True:
    #Fiz esse sistema de escolha para ficar mais facil de sair do loop
    n = int(input("Escolha uma opção:\n"
                  "1 - Fibonacci\n"
                  "2 - Sair\n"
                  ""))
    #Se n == 1 ele pede para inserir um numero verdadeiro e depois verifica se ele maior que zero
    if n == 1:
        x = int(input("1 - Digite um numero inteiro positivo: \n"))
        if x < 0:
            print("O número não pode ser negativo!\n")
        else:
            # Eu pulei uma linha porque achei que parecia muito grudado
            print("\n")
            #aparece o resultado
            print(f"Fib({x}) = {fibonacci_recursivo(x)}\n")
    #Saida do loop
    elif n == 2:
        print("Saindo...")
        break
    #caso o usuario digite um valor que não seja 1 ou 2
    else:
        print("Digite 1 ou 2\n")


# Linear
def fibonacci_linear(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    #Não precisava usar o valor do indice ai coloquei o _ que ignora o indice
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

while True:
    try:
        opcao = int(input("Escolha uma opção:\n"
                          "1 - Calcular Fibonacci (Linear)\n"
                          "2 - Sair\n"
                          "Digite sua escolha: "))

        if opcao == 1:
            numero = int(input("Digite um número inteiro positivo: "))
            if numero < 0:
                print("O número não pode ser negativo!\n")
            else:
                print(f"Fib({numero}) = {fibonacci_linear(numero)}\n")

        elif opcao == 2:
            print("Saindo...")
            break

        else:
            print("Opção inválida! Digite 1 ou 2.\n")

    except ValueError:
        print("Entrada inválida! Por favor, insira um número inteiro.\n")
