print("Welcome to my quiz game!")
right_question = 0

def count_score(num_questions, score = 25):
    if right_question != num_questions:
        print("Wrong, the questions you got right is: " + str(right_question))
    if right_question >= 3:
        print("Congratulations you passed!")
    if right_question <= 2:
        print("Sorry, you failed the test.")
    print(num_questions * score)
    return (right_question)


# A list containing the right answers
correct_answer = ["$1 trillion", "1998", "1558", "2012", "Eiffel & Cie"]
    
    
question_one = input("What much is Apple worth? ")
if question_one == correct_answer[0]:
    print("Correct!")
    right_question = right_question + 1
else:
    print("Sorry, the right answer is " + correct_answer[0])
    #End
    
question_two = input("What year did Michael Jordan win his last championship? ")
if question_two == correct_answer[1]:
    print("Correct!")
    right_question = right_question + 1
else:
    print("Sorry, the right answer is " + correct_answer[1])
    #End
    
question_three = input("What year did Queen Elizabeth I become queen? ")
if question_three == correct_answer[2]:
    print("Correct!")
    right_question = right_question + 1
else:
    print("Sorry, the right answer is " + correct_answer[2])
    #End
    
question_four = input("What year did Frank Ocean dropped his album channel ORANGE? ")
if question_four == correct_answer[3]:
    print("Correct!")
    right_question = right_question + 1
else:
    print("Sorry, the right answer is " + correct_answer[3])
    #End
    
question_five = input("Who designed & built the Eiffel Tower? ")
if question_five == correct_answer[4]:
    print("Correct!")
    right_question = right_question + 1
else:
    print("Sorry, the right answer is " + correct_answer[4])
    #End
    
count_score(num_questions = int(input("Enter the amount of questions you got right: ")))
print("Thank you for playing :)")