# Найти наименьшее общее кратное (НОК) пары чисел по формуле
# НОК = ab / НОД(a, b),
# где a и b - это натуральные числа, НОД - наибольший общий делитель.

a = int(input("a: "))
b = int(input("b: "))

aDivisors = []
bDivisors = []

for i in range(1, a+1):
    if a % i == 0:
        aDivisors.append(i)

for i in range(1, b+1):
    if b % i == 0:
        bDivisors.append(i)

common_divisors = []
for ad in aDivisors:
    for bd in bDivisors:
        if ad == bd:
            common_divisors.append(ad)

nod = 0
for i in common_divisors:
    if i >= nod:
        nod = i

nok = a * b / nod
print('Наименьшее общее кратное', nok)