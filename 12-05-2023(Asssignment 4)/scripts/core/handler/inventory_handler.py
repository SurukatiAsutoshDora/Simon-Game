from scripts.schemas.inventory_schemas import Item
import pymongo
from pymongo import MongoClient
from scripts.constants.db_constants import DatabaseConstants
from scripts.db.mongo import collection
import logging
from scripts.db.mongo import collection

class Item_handler:
 
    def add_item(self, item_id: int, item: Item):
     try:
        if list(collection.find({"item_id": item_id})):
            return {"error": "This ID is already present"}
            logging.debug({"error": "This ID is already present"})
        collection.insert_one(item.dict())
        return {"message": "Successfully Added"}
        logging.info({"message": "Successfully Added"})
        
        
     except Exception as e:
        return {"error": str(e)}
        logging.error({"error": str(e)})
        
    def delete_item(self,item_id: int):
     try:   
        if list(collection.find({"item_id":item_id})) == []:
            return{"error", "Item not found"}
            logging.debug({"error", "Item not found"})
        else:
            collection.delete_one({"item_id":item_id})
            return{"Message":"Item deleted succesfully"}
            logging.info({"Message":"Item deleted succesfully"})
            
     except:
        return {"error": str(e)}    
        logging.error({"error": str(e)})
        
            
    
    def update_item(self,item_id: int, item: Item):
     try:
        if list(collection.find({"item_id":item_id})) != []:
            collection.update_one({"item_id": item_id}, {"$set": item.dict()})
            return {"Message":"It is updated successfully"}
            logging.info({"Message":"It is updated successfully"})
        else:
            return {"error": "Item not found"}
            logging.debug({"error": "Item not found"})
     except:
        return {"error": str(e)}
        logging.debug({"error": str(e)})
            
         
            
  
    # def total_price(self, collection: dict) -> dict:
    #     try:
    #         item_list = [collection[key]["item_price"] * collection[key]["item_volume"] for key in collection]
    #         total_price = sum(item_list)
    #         return {"total_price": total_price}

        
    def fetch(self):
     try:
        items = list(collection.find({}))
        final_items = []
        for each in items:
            del each["_id"]
            final_items.append(each)
        return final_items
     except Exception as e:
        return {"error": str(e)}
        logging.error({"error": str(e)})
         
