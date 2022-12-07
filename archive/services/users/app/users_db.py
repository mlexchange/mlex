"""
Functions to manage the users collections in the mlexchange mongo database
"""

import motor.motor_asyncio
import os

MONGO_USER = os.getenv("MONGO_INITDB_ROOT_USERNAME") # provide by docker-compose yaml file
MONGO_PASSWD = os.getenv('MONGO_INITDB_ROOT_PASSWORD')

print(MONGO_USER)
MONGO_DETAILS = "mongodb://MONGO_USER:MONGO_PASSWD@mongo:27017" # assume run from docker-compose, 
                                                            # mongo is service name
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.users

user_collection = database.get_collection("users_collection")

# Helper Functions

def user_parser(user) -> dict:
    return {
        'id': str(user["_id"]),
        "fullname": user["fullname"],
        "username": user["username"],
        "email": user["email"],
    }

async def retrieve_users():
    """
    Retrieve all users in collection
    """
    users = []
    async for user in user_collection.find():
        users.append(user_parser(user))
    return users


async def add_user(user_data: dict) -> dict:
    """
    Add new user to mlexchange
    """
    user = await user_collection.insert_one(user_data)
    new_user = await user_collection.find_one({'_id': user.inserted_id})
    return user_parser(user)


async def delete_user(id: str):
    user = await user_collection.find_one({'_id': ObjectId(id)})
    if user:
        await user_collection.delete_one({"_id": Object(id)})
        return True


