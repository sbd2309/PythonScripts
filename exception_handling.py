class eh1:
    def __init__(self):
        pass
        
    def texecption(self,l1):
        try:
            for i in l1:
                print (i**2)
        except:
            print ('Exception Cached!')
        else:
            print ('You provided a Integer list !')
        finally:
            print ('I will run at any cost!')
    def texecption1(self,x,y):
        try:
            z=x/y
        except:
            print ('Value of y is {}'.format(y))
        else:
            print ('Value of y is {}'.format(y))
        finally:
            print ('We are over now.')
            
    def texecption2(self, n):
        while True:
            try:
                print (n**n)
            except:
                print ('Entered number must be a digit!')
            else:
                print ('Exceuted as the enterted number is a digit')
                break
            finally:
                print ('Another Chance...or may be you are correct!')
                break

i_eh1=eh1()
#i_eh1.texecption(['a','b','c'])
#i_eh1.texecption1(5,0)
i_eh1.texecption2(input('Enter a number'))
