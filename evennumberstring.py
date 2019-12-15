st = 'Print every word in this sentence that has an even number of letters'
list_word=st.split()
list_word1=[]
for ixx in list_word:
    length=len(ixx)
    #print (length)
    if (length%2==0):
        list_word1.append(ixx)
        print ("Even")
#list_word1  
