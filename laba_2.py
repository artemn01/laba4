import math

number = 1

for n in range(1, 11):
    nums = math.cos(n**3) + n**2 + 4
    den = math.sin(n**3) + n**2 + 6
    number *= nums / den

print(f'Результат: {number}')