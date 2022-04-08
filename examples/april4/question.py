class Question:
    def __init__(self, prompt, answer1, answer2, answer3, answer4, correct_answer):
        self.prompt = prompt
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.answers = (answer1, answer2, answer3, answer4)
        self.correct_answer = correct_answer
    
    def display_answers(self):
        for i in range(len(self.answers)):
            print(f"{i+1}. {self.answers[i]}")
    
    def is_correct(self, answer):
        if answer == self.correct_answer + 1:
            return True
        else:
            return False