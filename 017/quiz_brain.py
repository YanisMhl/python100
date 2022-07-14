class QuizBrain:
    
    def __init__(self, q_list):
        self.questionNumber = 0
        self.questionlist = q_list
        
    def stillHasQuestions(self):
        return self.questionNumber < len(self.questionlist)
        
    def nextQuestion(self):
        currentQuestion = self.questionlist[self.questionNumber]
        answer = input(f"Q.{self.questionNumber+1} {currentQuestion.text} (True/False)? ")
        self.questionNumber += 1