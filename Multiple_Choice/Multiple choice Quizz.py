questions = ["Em que ano foi fundado o Reino de Portugal?\n(a) - 1139\n (b) - 1974\n (c) - 1243\n (d) - 1138\nAnswer:", 
             "O filho mais novo do Elon Musk chama-se:\n(a) - Quim Musk\n (b) - X AE A-XII Musk\n (c) - Djibril al-Muhalim Silva Musk\n (d) - Exa Dark Sideræl Musk\nAnswer:", 
             " Um alentejano entra num bar. Quem ganhou a piada?\n(a) - o português\n(b) - o alentejano\n(c) - o francês\n(d) - o inglês\nAnswer:",
             "A avelã é um fruto de que árvore?\n(a) - Aveladeira \n(b) - Aveleira\n(c) - Avelinha\n(d) - Caravalho\nAnswer:"]

class question():
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

quizz  = [question(questions[0],"a"), question(questions[1],"d"),question(questions[2],"a"),question(questions[3],"b")]

def pop_quizz():
    score=0
    print("Welcome to your pop Quizz!")
    lol = input("Are you ready? ")
    print("of couse not, it's a surprise pop quizz IN PORTUGUESE, MUAHAHAH, enjoy")
    for question in quizz:
        answer = input(question.prompt)
        if answer == question.answer:
            score = score + 1
            print("Good job, honeybuns!")
        else:
            print("No, dumbass, it was.. the other one, you failed")
    print ("Well, Pop Quizz finished, your final score was")
    print(input("*Drumroll*"))
    print (f"{score} not bad, sport!")

class pessoa():
    def __init__(self, nome, curso, nota):
        self.nome = nome
        self.curso = curso
        self.nota = nota

    def quadro_de_honra(self):
        if self.nota > 18:
            return True
        else:
            return False
        
pessoa1 = pessoa("Zé","Medicina", 19)

print(pessoa1.quadro_de_honra())