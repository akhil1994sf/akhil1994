d={'A':100,'B':200}
del d['A']
print(d)

d=dict([('A',100),('B',200),('C',300)])#With list of tuple using dict #List of tuple
print(d)

d=dict((('A',100),('B',200),('C',300)))#With list of tuple of tuple
print(d)

d=dict({('A',100),('B',200),('C',300)})#with list of set 
for i in d.keys():
	print(i)
print(d)
print(d.keys())
print(d.values())
print(len(d))
print(d.get('A'))
print(d.get('D',200))
print(d)

d=dict(((100,'Akhilesh'),(200,'malak')))
print(d)
print(d.pop(100))
print(d)
print(d.popitem())
print(d)

d=dict(((100,'Akhilesh'),(200,'malak')))
for k,v in d.items():
	print(k,'....',v)

a={'AKhilesh':100,'Nilesh':200}
for k,v in a.items():
	print(k,'....',v)
print(d.popitem())
print(d)
print(d.setdefault(300,'kalpesh'))
print(a)

dict={100:'durga',200:'ravi',300:'shiva'}
print(dict.setdefault(400,'sunny'))#if key is not there it will consider new k and v
print(dict)
dict.update({500:'maddhu'})
print(dict)
d1={"A":"Apple",'B':"Ball"}
dict.update(d1)
print(dict)

a={'A':100,'B':200,'C':300,'D':400}
s=sum(a.values())
print(s)

a={100:'A',200:'B',300:'C',400:'D'}
s=sum(a.keys())
print(s)

word="radha vallabh shree hari vansh"
d={}
for x in word:
	d[x]=d.get(x,0)+1
print(d)
for k,v in sorted(d.items()):
	print("{} occured {} times".format(k,v))

#WAP numbe of occurances in vowel
word=" Radha vallabha shree hari vansh"	
d={}
vowls={'a','e','i','o','u'}
for x in word:
	if x in vowls:
		d[x]=d.get(x,0)+1
		print(d)
for k,v in sorted(d.items()):
	print("{}  occured {} times".format(k,v))

N=10
d={}
for i in range(N):
	name='AKhilesh'
	marks=50
	d[name]=marks
print(d)
for k,v in sorted(d.items()):
	print('{} occured {} marks'.format(k,v))

squares={x:x*x for x in range(1,6)}
print(squares)

double={x:2*x for x in range(1,10)}
print(double)










