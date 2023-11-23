import tkinter as tk
from standard_button_in_grid import StandardButtonInGrid


class EvaluationChecklistScreen(tk.Toplevel):
    def __init__(self, parent, controller, evaluation_checklist):
        super().__init__(parent)
        self._controller = controller
        self._evaluation_checklist = evaluation_checklist
        self.title("Evaluation Checklist")

        # Dictionary to store user's answers
        self._user_answers = {idx: tk.IntVar(value=0) for idx in
                              range(len(evaluation_checklist.get_questions()))}

        self._setup_ui()

    def _setup_ui(self):
        # Create a header row for answer options
        for score, desc in self._evaluation_checklist.get_response_options().items():
            header_label = tk.Label(self, text=desc)
            header_label.grid(row=0, column=score + 1, padx=10, pady=10)

        # Create the question rows with radio buttons
        for idx, question in enumerate(
                self._evaluation_checklist.get_questions()):
            question_label = tk.Label(self, text=question)
            question_label.grid(row=idx + 1, column=0, sticky='w', padx=10,
                                pady=2)

            # Create radio buttons for each response option
            for score in self._evaluation_checklist.get_response_options():
                radio_button = tk.Radiobutton(
                    self,
                    variable=self._user_answers[idx],
                    value=score
                )
                radio_button.grid(row=idx + 1, column=score + 1, padx=10,
                                  pady=2)

        # Add the submit button
        StandardButtonInGrid(
            parent=self,
            button_name="Submit Score",
            row=len(self._evaluation_checklist.get_questions()) + 1,
            column=0,
            command=self._submit
        )

    def _submit(self):
        # Calculate the total sum of the selected values
        total_score = sum(var.get() for var in self._user_answers.values())
        self._controller.on_submit_checklist_button(total_score)

        # Close window
        self.destroy()
