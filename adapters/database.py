import asyncio
import motor.motor_asyncio

# Connect to MongoDB database
client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
db = client['mydatabase']


# Define a coroutine to find documents in the database
async def find_documents(collection_name, query):
    collection = db[collection_name]
    cursor = collection.find(query)
    results = []
    async for document in cursor:
        results.append(document)
    return results

# Run some example coroutines
async def run_examples():
    # Insert a document into the "words" collection
    document = {'word': 'hello', 'translation': '你好'}
    result = await insert_document('words', document)
    print(f'Inserted document with ID {result}')

    # Find documents in the "words" collection
    query = {'translation': '你好'}
    results = await find_documents('words', query)
    print(f'Found {len(results)} documents matching query {query}')

# Run the example coroutines
loop = asyncio.get_event_loop()
loop.run_until_complete(run_examples())
