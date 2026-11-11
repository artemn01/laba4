def product_array(numbers):
    import math
    result = []
    for i in numbers:
        result.append(int(math.prod(numbers)/i))
    return result

print(product_array([1, 5, 2]))