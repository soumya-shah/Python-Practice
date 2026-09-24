# 1.
with open("answerfile1.txt","w") as f:
    lines=["my name is soumya\n","i am learning python\n","i want to become a good developer"]
    f.writelines(lines)

# 2.
with open("answerfile1.txt","r") as f:
    print(f.read())

# 3.
with open("answerfile1.txt","r") as f:
    lines=0
    x=f.readlines()
    for i in x:
        lines+=1
    print(lines)

# 4.
with open("answerfile1.txt", "r") as f:
    data = f.read()
    words = data.split()
    print(len(words))

# 5.
f=open("answerfile1.txt","r")
text=f.read()
print(text)
f.close()
f=open("backup1.txt","w")
f.write(text)
f.close()

# 6.
with open("answerfile1.txt","a") as f:
    a=str(input("enter a new skill:"))
    f.write(a+"\n")

# 7.
with open("answerfile1.txt","r") as f:
    file=f.read()
    words=file.split()
    a=input("enter a word:")
    for b in words:
        if a==b:
            print("word found")
            break
    else:
        print("word not found")

# 8.
with open("answerfile1.txt","r") as f:
    file=f.read()
    words=file.split()
    a=input("enter a word:")
    count=0
    for b in words:
        if a==b:
            count+=1
    print(count)

# 9.
with open("answerfile2.txt","r") as f:
    total=0
    count=0

    while True:
        
        file=f.readline()
        if not file:
            break
        m1=file.split()[0]
        m2=int(file.split()[1])
        total+=m2
        count+=1
        print(f"{m1} scored {m2}")
    avg=total/count
    print(avg)

# 10.
with open("answerfile1.txt","r") as f:
    file=f.read()
    no_of_lines=file.splitlines()
    print(len(no_of_lines))
    no_of_words=file.split()
    print(len(no_of_words))
    no_of_characters=len(file)
    print(no_of_characters)
        
            

    

    
    
    
    

    







    


    