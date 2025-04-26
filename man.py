from question_model import Question
import html
import data
from quiz_brain import QuizBrain
from ui import QuizzInterface

question_bank = []
question_data = data.question_data()
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(html.unescape(question_text), html.unescape(question_answer))
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_gui = QuizzInterface(quiz)

