import numpy as np

arr=np.array([1,2,3.1,4,5])
print(arr)
print(arr.dtype)    #automatically converted into float

lst=["string",1,2,5.6]
arr=np.array(lst)   #all values converted into string 
print(arr)
print(arr.dtype)

arr=np.array([1,2,31,4,5])  #int values
print(arr)
print(arr.dtype)

arr=np.array([1,2,3.1,4,5])    #will convert everything into float
print(arr)
print(arr.dtype)

arr=np.array([1,2,3,4])
print(arr.dtype)

arr=np.array([1,2,3,4],dtype=np.float64)  #will add .o
print(arr)
print(arr.dtype)

arr=np.array([1.1,2.8,3,4],dtype=np.int64) #will remove decimals
print(arr)
print(arr.dtype)

#TYPE CASTING

arr=np.array([1,2,3])
print(arr.dtype)