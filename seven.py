import decimal

# Напишите программу решения следующей задачи. Лотерейный номер
# состоит из трех чисел, каждое из которых может быть от 0 до 99
# включительно. Определите шанс угадать выигрышный лотерейный номер.

n = 1
nk = 1
for i in range(1, 101):
  n = n * i
for j in range(1, 101-3):
  nk = nk * j
print ("Шанс выиграть лотерейный билет 1 к", n / nk)
