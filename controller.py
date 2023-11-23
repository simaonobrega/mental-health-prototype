from model import Model
from view import View


class Controller:
    def __init__(self):
        # Initialize the remaining MVC paradigm components
        self._model = Model()
        self._view = View(controller=self)

    def start_program(self):
        self._view.display_main_screen()

    def on_submit_feeling_button(self):
        """Save data to the SQLite DB"""
        self._model.register_feeling_to_db()
        pass

    def on_register_feeling_button(self):
        self._view.display_register_feeling_screen()

    def on_evaluation_checklist_button(self):
        self._model.create_evaluation_checklist()
        checklist = self._model.get_evaluation_checklist()
        self._view.display_evaluation_checklist_screen(checklist)

    def on_submit_checklist_button(self, score):
        self._model.register_checklist_score(score)
        pass

    def emotion_factory_requested(self):
        self._model.create_emotion_factory()
        return self._model.get_emotion_factory()
