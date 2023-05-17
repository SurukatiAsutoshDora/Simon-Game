from scripts.schemas.inventory_schemas import Item
from scripts.utils.mongo_utility import collection
from scripts.logging.logs import logger
from scripts.constants.db_constants import db_constant_object


class Item_handler:

    def add_item(self, item_id: int, item: Item):
        try:
            if list(collection.find({"item_id": item_id})) == []:
                return {"error": "This ID is already present"}

            collection.insert_one(item.dict())
            logger.info({"message": "Successfully Added"})
            return {"message": "Successfully Added"}

        except Exception as e:
            logger.error({"error": str(e)})
            return {"error": str(e)}

    def delete_item(self, item_id: int):
        try:
            if list(collection.find({"item_id": item_id})) == []:
                logger.error({"error", "Item not found"})
                return {"error", "Item not found"}

            else:
                collection.delete_one({"item_id": item_id})
                logger.info({"Message": "Item deleted succesfully"})
                return {"Message": "Item deleted succesfully"}

        except Exception as e:
            logger.error({"error": str(e)})
            return {"error": str(e)}

    def update_item(self, item_id: int, item: Item):
        try:
            if list(collection.find({"item_id": item_id})) != []:
                collection.update_one({"item_id": item_id}, {
                                      "$set": item.dict()})
                logger.info({"Message": "It is updated successfully"})
                return {"Message": "It is updated successfully"}

            else:
                logger.error({"error": "Item not found"})
                return {"error": "Item not found"}

        except Exception as e:
            logger.error({"error": str(e)})
            return {"error": str(e)}

    def total_price(self):
        try:
            item_price = [item["item_price"] * item["item_volume"]
                          for item in collection.find()]
            total_price = sum(item_price)
            return total_price
        except Exception as e:
            logger.error({"error": str(e)})
            return {"error": str(e)}

    def fetch(self):
        try:
            items = list(collection.find({}, {'_id': 0}))
            return items
        except Exception as e:
            logger.error({"error": str(e)})
            return {"error": str(e)}

    def find_total(self):
        try:
            total = collection.aggregate(db_constant_object.aggregate)
            return (list(total))[0]['total']
        except Exception as e:
            logger.error({"error": str(e)})
            return {"error": str(e)}
