# Author: Logan Simonis
class Question:
    def __init__(self, question, answer,):
        self.question = question
        self.answer = answer
        self.answer_fragment = ""
        for letter in self.answer:
            if letter == " ":
                self.answer_fragment += " "
            else:
                self.answer_fragment += "_ "
               
    def get_question(self):
        return self.question    
    def get_answer(self):
        return self.answer
    def getAnswerFragment(self):
        return self.answer_fragment
    def guess(self, letter):
        correct = False
        tempVar = self.answer_fragment
        self.answer_fragment = ""
        
        for i in range(len(self.answer)):
            if letter.lower() == self.answer[i].lower():
                self.answer_fragment += letter
                correct = True
            elif self.answer[i] == " ":
                self.answer_fragment += " "
            else:
                self.answer_fragment += tempVar[i]
            
        return correct
