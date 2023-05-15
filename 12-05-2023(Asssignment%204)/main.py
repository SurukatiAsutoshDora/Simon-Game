from fastapi import FastAPI
from scripts.services.inventory_services import item_router
import logging
from scripts.logging.logs import getLogger

getLogger()

app = FastAPI()
item_data = {}

try:
    app.include_router(item_router)
except :
    logging.error({"Error:":"Unexpected scenario happened with the router"})    


