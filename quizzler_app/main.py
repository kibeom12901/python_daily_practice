from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface

# Create a list of Question objects from the question data.
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Create the quiz logic and pass it to the UI.
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
