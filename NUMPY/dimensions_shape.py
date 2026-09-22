import numpy as np 
arr=np.array(32)
a=arr.ndim 
b=arr.shape             #ndim is a built-in-function used to know the dimension of an array
print(a,b)
arr = np.array([1,2,3])
b=arr.shape 
a=arr.ndim
print(a,b)
arr= np.array([[1,2,3],[4,5,6]])
b=arr.shape 
a=arr.ndim
print(a,b)
arr=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
b=arr.shape 
a=arr.ndim
print(a,b)
arr=np.array([[[[]]]])
b=arr.shape
print(b)
