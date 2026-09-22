# 1.
class Student:
    total_students=0
    def __init__(self,name,rollno,branch,marks):
        self.name=name
        self.rollno=rollno
        self.branch=branch
        self.__marks=marks
        Student.total_students+=1

    @classmethod
    def count_students(cls):
        return ("total students:",cls.total_students)

    

    def displaydetails(self):
        return ("name:",self.name,"roll no:",self.rollno,"branch:",self.branch,"marks:",self.marks)


    @staticmethod
    def marks(marks):
        return marks >=0 and marks<=100

    @property
    def marks(self):
        return self.__marks

    
    def calculategrade(self):
        if self.marks >90:
            print("A*")
        elif self.marks <90 and self.marks>70:
            print("A")
        elif self.marks <70 and self.marks>50:
            print("B")
        else:
            print("fail")
        

            
s1=Student("soumya",229301103,"cse core",78)
print(s1.displaydetails())
s1.calculategrade()
print(s1.count_students())

# 2.
class Bankaccount:
    total_accounts=0
    def __init__(self,accountholder,balance):
        self.accountholder=accountholder
        self.__balance=balance
        Bankaccount.total_accounts+=1

    @classmethod
    def display_total_accounts(cls):
        print("Total accounts:", cls.total_accounts)

    def withdraw(self,amount):
        if self.validate_amount(amount) and amount <= self.__balance:
            self.__balance=self.__balance-amount
            return self.__balance
        else:
            return("invalid")
    def deposit(self,amount):
        if self.validate_amount(amount) :
            self.__balance=self.__balance+amount
            return self.__balance
        else:
            return ("invalid")

    

    @staticmethod
    def validate_amount(amount):
        return amount > 0 

    @property
    def readbalance(self):
       return self.__balance

a1=Bankaccount("soumya",20000)
print(a1.withdraw(-500))
print(a1.deposit(20000))
print(a1.readbalance)
Bankaccount.display_total_accounts()

# 3.
class Employee:
    def __init__(self, name, emp_id, base_salary):
        self.name = name
        self.emp_id = emp_id
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary


class Developer(Employee):
    def __init__(self, name, emp_id, base_salary, programming_language, bonus):
        super().__init__(name, emp_id, base_salary)
        self.programming_language = programming_language
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus


class Manager(Employee):
    def __init__(self, name, emp_id, base_salary, team_size, bonus):
        super().__init__(name, emp_id, base_salary)
        self.team_size = team_size
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus



e1 = Employee("Rahul", 101, 50000)
d1 = Developer("Soumya", 102, 60000, "Python", 10000)
m1 = Manager("Aman", 103, 80000, 10, 20000)

employees = [e1, d1, m1]

for e in employees:
    print(e.name, ":", e.calculate_salary())

# 5.
class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self):
        self.clutch=True
        self.acc=True
        self.brk=True
        print("vehicle started")

    @staticmethod
    def verifyyear(model):
        return model == 2025
    


class Bike(Vehicle):
    def __init__(self, brand, model,colour):
        self.colour=colour
        super().__init__(brand, model)

    def start(self):
         self.clutch=True
         self.acc=True
         self.brk=True
         print("bike started")

class Car(Vehicle):
    def __init__(self, brand, model,ignition):
        super().__init__(brand, model)
        self.ignition=ignition

    def start(self):
        self.clutch=True
        self.acc=True
        self.brk=True
        print("car started")


def start_vehicle(vehicle):
    vehicle.start()

c1=Vehicle("toyoto",2025)
c2=Bike("yamaha",2023,"black")
c3=Car("kia",2026,"diesel")

start_vehicle(c1)
start_vehicle(c2)
start_vehicle(c3)







        


        
    
        


        
        
