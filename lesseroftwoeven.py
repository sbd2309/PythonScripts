def less(a,b):
    if a%2==0 and b%2==0:
        if a<b:
            return a
        else:
            return b
    elif a%2==0 or b%2==0:
        if a>b:
            return a
        else:
            return b
less (2,5)
