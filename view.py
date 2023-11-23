import tkinter as tk

from evaluation_checklist_screen import EvaluationChecklistScreen
from register_feeling_screen import RegisterFeelingScreen
from standard_button_in_grid import StandardButtonInGrid


class View:
    def __init__(self, controller):
        self._controller = controller
        self._main_window = tk.Tk()

    def display_main_screen(self):
        self._main_window.geometry("300x150")
        self._main_window.title("Mental Health software")

        # Creating buttons in a 2x2 grid
        StandardButtonInGrid(parent=self._main_window, button_name="Stats",
                             row=1, column=0)
        StandardButtonInGrid(parent=self._main_window, button_name="Checklist",
                             row=1, column=1,
                             command=self._controller.on_evaluation_checklist_button)
        StandardButtonInGrid(parent=self._main_window, button_name="Perform "
                                                                   "Analysis",
                             row=2, column=0)
        StandardButtonInGrid(parent=self._main_window, button_name="Register "
                                                                   "Feeling",
                             row=2, column=1,
                             command=self._controller.on_register_feeling_button)

        self._main_window.mainloop()

    def display_register_feeling_screen(self):
        RegisterFeelingScreen(self._main_window, self._controller)

    def display_evaluation_checklist_screen(self, evaluation_checklist):
        EvaluationChecklistScreen(self._main_window, self._controller,
                                  evaluation_checklist)
