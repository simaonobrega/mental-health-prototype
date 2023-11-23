from emotion import Emotion


class SadEmotion(Emotion):

    emojy = "\U0001F61E"

    @property
    def name(self):
        return 'Sadness'

    @property
    def score(self):
        return 1

    @property
    def message(self):
        return "present sad emotion"
