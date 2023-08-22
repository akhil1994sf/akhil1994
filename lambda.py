s=lambda n:n*n
print(s(4))
print(s(5))  

l=[0,1,3,2,5,6,89,10,90]
l1=list(filter(lambda n:n%2==0,l))
l2=list(filter(lambda n:n%2!=0,l))
print(l1)
print(l2)

l=[0,2,3,4,5,6]
l1=list(map(lambda n:n*n,l))
l2=tuple(map(lambda n:n**n,l))
l3=map(lambda n:n+n,l)
print(l1)
print(l2)
print(l3)
print(type(l))


l1=[1,2,3,4,10,6,99,45]#extra number will be ignored
l2=[1,2,3,10]
l3=tuple(map(lambda x,y:x*y,l1,l2))
print(l3)


from functools import *
a=[10,40,50,100,500,1000,1500,2000]
result=reduce(lambda x,y:x+y,a)
print(result)

from functools import reduce
print(sum([10,40,50,100,500,1000,1500,2000]))

l=[1,10,24,25,29,28]
l1=list(filter(lambda n:n*n%2==0,l))
l2=tuple(map(lambda n:n*n,l))
l3=list(map(lambda n:n+n,l))
print(l1)
print(l2)
print(l3)

from functools import reduce
l=[1,10,24,25,29,28]
s=tuple(map(lambda n: n-n,l))
m=set(filter(lambda n:n+n,l))
b=str(reduce(lambda n,m:n*m,l))
print(b)
print(s)
print(m)
print(id(tuple))
print(id(map))
