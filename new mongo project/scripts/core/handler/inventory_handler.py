from scripts.db.mongo import item_object
from scripts.logging.logs import logger
from scripts.schemas.inventory_schemas import Item
from scripts.constants.db_constants import db_constant_object


class item_handler:
    def fetch(self):
        try:
            all_items = item_object.fetch()
            if all_items == []:
                logger.info({"Message": "No items present in the database"})
                return all_items
        except Exception as e:
            logger.error({"error": str(e)})
            return {"error": str(e)}

    def add_item(self, item_id: int, item: Item):
        try:
            if list(item_object.find_by_id({"id": item_id})) != []:
                return {"error": "item already exist"}
            return item_object.add_item(item)
        except Exception as e:
            logger.error({"error": str(e.args)})
            return {"error": str(e.args)}

    def update_item(self, item_id: int, item: Item):
        try:
            if item_object.find_by_id({"id": item_id}) == []:
                return {"error": "item does not exist"}
            return item_object.update_item(item_id, item)
        except Exception as e:
            logger.error({"error": str(e)})
            return {"error": str(e)}

    def delete_item(self, item_id: int):
        try:
            if item_object.find_by_id({"id": item_id}) == []:
                return {"error:": "item does not exist"}
            return item_object.delete_item(item_id)
        except Exception as e:
            logger.error({"error": str(e)})
            return {"error": str(e)}

    def find_total(self):
        try:
            total = item_object.get_total()
            return (list(total))[0]['total']
        except Exception as e:
            logger.error({"error": str(e)})
            return {"error": str(e)}
