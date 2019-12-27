class fibo():

    def __init__(self, n):
        self.n = n
        pass

    def dofibo(self):
        a = 0
        b = 1
        for i in range(1, self.n, 1):
            print(a)
            a, b = b, a + b


i_fibo = fibo(10)
i_fibo.dofibo()
