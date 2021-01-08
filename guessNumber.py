import random

number = random.randint(1,9)

guessesLeft = 0

while guessesLeft < 5:

   guess = int(input("Type Your Guess"))

   if number == guess:
      print("Congratulations You Guessed It Right!")
      break

   if number > guess:
      print("Your Guess Was Less Than The Number")
      guessesLeft += 1

   if number < guess:
      print("Your Guess Was More Than The Number")
      guessesLeft += 1

   

if not guessesLeft < 5:
    print("You Failed!")

