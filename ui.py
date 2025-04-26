from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"



class QuizzInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20,pady=10,bg=THEME_COLOR)


        self.score = Label(text="Score: 0")
        self.score.config(bg=THEME_COLOR, fg="White")
        self.score.grid(row=0,column=1, pady=20)

        self.canvas = Canvas(width=300, height=300)
        self.question_text = self.canvas.create_text(150, 150, text="Kanye Quote Goes HERE",width=290, font=("Arial", 15, "bold","italic"), fill="black")
        self.canvas.config(bg="white")
        self.canvas.grid(row=1,column=0,columnspan=2)



        self.correct_img = PhotoImage(file="images/true.png")
        self.correct_btn = Button(image=self.correct_img)
        self.correct_btn.config(highlightthickness=0, command=self.true_check)
        self.correct_btn.grid(row=2,column=0, pady=20)

        self.wrong_img = PhotoImage(file="images/false.png")
        self.wrong_btn = Button(image=self.wrong_img)
        self.wrong_btn.config(highlightthickness=0, command=self.false_check)
        self.wrong_btn.grid(row=2,column=1, pady=20)
        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_text, fill="black")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=question)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Congratulation!!! You've completed the quizz\n"
                                                            f"Your final score is {self.quiz.score}/{self.quiz.question_number}",font=("Calibri", 20, "bold"))
            self.correct_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")
    def true_check(self):
        self.give_feedback(self.quiz.check_answer("true"))
        self.score.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")

    def false_check(self):
        self.give_feedback(self.quiz.check_answer("false"))
        self.score.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.question_text, fill="white")
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.question_text, fill="white")


        self.window.after(1000, self.get_next_question)


