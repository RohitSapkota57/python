import random  # module

print("\n---[Welcome to Number Guessing Game]---\n")
print("Enter number you want to select between \n ")
a=int(input("enter first number"))
b=int(input("enter second number"))
secret_number = random.randint(a, b)  #  module 
print("I have selected a number between",a, "and" , b )

#condition 

while True:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("🎉 Correct! You guessed the number!")
        break