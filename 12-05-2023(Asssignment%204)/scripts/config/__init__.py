from configparser import ConfigParser

config = ConfigParser()
config.read("config/application.conf")


class Service:
    port = config["SERVICE"]["port"]
    host = config["SERVICE"]["host"]
    uri = config["MONGO_DB"]["uri"]
