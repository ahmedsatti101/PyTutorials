print("Welcome to guess the right answer!")
score = 0

# A list containing the right answer
correct_answer = ["1 trillion dollars", "1998", "1558", "2012", "Eiffel & Cie"]
    
question_one = input("What much is Apple worth? ")
if question_one == correct_answer[0]:
    print("Correct!")
    score = score + 25
else:
    print("Sorry, the right answer is " + correct_answer[0])
    score = score - 25
    
question_two = input("What year did Michael Jordan win his last championship? ")
if question_two == correct_answer[1]:
    print("Correct!")
    score = score + 25
else:
    print("Sorry, the right answer is " + correct_answer[1])
    score = score - 25
    
question_three = input("What year did Queen Elizabeth I become queen? ")
if question_three == correct_answer[2]:
    print("Correct!")
    score = score + 25
else:
    print("Sorry, the right answer is " + correct_answer[2])
    score = score - 25
    
question_four = input("What year did Frank Ocean dropped his album channel ORANGE? ")
if question_four == correct_answer[3]:
    print("Correct!")
    score = score + 25
else:
    print("Sorry, the right answer is " + correct_answer[3])
    score = score - 25
    
question_five = input("Who designed the Eiffel Tower? ")
if question_five == correct_answer[4]:
    print("Correct!")
    score = score + 25
else:
    print("Sorry, the right answer is " + correct_answer[4])
    score = score - 25
    
print("Your score is " + str(score) + " points.")
print("Thank you for playing :)")