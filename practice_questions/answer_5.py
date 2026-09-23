# 1.
a=int(input("enter a number 1:"))
b=int(input("enter a number 2:"))
try:
    c=a/b
    print(c)
except ZeroDivisionError:
    print("value cannot be 0")

# 2.
a=input("enter a number")


try:
    a=int(a)
    b=100/a
    print(b)
except ValueError:
    print("input is invalid.please enter an integer")

except ZeroDivisionError:
    print("cannot be divided by 0")


# 3.
try:
    a=int(input("enter a number:"))
    b=a**2
    print(b)
except ValueError:
    print("value should be an integer")
else:
    print("the square of",a,"is :",b)


# 4.
try:
    a=int(input("enter a number 1:"))
    b=int(input("enter a number 2:"))
    c=a/b
    print(c)
except Exception as e:
    print(e)
finally:
    print("program execution completed")

# 5.
numbers=[10,20,30,40,50]
try:
    a=int(input("enter a index value to be accessed:"))
    print(numbers[a])

except ValueError:
    print("the entered value must be an integer")

except IndexError:
    print("index value entered is out of range ")

finally:
    print("program execution completed ")

# 6.
try:
    a=int(input("enter a number "))
    print("the multiplication table of",a,"is :")
    for i in range(1,11):
        print(a,"X",i,"=",(a*i))

except Exception as e:
    print(e)

# 7.
try:
    a = int(input("Enter your age: "))

    if a < 0:
        raise ValueError("Age cannot be negative")

    elif a < 18:
        print("Not eligible")

    else:
        print("Eligible")

except ValueError as e:
    print(e)

# 8.
try:
    a=str(input("enter the password:"))
    if len(a)<8:
        raise ValueError("password length must be more than 8 characters")
    else:
        print("password accepted")
except Exception as e:
    print(e)

# 9.
try:
    a=int(input("enter a number 1:"))
    b=input("Enter an operator (+, -, *, /): ")
    if b !="+" and b !="-" and b!="*" and b!="/":
        raise ValueError("value must be a valid operator ")
    c=int(input("enter a number 2:"))
    if b == "+":
        print(f"Result: {a + c}")
    elif b == "-":
        print(f"Result: {a - c}")
    elif b == "*":
        print(f"Result: {a * c}")
    elif b == "/":
        print(f"result: {a/c}")
except ValueError as e:
    print(e)

except ZeroDivisionError:
    print("it cannot be divided by o")

finally:
    print("program execution completed")

# 10.
try:
    num=int(input("enter a number:"))
    result=10/num

except ZeroDivisionError:
    print("cannot be divided by 0")
except Exception as e:
    print("something went wrong")

else:
    print(result)

finally:
    print("done")




















