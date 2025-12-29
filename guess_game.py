secret = 7 # number guessing game 
guess = 0

while guess != secret:
    guess = int(input("Guess the number (1-10): "))
    
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("✅ Correct! You won!")


secret = 5 # practiced
guess = 0

while guess != secret:
    guess = int(input("guess the number between 1 to 10:"))
    if guess < secret:
        print ("too low")
    elif guess > secret:
        print ("too high")
    else:
        print ("✅ correct you won")
        