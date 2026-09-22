# 1.
name = "soumya"
age = 22
city = "jodhpur"
college = "MUJ"

print(name, age, city, college)

# 2.
num1= 10
num2= 3

total=num1+num2
print(total)

diff=num1-num2
print(diff)

prod=num1*num2
print(prod)

quot=num1/num2
print(quot)

floor=num1//num2
print(floor)

remain=num1%num2
print(remain)

power=num1**num2
print(power)

# 3.
var1= 35
print(type(var1),var1)
var2=35.0
print(type(var2),var2)
var3="35"
print(type(var3),var3)
var4=bool("35")
print(type(var4),var4)
var5=["apple",45,3.0,"True"]
print(type(var5),var5)
var6=("apple",45,3.0,"True")
print(type(var6),var6)
var7={
    "brand":"Kia",
    "model":"2026",
    "car name":"seltos",
    "year":2026
}
print(type(var7),var7)

# 4.
fullname="soumya shah"
print(fullname[0])
print(fullname[-1])
print(len(fullname))
print(fullname.upper())
print(fullname.lower())
fullname=" soumya shah "
print(fullname.strip())



# 5.
fname="soumya"
lname="shah"
fullname=fname+" "+lname
print(fullname)

# 6.
str1="PythonProgramming"
print(str1[0:6])
print(str1[-5:])
print(str1[2:9])
print(str1[::-1])

# 7.
# age=int(input("Enter your age: "))
age=10
has_id=True
if age>=18 and has_id:
    print("you can enter",has_id)
else:
    print("you cant enter")

#8.
list1=["burger","pizza","pasta","momos","fries"]
print(list1[0])
print(list1[4])
print(len(list1))
print(list1[1:4])

# 9.
list2=[1,2,4,5,7]
list2[1]=3
print(list2)
list2.append(8)
print(list2)
list2.insert(2,9)
print(list2)
list2.remove(3)
print(list2)

# 10.
tup1=("jodhpur","jaipur","udaipur","kota","jaisalmer")
print(tup1[0])
print(tup1[-1])
print(len(tup1))
print(tup1[0:3])

# 11.
dict1={
    "name":"soumya",
    "age":22,
    "branch":"btech",
    "cgpa":6.75

}
print(dict1["name"])
print(dict1["age"])
print(dict1["branch"])
print(dict1["cgpa"])

# 12. 
product={
    "name":"notebook",
    "price":"150",
    "quantity":"10"
}
product.update({"price":200})
print(product)
product["discount"]=10
print(product)
product.pop("quantity")
print(product)

# 13.
int1=80
int2=100

total=int1+int2
avg=total/2
print(avg)
diff=abs(int1-int2)
percentage=((diff/avg)*100)
print(percentage)

# 14.
a=15
b=4

sum1=a+b                    
# 19
print(sum1)
diff=a-b
# 11
print(diff)
prod=a*b
# 60
print(prod)
div=a/b
# 3.75
print(div)
quot1=(a//b)
# 3
print(quot1)
remain=(a%b)
# 3
print(remain)
power=a**b
# 50,625
print(power)
print(a>b)
print(a<b)
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)

# 15.
a = "Soumya@#SHAH@#2003"
b=a.replace("@","")
c=b.replace("#","")
print(c)
print(c.lower())



# 16.
email="soumyashah2905@gmail.com"
print(email[0])
print(email[-1])
print(email[0:14])
print(email[15:])


# 17.
passw="Soumya@#2003"
if len(passw)>=8 and "@" in passw and passw.startswith("S"):
    print("password accepted")
else:
    print("password not accepted")


# 18.
list1=[100,200,300,400,500]
total=(sum(list1))
print(total)
avg=total/len(list1)
print(avg)
print(max(list1))
print(min(list1))
fixed=5
disc_amount=(total*fixed)/100
final=total-disc_amount
print(final)

#19.
list1=[1,2,3,4,5,6,7,8,9,10]
print(list1[0:3])
print(list1[-3:])
print(list1[0: :2])
print(list1[::-1])
print(list1[3:7])


#20.
marks=[
    [85,90,95],
    [80,90,79],
    [79,80,84]
]
print(marks[0][0])
print(marks[1][2])
print(marks[2][1])

#21.
tup1=("soumya",22,"jodhpur","intern")
# var1=tup1[0]
# var2=tup1[1]
# var3=tup1[2]
# var4=tup1[3]
var1,var2,var3,var4=tup1
print("my name is",var1,"and age is",var2,"i live in",var3,"and i am an",var4)

#22.
dict1={
    "brand":"apple",
    "model":"iphone 16",
    "price":60000,
    "storage":256,
    "color":"white"
}
print(dict1["brand"])
print(dict1["model"])
print(dict1["price"])
print(dict1["storage"])
print(dict1["color"])
dict1["price"]=49000
print(dict1)
dict1.update({"warranty":"1 year"})
print(dict1)
dict1.pop("color")
print(dict1)

