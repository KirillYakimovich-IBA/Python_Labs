import random

A = []
j = 0
size = int(input("Введите размер списка: \n"))
for i in range(size):
    A.append(random.randint(0, 99))
print(A)
number = int(input("Введите число, которое необходимо удалить из списка: \n"))
while j < len(A):
    if A[j] == number:
        del A[j]
        print("Список изменен!")
        print(A)
    j += 1
