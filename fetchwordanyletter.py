st = 'Print only the words that start with s in this sentence'
st=st.lower()
print (st)
count=0
for i in st:
    if (i==" "):
        count +=1
print ("The number of space are {0}".format(count))   
word_list=st.split()
list_s=[]
for i in word_list:
    if (i.startswith('s')):
        list_s.append(i)
print (list_s)  
for i in word_list:
    string=i
    for j in string:
        if j=='s':
            print (i)
            break
        else:
            break
