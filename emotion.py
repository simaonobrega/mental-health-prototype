from abc import ABC, abstractmethod


class Emotion(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def score(self):
        pass

    @property
    @abstractmethod
    def message(self):
        pass

