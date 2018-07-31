def migratoryBirds(ar):
    li = [0, 0, 0, 0, 0, 0]
    for i in ar:
        li[i] += 1
    return li.index(max(li))
