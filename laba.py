import math

number = 0

for n in range(1, 51):
    num = ((-1)**n) * (math.pi / 6) ** (2 * n - 1)
    den = math.factorial(n - 1)

    number += num / den

print(f'Результат = {number}')