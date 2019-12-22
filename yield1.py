def gensquare(n):
    for i in range(n):
        yield i*i
for x in gensquare(10):
    print (x)
    