# 23.
dict1={
    "name":"soumya",
    "list1":[1,23,45,60,40],
    "tup1":("science","maths","chemistry")
}
print(dict1["list1"])
print(dict1["tup1"])
marks=(dict1["list1"])
total=sum(marks)
avg=total/len(marks)
print(avg)

#24.
str1="345"
str2="456"
print(type(str1))
print(type(str2))
age1=int(str1)
age2=int(str2)
print(type(age1))
print(type(age2))
sum1=age1+age2
print(sum1)
str_sum1=str(sum1)
diff1=age1-age2
print(diff1)
str_diff=str(diff1)
prod=age1*age2
print(prod)
str_prod=str(prod)
div=age1/age2
print(div)
str_div=str(div)

# 25.
name="lamp"
price=1500
quantity=1
discount_percentage=10
tax_percentage=5
subtotal=price*quantity
print(subtotal)
disc_amount=(subtotal*discount_percentage)/100
print(disc_amount)
taxable_amount=subtotal-disc_amount
tax_amount=(taxable_amount*tax_percentage)/100
print(tax_amount)
final_bill=tax_amount+taxable_amount
print(final_bill)

# 26.
num1=34543
num2=43535
num3=45253

print(num1>num2 and num1>num3)

print(num1==num2==num3)

print(num1==num2 or num1==num3 or num2==num3)

# 27.
dict1={
    "name":"SOUMYA",
    "age":22,
    "branch":"btech cse",
    "subjects":("nlp","dll","xai"),
    "marks":[80,85,79],
    "passed":True

}
var1,var2,var3=dict1["marks"]
total_marks=var1+var2+var3
print(total_marks)
avg_marks=total_marks/3
print(avg_marks)
dict1.update({"total_marks":total_marks})
dict1.update({"avg_marks":avg_marks})
print(dict1)


# 29.
product={
    "name":"lamp",
    "category":"decoration",
    "price":1000,
    "quantity":10,
    "supplier":"amazon",
    "availability":True
}
product["quantity"]=20
product["price"]=1500
print(product)
var1=product["price"]
var2=product["quantity"]
print(var1,var2)
inventory_value=var1*var2
print(inventory_value)
print(var2>0)

# 30.
contacts = {
    "soumya": {
        "phone_number": 7230827146,
        "city": "jodhpur",
        "tag": "friend"
    },
    "papa": {
        "phone_number": 9414136246,
        "city": "jaipur",
        "tag": "family"
    },
    "mummy": {
        "phone_number": 6375573360,
        "city": "jaisalmer",
        "tag": "work"
    },
    "papa2": {
        "phone_number": 8005885840,
        "city": "udaipur",
        "tag": "client"
    }
}

print(contacts)
print(contacts["soumya"])
print(contacts["papa"])
contacts["soumya"]["phone_number"] = 9052798989
print(contacts)
contacts.update({
    "radha": {
        "phone_number": 9571109660,
        "city": "sikar",
        "tag": "family"
    }
})
print(contacts)

#.31
movies={
    "movie1":{
        "title":"ramayana",
        "year":2026,
        "rating":4,
        "genres":("spiritual","entertainment"),
        "actors":["ranbir","sai","ravi"]

    },
    "movie2":{
        "title":"main wapas aaunga",
        "year":2026,
        "rating":4,
        "genres":("spiritual","entertainment"),
        "actors":["diljit","nasiruddin","sharvari"]

    },
    "movie3":{
        "title":"love aaj kal",
        "year":2005,
        "rating":4,
        "genres":("comedy","entertainment","romance"),
        "actors":["said","deepika","rishi"]
    }
}
print(movies)
print(movies["movie1"])
movies["movie1"]["rating"]=5
print(movies)
movies["movie1"].update({"actors":["ranbir","sai","ravi","rocky"]})
print(movies)
movies["movie1"]["genres"]=("entertainment",)

print(movies)

# 32.
list1=["so hduih iuyg","guddnbTGUY","grfief ","d6rdtf"]
var1=(list1[0].upper().strip().title())
var2=(list1[1].upper().strip().title())
var3=(list1[2].upper().strip().title())
var4=(list1[3].upper().strip().title())
list2=[var1,var2,var3,var4]
print(list2)
print("original=",list1)
print("cleaned=",list2)

#33.
tup1=(44,54,67,89,23,56)
var1,var2,var3,var4,var5,var6=tup1
total=var1+var2+var3+var4+var5+var6
print(total)
avg=total/6
print(avg)
a=(max(tup1))
b=(min(tup1))
c=a-b
d=(avg>=60)
analysis={
    "total":total,
    "avg":avg,
    "max value":a,
    "min value":b,
    "range of tuple":c,
    "if avg is atleast 60":d
}

print(analysis)


