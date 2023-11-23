from emotion import Emotion


class HappyEmotion(Emotion):

    emojy = "\U0001F600"

    @property
    def name(self):
        return 'Happiness'

    @property
    def score(self):
        return 5

    @property
    def message(self):
        return "present happy message"
