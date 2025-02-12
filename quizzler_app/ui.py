from tkinter import *

# Constants for styling
THEME_COLOR = "#375362"
FONT_NAME = "Arial"

class QuizInterface:
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain

        # Set up the main window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score label (top-right)
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=(FONT_NAME, 12))
        self.score_label.grid(row=0, column=1)

        # Canvas to display the question text
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280,
            text="Question",
            fill=THEME_COLOR,
            font=(FONT_NAME, 16, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # True button
        self.true_button = Button(text="True", command=self.true_pressed, highlightthickness=0, font=(FONT_NAME, 12))
        self.true_button.grid(row=2, column=0)

        # False button
        self.false_button = Button(text="False", command=self.false_pressed, highlightthickness=0, font=(FONT_NAME, 12))
        self.false_button.grid(row=2, column=1)

        # Load the first question
        self.get_next_question()

        # Start the GUI event loop
        self.window.mainloop()

    def get_next_question(self):
        """Fetch and display the next question from the quiz."""
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            # No more questions: show final score and disable buttons.
            self.canvas.itemconfig(
                self.question_text,
                text=f"You've completed the quiz.\nYour final score was: {self.quiz.score}/{len(self.quiz.question_list)}"
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        """Handler for when the True button is pressed."""
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        """Handler for when the False button is pressed."""
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        """Change canvas background to green if correct or red if wrong; then load next question."""
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        # Wait for 1 second before showing the next question.
        self.window.after(1000, self.get_next_question)
