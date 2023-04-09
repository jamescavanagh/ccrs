from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from typing import List
from .models import Flashcard
from .models import Flashcard, Word, UsageExample, Hanzi, Radicals, Idioms


app = FastAPI()

# Define a Pydantic model for creating a new flashcard
class FlashcardCreate(BaseModel):
    word: str
    selection: List[str]


class FlashcardFactory:
    def __init__(self, word_strategy, usage_example_strategy, hanzi_strategy, radicals_strategy, idioms_strategy):
        self.word_strategy = word_strategy
        self.usage_example_strategy = usage_example_strategy
        self.hanzi_strategy = hanzi_strategy
        self.radicals_strategy = radicals_strategy
        self.idioms_strategy = idioms_strategy

    def create_flashcard(self, word_data, usage_example_data, hanzi_data, radicals_data, idioms_data, user_selection):
        word = Word(word_data['characters'], word_data['pinyin'], word_data['translation'])
        usage_examples = [UsageExample(data['chinese'], data['pinyin'], data['english']) for data in usage_example_data]
        hanzi = [Hanzi(data['character'], data['pinyin'], data['english']) for data in hanzi_data]
        radicals = [Radicals(data['character'], data['pinyin'], data['meaning']) for data in radicals_data]
        idioms = [Idioms(data['chinese'], data['pinyin'], data['english']) for data in idioms_data]

        selected_word = self.word_strategy.choose_options(word.get_options())
        selected_usage_examples = [self.usage_example_strategy.choose_options(example.get_options()) for example in usage_examples]
        selected_hanzi = [self.hanzi_strategy.choose_options(hanzi.get_options()) for hanzi


from .models import Flashcard
from .flashcard_factory import FlashcardFactory
from .flashcard_strategy import WordStrategy, UsageExampleStrategy, HanziStrategy, RadicalsStrategy, IdiomsStrategy
from .database_adapter import DatabaseAdapter

class FlashcardService:
    def __init__(self):
        self.db_adapter = DatabaseAdapter()
        self.flashcard_factory = FlashcardFactory(
            WordStrategy(),
            UsageExampleStrategy(),
            HanziStrategy(),
            RadicalsStrategy(),
            IdiomsStrategy()
        )

    async def create_flashcard(self, flashcard_data):
        # Get the necessary data from the database
        word_data = await self.db_adapter.get_word_data(flashcard_data['word'])
        usage_example_data = await self.db_adapter.get_usage_example_data(flashcard_data['word'])
        hanzi_data = await self.db_adapter.get_hanzi_data(flashcard_data['word'])
        radicals_data = await self.db_adapter.get_radicals_data(flashcard_data['word'])
        idioms_data = await self.db_adapter.get_idioms_data(flashcard_data['word'])

        # Create the flashcard using the factory and strategies
        flashcard = self.flashcard_factory.create_flashcard(
            word_data,
            usage_example_data,
            hanzi_data,
            radicals_data,
            idioms_data,
            flashcard_data['selection']
        )

        # Save the flashcard to the database
        await self.db_adapter.save_flashcard(flashcard)

        return flashcard.to_dict()
