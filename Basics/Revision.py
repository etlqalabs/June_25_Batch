# Assigment:
#1. work on how to delete second or 3rd occurent of an element in list
#2. work on how to reverse order sorting ( descening order )
#3. practice all other similar functions in set like we didi for list



#List
emp_list = [1,2,3,4,5,6,1,2,3,2]

#1. Append ( add the elemnt at the end
emp_list.append(7);
#print(emp_list)

#2. add multiple element
emp_list.extend([8,9,10,7,3])
#print(emp_list)

# 3. add element at specific location(index)
emp_list.insert(0,20)
#print(emp_list)

#4. delete an element
#emp_list.remove(7)
#print(emp_list)
# 5. delete the first occurence of the element
emp_list.remove(3)
#print(emp_list)

#6. pop - removes and return the element at the given index , by default it pops at last index
'''
print(emp_list)
print(emp_list.pop())
print(emp_list)
print(emp_list.pop())
print(emp_list)
print(emp_list.pop(0)) # pop the item at 0th index
print(emp_list)
'''
#7. clear()
#print(emp_list)
#emp_list.clear()
#print(emp_list)
'''
# count() , count the occurence of an element
print(emp_list)
# get the occuence of value 2
print(emp_list.count(2))

# sort() # arranguig and ascedning orde rof the values
emp_list.sort()
print(emp_list)

# reverse()
emp_list.reverse()
print(emp_list)
'''

# Tuple
#1. count function
emp_tuple = (1,2,3,4,5,6,1,2,3,2)
#print(emp_tuple)
#print(emp_tuple.count(3)) # 2
#print(emp_tuple.count(5)) # 1

#2 . index
#print(emp_tuple.index(3)) # 2
#print(emp_tuple.index(0)) # 2
'''
# Set
emp_set = {1,2,3,4,5,6,1,2,3,2}
print(emp_set)

# add() to add an element
emp_set.add(20)
print(emp_set)

# update()
emp_set.update([30,40])
print(emp_set)

# Set theory ( union,intersection,minus )

set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
print(set1)
print(set2)

# Union
set_result = set1 | set2
print(set_result)

# Intersection
set_result = set1 & set2
print(set_result)

# Minus
set_result = set1 - set2
print(set_result)


# Dictionary ( map ) : unordered data strcurure which store key-value pair

emp_dict = {1:"A",2:"B",3:'C',4:"D",5:"E"}
print(type(emp_dict))
print(emp_dict)

# Get me empname of empno= 3
print(emp_dict[3])

# get me all the empno
keys = emp_dict.keys()
print(keys)

# get me all the emp names
values = emp_dict.values()
print(values)

# add or modify the dictionary
emp_dict[10] = 'L'
print(emp_dict)
emp_dict[1] = 'P'
print(emp_dict)

# Deleting items from dict
emp_dict.pop(1)
print(emp_dict)
emp_dict.popitem()
print(emp_dict)

# iterate the dictionary and print empno and correspondinf emp name
emp_dict = {1:"A",2:"B",3:'C',4:"D",5:"E"}
for key,value in emp_dict.items():
    print(key,"====> ",value)

for key in emp_dict.keys():
    print(key+100)




# maximum ( highest ) no. from the list
marks_list = [20,30,89,29,50]

# way 1 : using sort
marks_list.sort()
#print(marks_list)
noOfElement = len(marks_list)
#print(marks_list[noOfElement-1])

# way 2 : using for loop without function

marks_list = [20,30,89,29,50]

maxi = marks_list[0] # 20
for ele in marks_list:
    if maxi < ele:  # 89 < 50
        maxi = ele  # 89
print(maxi)


# Way 3 using a function

def getMaxi(marks_list):
    maxi = marks_list[0]  # 20
    for ele in marks_list:
        if maxi < ele:  # 89 < 50
            maxi = ele  # 89
    return maxi

marks_list = [20, 30, 89, 29, 50]
maximum_mark = getMaxi(marks_list)
print(maximum_mark)


# Given a list , i want the count of each element in the list



def count_emp_list(list):
    count_dict = {}
    for ele in list:
        if ele in count_dict:
            count_dict[ele] = count_dict[ele] +1
        else:
            count_dict[ele] = 1  # 1:2,2:1,3:3,4:2,5:1
    return count_dict

emp_list = [1,2,3,4,5,1,3,4,3]
ans =  count_emp_list(emp_list)
print(ans)


emp_dict = {1:100,2:200}
print(emp_dict[1])
emp_dict[1] = emp_dict[1] + 50
print(emp_dict[1])


# Strings - Set of characters
# In python, we don't have special data type for character, here we have a single length string as character\


name = 'ETLQA Labs'
first_char ="E"

#print(type(name))
#print(name)
#print(type(first_char))
#print(first_char)

# how can i print each caharcter from the string
# way 1 using indexes
n = len(name)  # no of char in the string
for idx in range(0,n):
    print(name[idx],end = " ")


# way 2 using advanced for loop
print()
for ch in name:
    print(ch,end = " ")

'''

# Get me the first 5 character from the string ( o/p = ETLQA )
name = 'ETLQALabs'

# Way 1 using for loop
'''
for idx in range(0,5,1):
    print(name[idx],end = "")
'''
print()
# Way 2 slicing
# start - start index ( start index should lways be lesser than end end index )
# end  - end index -1
# step  - positive ot negative


#print(name[0:5:1])

#print(name[0:5:2])

# print the entire string in the reverse order
e = len(name)
#print(name[0:e:1])  # forward order
#print(name[::1])  # forward order

#print(name[::-1])  # forward order

print(name)
print(name[-1])
print(name[-1:-5:-1])

# Split function
name_channel = "ETL@QA@Labs"
words = name_channel.split("@")
print(type(words))
print(words)
print(words[0])
print(words[1])
print(words[2])


emp = {"empid":[101,102,102],"empname":"John","deptid":100}
emp_list = emp['empid']
for ele in emp_list:
    print(ele)


# Check the immutability of string
name = "Hetu"
print(name)
print(id(name))
name = name+" ETLQA"
print(name)
print(id(name))


list = [1,2,3]
print("values before append :",list ," and id is ",id(list))
list.extend([4,5])
print("values after append  :",list ," and id is ",id(list))

