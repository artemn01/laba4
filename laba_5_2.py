n = int(input('Введите количество чисел... '))
max_num = 1

prev = int(input('Введите первое число... '))

for i in range(n - 1):
    curr = int(input('Введите число... '))
    pr = prev * curr
    if pr > max_num:
        max_num = pr

    prev = curr

print(max_num)