class QuizBrain:
    
    def __init__(self, q_list):
        self.questionNumber = 0
        self.score = 0
        self.questionlist = q_list
        
    def stillHasQuestions(self):
        return self.questionNumber < len(self.questionlist)
        
    def nextQuestion(self):
        currentQuestion = self.questionlist[self.questionNumber]
        answer = input(f"Q.{self.questionNumber+1} {currentQuestion.text} (True/False)? ")
        self.questionNumber += 1
        self.checkAnswer(answer, currentQuestion.answer)
        
    def checkAnswer(self, answer, correctAnswer):
        if answer.lower() == correctAnswer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"Your current score is: {self.score}/{self.questionNumber}")
        print(f"The correct answer was: {correctAnswer}")
