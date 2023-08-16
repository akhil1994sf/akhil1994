#2 types of function
#1)predefined function also known as inbuild
#==>print(),len(),eval(),input(),id(),sorted()
#2)user defined function also custom function

def wish(name,age,village):
	print('Good Morning',name)
	print('Good Afternoon',name,age)
	print('Good Night',name,village)
wish('vedant',30,'Kukaval')

def sequre(x):
	print(' the sequre of {} is {}'.format(x,x*x))
sequre(10)
sequre(20)

def add(a,b):
	return a+b
result=add(10,20+30)
print("the sum is ",result)
print("the sum is ",add(100,200))

def f1():
	print("Hello")
print(f1())

def evenodd(n):
	if n%2==0:
		print('even nmubr {}'.format(n))
	else:
		print('Odd number {}'.format(n))
evenodd(10)

def fact(n):  
	result=1           
	while n>=1:            
		result=result*n  
		n=n-1            
	return result            
for i in range(1,10):
	print("The factorial {} is {}".format(i,fact(i)))
fact(10)

def cal(a,b):#positinal arguments
	sum=a+b
	sub=a-b
	mul=a*b
	div=a/b
	return sum,div,mul,sub   #sequence belong from return
t=cal(100,50)
print("The Result are:")
for x in t: 
	print(x)


#positinal Arguments
#Keyword Arguments
#Default Arguments
#Variable lenght Arguments
#1)positinal arguments=
def fuction(a,b):
	sum=a+b
	print(sum)
fuction(100,50)

#2)Keyword Arguments
def wish(name, msg):
	print('hello',name,msg)
wish(name='Akhil',msg='Good Morning')#positinal
wish(msg='Akhil',name='Good Morning')#keywords 
wish('Akhil',msg='Good Morning')#Default arguments
#wish(msg='Good Morning','Akhil') positinal arguments shud be begins only

def wish(name="Guest"):
	print('Hello',name,'Good evining')
wish()

def wish(name=''):
	print('Hello',name,'Good Morning')
wish('Akhilesh')

def school(marks, age, stdname='Akhilesh',msg='please focus on study'):
	print('marks is',marks)
	print(stdname)
	print(msg)
	print('Age is',age)
school(80,30,'bhanu')


def sum(*n):
	result=0
	for x in n:
		result=result+x
	print("the sum is ",result)	
sum()
sum(10,20)
sum(10,20,30)
sum(10,20,30,40)
sum(10,20,30,40,50)

def sum(name,*n):
	result=0
	for x in n:
		result=result+x
	print("the sum is ", name, result)	
sum('Akhil')
sum('gautam',10,20)
sum('gaurav',10,20,30)
sum('Ramgopal',10,20,30,40)
sum('charan', 10,20,30,40,50)

def sum(*n,name):
	result=0
	for x in n:
		result=result+x
	print("the sum of ", name, result)	
sum(name='Akhil')
#sum(name='gautam',10,20)#positional argument follows keyword argument
sum(10,20, name='gautam')
sum(10,20,30, name='gaurav',)
sum(10,20,30,40,name='Ramgopal',)
sum(10,20,30,40,50,name='charan', )

def display(**kwargs):
	print('Record Information')
	for k, v in kwargs.items():
		print(k,'....',v)
display(name='Akhilesh',marks=95,age=30,status='single')
display(name='hrushikesh',marks=55,age=33,status='married')


