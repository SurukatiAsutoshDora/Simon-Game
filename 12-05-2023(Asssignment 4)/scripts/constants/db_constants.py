import logging
class DatabaseConstants:
 """ this class is used to create database constants """       
 try:
    database_name = "interns_b2_23"
    collection_name = "Asutosh_Dora"
    uri="mongodb://localhost:27017/interns_b2_23"
 except Exception as e:
     logging.error({"Error:": "Unexpected error occured while connecting with Database"})

db_constant_object=DatabaseConstants()
