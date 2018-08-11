def happyLadybugs(b):
    if b.count('_') == 0:
        if len(b) == 1:
            return 'NO'
        for i in range(len(b) - 1):
            yesNoList = ['yes' if b[i] == b[i + 1] else 'no' for i in range(len(b) - 1)]
        if yesNoList[0] == 'no' or yesNoList[-1] == 'no':
            return 'NO'
        elif 'nono' in ''.join(yesNoList):
            return 'NO'
        else:
            return 'YES'
    else:
        letterCountList = [b.count(i) for i in b if i != '_']
        if 1 in letterCountList:
            return 'NO'
        else:
            return 'YES'
