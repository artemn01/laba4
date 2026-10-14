s = input("Введите строку... ")
res = ''

for i in range(0, len(s), 2):
    char = s[i]
    num = int(s[i+1])
    res += char * num

print(res)
