lst = [0,3,7,2,5,8,4,6,0,1] 

nums = set(lst)
max_lenght = 0

for i in nums:
    num = i
    l = 1
    if i - 1 not in nums:
        num = i
        l = 1

    while num + 1 in nums:
         num += 1
         l += 1
    if l > max_lenght:
        max_lenght = l

print(max_lenght)

