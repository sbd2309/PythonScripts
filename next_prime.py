class nextprime():

    def __init__(self):
        pass

    def find_near_prime(self, n):
        for i in range(n + 1, n + 100, 1):
            flag = 0
            for x in range(2, i, 1):
                if i % x == 0:
                    flag = 1
                    break
            if flag == 0:
                print(i)
                break


i_nextprime = nextprime()
st = 'YES'
while st.capitalize() == 'Yes':
    n = int(input("Enter Any Number :"))
    i_nextprime.find_near_prime(n)
    st = input("Continue (Yes/No)")
