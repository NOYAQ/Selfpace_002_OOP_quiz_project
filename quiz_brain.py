"""
initialize a question number, question list and user score.
"""
class QuizBrain:
    def __init__(self,q_list):
        self.q_number=0
        self.q_list=q_list
        self.user_score=0
    """
    asks a question from the question list, stores the user's answer 
    and sends the user's answer to the checking function
    """
    def ask_question(self):
        user_answer=input(f"Q.{self.q_number+1}: {(self.q_list[self.q_number].question)}(True\\False):\n".capitalize())
        self.check_question(user_answer=user_answer)

    """
    compares the user's answer and the question's answer,
    if it is correct, add 1 point to the user's score.
    """
    def check_question(self,user_answer):
        if user_answer==self.q_list[self.q_number].answer:
            self.user_score +=1
            print(f"You're correct: {self.user_score} / {self.q_number+1}")
        else:
            print(f"You failed: {self.user_score} / {self.q_number+1}")
        self.q_number +=1


    """
    compares the question quantity and questions in the list, if all questions are asked then return False
    otherwise, return True
    """
    def any_new_question(self):
        if self.q_number==len(self.q_list):
            print(f"Congrats!, You have completed the quiz: {self.user_score} / {len(self.q_list)}!")
            return False
        else:
            return True