class pitilln():

    def __init__(self, n):
        self.n = n

    def givePi(self, pie):
        print('Printing value till {}th decimal '.format(self.n), end="")

        # printing using normal static syntax "{0:.2f}".format(<Variable name whoes till 6th decimal number will be print>)
        # print("{0:.6f}".format(pie))

        st = str(pie)
        # print(str[1])
        x = 0
        for i in st:

            if i == '.':
                print('{}{}'.format(i, st[x + 1:x + 1 + self.n]))
                break
            else:

                print(i, end="")
            x += 1


pi = 33.12345
print('Value of pi is {}'.format(pi))
# print (pi)
i_pitilln = pitilln(int(input("Enter value of n: ")))

i_pitilln.givePi(pi)
