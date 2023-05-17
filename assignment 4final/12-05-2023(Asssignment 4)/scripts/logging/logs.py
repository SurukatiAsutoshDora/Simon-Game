import logging

def getLogger():
    __logger__ = logging.getLogger("")
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(funcName)s - %(message)s',
        filename='logs/app.log')
    return  __logger__
      


logger=getLogger()

