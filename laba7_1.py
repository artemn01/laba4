def partlist():
    a = ["az", "toto", "picaro", "zone", "kiwi"]
    result = []
    for i in range(1, len(a)):
        result.append([' '.join(a[:i]), ' '.join(a[i:])])

    return result

print(partlist())
    
