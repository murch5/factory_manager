
import logging
logger = logging.getLogger(__name__)


class FactoryObject():

    def __init__(self, kwargs = None):

        self.child_objects = None

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

    def add_child_object(self, obj):
        if self.child_objects is not None:
            self.child_objects.append(obj)
        else:
            self.child_objects = [obj]
        pass


    def push_all(self,key,value):
        for obj in self.child_objects:
            obj.set(key,value)
        pass

    def push_attr(self,index,key,value):
        self.child_objects[index].set(key,value)
        pass

    def call_all(self, func, input=None):
        output = None
        if input.any():
            output = input
            for obj in self.child_objects:
                input = obj.get(func)(output)

        else:

            for obj in self.child_objects:
                obj.get(func)()

        return output

    def get_all(self, attr):
        return [obj.get(attr) for obj in self.child_objects]

    def call(self, index, func):
        self.child_objects[index].get(func)()
        pass