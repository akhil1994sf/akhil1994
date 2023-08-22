def patil(function):
	def inner(name):
		print("patil (my) is flow of execution")
		function (name)
	return inner
def patil1(function):
	def inner(name):
		print('patil (my) is execution)')
		function (name)
	return inner
@patil
@patil1
def wish(name):
	print("hello",name,"good morning")
wish('Vishnu')


def patil(function):
	def inner(name):
		print("@patil decor is execution")
		function (name)
	return inner
def patil1(function):
	def inner(name):
		print('@patil 1 decor is execution first')
		function (name)
	return inner
@patil1
@patil
def wish(name):
	print("hello",name,"good morning")
wish('ak')

def decor1(function):
	def inner():
		x=function()
		return x*x
	return inner
def decor2(function):
	def inner():
		x=function()
		return 2*x
	return inner
decor2
@decor1
def num():
	return 10
print(num())

"""
import random
import time
names=['sunny','bunny','chinny','gaurav']
subjects=['paython','java','blockchain']

def people_list(num_people):
	result=[]
	for i in range(num_people):
		person={
		'id': i,
		'name': random.choice(names),
		'subject':random.choice(subjects)
		}
		result.append(person)
	return result
def people_generator_result(num_people):
	for i in range(num_people):
		person={
		'id': i,
		'name': random.choice(names),
		'major':random.choice(subjects)
		}
	yield person
t1= time.time()
prople_list_result=people_list(100000)
t2=time.time

t1=time.time
people_generator_result = list(people_genrator(10000000))
t2=time.time()
print('people_generator{}'.format(t2-t1))
t1 = time.time()  # Use time.time() instead of time.clock()
people_generator_result = list(people_generator(10000000))  # Convert generator to list for fair comparison
t2 = time.time()  # Use time.time() instead of time.clock()
print('people_generator took {}'.format(t2 - t1))
"""