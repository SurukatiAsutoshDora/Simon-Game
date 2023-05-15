import logging
from scripts.logging.logs import getLogger

getLogger()

class DatabaseConstants:
 try:    
    """ this class is used to create database constants """
    database_name = "interns_b2_23"
    collection_name = "Asutosh_Dora"
    uri = "mongodb://localhost:27017/"
 except Exception as e:
    logging.error({})    


db_constant_object = DatabaseConstants()
