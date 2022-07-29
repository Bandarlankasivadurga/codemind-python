x = int(input())
y = int(input())
def sel(n):
    c=0
    d=0
    e=0
    m=n
    while n>0:
        r=n%10
        if r==0:
            c+=1
            break
        e+=1
        if m%r==0:
            d+=1
        n=n//10
    if e==d and c==0:
        return True
    else:
        return False
for i in range(x,y+1):
    if sel(i)==True:
        print(i,end=' ')