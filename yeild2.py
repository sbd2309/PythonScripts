import random

def say_random(low,high,n):
    for x in range(n):
        yield random.randint(low,high)
    
for i in say_random(1,10,12):
    print (i)
