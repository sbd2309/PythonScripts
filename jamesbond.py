def spy_game(l2):
    flag=0
    james=""
    for i in l2:
        if i==0 or i==7:
            james=james+str(i)
            if james=='007':
                flag=1
                break
    if (flag==1):
        return True
    else:
        return False
spy_game([1,0,2,0,7,7])
