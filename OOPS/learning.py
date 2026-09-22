# creating class and object
class Student:
    name="soumya" 
    # humne default value assign krdi jitne objects bnege sbka name soumya hi hoga. 

s1=Student()
print(s1.name)
s2=Student()
print(s2.name)

class Car:
    colour="blue"
    brand="mercedes"

s1=Car()
print(s1.colour)
print(s1.brand)

# __initt__ function
# even if we dont create any function it is always been called by python and written automatically by it. 
class Student1:
    name="soumya"
    def __init__(self):
        # self points to the new object being created jese s1 ab call kr ra h to vo s1 ko hi point kr ra hai 
        print("adding a new student")

        # hum kuch b krwa skte h iss function ke andr this is just a demo 

s3=Student1()
# yeh ( ) hum init function ke liye hi lgate hai 

# ab hume har stydent ka naam soumya nahi chahiye to what we will do is :
class Student2:
    def __init__(self,fullname):
        self.firstname=fullname
        # jab bhi me print krugi object ka naam.firstname attribute to vo fullname me jaake store hojayega aur fir humne print lgaya hai to vo print krdega jo humne pass kra hai 
        print("adding a new student")

s1=Student2("ayush")
print(s1.firstname)

class Student3:
    college="manipal"
    # since college name to same ho skta h sbke liye kyunki hum ek hi college ka database ban re h so this is class attribute
    def __init__(self,fullname,marks):       
        self.firstname=fullname
        # har object ka firstname alg hoga 
        self.marks=marks
        # har object ke marks alg honge 
        # so self.name and self.marks are instance attributes
        # jab bhi me print krugi object ka naam.firstname attribute to vo fullname me jaake store hojayega aur fir humne print lgaya hai to vo print krdega jo humne pass kra hai 
        print("adding a new student")     
s1=Student3("agarwal",44)
print(s1.firstname,s1.marks)
print(s1.college)

# defining methods

class Student4:
    def __init__(self,fullname):
        self.name=fullname

    def hello(self):
       print("hello",self.name)


s1=Student4("anika")
print(s1.name)
s1.hello()


# first method in which 3 variables are given for marks
class Student5:
    def __init__(self,name,marks1,marks2,marks3):
        self.name=name
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3
    def get_avg(self):
        total=self.marks1+self.marks2+self.marks3
        print(total)
        avg=total/3
        print(avg)

s1=Student5("keshav",10,20,30)
s1.get_avg()
        
# 2nd method where we take marks as list
class Student6:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_avg(self):
        sum=0
        for v in self.marks:
            sum=sum+v
        print("hi",self.name,"your avg score is",sum/3)

s1=Student6("saxena",[10,20,30])
s1.get_avg()

# static method
class Student7:
    def __init__(self,fullname):
        self.name=fullname

    @staticmethod
    def hello():
       print("hello")


s1=Student7("anika")
print(s1.name)
s1.hello()


# abstraction
class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self):
        self.clutch=True
        self.acc=True
        print("car started")


car1=Car()
car1.start()
# yaha mene start kri car ko aur car start hogyi.. meko ni pta chla ki phle clutch ko dabaya fir acc ko dabaya kyunki yeh class ke andr h so this is abstraction 


# encapsulation
class Student6:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_avg(self):
        sum=0
        for v in self.marks:
            sum=sum+v
        print("hi",self.name,"your avg score is",sum/3)

s1=Student6("saxena",[10,20,30])
s1.get_avg()
    
# practice question
class Account:
    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no

    def debit(self,amount):
        self.balance=self.balance-amount
        print("Rs",amount,"was debited")

    def credit(self,amount):
        self.balance=self.balance+amount
        print("Rs",amount,"was credited")

    def get_balance(self):
        return self.balance


acc1=Account(500000,272089)
print(acc1.balance,acc1.account_no)
acc1.debit(100000)
print(acc1.get_balance())
acc1.credit(100000)
print(acc1.get_balance())

