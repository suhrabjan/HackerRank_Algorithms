def sherlockAndAnagrams(s):
    count = 0
    r = 0
    i = 0
    j = r + 1
    k = 1
    l = r + 2
    x = sorted(s[i:j])
    while r < len(s) - 1:
        if x == sorted(s[k:l]):
            count += 1
        k += 1
        l += 1
        if l > len(s):
            i += 1
            j += 1
            k = i + 1
            l = j + 1
            x = sorted(s[i:j])
        if j > len(s) - 1:
            r += 1
            i = 0
            j = r + 1
            k = 1
            l = r + 2
            x = sorted(s[i:j])
    return count
