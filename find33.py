def check(l1):
    flag=1
    x=0
    for i in l1:
        if x==i:
            flag=0
            break
        x=i    
    if flag==0:
        return True
    else:
        return False
check([3,1,3]) 
