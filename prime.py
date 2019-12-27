def prime():
    for i in range(2, 10, 1):
        flag = 0
        for x in range(2, i, 1):
            if i % x == 0:
                flag = 1
                break
        if flag == 0:
            print(i)


prime()
