# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# Первый вариант:
n = int(input('Введите N: '))

res = 1
print(f'N = {n} ->', end=' ')
for i in range(1, n + 1):
    res *= i
    i += 1
    print(res, end=' ')


#Второй вариант:
# n = int(input('Введите N: '))

# spisok = [1]
# for i in range(2, n + 1):
#     spisok.append(spisok[i - 2] * i)
# print(f'N = 4 -> {spisok}')    

