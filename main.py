# class Egl:
#
#     def __init__(self, age, name):
#         self.age = age
#         self.name = name
#
#
# egl = Egl(25, "Rashid")
#
# print(egl.age)
# print(egl.name)


from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = Quizbrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
    if not quiz.still_has_questions():
        print("You have completed the quiz")
        print(f"Your final score was: {quiz.score}/{quiz.question_number}")
