
class Flashcard:
    def __init__(self, word: Word, usage_example: UsageExample, hanzi: Hanzi, radicals: List[Radical], idioms: List[Idiom]):
        self.word = word
        self.usage_example = usage_example
        self.hanzi = hanzi
        self.radicals = radicals
        self.idioms = idioms
    
    def generate_flashcard(self, user_selection):
        # Generate the flashcard based on the user's selection
        pass

class Word:
    def __init__(self, word: str, pronunciation: str, definition: str):
        self.word = word
        self.pronunciation = pronunciation
        self.definition = definition

class UsageExample:
    def __init__(self, usage_example: str):
        self.usage_example = usage_example

class Hanzi:
    def __init__(self, hanzi: str, pinyin: str, meaning: str):
        self.hanzi = hanzi
        self.pinyin = pinyin
        self.meaning = meaning

class Radical:
    def __init__(self, radical: str, meaning: str):
        self.radical = radical
        self.meaning = meaning

class Idiom:
    def __init__(self, idiom: str, pinyin: str, meaning: str):
        self.idiom = idiom
        self.pinyin = pinyin
        self.meaning = meaning
