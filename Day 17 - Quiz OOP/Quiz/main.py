from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questionBank = []

for result in question_data:

    question = result["text"]
    answer = result["answer"]

    final = Question(question, answer)
    questionBank.append(final)

quiz = QuizBrain(questionBank)

while quiz.StillHasQuestions():
    quiz.qGet()

print("You have completed the quiz!")
print(f"Your score was {quiz.score}/{len(questionBank)}")