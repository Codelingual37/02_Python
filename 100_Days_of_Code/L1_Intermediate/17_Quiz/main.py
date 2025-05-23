from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random

question_bank = []
set = random.choice(question_data)

for question in set:
	new_question = Question(question["question"], question["correct_answer"])
	question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while (quiz.still_has_questions()):
	quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score is {quiz.score}/{len(question_bank)}")