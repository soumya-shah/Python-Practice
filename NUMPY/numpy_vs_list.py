import numpy as np
import time

#list speed operation 
a=[1,2,3,4,5,6,7,8,9,10] * 10000000   #i have created a list heree and *100000 means the items in list(1,2,3,4,5,6,7,8 etc.) appear these many times in list
start=time.time()                #here i have taken the start time
for i in range(len(a)):          #now i have to multiply each item in list by 2 so i have to use a loop
    a[i]=a[i]*2                  #and now manually multiply each element by 2

print("\nTime taken for list:",time.time()-start)   #print the time taken for this operation on list without numpy

#numpy speed operation
a=[1,2,3,4,5,6,7,8,9,10] * 10000000
b=np.array(a)                    #converted the list into numpy array
start=time.time()                 #imported the start time
new_b=b*2                        #multiplied each item by 2 
print("\nTime taken for list:",time.time()-start)

#memory difference between list and numpy
import sys

a=[1,2,3,4,5]
arr=np.array(a)

print("list size:",sys.getsizeof(a))

print("array size:",arr.nbytes)


#data types in list vs numpy
a=[1,"a","apple",2.4]
print(type(a))

arr=np.array(a)
print(arr)          #we could see all ements are being converted into string

