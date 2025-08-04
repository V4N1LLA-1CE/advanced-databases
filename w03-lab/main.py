import pymongo

def connect_to_mongo():
    c = pymongo.MongoClient("mongodb://localhost:27017/")
    print(c.list_database_names())

    db = c["fit3176"]
    print(db.list_collection_names())

if __name__ == "__main__":
    db = connect_to_mongo()
