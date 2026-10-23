lst = [10, 21, 34, 43, 52]
el_max = max(lst)
el_min = min(lst)

max_index = lst.index(el_max)
min_index = lst.index(el_min)

lst[max_index], lst[min_index] = lst[min_index], lst[max_index]

print(lst)