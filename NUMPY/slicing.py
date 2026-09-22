import numpy as np
arr=np.arange(1,10)
print(arr)
arr=np.arange(1,10,2)      #start:end:step
print(arr)
arr=np.arange(10,1,-2)     #negative slicing  
print(arr) 
list=[1,2,4,5,6,7]
arr=np.array(list)
print(arr[1:4])