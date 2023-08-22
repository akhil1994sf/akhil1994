#even odd using list comphersion
l=[1,2,3,4,5,6,7,8,9,10]
even=[x for x in l if x %2==0]
odd =[x for x in l if x %2!=0]
print(even)
print(odd)

l=[x*x for x in range(1,11) if x%2==0]
print(l)
l=[x*x for x in range(1,11) if x%2!=0]
print(l)

a=[1,2,3]
print(type(a))

word="radha vallabh shree hari vansh"
d={}
for x in word:
	d[x]=d.get(x,0)+1
print(d)

s="mahesh akhilesh vishnu"
d={}
for i in s:
	d[i]=d.get(i,0)+1
print(d)

s=['rohan rohan patil',10,10,2,5,55,55,44]
d={}
for i in s:
	d[i]=d.get(i,0)+1
print(d)
for k,v in d.items():
	print('{} and {}'.format(k,v))


l=[1,2,3,4,1,2,3,4]
d={}
for z in l:
 	d[z]=d.get(z,0)+1
print(d)
for k,v in (d.items()):
	print("{} occured {} times".format(k,v))
#duplicates using method
duplicate = [1, 2, 3, 4, 1, 2, 3, 4]
unique_list = list(set(duplicate))
print(unique_list)


#remove duplicate from set
list=[10,10,15,15,20,20]
unique_set= set()
for item in list:
    unique_set.add(item)
print(unique_set)


#find duplicate and stored in another list
a=[1,1,3,2,4,5,6,7,8,8,9,9]
b=[]
for i in a:
	if i not in b:
		b.append(i)
print(sorted(b))
print(a)

#vowls
s='akhilesh bhimrao desale'
d={}
vowls={'a','e','i','o','u'}
for x in s:
	d[x]=d.get(x,0)+1
print(d)
for k,v in sorted(d.items()):
	print('{} occured {}'.format(k,v))

#default arguments
a=10
b=20
def function(x,y=50):
	print('x',x)
	print('y',y)
function(a,b)

#default arguments
a=10
b=20
c=30
def function(*args):
	print(args)
function(a,b,c)

#default arguments
a=10
b=20
c=30
d={"name":'radha'}
e='string'
def function(*args):
	for i in args :
		print(i)
	#print(args)
function(a,b,c,d,e)

d={'name','Akhilesh'}
def func(*args,d={"key","demo"}):
	print(args)
	
func(1,2,3,4,5,20)
#default arguments
def test(a,v=30):
	print(a+v)
test(3)
test(4,20)
test(100)

demo=(3,2)
demo=(2+3)
def test(a,b=3):
	print(a+b)
test(3,2)
test(2,3)

#deepcopy
from copy import *
a = [10, 20, 30, 40, [10, 20]]
b = deepcopy(a)
print(a)
print(b)

import copy
a=[1,2,3,4,[10,20,30,40]]
b=copy.deepcopy(a)
b[4][0]=200
print(a)
print(b)

import copy
l = [1, 2, 3, 4, [10, 20, 30, 40]]
m = copy.copy(l)
l[4][0] = 100
print("Original List:", l)
print("Shallow Copied List:", m)
#deepcopy
import copy
l = [1, 2, 3, 4, [10, 20, 30, 40]]
m = copy.deepcopy(l)
m[4][0] = 100
print(l)
print(m)
l.append([1,2,3,4])
print(l)
#shallowcopy
import copy
c = [1, 2, 3, 4, [10, 20, 30, 40]]
d = c.copy()
d[4][0] = 500
print(c)
print(d)
c.append([1,2,3,4])
print(c)

#del using slicing
a = [10, 20, 30, 40, 50]
del a[1:4:1]
print(a)

b=['str',10,20,40,50,60]
del b[:]
print(b)

c=['str',10,20,40,50,60]
del c[1:4:1]
print(c)

d=['akhilesh',10,20,[10,20,30]]
del d[3]
print(d)
del d[:]
print(d)

e=[1,2,3,4,5,6,7,8,9]
del e[1:8:1]
print(e)

a=[1,2,3,4,[1,2,3,4]]
del a[2:4:1]
print(a)

#Dictinary
d={'A':100,'B':200}
del d['A']
print(d)

def odd_even(number):
    match number % 2:
    	#match number 0==0:
        case 0:
            print(f"{number} is even.")
        case 1:
            print(f"{number} is odd.")
        case 2: 
        	print(f'''"{Number}"''')
