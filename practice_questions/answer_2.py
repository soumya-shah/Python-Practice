# 1.
for x in range(1,51):
    print(x)

# 2.
for x in range(1,101):
    if x%2==0:
        print(x)

# 3.
for x in range(1,101):
    if x%2==1:
        print(x)

# 4.
x=int(input("please enter a number "))
y=0
while y<10:
    y+=1
    print(x*y)

# 5.
total=0
for x in range(1,101):
    total=(total+x)
print(total)

#6.
x=int(input("enter a number:"))
fact=1
for n in range(1,x+1):
    fact=fact*n
print(fact)

# 7.
x=int(input("enter a number:"))
count=0
while x>0:
    count=count+1
    n=n//10
print(count)

# 8.

x=int(input("enter a number:"))
reverse=0
while x>0:
    y=x%10
    x=x//10
    reverse=reverse*10+y
print(reverse)

# 9.
x=int(input("enter a number:"))
prime=True
for y in range(2,x):
    if x%y==0:
        prime=False
        break
        
if prime:
    print("its a prime number")
else:
    print("its not")

# 10
for x in range(1,101):
    prime=True
    for y in range(2,x):
        if x%y==0:
            prime=False
            break
    if prime:
        print(x)

# 11
x=int(input("enter a number"))
sum=0
while x>0:
    y=x%10
    x=x//10
    sum=sum+y
print(sum)

# 12
x=int(input("enter a number: "))
original=x
pal=0
while x>0:
    y=x%10
    x=x//10
    pal=pal*10+y

if pal==original:
    print("a palindrome")
else:
    print("not a palindrome")

# 13.
for x in range(1,6):
    for y in range(1,x+1):
       print("*", end="")
    print()                        
# yaha print() jo phle sre stars ek line me aayenge unko alg alg line me daalega

# 14.
for x in range(1,6):
    for y in range(1,x+1):
       print(y, end="")
    print()

#15.
# 7
n=int(input("enter a number:"))
first=0
second=1
for x in range(1,n+1):
    next=first+second
    print(first)
    first=second
    second=next

