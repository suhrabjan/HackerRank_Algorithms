from collections import defaultdict


def steadyGene(gene):
    result = []
    s = defaultdict(int)
    for ch in gene:
        s[ch] += 1
    sd = {key: (value - (len(gene) // 4)) for key, value in s.items() if value > len(gene) // 4}
    ld = defaultdict(list)
    for i in range(len(gene)):
        if gene[i] in sd:
            ld[gene[i]].append(i)
    if len(sd) == 1:
        [x] = [i for i in sd]
        i = 0
        while i <= len(ld[x]) - sd[x]:
            minIndex = ld[x][i]
            maxIndex = ld[x][i + sd[x] - 1]
            result.append(maxIndex - minIndex + 1)
            i += 1
    elif len(sd) == 2:
        x, y = sd
        i = 0
        j = 0
        while i <= len(ld[x]) - sd[x] and j <= len(ld[y]) - sd[y]:
            xIndexStart = ld[x][i]
            xIndexEnd = ld[x][i + sd[x] - 1]
            yIndexStart = ld[y][j]
            yIndexEnd = ld[y][j + sd[y] - 1]
            maxIndex = max(xIndexEnd, yIndexEnd)
            minIndex = min(xIndexStart, yIndexStart)
            result.append(maxIndex - minIndex + 1)
            if minIndex == xIndexStart:
                i += 1
            else:
                j += 1
    elif len(sd) == 3:
        x, y, z = sd
        i = 0
        j = 0
        k = 0
        while i <= len(ld[x]) - sd[x] and j <= len(ld[y]) - sd[y] and k <= len(ld[z]) - sd[z]:
            xIndexStart = ld[x][i]
            xIndexEnd = ld[x][i + sd[x] - 1]
            yIndexStart = ld[y][j]
            yIndexEnd = ld[y][j + sd[y] - 1]
            zIndexStart = ld[z][k]
            zIndexEnd = ld[z][k + sd[z] - 1]
            maxIndex = max(xIndexEnd, yIndexEnd, zIndexEnd)
            minIndex = min(xIndexStart, yIndexStart, zIndexStart)
            result.append(maxIndex - minIndex + 1)
            if minIndex == xIndexStart:
                i += 1
            elif minIndex == yIndexStart:
                j += 1
            else:
                k += 1
    else:
        result.append(0)

    return min(result)
