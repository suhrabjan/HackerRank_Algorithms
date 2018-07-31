def bonAppetit(bill, k, b):
    estimated = (sum(bill) - bill[k]) // 2
    print ('Bon Appetit' if estimated == b else b - estimated)
