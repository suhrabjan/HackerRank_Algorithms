def kangaroo(x1, v1, x2, v2):
    if v2 - v1 == 0:
        return 'NO'
    else:
        division, remainder = divmod((x1 - x2), (v2 - v1))
        if division > 0 and remainder == 0:
            return 'YES'
        else:
            return 'NO'
