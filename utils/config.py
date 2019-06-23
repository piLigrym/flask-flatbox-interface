import json


class ParserConfig:

    def __init__(self, path):
        self.__path = path
        with open(path, 'r') as f:
            self.__config = json.load(f)

    def __getitem__(self, item):
        return self.__config[item]
