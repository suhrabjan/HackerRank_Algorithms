def getTotalX(a, b):
    count = 0
    k = []
    for i in range(max(a), min(b) + 1):
        for num in a:
            if i % num != 0:
                break
            elif num == a[len(a) - 1]:
                k.append(i)
    for num in k:
        for num2 in b:
            if num2 % num != 0:
                break
            elif num2 == b[len(b) - 1]:
                count += 1
    return count
