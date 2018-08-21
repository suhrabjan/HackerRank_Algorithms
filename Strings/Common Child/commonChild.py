# Note: This code passes all test-cases in Python 2 but not Python 3. It looks like python 3 is slower than python 2. Changing max() to if else inside the for loop increases the speed of code by couple seconds but still not enough for passing all test-cases in python3.


def commonChild(s1, s2):
    d1, d2 = '/', '/'
    for ch in s1:
        if ch in s2:
            d1 += ch
    for ch in s2:
        if ch in s1:
            d2 += ch
    if d1 == '/':
        return 0
    else:
        matrix = [(len(d1)) * [0] for i in range(len(d2))]
        for row in range(1, len(d2)):
            for col in range(1, len(d1)):
                if d2[row] == d1[col]:
                    matrix[row][col] = matrix[row - 1][col - 1] + 1
                else:
                    matrix[row][col] = max(matrix[row - 1][col], matrix[row][col - 1])
        return matrix[-1][-1]
