def isValid(s):
    result = 'YES'
    charCounts = {}
    inequalityCount = 0
    for char in s:
        if char in charCounts:
            charCounts[char] += 1
        else:
            charCounts[char] = 1
    if [i for i in charCounts.values()].count(min(charCounts.values())) == 1:
        temp = max(charCounts.values())
    else:
        temp = min(charCounts.values())
    for num in charCounts.values():
        if num != 1 and 1 < abs(temp - num):
            inequalityCount = 100
            break
        elif temp != num:
            inequalityCount += 1
    if inequalityCount > 1:
        result = 'NO'
    return result
