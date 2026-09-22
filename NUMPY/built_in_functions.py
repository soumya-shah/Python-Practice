import numpy as np 

#linspace
arr=np.linspace(0,1,5) #start,stop,no of values between them
print(arr)             # 0.25 gap between each number

#logspace
arr=np.logspace(1,3,3) #logarithmic scale array -->10^1 --> 10^3 ... 3 points
print(arr)

#zeros
arr=np.zeros(5)
print(arr)
arr=np.zeros([2,3])   #rows,columns
print(arr)

#ones
arr=np.ones(5)
print(arr)
arr=np.ones([2,3])
print(arr)
arr=np.ones([4,2],dtype=int)

#full
arr=np.full(10,2)
print(arr)
#2-d array
arr=np.full([2,4],7)  #([row,column],value)
print(arr)

#empty
arr=np.empty([2,3]) 
print(arr)

#random.rand()
arr=np.random.rand(10)
print(arr)
arr=np.random.rand(2,3)
print(arr)

#random.randn
arr=np.random.randn(2,3)
print(arr)

#random.randint
arr=np.random.randint(10,100,size=(2,3))
print(arr)


