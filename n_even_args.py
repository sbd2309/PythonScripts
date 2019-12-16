def n_even(*args):
    list1=[]
    for i in range(0,len(args),1):
        if (args[i]%2==0):
                list1.append(args[i])
    return list1    
        
                
         
n_even(5,6,7,8)
