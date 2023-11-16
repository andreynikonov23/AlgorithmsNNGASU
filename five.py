# Вычислить n -ый факториал рекурсией
n = int(input("Введите n: "))

def factorial(n, i, r):
    diff = n - i
    result = r * diff
    if i == 0:
        print(result)
        return result
    else:
        i = i - 1
        factorial(n, i, result)

factorial(n, n-1, 1)

