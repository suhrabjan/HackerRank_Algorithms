def howManyGames(p, d, m, s):
    count = 0
    while (p >= m and s >= p):
        count += 1
        s -= p
        p -= d

    while s >= m and s >= p:
        count += 1
        s -= m

    return count
