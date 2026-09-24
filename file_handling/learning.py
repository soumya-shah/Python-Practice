
# # reading a file
f=open("myfile.txt","r")
# print(f)
text=f.read() 
# # extracting the text to read from this file                                                                                     z.                                                     
print(text)
f.close()
# # writing to a file
g=open("myfile2.txt","w")
g.write("hello world")
g.close()
# # appending a file
h=open("myfile2.txt","a")
h.write("hello world")
h.close()
# using with keyword
with open("myfile2.txt","a") as f:
    f.write("hey i am inside with")

# readlines method
f=open("myfile.txt","r")
while True:
    line=f.readline()
    print(line)
    if not line:
        print(line,type(line))
        break

# writelines()method
f=open("myfile3.txt","w")
lines=["line1\n","line2\n","line3\n"]
# an extra line cause of \n
f.writelines(lines)
f.close()

# seek function
with open("myfile.txt","r") as f:
    # move to the 10th byte in the file 
    f.seek(10)

# tell() function 
    print(f.tell())
    # read the next 5 bytes
    data=f.read(5)
    print(data)

# truncate function
with open("myfile4.txt","w") as f:
    f.write("hello world...")
    f.truncate(5)
    # only allow 5 characterds to be added in the myfile4

with open("myfile4.txt") as f:
    print(f.read())
