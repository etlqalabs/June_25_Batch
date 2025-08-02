# code for Adding 2 numbers

class Addition:
    name  = "Hetu"
    def addTwoNumber(self,a,b):
        sum = a + b
        print("Sum of two numbers is :", sum)

    def addThreeNumber(self,a,b,c):
        sum = a + b +c
        print("Sum of two numbers is :", sum)

ref =  Addition()

print("Calling addition function/method of addition of 2 numbers ")
ref.addTwoNumber(10,20)
ref.addTwoNumber(20,20)
print(ref.name)

print("Calling addition function/method of addition of 3 numbers ")
ref.addThreeNumber(10,20,20)
ref.addThreeNumber(10,20,40)



