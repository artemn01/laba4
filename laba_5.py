n = int(input('Введите колличество чисел... '))
count = 0

prev = int(input('Введите первое число... '))
curr = int(input('Введите второе число... '))

for i in range(n - 2):
    nxt = int(input('Введите число... '))

    if curr > prev and curr > nxt:
        count += 1

    prev = curr
    curr = nxt

print(count)


    