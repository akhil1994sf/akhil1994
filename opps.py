class Collage():
    collage_name = 'D Y Patil' 
    #branch = "Mechanical"
    def my_collage_name(self):
        print(self.collage_name)
      #  print(self.branch)

class Percentage():
    my_percentage = 65
    def percentage(self):
        print(self.my_percentage)
       
class Branch():
    branch_name='Mechanical'
    def Department(self):   
        print(self.branch_name)
class Name():
    my_name = 'Akhilesh'
    def name_is(self):
        print(self.my_name)
        
class Student(Collage, Percentage, Branch, Name):
    def student_information(self):
        print(self.my_name)

Student = Student()
Student.student_information()
Student.my_collage_name()
Student.Department()
Student.percentage()
Student.name_is()





#opps principle
class User():
	age=20
	name='Akhilesh'
	mobile_number=7798731221
	def first_name(self):
		print(self.age)
		print(self.name)
		print(self.mobile_number)

class Employes(User):
	def salary(self):
		print(self.salary)
		print(self.name)
		print(self.mobile_number)
		pass
obj1= User()
#obj2= User()   

obj=Employes()
obj.age
obj.name
obj.mobile_number
print(obj)


class Student:
    Student_name = 'Akhilesh'

    def display_name(self):
        print(self.Student_name)

class Collage(Student):
    collage_name = 'D Y Patil'

    def display_collage_name(self):
        print(self.collage_name)

class Percentage:
    Student_percentage = 80

    def display_percentage(self):
        print(self.Student_percentage)

# Create objects
student = Student()
collage_student = Collage()
percentage = Percentage()

# Access methods
student.display_name()
collage_student.display_collage_name()
percentage.display_percentage()

'''
class Collage(Student_name):
	
		Student_name='Akhilesh'
		collage_name='D Y Patil'

def collage_name(self):
		print(self.name)

class Student():
		def Student_name(self):
			print(self.Student_name)

class Percentage():
		def percentage(self):
			print(self.Student_percentage)

obj1 = Collage(Student,Percentage)
obj.Student_name
'''


