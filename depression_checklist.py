class DepressionChecklist:
    def __init__(self):
        self._overall_score = 0

        self.questions = [
            "Feeling sad or down in the dumps",
            "Feeling unhappy or blue",
            # ... (other questions)
        ]

        self.response_options = {
            0: "Not At All",
            1: "Somewhat",
            2: "Moderately",
            3: "A Lot",
            4: "Extremely"
        }

    def increase_overall_score(self, value):
        self._overall_score += value

    def reset_overall_score(self):
        self._overall_score = 0

    def get_question(self, question_number):
        if 0 <= question_number < len(self.questions):
            return self.questions[question_number]
        else:
            return "Invalid question number"

    def get_number_of_questions(self):
        return len(self.questions)