print(type(odd_even))
odd_even(10)
odd_even(11)
odd_even(1)
odd_even(0)

num=1234567890
num_str=str(num)
for i in num_str:
	i=int(i)
	if i % 2 == 0:
		print('even number',i)
	else:
		print('odd number',i)
print(num)

#odd even
my_range=range(1,20)
total = sum(my_range)
for i in my_range:
	if i%2==0:
		print(' even number',i)
	else:	
		print(' odd number',i)
print(total)

#sqre of range
for i in range(1,10):
	print('{} of square is {}'.format(i,i*i))
print(id(format))

#check string in list
l=[1,2,3,4,5,'pune']
if 'pune' in l:
	print('string is there in list')
else:
	print('string is not there in list')

a=['Akhilesh','bhimrao','patil']
b=[]
for x in a:
	if 'a' in x:
		b.append(x)
print(b)



#char in string
x='Akhilesh bhimrao patil'
y={}
for i in x:
	y[i]=y.get(i,0)+1
print(y)
for k,v in sorted(y.items()):
	print('{} occured {}'.format(k,v))

#list comprehension
a=[1,2,3,4,5,6,78,7,8,9,99,100]
b=[x for x in a if x % 2 == 0]
c=[x for x in a if x % 2 != 0]
print(c)
print(b)

#namespace

global_variable = 40# Global namespace
def my_function():
    local_variable = 10 # Local namespace
    print(local_variable)
my_function()
print(global_variable)

#genrator
def even_odd_generator(start, end):
    for number in range(start, end + 1):
        if number % 2 == 0:
            yield "Even", number
        else:
            yield "Odd", number
start = 1
end = 10

for result, number in even_odd_generator(start, end):
    print(f"{number} is {result}.")

#hoe to write return
a = 1234567890
reversed_a = int(str(a)[::-1])
print("Original number:", a)
print("Reversed number:", reversed_a)

num=1234567890
num_str=str(num)
for digit in num_str:
	digit=int(digit)
	if digit % 2 == 0:
		print('even number',digit)
	else:
		print('odd number',digit)
print(num)

#static function
class test():
	test=10
	@staticmethod
	def static_function(self):
		print(self.test)
		self.test=20
		print(self.test )
		print('hi this is instance')
	print(test)
obj=test()
obj.static_function(test)

#class function
class Test():
	test=10
	@classmethod
	def class_function(cls):
			print(cls.test)
			cls.test=50
			#print(cls.test)
			print('Hi this is from  Instance')
			print(cls.test)
	def object_instance_function(self):
		print(self.test)
obj=Test()
obj.class_function()
obj.object_instance_function()


#palindrome string
string = 'civic'
if string == string[::-1]:
    print("The letter is a palindrome")
else:
    print("The letter is not a palindrome")

#to check number available in list
A=[1,2,3,4,5,6,7,8,9,]
target=5
try:
    print(target,'available in list',A.index(target))
except ValueError:
    print(target,'not available')

#To add element to list upto 100 which are divisuable by 10
l=[]
for x in range(0,101,10):
    if x%10 ==0:
        l.append(x)
print(l)

#insert argument in list
A=[1,2,3,4,5,6,7,8,9,]
A.insert(0,100)
print(A) 

#compairing 2 list
x=[50,20,30]
y=[40,90,100,120,170]
print(x>y)

#positive number
num =-2
if num > 0:
   print('Positive')
elif num == 0:
   print('Zero')
else:
   print('negative number')

#prime number
num = 500
if num < 2:
    print(num, 'This is not a prime number')
else:
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num, 'This is a prime number')
    else:
        print(num, 'This is not a prime number')

#palidrome
s = "civic" 
s1 = ""
for i in s:
    s1 = i + s1
if (s == s1):
    print("String is palindrome")
else:
    print("String is not palindrome")

#Fibonacci
a= 10
n1, n2 = 0 , 10
print('Fibonaccie',n1,n2,end=' ')
for x in range(2,a):
	n3 = n1 + n2
	n1=n2
	n2=n3
	print(n3,end = ' ')
print()

#divisiors 
def printDivisors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")

# Driver method
print("The divisors of 100 are: ")
printDivisors(150)

#leap year
year = 2000
if (year%400 == 0) or (year%4==0 and year%100!=0):
    print("Leap Year")
else:
    print("Not a Leap Year")


num=14
if (num %2==0):
	print('even')
else:
	print(odd)


