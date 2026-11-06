import math
lst = [1, 5, 2]

result = []

for i in lst:
    result.append(int(math.prod(lst)/i))

print(result)