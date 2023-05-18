from configparser import ConfigParser

config = ConfigParser()
config.read("config/application.conf")


class Service:
    port = config["SERVICE"]["port"]
    host = config["SERVICE"]["host"]
    uri = config["MONGO_DB"]["uri"]
    database_name = config["MONGO_DB"]["database_name"]
    collection_name = config["MONGO_DB"]["collection_name"]
    set_level = config["LOGGER_LEVEL"]["set_level"]


service_object=Service()