from pymongo import MongoClient

uri = 'mongodb+srv://ernest:FOcgcNpxj0Y7iemh@signify.tgzf9r1.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(uri)

db = client.Signify
collection = db["Signs"]