def summer_69(arr):
    flag=0
    add=0
    for i in arr:
        if (i==6):
            flag=1            
            continue
        elif (flag==1 and i==9):
            flag=0
            continue
        elif flag==0:
            add=add+i
    return add       
summer_69([2, 1, 6, 7,8])
