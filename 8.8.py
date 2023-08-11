s1=input("entre first string")
s2=input("entre second string")
if s1==s2:
	print("Bothe string are same")
elif s1<s2:
	print("first string is smaller than second string")
else:
	print("first string is Bigger than second string")

city=input("entre city name")
list=['Hyd','Delhi','Mumbai','Banglore']
if city.strip() in list:
	print("your city is available is servicecs")
else:
	print(city,'please entre valid city name')

s=input("Entre Main String")
subs=input("Entre substrings")
try:
	n=s.index(subs)
except ValueError:
	print("substring is not faund in main string")
else:
	print("substring faund") 
