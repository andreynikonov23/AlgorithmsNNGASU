# Написать программу, которая выполняет над двумя вещественными числами
# одну из четырех арифметических операций (сложение, вычитание,
# умножение или деление). Программа должна завершаться только по
# желанию пользователя.

while 1:
    str = input("Введите арифметическую операцию над двумя числами: ")
    if str == "exit":
        break
    str.replace(' ', '')
    try:
        if not str.find('+') == -1:
            nums = str.split('+')
            a = int(nums[0])
            b = int(nums[1])
            result = a + b
            print(result)
        if not str.find('-') == -1:
            nums = str.split('-')
            a = int(nums[0])
            b = int(nums[1])
            result = a - b
            print(result)
        if not str.find('*') == -1:
            nums = str.split('*')
            a = int(nums[0])
            b = int(nums[1])
            result = a * b
            print(result)
        if not str.find('/') == -1:
            nums = str.split('/')
            a = int(nums[0])
            b = int(nums[1])
            result = a / b
            print(result)
    except Exception as e:
        print("Операция записана неправильно")

