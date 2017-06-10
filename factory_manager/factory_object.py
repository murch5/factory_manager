

class FactoryObject():

    def __init__(self, kwargs):
        for k in kwargs.keys():
            self.__setattr__(k, kwargs[k])
        pass

    def get(self, attr):
        return self.__getattribute__(attr)

    def set(self, attr, val):
        return self.__setattr__(attr, val)

    def do(self, data):
        pass

    def get_name(self):
        return self.get("name")



