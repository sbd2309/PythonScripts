def macdonald(st):
    new_str=""
    index=0
    for i in st:
        if index==0:
            new_str=new_str+i.upper()
            index +=1
        elif index==3:
            new_str=new_str+i.upper()
            index +=1
        else:
            new_str=new_str+i
            index +=1
    print (new_str)        
macdonald('macdonald') 
