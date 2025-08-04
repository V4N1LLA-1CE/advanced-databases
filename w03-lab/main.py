import pymongo

# returns mongo client
# use this client to do all db operations
def connect_to_mongo() -> pymongo.MongoClient:
    c = pymongo.MongoClient("mongodb://localhost:27017/")
    print(c.list_database_names())

    return c

# creates the database and collection
# initialises the database
def init_mongo(client: pymongo.MongoClient) -> None:
    # TODO: initialise db and collection in that db for the lab


if __name__ == "__main__":
    client = connect_to_mongo()
