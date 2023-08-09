'''
#with slice operator
s=input('Entre some string')
print('Charecters at even position:',s [::2])
print('charecter at odd position',s [1::2])

#based on the index
s=input("entre some string")
i=0
print("The charecter is even position")
while i<len(s):
	print(s[i],end=',')
	i=i+2
print()
print("The charecter is odd position")
while i<len(s):
	print(s[i],end=',')
	i=i+2

def function(s):
	s1=s2=output=''
	for x in s:
		if x.isalpha():
			s1=s1+x
		else:          
			s2=s2+x
input_string='A4B3C5'
s1,s2 = function(input_string)
print(s1)
print(s2)
'''
def separate_characters(s):
    s1 = s2 = ''
    for x in s:
        if x.isalpha():
            s1 = s1 + x
        else:
            s2 = s2 + x
    return s1, s2  
input_string = 'A4B3C5'
result_s1, result_s2 = separate_characters(input_string) 
print(result_s1)  
print(result_s2)

s='AKHIL5588LESH'
s1=s2=output=''
for x in s:
	if x.isalpha():
		s1=s1+x
	else:
		s2=s2+x
for x in sorted(s1):
	output=output+x
for x in sorted(s2):
	output=output+x
print(output)

a='AKhileshPatil5848Kukawal'
s1=s2=output=''
for x in a:
	if x.isalpha():
		s1=s1+x
	else:
		s2=s2+x
for x in sorted(s1):
	output=output+x
for x in sorted(s2):
	output=output+x
print(output)

a='AKhileshPatil5848Kukawal'
s1=s2=output=''
for x in a:
	if x.isalpha():
		s1=s1+x
	else:
		s2=s2+x
output=s1+s2
print(sorted(output))

x='KJJFDHVI54645NKJBK'
output=''
for x in s:
	if x.isalpha():
		output=output+x
		previous=x
	else:
		newch=chr(ord(previous)+int(x))
		output=output+newch
print(output)

s1='Akhilesh'
s2='Darshana'
output=''
i=j=0
while i<len(s1)or j<len(s2):
	output=output+s1[i]+s2[j]
	i=i+1
	j=j+1
print(output)

s1='Akhilesh'
s2='Darshana JADHAV'
output=''
i=j=0
while i<len(s1)or j<len(s2):
	if i<len(s1):
		output=output+s1[i]
		i=i+1
	if j<len(s2):
		output=output+s2[j]
		j=j+1
print(output)	 

str='ABCABCDABCDEF'
l=[]
for x in str:
	if x not in l:
		l.append(x)
print(''.join(l))

a='abcdabcdefghabvgdf'
print(''.join(set(a)))
#remove duplicate and remove occurancecs
a='AABBCCDDEEFF'
print(''.join(set(a)))

d={100:'akhi',200:'bhanu'}
print(d.keys())
print(d.values())
d.update({300:'Dajbhau'})
d[400]='dadasaheb'
print(d)
for k,v in d.items():
	print('{}=={}'.format(k,v))

d={'a':1,'a':1,'a':3}
for x in d:
	if x not in d.keys():
		d[x]=1
	else:
		d[x]=d[x]+0
print(d)

d={}
print(type(d))

name='AKhilesh'
age=29
salary=15000
print("{}'s age is {} and his salary is:{}".format(name,age,salary))
print("{0}'s age is {1} and his salary is:{2}".format(name,age,salary))
print("{x}'s age is {y} and his salary is:{z}".format(z=salary,y=age,x=name))

#write a programme to reverse a given string
a='Akhilesh'
#print(a[::-1])
print("".join(reversed(a)))
print(reversed(a))# it will reteurn object

a=input('Entre some string')
i=len(a)-1
output=''
while i>=0:
	output=output+a[i]
	i=i-1
print(output)

s=input('Entre some string')
l=s.split()
l1=[]
i=len(l)-1
while i>=0:
	l1.append(l[i])
	i=i-1
print(l1)
output=''.join(l1)
print(output)

s=input("entre some string")
l=s.split()
l1=[]
for x in l:
	l1.append(x[::-1])
output=''.join(l1)
print(output)

