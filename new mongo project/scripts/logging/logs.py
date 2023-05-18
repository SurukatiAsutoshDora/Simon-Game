import logging
#from scripts.config import Service


# def getLogger():
#     __logger__ = logging.getLogger("")
#     logging.basicConfig(
#         format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(funcName)s - %(message)s',
#         filename='logs/app.log')
#     return __logger__
import logging

def getLogger():
    __logger__ = logging.getLogger("")
    __logger__.setLevel(logging.DEBUG)  # Set the root logger level to the desired minimum level

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(funcName)s - %(message)s')

    file_handler = logging.FileHandler('logs/app.log')
    file_handler.setLevel(logging.INFO)  # Set the file handler level to the desired level
    file_handler.setFormatter(formatter)
    __logger__.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)  # Set the console handler level to the desired level
    console_handler.setFormatter(formatter)
    __logger__.addHandler(console_handler)

    return __logger__



logger = getLogger()
