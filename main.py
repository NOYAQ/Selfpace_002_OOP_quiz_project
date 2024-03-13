from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = [] # a list used to store questions and their answer.
game_on = True # a variable enables game loop

def create_question_bank():
    """
    reading question data from data, storing questions and their answers and adding to a list variable.
    """
    for index in  range(len(question_data)):
        new_question = Question(question=question_data[index]["text"],answer=question_data[index]["answer"] )
        question_bank.append(new_question)

create_question_bank() # calls the function to assign questions and answers to the 'question_bank' list
main_quiz_brain=QuizBrain(question_bank) # creates an object to use in a game loop.

while game_on:
    main_quiz_brain.ask_question() # calls a function that asks questions and also compares the user's answers, from the object
    game_on = main_quiz_brain.any_new_question()
