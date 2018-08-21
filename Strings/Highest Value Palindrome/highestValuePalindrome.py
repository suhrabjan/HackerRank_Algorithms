def highestValuePalindrome(s, n, k):
    s = [int(i) for i in s]
    if n % 2 == 0:
        A = s[:n // 2]
        B = s[n // 2:][::-1]
        C = []
    else:
        A = s[:n // 2]
        B = s[n // 2 + 1:][::-1]
        C = [s[n // 2]]
    temp = [1 for i, j in zip(A, B) if i != j]
    minChanges = len(temp)
    if minChanges > k:
        return '-1'
    else:
        for i in range(len(A)):
            if k - minChanges > 1:
                if A[i] != B[i]:
                    minChanges -= 1
                if A[i] != 9:
                    A[i] = 9
                    k -= 1
                if B[i] != 9:
                    B[i] = 9
                    k -= 1
            elif k - minChanges == 1:
                if A[i] != B[i]:
                    if A[i] != 9 and B[i] != 9:
                        A[i] = 9
                        B[i] = 9
                        minChanges -= 1
                        k -= 2
                    elif A[i] == 9 and B[i] != 9:
                        B[i] = 9
                        k -= 1
                        minChanges -= 1
                    elif A[i] != 9 and B[i] == 9:
                        A[i] = 9
                        k -= 1
                        minChanges -= 1
            else:
                if A[i] > B[i]:
                    B[i] = A[i]
                    minChanges -= 1
                    k -= 1
                if A[i] < B[i]:
                    A[i] = B[i]
                    minChanges -= 1
                    k -= 1
        if k > 0 and len(C) > 0:
            C[0] = 9

    return ''.join(map(str, (A + C + B[::-1])))
