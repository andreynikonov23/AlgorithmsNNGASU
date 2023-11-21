# Поле шахматной доски определяется парой натуральных чисел, каждое из
# которых не превосходит 8 По введённым координатам двух полей (k, l) и (m, n)
# выясните, угрожает ли ферзь, находящийся на поле (k, l), полю (m, n)?
# Входные данные
# На вход программе подаются четыре целых числа k, l, m, n.
# Выходные данные
# Выведите YES или NO в зависимости от ответа на вопрос задачи.

coordinates_str = input("Введите координаты ферзя и короля k, l, m, n: \n")
coordinates_str_arr = coordinates_str.split(" ")
coordinates = [int(i) for i in coordinates_str_arr]
x_king = coordinates[0]
y_king = coordinates[1]
x_queen = coordinates[2]
y_queen = coordinates[3]

if x_king == x_queen or y_king == y_queen:
    print("YES")
else:
    is_true = 1
    if x_king < x_queen and y_king > y_queen:
        while x_queen > 0 and y_queen < 9:
            x_queen = x_queen - 1
            y_queen = y_queen + 1
            if x_queen == x_king and y_queen == y_king:
                print("YES")
                is_true = 0
                break
    if x_king > x_queen and y_king < y_queen:
        while x_queen < 9 and y_queen > 0:
            x_queen = x_queen + 1
            y_queen = y_queen - 1
            if x_queen == x_king and y_queen == y_king:
                print("YES")
                is_true = 0
                break
    if x_king < x_queen and y_king < y_queen:
        while x_queen > 0 and y_queen > 0:
            x_queen = x_queen - 1
            y_queen = y_queen - 1
            if x_queen == x_king and y_queen == y_king:
                print("YES")
                is_true = 0
                break
    if x_king > x_queen and y_king > y_queen:
        while x_queen < 9 and y_queen < 9:
            x_queen = x_queen + 1
            y_queen = y_queen + 1
            if x_queen == x_king and y_queen == y_king:
                print("YES")
                is_true = 0
                break
    if is_true == 1:
        print("NO")