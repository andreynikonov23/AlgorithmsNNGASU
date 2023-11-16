# Данная программа должна вывести все простые числа в заданном диапазоне (от 0
# до n) при помощи алгоритма «Решето Эратосфена».

length = int(input("Введите диапазон чисел от 0: "))

nums = [i for i in range(2, length + 1)]

print(nums)

composite = set()

for i in range(2, len(nums)):
    a = i + 1
    for j in range(i + 1, len(nums)):
        if nums[j] % nums[i] == 0:
            composite.add(nums[j])
for n in nums:
    if not n in composite:
        print(n, end=' ')
