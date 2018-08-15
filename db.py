from pymongo import MongoClient
from bson.objectid import ObjectId

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri)
db = client.get_default_database()

def get_all_posts():
    return db['posts'].find()
  
def find_post_by_id(post_id):
  return db["posts"].find_one({'_id': ObjectId(post_id)})

def delete_post(post_id):
  db['posts'].delete_one({'_id': ObjectId(post_id)})
