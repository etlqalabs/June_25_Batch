'''
name = "Akash"
print("Type of name is ",type(name))
age = 25
print("Type of age is ",type(age))
workingInIt = True
print("Type of workingInIt is ",type(workingInIt))
salaryPerMonth = 180000.50
print("Type of salaryPerMonth is ",type(salaryPerMonth))


# Type casting ( conerting data form one data type to another ) in to int and adding
markInMaths = "70"
markInPhysics = "95"

print("Type of marks in Maths  ",type(markInMaths))
print("Type of marks in Physics  ",type(markInPhysics))

totalMarks = markInMaths+markInPhysics
print("Type of totalMarks ",type(totalMarks), " and the total marks is ",totalMarks)

# Convert in to int
totalMarksInt = int(markInMaths)+int(markInPhysics)
print("Type of totalMarksFloat ",type(totalMarksInt), " and the total marks is ",totalMarksInt)



# Type casting ( conerting data form one data type to another ) in to int and adding
markInMaths = "70.75"
markInPhysics = "95.25"

print("Type of marks in Maths  ",type(markInMaths))
print("Type of marks in Physics  ",type(markInPhysics))

totalMarks = markInMaths+markInPhysics
print("Type of totalMarks ",type(totalMarks), " and the total marks is ",totalMarks)

# Convert in to float

totalMarksFloat = float(markInMaths)+float(markInPhysics)
print("Type of totalMarksFloat ",type(totalMarksFloat), " and the total marks is ",totalMarksFloat)


# Downcasting and upcasting

num1 = 10.20
num2 = 20.30
print(" addition is ",num1+num2)

num3  = int(num1)
num4  = int(num2)
print(" addition is ",num3+num4)

# Control statements - which decides the flow of execution of the program
# if , if...else , if ...elif ..else

# based on age , determine the person ellibigle for voting
age = 20

if (age >= 18):
    print("printing inside ...")
    print("person is elligible to vote")
print("printing out side...")



# if ...else
age = 10
if (age >= 18):
    print("person is elligible to vote")
else:
    print("person is not elligible to vote")
print("printing out side...")



# if ..elif ...else
marks = int(input("Enter marks .."))
if (marks >= 65):
    print("First Grade")
    print("Congates ...")
    marks = marks +10
    print("You are genuius so your mark is increased",marks)
elif(marks >=35 and marks <65):
    print("Second grade")
elif (marks >=35 and marks < 65):
    print("Third grade")
else:
    print("Failed")
print(" results declared ...")


# range function
#print(range(10))

# Looping contruct
# for loop and while loop

print(1)
print(2)
print(3)
print(4)
print(5)

# 0, 5
for x in range(6):
    if x > 0 :
        print(x)

# range(startIndex,EndIndex,step)
# by default stratIndex 0 and step is 1

for x in range(1,6):
        print(x)

for x in range(1,6,1):
        print(x)

# I want to print all the odd number
for x in range(1,10,2):
        print(x)


# I want to print all the odd number
for x in range(2,10,2):
        print(x)



# While loop ( contine to execute until the condition is True)

# Print odd number from 1 to 10

num = 1
while num <=10:
    print(num)
    num = num + 2


name = "Akash"
print(name)


# Collections : group of things/items
name1 = "Akash"
name2 = "Rakesh"
name3 = "Roshan"
print(name1)
print(name2)
print(name3)


# if we need to store all thes ename in a single variable . thats where collection comes in to play
# List - stores group of items ( empid) , can stores duplicates and can add , remove items from the list(mutable)
# Tuple - stores group of items ( empid) ,can stores duplicates and can not add , remove items from the tuple(immutable)
# Set - stores group of items ( empid) , will not accept duplicates ( mutable)
# Dictionary - stores group of items with key and value pair ( empid : ename )

empList = ["Akash","Roshan","Rakesh"]
print("Type of the empList ;",type(empList))
print("Items inthe empList ;",empList)

# Add one more emp in the list
empList.append("Samrat")
#print("Reised empList ;",empList)

# Remove an element/items from the list
empList.remove("Rakesh")
#print("Reised empList ;",empList)

# Get the first items from the list ( index =  0)
#print(empList[0])

# Get the last items from the list
# get the total no of items
l = len(empList)
#print(l)
lastIndex =  l -1
#print(empList[lastIndex])


# using for loop , we can print al the items

for x in range(0,l,1):
    print(empList[x])

# Assigment : use while loop to print all elements


# Tuple:
empTuple = ("Akash","Roshan","Rakesh")
print(type(empTuple))

for item in empTuple:
    print(item)

# or
l = len(empTuple)
for x in range(l):
    print(empTuple[x])

'''

# SET ( unordered collection which doesn not store any duplicate values )

empTuple = ("Akash","Roshan",""," ","Rakesh","Akash")
print(empTuple)

empSet = {"Akash","Roshan","Rakesh","akash"}
print(empSet)

for item in empSet:
    print(item)


from datetime import datetime,date

date_in_string= "2025-05-16"
print(date_in_string,":", type(date_in_string))

date_field = datetime.strptime(date_in_string,"%Y-%m-%d")
print(date_field)

# create a new date
d1  = date(2025,5,16)
print(d1,type(d1))




