# class Student:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Student("Rishav", 18)
# p1.name = 'Vinay'

# print(p1.name)
# print(p1.age)

# class Person:
#     def __init__(self, name, sex, profession):
#         # data members (instance variables)
#         self.name = name
#         self.sex = sex
#         self.profession = profession

#     # Behavior (instance methods)
#     def show(self):
#         print('Name:', self.name, 'Sex:', self.sex, 'Profession:', self.profession)

#     # Behavior (instance methods)
#     def work(self):
#         print(self.name, 'working as a', self.profession)


# # create object of a class
# Rishav = Person('Rishav', 'male', 'TopG')

# # call methods
# Rishav.show()
# Rishav.work()        

# class car:
#     #Instance variables - value varies from obj to obj
#     def __init__(self):
#         self.company = "BMW"
#         self.mileage = 10

# car1 = car()
# car2 = car()

# print(car1.mileage)
# print(car2.mileage)

class student:

    def __init__(self, python, web, math):

        self.subject1 = python
        self.subject2 = web
        self.subject3 = math

    def avg(self):
        return ((self.subject1+self.subject2+self.subject3)/3)

    def set_marks(self, value):
        self.subject1 = value

    def get_subject1(self):
        return self.subject1 = value

    #Below is a class method
    @classmethod
    def collegedetail(cls):
        return cls.colleName    



student1 = student(5,8,9)
student2 = student(9,9,9)
print(student1.avg()) 
print(student2.avg())      

        




        
    
