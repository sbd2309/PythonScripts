import random


class findNumber():
    def __init__(self, n):
        self.n = n

    def findnumber(self):
        x = random.randint(1000, 5000)
        while True:
            if self.n < x:
                print("Greater!")
                self.n = int(input("Enter: "))
            elif self.n > x:
                print("Lower")
                self.n = int(input("Enter: "))
            elif self.n == x:
                print('You Got ME!')
                break


i_fn = findNumber(int(input("Enter a Number:")))
i_fn.findnumber()
