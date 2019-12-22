def all_math(multi):
    def sum():
        return 10+20
    
    multi()
    
    def sub():
        return 20-10
    
    catch=sum
    #return catch
    catch2=sub
    return catch2
@all_math
def multi():
    print (9*10)

#result=all_math(multi)
#print (result())