# del keyword
class Student7:
    def __init__(self,name):
        self.name=name

s1=Student7("soumya")
print(s1.name)
# del s1.name attribute deleted
# del s1      object deleted
# print(s1.name)
        
# private attribute
class Account1:
    def __init__(self,account_no,account_passw):
        self.account_no=account_no
        self.__account_passw=account_passw
        

acc1=Account1("12345","abcde")
print(acc1.account_no)
# print(acc1.account_passw)
# will give an error cause now passw is private

# privat method
class Person1:
    __name="anonymous"

    def __hello(self):
        print("hello person")

        # humne isko pvt isliye banaya qki yeh class ke hi dusre function me call hora hai 

    def welcome(self):
        self.__hello()

p1=Person1()
(p1.welcome()) 

# inheritance
class Car1:
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped")

class Toyota(Car1):
    def __init__(self,brand):
        self.name=brand

class Fortuner(Toyota):
    def __init__(self,type):
        self.type=type

# multi level inheritance

car1=Fortuner("ev")
car1.start()

# multiple inheritance
class A:
    var1="welcome to class a"

class B:
    var2="welcome to class b"

class C(A,B):
    var3="welcome to class c"

c1=C()
print(c1.var1,c1.var2,c1.var3)

# super() method:
class Car1:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped")

class Toyota(Car1):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)
        # calling method of parent class

car1=Toyota("prius","electric")
print(car1.type)

# class method  
class Person2:
    name="anonymous"

    # def changename(self,name):
    #     self.name=name
    # agr me yeh krti to class ka main name attribute same hi rehta yeh object me naya attribute bn jata h name sirf usse change krta hai 
    #     Person2.name=name karu to yeh ek tareeka h cls ke attribute ko change krne ka
   
# offcially
    @classmethod
    def changename(cls,name):
        cls.name=name

c1=Person2()
c1.changename("soumya")
print(c1.name)
print(Person2.name)

# property method 
class Student11:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math

        # now we want another attribute percentage in class student 
        # self.percentage=((self.phy+self.chem+self.math)/3)+"%" 
        # one method is above one
        # here percentage depends on mraks of phy,chem,math
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"

s1=Student11(98,97,99)
print(s1.percentage)

s1.phy=86
print(s1.percentage)

# polymorphism
# python dosent have a class to create complex numbers so we will use this example.
# now if we want to add complex numbers to isko logic bhi hume hi dena pdega jese strings me concatenate predefined h vese hume yha define krna pdga 
class complex:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary

    def show(self):
        print(self.real,"i+",self.imaginary,"j")

    def __add__(num1,num2):
        newreal=num1.real+num2.real
        newimaginary=num1.imaginary+num2.imaginary
        return complex(newreal,newimaginary)

num1=complex(1,6)
num1.show()
num2=complex(3,12)
num2.show()

# num3=num1.add(num2)
# num3.show(). agr me dunder function nai bnati to aise print krwane ki zrurat hoti but now 

num3=num1+num2
num3.show()


# practice question 1
class Circle:
    def __init__(self,r):
        self.r=r

    @property
    def area(self):
        return (22/7*(self.r**2))
    @property
    def perimeter(self):
        return (2*22/7*self.r)

s1=Circle(21)
print(s1.area)
print(s1.perimeter)


#practice question 2
class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary

    def showdetails(self):
        return self.role,self.dept,self.salary

class engineer(Employee):
    def __init__(self, role, dept, salary,name,age):
        super().__init__(role, dept, salary)
        self.name=name
        self.age=age

    def showdetails(self):
        return super().showdetails(),self.name,self.age
    

e1=Employee("developer","it dept",75000)
print(e1.showdetails())
e2=engineer("developer","it dept",75000,"soumya",22)
print(e2.showdetails())

# practice question 3
class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(odr1,odr2):
        return odr1.price>odr2.price

odr1=Order("chips",10)
odr2=Order("tea",20)

print(odr1>odr2)

    
        





    
        

        


    

        


        
    


    

 






    