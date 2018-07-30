def countApplesAndOranges(s, t, a, b, apples, oranges):
    _apples = [apple for apple in apples if s <= apple + a <= t]
    _oranges = [orange for orange in oranges if s <= orange + b <= t]
    print(len(_apples))
    print(len(_oranges))
