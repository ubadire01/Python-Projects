import random

my_score = 0
computer_score = 0

options = ["rock", "paper", "scissors"]

while True:
    u_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if u_input == "q":
        break
    if u_input not in options:
        print("Invalid input, please try again.")
        continue
    
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    
    print(f"Computer picked {computer_pick}.")
    
    if (u_input == "rock" and computer_pick == "scissors") or \
       (u_input == "paper" and computer_pick == "rock") or \
       (u_input == "scissors" and computer_pick == "paper"):
        print("You won!")
        my_score += 1
    elif u_input == computer_pick:
        print("It's a tie!")
    else:
        print("You lost!")
        computer_score += 1

print(f"You won {my_score} times")
print(f"Computer won {computer_score} times")        
print("Goodbye")
