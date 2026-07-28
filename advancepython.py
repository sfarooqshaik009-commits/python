#program 1 Student

# class student:
#     def __init__(self,name,age,course):
#         self.name = name
#         self.age = age
#         self.course = course

#     def display(self):
#         print(f'Name:{self.name},Age: {self.age}')
    
#     def study(self,subject):
#         print(f'{self.name} is studying {subject}')

# s=student('Farooq',22,"pfsd")

# s.display()
# s.study('python')


#program 2 employee 

# class Employee:
#     def __init__(self, emp_id, name, age, department, salary):
#         self.emp_id = emp_id
#         self.name = name
#         self.age = age
#         self.department = department
#         self.salary = salary

#     def display(self):
#         print(f"Employee ID: {self.emp_id}")
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Department: {self.department}")
#         print(f"Salary: {self.salary}")

#     def work(self, task):
#         print(f"{self.name} is working on {task}.")

#     def increment_salary(self, amount):
#         self.salary += amount
#         print(f"New Salary: {self.salary}")



# e = Employee(101, "Farooq", 22, "is Working in software Developer", 50000)


# e.display()
# e.work("Python Project")
# e.increment_salary(5000)


#program 3 area of cicle

# import math

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius ** 2

# r = float(input("Enter the radius: "))
# c = Circle(r)

# print("Area of Circle =", c.area())

# program 4 area of triangle

# class Triangle:
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         area = 0.5 * self.base * self.height
#         print(f"Area of Triangle = {area}")

# b = float(input("Enter the base: "))
# h = float(input("Enter the height: "))

# t = Triangle(b, h)
# t.area()


#############oops concept--------------
# class student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print(f'Name:{self.name},Age: {self.age}')

# s = student('name',22)
# s.display()





# class student:
#     def __init__(self,name,age,course):
#         self.name = name
#         self.age = age
#         self.course= course
#     def display(self):
#         print(f'Name:{self.name},Age: { self.age}')
#     def study(self,subject):
#         print(f'{self.name} is studying {subject}')

# s = student('name',22,"pfsd")
# s.display()
# s.study('python')



# class Employee:
#     def __init__(self, name, emp_id, salary, dept):
#         self.name = name
#         self.emp_id = emp_id
#         self.salary = salary
#         self.dept = dept

#     def display(self):
#         print(f"Name      : {self.name}")
#         print(f"Employee ID: {self.emp_id}")
#         print(f"Salary    : {self.salary}")
#         print(f"Department: {self.dept}")

#     def work(self):
#         print(f"{self.name} is working in the {self.dept} department.")


# # Create an object
# s = Employee("Arun", 101, 50000, "IT")

# # Call methods
# s.display()
# s.work()



#area of the circle-----------------

# class  circle:
#     pi = 3.14
#     def __init__(self,radius):
#         self.radius = radius
#     def area(self):
#         return circle.pi * self.radius ** 2

# c = circle(5)
# print(c.area())



#area of the triangle----------------------


# class triangle:
#     def __init__(self,base,height):
#         self.base = base
#         self.height = height
#     def area(self):
#         return 0.5 * self.base * self.height

# t = triangle(10,20)
# print(t.area())



#---------------------
# class circle:
#     def __init__(self,radius):
#         self.radius = radius
#     @classmethod
#     def change_pi(cls,value):
#         cls.pi = value

#     @staticmethod
#     def info():
#         print('this area of the circle')
#     def area(self):
#         return self.pi * self.radius ** 2
   

# c = circle(5)
# d = change_pi(6)
# print(c.area())
# circle.info()


# # single inheritances-----------------
# class parent:
#     def dispaly(self):
#         print("this is a parent class")
#     def child(parent):
#         def show(self):
#             print("this is a child class")


# obj = child()
# obj.display()
# obj.show()


######multiple inheritances---------------
# class father:
#     def display(self):
#         print("this  is a parent class")
# class mother(father):
#     def show(self):
#         print("this is a child class")
# class child(mother):
#     def show1(self):
#         print("this is a multiple inheritance")

# obj = child()
# obj.display()
# obj.show()
# obj.show1()


# product details-------------

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def display(self):
#         print(f"Product : {self.name}")
#         print(f"Price   : {self.price}")


# class Clothing(Product):
#     def __init__(self, name, price, warranty):
#         super().__init__(name, price)
#         self.warranty = warranty

#     def display1(self):
#         self.display()
#         print(f"Warranty: {self.warranty} year(s)")


# c1 = Clothing("Shirt", 2000, 1)
# c1.display1()ytg