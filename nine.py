# Напишите программу, в которой предлагается вводить студентов различных
# групп, посещающих футбольную секцию. Требуется упорядочить список по
# возрастанию групп. Распечатать список фамилий и групп.

groups = {}
print("Вводите фамилии и группы студентов, для выхода напишите exit:")

while 1:
    student = input()
    if student == "exit":
        break
    temp = student.split(' ')
    surname = temp[0]
    group = int(temp[1])
    groups[surname] = group

sorted_groups = sorted(groups.items(), key=lambda item: item[1])
print(sorted_groups)



