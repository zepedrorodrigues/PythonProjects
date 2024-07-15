from question_data import question_data

class questions():
    def __init__(self,text,answer):
        self.text = text
        self.answer = answer

def initialise_quizz():
        for x in range (len(question_data)):
            question = question_data[x]
            text = question['text']
            answer = question['answer']
            a = questions(text,answer)
            question_data[x] = a
        return question_data

class quizz_brain():
    def __init__(self,questions_list,score):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0
    
    def next_question(self):
        item = self.questions_list[self.question_number]
        answer = input(f'Q.{self.question_number+1}: {item.text} True or False? ')
        self.question_number = self.question_number +1
        if self.check_answer(item,answer) == True:
            self.score = self.score+1
            print(f'Correct Answer! You have {self.score}/{self.question_number} points.\n')
        else:
            self.score = self.score
            print(f'Wrong Answer! You have {self.score}/{self.question_number} point.\n')     
    
    def still_has_questions(self):
         if len(self.questions_list) >= (self.question_number +1):
             return True
         else:
             return False
             
    def check_answer(self,item,answer):
        if answer.lower().strip() == item.answer.lower().strip():
            return True
            
        else:
            return False
   
quizz = quizz_brain(initialise_quizz(),0)

while quizz.still_has_questions() == True:
    quizz.next_question()
else:
    print(f'End of game! You have {quizz.score} points out of {len(quizz.questions_list)}')
