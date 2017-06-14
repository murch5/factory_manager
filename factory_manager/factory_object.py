
import logging
logger = logging.getLogger(__name__)


class FactoryObject():

    def __init__(self, kwargs = None):


        logger.debug("Attributes: " + str(kwargs))
        for k in kwargs.keys():
            self.__setattr__(k, kwargs[k])

        self.initialize()

        pass

    def get(self, attr):
        return self.__getattribute__(attr)

    def set(self, attr, val):
        return self.__setattr__(attr, val)

    def do(self, data):
        pass

    def update_attr(self, new_attr_dict, overlap="overwrite"):

        if overlap in ["overwrite","o"]:
            for k in new_attr_dict.keys():
                self.__setattr__(k, new_attr_dict[k])

        elif overlap in ["drop","d"]:
            for k in new_attr_dict.keys():
                if k not in self.__dict__.keys():
                    self.__setattr__(k,new_attr_dict[k])

        pass

    def get_name(self):
        return self.get("name")

    def initialize(self):
        pass


