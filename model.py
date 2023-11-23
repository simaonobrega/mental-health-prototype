from emotion_factory import EmotionFactory
from evaluation_checklist import EvaluationChecklist


class Model:
    def __init__(self):
        self._evaluation_checklist = None
        self._emotion_factory = None

    def register_feeling_to_db(self):
        pass

    def create_evaluation_checklist(self):
        self._evaluation_checklist = EvaluationChecklist()

    def get_evaluation_checklist(self):
        return self._evaluation_checklist

    def create_emotion_factory(self):
        self._emotion_factory = EmotionFactory()

    def get_emotion_factory(self):
        return self._emotion_factory

    def register_checklist_score(self, score):
        self._evaluation_checklist.register_checklist_score_to_db(score)

    def load_ia_model(self):
        pass

    def compute_average_emotional_state(self):
        pass

