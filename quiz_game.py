print('Welcome to uzi guseeing game!')

playing = input("Do you want to play my game: ")
if playing !="yes":
    quit()

print("Let's Play Homie :)")

score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect -1 point")
    score -= 1

answer = input("What is the capital of France? ")
if answer.lower() == "paris":
    print("Correct")
    score += 1
else:
    print("Incorrect -1 point")
    score -= 1

answer = input("What is the chemical symbol for water? ")
if answer.lower() == "h2o":
    print("Correct")
    score += 1
else:
    print("Incorrect -1 point")
    score -= 1

answer = input("Who wrote 'Romeo and Juliet'? ")
if answer.lower() == "william shakespeare":
    print("Correct")
    score += 1
else:
    print("Incorrect -1 point")
    score -= 1
answer = input("What is the largest planet in our solar system? ")
if answer.lower() == "jupiter":
    print("Correct")
    score += 1
else:
    print("Incorrect -1 point")
    score -= 1

answer = input("What year did the Titanic sink? ")
if answer.lower() == "1912":
    print("Correct")
    score += 1
else:
    print("Incorrect -1 point")
    score -= 1

answer = input("What is the speed of light? (answer in km/s) ")
if answer.lower() == "299792":
    print("Correct")
    score += 1
else:
    print("Incorrect -1 point")
    score -= 1

answer = input("Who is known as the father of computers? ")
if answer.lower() == "charles babbage":
    print("Correct")
    score += 1
else:
    print("Incorrect -1 point")
    score -= 1

answer = input("What is the hardest natural substance on Earth? ")
if answer.lower() == "diamond":
    print("Correct")
    score += 1
else:
    print("Incorrect -1 point")
    score -= 1

answer = input("What is the smallest prime number? ")
if answer.lower() == "2":
    print("Correct")
    score += 1
else:
    print("Incorrect -1 point")
    score -= 1
    
print(f"Your Final score is: {score}")
