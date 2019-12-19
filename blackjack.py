def blackjack(a,b,c):
    if a<=11 and b<=11 and c<=11:
        add=a+b+c
        if add<=21:
            return add
        elif a==11 or b==11 or c==11:
            return add-10
        else:
            return "BUST"
print(blackjack(5,6,7))
