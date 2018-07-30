def breakingRecords(scores):
    maxScore = scores[0]
    minScore = scores[0]
    countMax = 0
    countMin = 0
    for score in scores[1:]:
        if score > maxScore:
            maxScore = score
            countMax += 1
        elif score < minScore:
            minScore = score
            countMin += 1
    return [countMax, countMin]
