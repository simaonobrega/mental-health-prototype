import tkinter as tk


class View:
    def __init__(self, controller, model):
        self._controler = controller
        self._model = model
        self.main_window = tk.Tk()

    def open_main_screen(self):
        self.main_window.title("Mental Health software")

        label = tk.Label(self.main_window, text="Welcome to the Program!")
        label.pack()

        stats_button = tk.Button(self.main_window, text="Go to Statistics")
        stats_button.pack()

        form_button = tk.Button(self.main_window, text="Fill Out Form",
                                command=lambda:
                                self.present_depression_checklist())
        form_button.pack()

        self.main_window.mainloop()

    def present_depression_checklist(self):
        checklist_window = tk.Toplevel(self.main_window)
        checklist_window.title("Depression Checklist")

        # Dictionary to store the IntVar associated with each question's set
        # of radio buttons
        user_answers = {}

        # Create a header row for answer options
        for score, desc in self._model.depression_checklist.response_options.items():
            header_label = tk.Label(checklist_window, text=desc)
            header_label.grid(row=0, column=score + 1, padx=10,
                              pady=10)  # Adjust the padding as needed

        # Create the question rows with radio buttons for answer options
        for idx, question in enumerate(
                self._model.depression_checklist.questions):
            # Label for the question
            question_label = tk.Label(checklist_window, text=question)
            question_label.grid(row=idx + 1, column=0, sticky='w', padx=10,
                                pady=2)  # Align left (west)

            # IntVar to store the answer to this question
            user_answers[idx] = tk.IntVar(value=0)  # Default value

            # Create a radio button for each response option
            for score in self._model.depression_checklist.response_options:
                radio_button = tk.Radiobutton(checklist_window,
                                              variable=user_answers[idx],
                                              value=score)
                radio_button.grid(row=idx + 1, column=score + 1, padx=10,
                                  pady=2)
