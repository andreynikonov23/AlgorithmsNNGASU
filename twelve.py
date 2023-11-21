import math
# Написать программу для Треугольника, заданного длинами сторон. Найти:
# а) длины высот;
# б) длины медиан;
# в) длины биссектрис;
# г) радиусы вписанной и описанной окружностей.


a = int(input("Введите сторону A: "))
b = int(input("Введите сторону B: "))
c = int(input("Введите сторону C: "))

p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
ha = 2 * s / a
hb = 2 * s / b
hc = 2 * s / c
ma = math.sqrt(2 * (c ** 2) + 2 * (b ** 2) - (a ** 2)) / 2
mb = math.sqrt(2 * (a ** 2) + 2 * (c ** 2) - (b ** 2)) / 2
mc = math.sqrt(2 * (a ** 2) + 2 * (b ** 2) - (c ** 2)) / 2
la = (2 * math.sqrt(b * c * p * (p - a))) / (b + c)
lb = (2 * math.sqrt(a * c * p * (p - b))) / (a + c)
lc = (2 * math.sqrt(a * b * p * (p - c))) / (a + b)
rIn = math.sqrt(((p - a) * (p - b) * (p - c)) / p)
rC = (a * b * c) / (4 * math.sqrt(p * (p - a) * (p - b) * (p - c)))

print("Длинна высоты a: ", ha)
print("Длинна высоты b: ", hb)
print("Длинна высоты c: ", hc)
print("Медиана a: ", ma)
print("Медиана b: ", mb)
print("Медиана c: ", mc)
print("Биссектриса a", la)
print("Биссектриса b", lb)
print("Биссектриса c", lc)
print("Радиус вписанной окружности: ", rIn)
print("Радиус описанной окружности: ", rC)

