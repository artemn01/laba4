def partlist(arr):
    result = []
    for i in range(1, len(arr)):
        result.append((' '.join(arr[:i]), ' '.join(arr[i:])))
    
    return result

print(partlist(["az", "toto", "picaro", "zone", "kiwi"]))
