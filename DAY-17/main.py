from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    qst = Question(question["question"], question["correct_answer"])
    question_bank.append(qst)

get_qstn = QuizBrain(question_bank)

while get_qstn.still_has_questions():
    get_qstn.next_question()

print("You've completed the quiz")
print(f"Your final score was {get_qstn.score}/{get_qstn.question_number}")