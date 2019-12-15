for i in range (1,100,1):
    if (i%3==0 and i%5==0):
        print ("{} is FizzBuzz".format(i))
    elif (i%3==0):
        print ("{} is Fizz".format(i))
    elif (i%5==0):
        print ("{} is Buzz".format(i))