#34.
shopping_cart={
    "customer1":{
        "info":{
            "name":"hitesh",
            "email":"shikhahitesh189@gmail.com"

        }},
    "products":[
        {
            "name":"ac",
            "price":50000,
            "quantity":10
        },
        {
            "name":"fridge",
            "price":1000000,
            "quantity":4
        },
        {
            "name":"bedside organiser",
            "price":1000,
            "quantity":40
        }

    ],
    "coupon":"SOMU",
    "delivery charge":50
    
    
    
}


print(shopping_cart)
a=shopping_cart["products"][0]
print(a)
total_1=a["price"]*a["quantity"]
b=shopping_cart["products"][1]
total_2=b["price"]*b["quantity"]
c=shopping_cart["products"][2]
total_3=c["price"]*c["quantity"]
sub_total=total_1+total_2+total_3
print(sub_total)
discount=sub_total*(10/100)
print(discount)
amount_after_discount=sub_total-discount
print(amount_after_discount)
d=shopping_cart["delivery charge"]
final_amount=amount_after_discount+d
print(final_amount)

# 35.
employee={
    "employee1":{
        "name":"hitesh",
        "salary":250000,
        "allowances":10000,
        "deductions":5000,
        "tax_rate":10

    },
    "employee2":{
        "name":"shikha",
        "salary":25000000,
        "allowances":100000,
        "deductions":50000,
        "tax_rate":12
    
    }
}

gross_salary_1=employee["employee1"]["salary"]+employee["employee1"]["allowances"]
print(gross_salary_1)
gross_salary_2=employee["employee2"]["salary"]+employee["employee2"]["allowances"]
print(gross_salary_2)
taxable_salary1=gross_salary_1-employee["employee1"]["deductions"]
print(taxable_salary1)
taxable_salary2=gross_salary_2-employee["employee2"]["deductions"]
print(taxable_salary2)
tax1=taxable_salary1*(employee["employee1"]["tax_rate"]/100)
print(tax1)
tax2=taxable_salary2*(employee["employee2"]["tax_rate"]/100)
print(tax2)
net_salary1=taxable_salary1-tax1
print(net_salary1)
net_salary2=taxable_salary2-tax2
print(net_salary2)

salary_details={
    "employee1":{
        "gross salary":gross_salary_1,
        "taxable salary":taxable_salary1,
        "tax":tax1,
        "net salary":net_salary1
    },
    "employee2":{
        "gross salary":gross_salary_2,
        "taxable salary":taxable_salary2,
         "tax":tax2,
        "net salary":net_salary2
        
    }
}

print(salary_details)

#36.
sent="i am soumya and engineering student who is currentyly working as an intern."
list1=["i","am","soumya","and","engineering","student","who","is","currently","working","as","an","intern"]

sentence={
    "original":sent,
    "word list":list1,
    "first word":list1[0],
    "last word":list1[-1],
    "word count":len(list1),
    "uppercase sentence":sent.upper(),
    "reversed sentence":sent[::-1]
}
print(sentence)

#37.
a=True
b=False

print(a and b)
print(a or b)
print( not a)
print(not b)
print(a and not b)
print(a or not b)
print((a and not b)or(not a and b))

#38.
report_card={
    "student1":{
        "name":"soumya",
        "roll_no":21,
        "subjects":("maths","science","chemistry"),
        "marks":[85,88,92],
        "attendance":84,
        "pass_status":True
    },
    "student2":{
        "name":"hardik",
        "roll_no":10,
        "subjects":("maths","science","biology"),
        "marks":[81,80,95],
        "attendance":88,
        "pass_status":False
    }
}

var1,var2,var3=report_card["student1"]["marks"]
total_1=var1+var2+var3

var4,var5,var6=report_card["student2"]["marks"]
total_2=var4+var5+var6

avg1=total_1/3

avg2=total_2/3

a=(max(report_card["student1"]["marks"]))
b=(min(report_card["student1"]["marks"]))
c=(max(report_card["student2"]["marks"]))
d=(min(report_card["student2"]["marks"]))
percentage1=(total_1/(3*100))*100
percentage2=(total_2/(3*100))*100

eligibility1=(
    percentage1>=60 and report_card["student1"]["attendance"]>60 and report_card["student1"]["pass_status"] is True
)
print(eligibility1)
eligibility2=(
    percentage2>=60 and report_card["student2"]["attendance"]>60 and report_card["student2"]["pass_status"] is True

)
print(eligibility2)

report_card["student1"].update({"total marks":total_1})
report_card["student1"].update({"avg marks":avg1})
report_card["student1"].update({"highest":a})
report_card["student1"].update({"lowest":b})
report_card["student1"].update({"percentage":percentage1})
report_card["student1"].update({"eligibility":eligibility1})
report_card["student2"].update({"total marks":total_2})
report_card["student2"].update({"avg marks":avg2})
report_card["student2"].update({"highest":c})
report_card["student2"].update({"lowest":d})
report_card["student2"].update({"percentage":percentage2})
report_card["student2"].update({"eligibility":eligibility2})

print(report_card)

