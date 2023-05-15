from scripts.constants.db_constants import db_constant_object
from pymongo import MongoClient
import logging
from scripts.logging.logs import logger



try:
    client = MongoClient(db_constant_object.uri)
    mydb = client[db_constant_object.database_name]
    collection = mydb[db_constant_object.collection_name]
    logging.info({"Message:","Succesfully connected to MongoDB"})
except Exception as e:
    logger.error({"Error:", "while connecting to MongoDB"})
