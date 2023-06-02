import random


class Answer:
    def __init__(self, answer_txt):
        self.answer_txt = answer_txt


class Question:
    def __init__(self, question_txt, list_answers):
        self.question_txt = question_txt
        self.list_answers = list_answers


class Test:
    list_question = []

    def __init__(self):
        self.amount_answers = 0
        self.questionGenerator()

    def questionGenerator(self):
        question_txt = input("Введите текст вопроса: ")
        self.amount_answers = int(input("Задайте количество возможных ответов: "))

        myAnswers = []
        for i in range(self.amount_answers):
            answer_txt = input(f"Введите текст {i + 1} ответа: ")
            myAnswers.append(Answer(answer_txt))

        question = Question(question_txt, myAnswers)
        Test.list_question.append(question)

    @classmethod
    def getTest(cls):
        for question in cls.list_question:
            print(f"Текст вопроса: {question.question_txt}")
            random.shuffle(question.list_answers)
            for i, answer in enumerate(question.list_answers):
                print(f"{i + 1}. Вариант ответа: {answer.answer_txt}")



myQuest1 = Test()
myQuest2 = Test()

Test.getTest()
Test.getTest()

