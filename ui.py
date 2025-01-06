from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        #Label creation
        self.score_label = Label(text="score :  ", fg="white", bg=THEME_COLOR, font=("Arial", 12))
        self.score_label.grid(column=1, row=0)

        #Canvas Creation
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Some other text", fill=THEME_COLOR, font=("Arial", 15, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)


        # self.card_background = self.canvas.create_image(400, 263)
        #Button creation
        wrong_img = PhotoImage(file="D:/Courses_tele/Practical/Quizzer-app/images/false.png")
        self.wrong_but = Button(image=wrong_img, highlightthickness=0, command=self.got_false)
        self.wrong_but.grid(column=0, row=2)

        right_img = PhotoImage(file="D:/Courses_tele/Practical/Quizzer-app/images/true.png")
        self.right_but = Button(image=right_img, highlightthickness=0, command =self.got_true)
        self.right_but.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="The Quiz is finished. Thank you")
            self.wrong_but.config(state="disabled")
            self.right_but.config(state="disabled")


    def got_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def got_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)