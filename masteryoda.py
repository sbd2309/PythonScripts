def rev_sen(st):
    list1=st.split()
    list2=[]
    index=0
    index1=-1
    for i in list1:
        list1[index]=i[::-1]
        list2.append(list1[index1])
        index1 =index1 + (-1)
        index +=1
    return list2
rev_sen('I am a good boy')
