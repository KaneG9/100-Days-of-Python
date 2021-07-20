class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {question.text} (True/False)?:")
        self.check_answer(question, answer)

    def check_answer(self, question, answer):
        if question.answer == answer:
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong!")
        print(f"The correct answer was {question.answer}")
        print(f"Your current score is: {self.score}/{self.question_number}.")

    def start_quiz(self):
        while self.question_number < len(self.question_list):
            self.next_question()
        print(f"You've completed the quiz!\nYour final was was: {self.score}/{self.question_number}.")