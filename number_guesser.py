import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("Please type a number larger than 0.")
        quit()
else:
    print("Please type a number larger than 0 next time.") 
    quit()   

random_number = random.randint(1, top_of_range)
guess_score = 0

while True:
    guess_score += 1

    user_guess = input("Make a guess: ")
    
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a valid number.")
        continue

    if user_guess <= 0:
        print("Please type a number larger than 0.")
        continue
    
    if user_guess == random_number:
        print("You got it right!")
        break
    elif user_guess > random_number:
            print("Your guess is greater than the number.")
    else: 
            print("Your guess is less than the number.")

print("You got it in", guess_score, "guesses.")
