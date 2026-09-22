# 1.
def hello(name):
    return ("hello"+" "+ name)

print(hello("soumya"))

# 2.
def greet(name):
    return("hello"+" "+name)
print(greet("soumya"))

# 3.
def add(a,b):
    return (a+b)

print(add(3,5))

# 4.
def even_or_odd(number):
    if number%2==0:
        print("even")
    else:
        print("odd")
even_or_odd(7)

# 5.
def square(number):
    return number*number

print(square(7))

# 6.
def max_element(list):
    largest_number=list[0]
    for n in list:
        if n>largest_number:
            largest_number=n
    return largest_number

my_list=[3,5,7,9]
print(max_element(my_list))    

# 7.
def vowels(name):
    name=name.lower()
    print(name)
    x=0
    for n in name:
        if n=="a" or n=="e" or n=="i" or n=="o" or n=="u":
            x=x+1  
    print(x)   
myname="SOUMYA"
vowels(myname)

# 8.
def factorial(number):
    fact=1
    for n in range(1,number+1):
        fact=fact*n
    return fact

print(factorial(5))

# 9.
def prime(number):
    if number <= 1:
        return False

    isprime = True

    for n in range(2, number):
        if number % n == 0:
            isprime = False

    return isprime

print(prime(1))

# 10.
def reverse(name):
    result=""
    for n in name:
        result=n+result
    return result

print(reverse("hello"))    

# 12.
def multiply(a, b):
    return a * b
result = multiply(4, 5)
print(result+10)

# 13.
def calculation(a,b):
    sum=a+b
    product=a*b
    diff=a-b
    return sum,product,diff
print(calculation(10,5))

# 14.
def info(name,age,city):
    print("my name is ",name," and I am ",age,"and i live in ",city)

info("soumya",22,"jaipur")

# 15.
def info(name,age,city):
    print("my name is ",name," and I am ",age,"and i live in ",city)

info(name="soumya",age=22,city="jodhpur")

# 16.
def greet(name="guest"):
    print("hello ",name)

greet()
greet("soumya")

# 17.
def calculate_bill(price,quantity=1):
    return price*quantity

print(calculate_bill(400,2))

# 20.
def add_number(*numbers):
    return(sum(numbers))


print(add_number(1,2,3))

# 21.
def max_number(*number):
    max=number[0]

    for n in number:
        if n>max:
            max=n
    return max

print(max_number(1,2,34,5,5))

# 22.
def avg_number(*number):
    
        total=sum(number)
        count=len(number)
        avg=total/count
        return avg
        



print(avg_number(1,2,3))

# 24.
def student(name, *marks):
    total = sum(marks)
    count = len(marks)
    avg = total / count
    return name, marks, avg

print(student("soumya", 1, 2, 3, 4, 5))


# 25.
def student_info(**details):
    for key,value in details.items():
        # by using items we get key value pairs else we will only get keys as it is dictionary
        print(key,value)

student_info(name="soumya",age=22, city='Jodhpur')

# 26.
def product(**details):
    return details

print(product(name='Laptop', price=50000, brand='HP'))

# 28.
def student(name, age=20, *subjects, **details):
    print("Title:", name,age)
    print("Positional arguments:", subjects)
    print("Keyword arguments:", details)

print(student("soumya",22,"maths","science", "physics",status="pass",fees="paid"))

# 34.
count=0
def inc():
    global count
    count=count+1
    print(count)

inc()
inc()
inc()

# 35.
def first():
     
    x=5
    def second():
        
        print(x)

    second()

first()

# 36.
def outer():
    count=0
    def inner():
        nonlocal count
        count=count+1
        print(count)

    inner()

outer()

# 37.
def factorial(n):
    if n <= 0:
        return 1
    else:
        x=n*factorial(n-1)
        return x

print(factorial(5))

# 38.
def sum1(n):
    if n==0:
        return 0
    else:
        return n+sum1(n-1)

print(sum1(5))

# 39.
def fibonaaci(n):
    if n<=1:
        return n
    else:
        return fibonaaci(n-1)+fibonaaci(n-2)

print(fibonaaci(5))

# 46.
def sum_of_list(n):
    if len(n)==0:
        return 0
    else:
        return n[0]+sum_of_list(n[1:])

n=[1,2,3,4,5]
print(sum_of_list(n))

# 47.
def reverse(n):
    if len(n)==0:
        return ""
    else:
        return n[-1] + reverse(n[:-1])

n="python"
print(reverse(n))

# 48.
def count(n):
    if n==0:
        return 0
    else:
        return 1+count(n//10)

n=12345
print(count(n))


# 49.
# def palindrome(n):
#     if len(n)==0:
#         return ""
#     else:
#         return n[-1]+palindrome(n[:-1])

# n="madam"
# x=palindrome(n)
# if x==n:
#     print("its a palindrome")
# else:
#     print("its not")

def palindrome(n):
    if len(n) <= 1:
        return True

    if n[0] != n[-1]:
        return False

    return palindrome(n[1:-1])

n = "madam"
print(palindrome(n))

# 50.
def maximum(n):
    if len(n)==1:
        return n[0]
    if n[1]>n[0]:
        return maximum(n[1:])
    else:
        return maximum([n[0]]+n[2:])

n=[1,2,3,8,5,0]
print(maximum(n))

# 64.
def school(name,city="jodhpur",*marks,**details):
    total_marks=sum(marks)
    count=len(marks)
    avg_marks=total_marks/count
    print(name,city,avg_marks)
    print(details)




(school("soumya","jodhpur", 1, 2, 3, 4, 5,status="passed"))

# 65.
def analyze_numbers(*numbers):
    total=0
    for  n in numbers:
        total=total+n
    count=len(numbers)
    avg=total/count
    def maximum(numbers):
        largest=[numbers[0]]
        if len(numbers)<=1:
            return numbers[0]
        elif numbers[1]>=numbers[0]:
            largest=numbers[1]
            return maximum(numbers[1:])
        else:
            largest=numbers[0]
            return maximum((numbers[0],)+numbers[2:])

    def minimum(numbers):
                lowest=[numbers[0]]
                if len(numbers)<=1:
                    return numbers[0]
                elif numbers[1]<=numbers[0]:
                    lowest=numbers[1]
                    return minimum(numbers[1:])
                else:
                    lowest=numbers[0]
                    return minimum((numbers[0],)+numbers[2:])

    def even_count(numbers):
        count=0
        for n in numbers:
            if n%2==0:
                count=count+1
        return count

    def odd_count(numbers):
            count=0
            for n in numbers:
                if n%2!=0:
                    count=count+1
            return count
        
    return {
        "sum of marks":total,
        "avg marks":avg,
        "maximum":maximum(numbers),
        "minimum":minimum(numbers),
        "even numbers":even_count(numbers),
        "odd numbers":odd_count(numbers)
        
    }

 

print(analyze_numbers(1,2,34,7))




     



        
        


    






    



    
 



        




