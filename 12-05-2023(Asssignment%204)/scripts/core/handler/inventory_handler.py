from scripts.schemas.inventory_schemas import Item
import pymongo
from pymongo import MongoClient
from scripts.db.mongo import collection
import logging
from scripts.logging.logs import getLogger

getLogger()


class Item_handler:

    def add_item(self, item_id: int, item: Item):
        try:
            if list(collection.find({"item_id": item_id})):
                return {"error": "This ID is already present"}

            collection.insert_one(item.dict())
            logging.info({"message": "Successfully Added"})
            return {"message": "Successfully Added"}

        except Exception as e:
            logging.error({"error": str(e)})
            return {"error": str(e)}

    def delete_item(self, item_id: int):
        try:
            if list(collection.find({"item_id": item_id})) == []:
                logging.debug({"error", "Item not found"})
                return {"error", "Item not found"}

            else:
                collection.delete_one({"item_id": item_id})
                logging.info({"Message": "Item deleted succesfully"})
                return {"Message": "Item deleted succesfully"}

        except Exception as e:
            logging.error({"error": str(e)})
            return {"error": str(e)}

    def update_item(self, item_id: int, item: Item):
        try:
            if list(collection.find({"item_id": item_id})) != []:
                collection.update_one({"item_id": item_id}, {
                                      "$set": item.dict()})
                logging.info({"Message": "It is updated successfully"})
                return {"Message": "It is updated successfully"}

            else:
                logging.debug({"error": "Item not found"})
                return {"error": "Item not found"}

        except Exception as e:
            logging.debug({"error": str(e)})
            return {"error": str(e)}

    def total_price(self):
     try:
        item_price = [item["item_price"] * item["item_volume"]
                      for item in collection.find()]
        total_price = sum(item_price)
        return total_price
     except Exception as e:
        return {"Error:":"Error while calculating the total price"}

    def fetch(self):
     try:
        items = list(collection.find({}, {'_id': 0}))
        return items
     except Exception as e:
        return {"error": str(e)}
        logging.error({"error": str(e)})


    def find_total(self):
     try:
        total = collection.aggregate([
            {
                '$project': {
                    '_id': 0,
                    'mul': {
                        '$multiply': [
                            '$item_price', '$item_volume'
                        ]
                    }
                }
            }, {
                '$group': {
                    '_id': None,
                    'Total_Price': {
                        '$sum': '$mul'
                    }
                }
            }, {
                '$project': {
                    '_id': 0
                }
            }
        ])
        return (list(total))[0]['Total_Price']
     except Exception as e:
         logging.error({"Error:":"Unexpected error while using the aggregate function"})
        
