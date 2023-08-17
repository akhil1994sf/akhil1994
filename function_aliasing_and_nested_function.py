def f1():
	print('Hello')
print(f1)#function also object internally
print(id(f1))
#print is an also object eveything treated as object only
print(id(print))#address value  
print(id(id))

def wish(name):#function aliasing
	print('Hey how are you',name)
greeting=wish
print(id(wish))
print(id(greeting))
wish('Akhilesh')
greeting('sunny')
del wish
greeting('jjj')#if u remove one refrance another is working
#wish('hhhh')

def wish(name):#function aliasing
	print('Hey how are you',name)
greeting=wish
del wish

def akhi(name):
	print('Akhilesh')
akhi('Akhilesh')
hello = akhi
kumar = akhi
print(id(hello))
print(id(akhi))
print(id(kumar))
del kumar
print(id(akhi))

#Nested function
def outer():
	print('outer function started')
	def inner():
		print('inner function started')
	inner()
outer()

def d():
	def inner(a,b):
		print('The sum',a+b)
		print('The avarage',a+b/2)
	inner(10,20)
	inner(30,20)
	inner(100,50)
d()
#inner(500,200) its a direct entity its a part of d we cannot call outside of d

