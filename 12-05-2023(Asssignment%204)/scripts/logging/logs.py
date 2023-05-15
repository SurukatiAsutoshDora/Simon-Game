import logging

def getLogger():
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(funcName)s - %(message)s',
        filename='logs/app.log',
    )

logger=getLogger()