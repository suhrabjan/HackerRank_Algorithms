def matrixRotation(matrix):
    m = len(matrix)
    n = len(matrix[0])
    if min(m, n) == 2:
        rotations = r % (m * n)
        if m > n:
            columns = [[*x] for x in zip(*matrix)]
            singleLayerBeforeRotation = columns[0] + columns[1][::-1]
            singleLayerAfterRotation = singleLayerBeforeRotation[-rotations:] + singleLayerBeforeRotation[:-rotations]
            finalResult = [[*x] for x in zip(singleLayerAfterRotation[:m], reversed(singleLayerAfterRotation[m:]))]
        else:
            singleLayerBeforeRotation = matrix[0] + matrix[1][::-1]
            singleLayerAfterRotation = singleLayerBeforeRotation[rotations:] + singleLayerBeforeRotation[:rotations]
            finalResult = [singleLayerAfterRotation[:n], singleLayerAfterRotation[n:][::-1]]
        return finalResult
    elif min(m, n) > 2:
        columns = [[*x] for x in zip(*matrix)]
        outerLayerBeforeRotation = [*matrix[0], *columns[-1][1:m - 1], *matrix[-1][::-1], *columns[0][::-1][1:m - 1]]
        rotations = r % len(outerLayerBeforeRotation)
        outerLayerAfterRotation = outerLayerBeforeRotation[rotations:] + outerLayerBeforeRotation[:rotations]
        innerMatrix = [i[1:n - 1] for i in matrix[1:m - 1]]
        innerSquare = matrixRotation(innerMatrix)
        temp = [[x, *j, y] for x, j, y in zip(outerLayerAfterRotation[2 * n + m - 2:][::-1], innerSquare, outerLayerAfterRotation[n:n + m - 2])]
        finalResult = [outerLayerAfterRotation[:n], *temp, outerLayerAfterRotation[n + m - 2:2 * n + m - 2][::-1]]
        return finalResult


example = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15, 16]]
r = 5
result = matrixRotation(example)
for i in result:
    print(*i)
