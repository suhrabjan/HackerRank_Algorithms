def divisibleSumPairs(n, k, ar):
    ar_result = [[ar[i], ar[j]] for i in range(len(ar)) for j in range(i + 1, len(ar)) if (ar[i] + ar[j]) % k == 0]
    return len(ar_result)
