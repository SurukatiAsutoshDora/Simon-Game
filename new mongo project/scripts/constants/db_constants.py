import logging
from scripts.logging.logs import logger


class DatabaseConstants:
    try:
        """ this class is used to create database constants """
        database_name = "interns_b2_23"
        collection_name = "Asutosh_Dora"
        uri = "mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23"
        set_level = logging.DEBUG
        aggregate=[
            {
                '$addFields': {
                    'total_amount': {
                        '$multiply': [
                            '$item_price', '$item_volume'
                        ]
                    }
                }
            }, {
                '$group': {
                    '_id': None, 
                    'total': {
                        '$sum': '$total_amount'
                    }
                }
            }, {
                '$project': {
                    '_id': 0
                }
            }
]
    except Exception as e:
        logging.error({"error:": "error"})


db_constant_object = DatabaseConstants()
