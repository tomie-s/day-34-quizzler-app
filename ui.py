from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quizz On!')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text='Score: 0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text='Text Goes Here',
            fill=THEME_COLOR,
            justify='center',
            font=('Arial', 20, 'italic')
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_btn_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_btn_img, highlightthickness=0, borderwidth=0, command=self.selected_true)
        self.true_btn.grid(column=0, row=2)

        false_btn_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_btn_img, highlightthickness=0, borderwidth=0, command=self.selected_false)
        self.false_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        self.score_label.configure(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text, fill=THEME_COLOR)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text="Quiz Over!\n\nThanks for playing.",
                                   fill=THEME_COLOR)
            self.true_btn.config(state='disabled')
            self.false_btn.config(state='disabled')

    def selected_true(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def selected_false(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
            self.canvas.itemconfig(self.question_text, fill='white')
        else:
            self.canvas.config(bg='red')
            self.canvas.itemconfig(self.question_text, fill='white')
        self.window.after(1000, self.get_next_question)
