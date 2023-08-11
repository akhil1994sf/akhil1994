t=10,
print(t)

t=10,20,30,40
print(len(t))
print(t)

t=10,20,30,40
print(len(t))
print(t)

t=10,20,30,40
print(len(t))
print(t)

t=10,20,30,40
print(len(t))
print(t)


t=10,20,30,40,10,10,10 
print(t.index(10))
print(t.count(10))
print(t)

t=(100,10,20,30,40,10,10,10)
l=tuple(sorted(t))
print('Tuple',t)
print('list',l)

tuple1=(30,40,10,20,50)
tuple2=tuple(sorted(tuple1, reverse=True))
print(tuple1)
print(tuple2)
print(min(tuple1))
print(max(tuple2))

#packed tuple or tuple packing
a=10
b=20
c=30
d=40
t=a,b,c,d
print(t)
#Unpackaging tuple
t=(10,20,30,40)
a,b,c,d=t
print('a =',a,'b =',b,'c =',c,'d =',d)

#Tuple comprehension
l=(x*x for x in range(1,11))
print(type(t))
for x in l:
	print(x)
print(l)
print(id(l))

t=10,20,30
l=len(t)
sum=0
for x in t:
	sum=sum+x
print('The sum is',sum)
print('The sum is',sum//l)


a=10,20,30,40
b=len(a)
sum=0
for x in a:
	sum=sum+x
print('the sum is',sum)
print('the sum is' , sum// l)

s=set('Akhilesh')
print(s)

s=set(range(1,11))
for x in s:
	if x %2==0:
		print('even number',x)
	else:
		print(' odd number',x),x

a=set('AAKKHHIILLEESSHH')
print(a)

s={10,20,30}
s.add(40)
print(s)

s=set()
s.add(10)
s.add(20)
s.add(30)
s.add(40)
s.update({10})
print(s)

s={10,20}
s.update('bha'+'bu')
s.update(range(1,5),'Akhilesh')
print(s) 

a={10,20,30}
b=a.copy()
print(b)

a={10,20,30,40,50}
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())

s={10,20,30,40}
print(s.remove(40))
print(s.discard(140))
print(s)







