# homework2 

name = input("enter your name :")
age = int(input("enter your age:"))

if age >= 60:
    print("you are senior citizen")
if age >= 18 and age <=  59:
    print("you are adult")
if age < 18:
    print ("you are minor")

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 60:
    print(name, "you are a Senior Citizen")
elif age >= 18:
    print(name, "you are an Adult")
else:
    print(name, "you are a Minor")
    
age = int(input("Enter age:"))
print(age + 10)