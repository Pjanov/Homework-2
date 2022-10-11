# Реализуйте алгоритм перемешивания элементов списка.
# Без функции shuffle из модуля random, другие методы использовать можно.


# using random.sample()


import random

# Первый вариант:
random_spisok = []
for i in range(10):
    random_spisok.append(random.randint(-10, 10))
print(f'Список заданный рандомно: {random_spisok}')

res = random.sample(random_spisok, len(random_spisok))
print(f'Перемешанный список: {res}')


# Второй вариант:
# spisok = []
# for i in range(10):
#     spisok.append(random.randint(-10, 10))
# print(f'Список заданный рандомно: {spisok}')

# for i in range(len(spisok)-1, 0, -1):
#     j = random.randint(0, i + 1)
#     spisok[i], spisok[j] = spisok[j], spisok[i]
# print(f'Перемешанный список: {spisok}')
