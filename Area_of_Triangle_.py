x,y,z = map(int,input().split())
s = (x+y+z)/2
a = ((s*(s-x)*(s-y)*(s-z))**0.5)
print('%.2f'%a)