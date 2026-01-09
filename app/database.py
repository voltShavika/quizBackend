from pymongo import MongoClient

MONGO_URI = "mongodb+srv://shavika:Test123@cluster0.evijg.mongodb.net/?appName=quizdb"

client = MongoClient(MONGO_URI)
db = client.quizdb

users = db.users
quizzes = db.quizzes
attempts = db.attempts