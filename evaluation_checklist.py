class EvaluationChecklist:
    def __init__(self):
        self._overall_score = 0

        self._questions = [
            "Feeling sad or down in the dumps",
            "Feeling unhappy or blue",
            "Questionário por finalizar..."

        ]

        self._response_options = {
            0: "Not At All",
            1: "Somewhat",
            2: "Moderately",
            3: "A Lot",
            4: "Extremely"
        }

    def get_overall_score(self):
        return self._overall_score

    def increase_overall_score(self, value):
        self._overall_score += value

    def reset_overall_score(self):
        self._overall_score = 0

    def get_questions(self):
        return self._questions

    def get_response_options(self):
        return self._response_options

    def register_checklist_score_to_db(self, score):
        pass
