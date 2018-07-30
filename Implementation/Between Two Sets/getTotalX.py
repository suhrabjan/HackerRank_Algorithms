def getTotalX(a, b):
    c = range(max(a), min(b) + 1)
    firstSet = set(c) - set([i for j in a for i in c if i % j != 0])
    finalSet = set(firstSet) - set([i for j in b for i in firstSet if j % i != 0])
    return len(finalSet)
