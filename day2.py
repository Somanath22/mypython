name_of_the_user = input("Enter your name: ")
length_of_name = len(name_of_the_user)
print(type("length of letter in your name :")) #string
print(type(length_of_name)) #int


#PEMDAS
# ()
# **
# *
# /
# +
# _
result = 3 + 5 * 2 - (4 / 2) ** 2
print("The result of the expression is:", result)


#tip calculator
bill_amount = float(input("Enter the Bill amount: $"))
tip_percentage = int(input("Enter the Tip percentage (e.g., 15 for 15%): "))
tip_amount = bill_amount * (tip_percentage / 100)
total_amount = bill_amount + tip_amount
people = int(input("Enter the number of people to split the bill: "))
each_amount = total_amount / people
print("Total bill amount is: $", total_amount)
print("each person to be paid is: $", each_amount)
