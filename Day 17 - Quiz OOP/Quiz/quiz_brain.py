class QuizBrain:

    def __init__(self, qList):
        self.questionNum = 0
        self.questionList = qList
        self.score = 0

    def StillHasQuestions(self):
        currentList = len(self.questionList)
        if self.questionNum < currentList:
            return True
        else:
            return False
        
        # can just return self.questionNum < currentList

    def qGet(self):
        currentQuestion = self.questionList[self.questionNum]
        self.questionNum += 1
        userAnswer = input(f"Q.{self.questionNum}: {currentQuestion.text} True/False?: ")
        self.CheckAnswer(userAnswer, currentQuestion.answer)

    def CheckAnswer(self, userAnswer, correctAnswer):
        if userAnswer.lower() == correctAnswer.lower():
            self.score += 1
            print("Correct!")
        else:
            print("Wrong!")
            print(f"The correct answer was {correctAnswer}!")
        print(f"You current score is {self.score}/{self.questionNum}!")
