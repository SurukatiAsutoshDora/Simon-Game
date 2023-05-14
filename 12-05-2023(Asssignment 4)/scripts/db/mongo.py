from scripts.constants.db_constants import db_constant_object
from pymongo import MongoClient
import logging

try:
    client = MongoClient(db_constant_object.uri)
    mydb = client[db_constant_object.database_name]
    collection = mydb[db_constant_object.collection_name]
except Exception as e:
    logging.error({"Error:","while connecting to MongoDB"})
   
