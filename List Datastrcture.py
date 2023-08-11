#collection = is a gropu of object withing single entities
#insertion order is preserved
#duplicates objects are allowed 
#Heterpogeneous objects are allowed
#Growable
#represent by [] notation
#index always start with 0

l=[10,20,30,'AKhilesh']
print(l)

l = list(range(0, 10000, 5))
print(l)

A='AKhilesh'
l=list(A)
print(l)

b='Learning python is very very easy'
print(b.split())

l=[10,20,30,40,[100,200,300]]
print(id(l))
print(l[0])
print(l[-1])
print(l[4])
print(l[::])
print(l[::2])
print(l[::-1])
print(l[0:3])
l[4]=[1000,2000,3000]
print(id(l))
print(l)

l=[1,2,3,4,5,6,7,8,9,]
for i in l:
	print(l)
	i=i+1
	print(i)

l=[1,2,3,4,5,6,7,8,9,]
i=0
while i<len(l):
	print(l[i])
	i=i+1
print(l)

l=[1,2,3,4,5,6,7,8,9,]
for X in l:
	if X%2==0:
		print(X)

list=["A","B","C","D"]
x=len(list)
for i in range(x):
	print(list[i],"available at positive index",i,"available at negative index",i-x)


a=[1,2,3,4,5,6,7,8,9,10]
x=len(a)
for i in range(x):
	print(a[i],"list available in positive index",i,"list available in negative index",i-x)

def f1():
	print("Hello this from function")
class student:
	def info(self):
		print("Hello this is from method")
f1()
s=student()
s.info() 

l=[10,20,30,40,50]
print(len(l))#list a function 

l=[10,20,30,40,50,10,10,10,10]
print(l.count(10))#count is a method

l=[20,30,40,50,10,10,10,10]
target=10
if target in l:
	print(target,"available at index",l.index(target))
else:
	print(target,'not available')

A=[1,2,3,4,5,6,7,8,9,]
target=1
if target in A:
	print(target,'available in list',A.index(target))
else:
	print(target,'not available')

A=[1,2,3,4,5,6,7,8,9,]
target=5
try:
	print(target,'available in list',A.index(target))
except valueError:
	print(target,'not available')


list=[]
list.append(10)
list.append(20)
list.append(30)
list.append(40)
print(list)

l=[]
for x in range(101):
	if x%10 ==0:
		l.append(x)
print(l)

l=[]
for x in range(10,101,5):
	if x%5 ==0:
		l.append(x)
print(l)

A=[1,2,3,4,5,6,7,8,9,]
A.insert(1000,100)#if we pass the index 100 we dont get error but element place in last of index
A.insert(-10,900)
print(A.index(900))
print(A.index(100))
print(A)

list=["Kedarnath","badrinath","tungnath","Madhyamaheshwar"]
list1=["mahadev","uttrakhand","Devbhumi"]
list2=['Har Har Mahadev']
adding_list=list+list1+list2
#list.extend(list1,list2)
print(adding_list)

list=["Kedarnath","badrinath","tungnath","Madhyamaheshwar"]
list1=["mahadev","uttrakhand","Devbhumi"]
list2=['Har Har Mahadev']
combined_list=list+list2
list1.extend(combined_list)
print(list1)

a=[1,2,3,4]
b=[5,6,7,8]
a.extend(b)
a.extend('AKhilesh')
b.append('Akhilesh')
print(a)
print(b)

a=[10,20,30,40,50,60,70,80,90,100]
a.remove(10)#To remove the specified elements from the list
print(a)

a=[10,20,30,40,50,60,70,80,90,100]
a.pop()#using pop remving last elemnet from the index and pop is method
a.pop(0)#if i passing the index value it will work also
print(a.pop(5))
print(a)
print(a.pop())

list=[1,2,3,4,5]
list.reverse()
print(list)

list=[100,20,45,89,9,8,7,6,5,4]
list.sort()
print(list) 

string=['AKhilesh','patil','village','kukwala','akhilesh','akhil']
string.sort()
print(string)

string=['AKhilesh','patil','village','kukwala','akhilesh','akhil']
string.sort(reverse=True)
print(string)

a=[1,2,3,4,5]
b=a
print(b)
print(a)
b.append(6)
print(b)
print(id(a))
print(id(b))

x=[1,2,3,4,5]
y=x.copy()
print(id(x))
print(id(y))

x=[1,2,3,4,5]
y=x[:]#creation of duplicates object using slice operator
y[1]=100
print(x)
print(y)

x=[1,2,3,4,5]
y=[6,7,8,9,10]
z=x+y
print(z)

a=['Dog','Cat','Rat']
b=a
b.append('mat')
print(id(a))
print(id(b))


a=['Dog','Cat','Rat']
b=['Dog','Cat','Rat']
c=['Dog','Cat','Rat']
d=a.copy()
print(id(b))
print(id(c))
print(id(d))
print(a is b)
print(id(b))

x=[50,20,30]
y=[40,90,100,120,170]
print(x>y)

x=[40,90,100,120,170]
y=[50,20,30]
print(x>y)


x=[10,20,30]
print(x)
x.clear()#to remove all element from list
print(x)


a=[[10,20,30],[40,50,60],[70,80,90]]
print(a)
print('Emement in row wise')
for r in a:
	print(r)
print('Elment is matrix type')
for i in range(len(a)):
	for j in range(len(a[i])):
		print(a[i][j],end=' ')
	print()

l=[]
for x in range(1,11):
	l.append(x*x)
print(l)

#List comphersion
#list=[expression for x in sequence if conditon]
a=[x*x for x in range(1,21)]
print(a)

a=[x+x for x in range(1,11)]
print(a)

a=[x-x for x in range(1,11)]
print(a)

a=[x*x for x in range(1,21) if x%2==0]
print(a)

a=[x*x for x in range(1,21) if x%2!=0]
print(a)

l=[2**x for x in range(1,11)]
print(l)

words=['Rohan','Nilesh','Gaju','Kalpesh']
l=[a for a in words if len(a)>6]
print(l)


n=[10,20,30,40]
m=[50,60,70,10]
o=[x for x in m if x not in n]
print(o)

words="the quick brown for jumps over the lazy dog".split()
print(words)
l=[(w.upper(),len(w)) for w in words]
print(l)



l1=[]
for x in  range(1,11):
	l1.append(x*x)
print(l1)

l=[x*x for x in range(1,11) if x%2==0]
print(l)

l=[x**2 for x in range(1,11) if (x**2)%2==0]
print(l)

vowels=['v','o','w','e','l','s','A','O']
found=[]
a="the quick brown for jumps over the lazy dog"
#B='Akhilesh'
for letter in vowels:
	if letter.lower() in vowels:
		if letter.lower() not in found:
			found.append(letter)
#print(found)
print("The number of diffrent vowels present in", a,"is:",len(found))
print(found)

t=10,20,30,40#no need for parenthesis
print(t)
print(type(t))

a=10#int type single  element
print(type(a))

a=10,#it is tuple single value ends with comma, is mandatory
print(type(a))


t=[10,20,30]
t=tuple(list)
print(t)

a=tuple(range(0,11,2))
print(a)

b=tuple(range(1,11,2))
print(b)
print(b[0])
print(b[0:4:1])

t=[10,20,30]
t1=t*4
print(t1)
