score = 0    # the Score of the Quiz

Question = input("What is the capital of France? ")
if Question.lower() == "paris":           # the Question.lower() used to convert the give output in lower form
    print("Correct")
    score = score + 1                     # the old score plus the new score
else:
    print("Wrong")                    # if the Answer is not correct

Question = input("What is the capital of Japan? ")
if Question.lower() == "tokyo":
    print("Correct")
    score = score + 1
else:
    print("Wrong")

Question = input("What is the capital of Brazel? ")
if Question.lower() == "brasilia":
    print("Correct")
    score = score + 1
else:
    print("Wrong")

Question = input("What is the capital of Egypt? ")
if Question.lower() == "cairo":
    print("Correct")
    score = score + 1
else:
    print("Wrong")

Question = input("What is the capital of Canada? ")
if Question.lower() == "ottawa":
    print("Correct")
    score = score + 1
else:
    print("Wrong")

Question = input("What is the capital of Australia? ")
if Question.lower() == "canberra":
    print("Correct")
    score = score + 1
else:
    print("Wrong")

Question = input("What is the capital of India? ")
if Question.lower() == "new delhi":
    print("Correct")
    score = score + 1
else:
    print("Wrong")

Question = input("What is the capital of Germany? ")
if Question.lower() == "berlin":
    print("Correct")
    score = score + 1
else:
    print("Wrong")

Question = input("What is the capital of China? ")
if Question.lower() == "beijing":
    print("Correct")
    score = score + 1
else:
    print("Wrong")

Question = input("What is the capital of Mexico? ")
if Question.lower() == "mexico city":
    print("Correct")
    score = score + 1
else:
    print("Wrong")

print("Your total score is:", score, "/10") # total score with the Awaeded Score 
