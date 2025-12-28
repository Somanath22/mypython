#lesson2 part-1 using input function to take user input

name = input("Enter your name: ")
print ("hello", name)

name = input("what is your name?:")
print ("welcome", name)

name = input("what is your name ?:")
nationality = input ("what is your nationality?:")
passport_no = input (" what is your last 4 digit of your passport no.?:")
print ("hello",name + "your identification number is :", nationality,passport_no)
name = input(" enter your name ?:")
age = int(input("enter your age:"))
height = float(input("enter your height:"))
car = input("enter your favorite car:")

print("\n ---your details---")
print ("name:", name )
print ("age:",age)
print ("height:", height)
print ("favorite car:", car)

#lesson2 part-2 using escape sequence characters in python

age = int(input("enter your age:"))

if age >=18:
    print("you are adult")
else: 
    print ("you are minor")
