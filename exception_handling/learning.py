a=input("enter a number:")
# whenever i will enter like a name soumya or something to try wala block print nai hoga 
print(f"multiplication table of {a} is:")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i}={int(a)*i}")

except Exception as e:
    # here i chose ki agr error aaye to yeh hoye. 
    print(e)
    print("invalid input")
    # here mene choose kia hai error ko print krna agr kuch aur print krna hai to vo b likh skte h

print("some lines of code")
print("end of code ")
# yeh lines error aane ke bd b print hoyengi.. 
# so our program does not halts 

# handling specific types of error 
try:
    num=int(input("enter a integer:"))
    a=[6,3,4]
    print(a[num])

except ValueError:
    # type 1
    print("number entered is not an integer ")
    # if i enter anything other thn integer it will give value error 

except IndexError:
    # type 2
    print("index error") 
    # if i enter 4 then it wioll give index error as list a is not big or does not have anything at 4 index

# finally keyword

try:
    l=[1,2,3,4,4]
    i=int(input("enter the index:"))
    print(l[i])

except:
    print("some error occurred")

finally:
    print("i am also executed") 

# now we think we can simply write to bhi yeh hamesha chlega tohh
print("i am also executed")

# if we wrpa entire thing in a function

def func1():
    try:
        l=[1,2,3,4,4]
        i=int(input("enter the index:"))
        print(l[i])
    except:
        print("some error occurred")
    finally:
        print("i am also executed") 
    # finally se hi hoga vrna beech me return ke bd kuch b execute ni hoga

x=func1()

# custom errors
a=int(input("enter a value between 5 and 9:"))
# python me kuch built in errorsa hote hai jese ab me yha string value pass kriugi tovo apne aap yhi rok dega 

if(a<5 or a>9):
    raise ValueError("value should be between 5 and 9") 

# here i myself raise an error ki nai 5 or 9 ke beech me hi honi chahiye..
 



