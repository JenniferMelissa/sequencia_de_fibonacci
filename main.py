# #funcao

def calcular_fibonacci(n):
    if n <= 1:
        return n
    else: 
        return calcular_fibonacci(n-1) + calcular_fibonacci(n-2)

# Principal
n = int(input('Informe o número de sequências a ser calculada: '))

for x in range(n):
    print(calcular_fibonacci(x))


