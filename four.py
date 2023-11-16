# Числа Фибоначчи – это ряд чисел, в котором каждое следующее число
# равно сумме двух предыдущих.
# 1, 1, 2, 3, 5, 8, 13, ...
# Вычисление n-го числа ряда Фибоначчи с помощью цикла while

n = int(input("Введите n-число ряда Фибоначчи: "))
fibonacci_series = [1, 1]

i = 1
while i <= n - 2:
    num = fibonacci_series[i] + fibonacci_series[i - 1]
    fibonacci_series.append(num)
    i += 1
print(fibonacci_series)
print(fibonacci_series[n-1])


