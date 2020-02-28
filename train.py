n = int(input())
l=[]
for i in range (1,n+1,1):
    l.append(input())
for i in l:
    print(i)

while len(l)>1 and len(l)<4:
    print("OK")