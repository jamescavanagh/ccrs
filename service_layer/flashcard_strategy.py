from abc import ABC, abstractmethod
from .models import Word, UsageExample, Hanzi, Radicals, Idioms

class FlashcardStrategy(ABC):
    @abstractmethod
    def choose_options(self, options):
        pass

class WordStrategy(FlashcardStrategy):
    def choose_options(self, options):
        pass

class UsageExampleStrategy(FlashcardStrategy):
    def choose_options(self, options):
        pass

class HanziStrategy(FlashcardStrategy):
    def choose_options(self, options):
        pass

class RadicalsStrategy(FlashcardStrategy):
    def choose_options(self, options):
        pass

class IdiomsStrategy(FlashcardStrategy):
    def choose_options(self, options):
        pass
