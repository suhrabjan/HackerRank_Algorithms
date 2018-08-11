def surfaceArea(A):
    flattenedNoZeros = [j for i in A for j in i if j > 0]
    columnList = [[*a] for a in zip(*A)]
    rowList = A
    absDifferenceOfColumns = [abs(i[j] - i[j + 1]) for i in rowList for j in range(len(i) - 1)]
    absDifferenceOfRows = [abs(i[j] - i[j + 1]) for i in columnList for j in range(len(i) - 1)]
    result = 2 * len(flattenedNoZeros) + sum(columnList[0]) + sum(columnList[-1]) + sum(rowList[0]) + sum(rowList[-1]) + sum(absDifferenceOfColumns) + sum(absDifferenceOfRows)
    return result
