

class FactoryObject():

    def __init__(self, **kwargs):
        for k in kwargs.keys():
            self.__setattr__(k, kwargs[k])
        pass

    def get(self, attr):
        return self.__getattribute__(attr)

    def do(self, data):
        pass


