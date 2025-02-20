import pymongo
import pymongo.mongo_client

url="mongodb+srv://khushrezzainab:48sXvWILspxphGN9@zainabk.ikmcl.mongodb.net/"

client=pymongo.MongoClient(url)

db= client["store"]