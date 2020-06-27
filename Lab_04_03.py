import random

A = []
size = int(input("Введите размер списка: \n"))

for i in range(size):
    A.append(random.randint(0, 99))
print(A)
number = int(input("Введите число, которое необходимо удалить из списка: \n"))

j = 0
while j < len(A):
    if A[j] == number:
        del A[j]
        print("Список изменен!")
    j += 1
print(A)

k = 0
s = len(A)
while s > k:
    if (A[s-1] % 2) == 0:
        A.insert(s, 0)
        print("Список изменен!")
    s -= 1
print(A)