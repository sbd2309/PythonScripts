class pfactor():

    def __init__(self):
        pass

    def find_factor(self, n):
        print("Prime Factors are: ", end="")
        for i in range(2, n, 1):
            if n % i == 0:
                flag = 1
                for x in range(2, i, 1):
                    if i % x == 0:
                        flag = 0
                        break
                if flag == 1:
                    print('{},'.format(i), end="")


i_pfactor = pfactor()
i_pfactor.find_factor(int(input("Enter Any Number: ")))
