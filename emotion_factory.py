from happy_emotion import HappyEmotion
from sad_emotion import SadEmotion


class EmotionFactory:
    """
    A factory class for creating emotion objects.
    It provides methods to create emotion objects based on their names,
    and to retrieve information about all available emotions.
    """

    def __init__(self):
        """New emotions should be added to the _emotions attribute"""
        self._emotions = {
            "Happiness": HappyEmotion,
            "Sadness": SadEmotion
        }

    def create_emotion(self, emotion):
        emotion_class = self._emotions.get(emotion)
        if emotion_class:
            return emotion_class()
        raise ValueError(f"Emotion '{emotion}' not recognized")

    def get_all_emotions(self):
        return list(self._emotions.values())

    def get_all_emojis(self):
        emojis = {}
        for emotion_name, emotion_class in self._emotions.items():
            emojis[emotion_name] = emotion_class.emojy
        return emojis
