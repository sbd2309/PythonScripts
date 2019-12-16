x=371
count=0
num=x
num1=x
#print (num)
while num>0:
    count = count + 1
    num=int (num/10)
#print (count)
s=0
pallindrome=1
while num1>0:
    rem=int (num1%10)
    for i in range (1,count+1,1):
        pallindrome=pallindrome*rem
    s=s+pallindrome
    pallindrome=1
    num1=int(num1/10)
if (s==x):
    print("Amstrong")
else:
    print ("Amstrong")    
    
