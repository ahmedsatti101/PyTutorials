print("Welcome to guess the right answer!")

# A list containing the right answer
correct_answer = ["1 trillion dollars", "1998", "1558", "2012", "Eiffel & Cie"]
    
question_one = input("What much is Apple worth? ")
if question_one == correct_answer[0]:
    print("Correct!")
else:
    print("Sorry, the right answer is " + correct_answer[0])
    
question_two = input("What year did Michael Jordan win his last championship? ")
if question_two == correct_answer[1]:
    print("Correct!")
else:
    print("Sorry, the right answer is " + correct_answer[1])
    
question_three = input("What year did Queen Elizabeth I become queen? ")
if question_three == correct_answer[2]:
    print("Correct!")
else:
    print("Sorry, the right answer is " + correct_answer[2])
    
question_four = input("What year did Frank Ocean dropped his album channel ORANGE? ")
if question_four == correct_answer[3]:
    print("Correct!")
else:
    print("Sorry, the right answer is " + correct_answer[3])
    
question_five = input("Who designed the Eiffel Tower? ")
if question_five == correct_answer[4]:
    print("Correct!")
else:
    print("Sorry, the right answer is " + correct_answer[4])
    
print("Thank you for playing :)")