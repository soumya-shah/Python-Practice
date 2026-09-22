a=[1,2,3,4,5]
a.append(6)                     #adds a single integer
print(a)
a.extend([7,8,9])               #adds multiple integers
print(a)
a.insert(0,0)                   #adds using specific index(position,value)
print(a)
a[0]=1                          #adds at index without using index keyword
print(a)                        
a.remove(0)                     #remove first matching value
print(a)
a.pop(2)                        # remove by index
print(a)
# a.clear()                     #clear list,del() will delete entire list
# print(a)
a.copy()                        #copy list
print(a)
b=a.count(1)                    # gives the count of element appearing like 1 is appearing 1 time so 1
print(b)
b=a.index(4)                    #gives the index of element
print(b)
c=a.sort(reverse=True)          #it should give the list in descending order
print(c)
print(len(a))                   #gives the len of list
print(max(a))                   #gives the maximum element in list
print(min(a))                   #gives the minimum element in list
print(sum(a))                   #gives the sum of all elements in list
print(all(a))                   #gives true if all elements are true
print(2 in a)                   #gives true if 2 exists in list