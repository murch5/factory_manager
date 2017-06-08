
import inspect as inspect
import sys as sys

class FactoryManager():

    def __init__(self):
        self.obj_list = []
        self.available_class_types = {}
        self.module = self.set_module()

        pass

    def add_class_object(self, type, settings):

        new_class_obj = self.available_class_types[type](**settings)
        self.obj_list.append(new_class_obj)

        pass

    def evaluate_stack(self):

        for obj in self.obj_list:
            obj.do()
        pass

    def pass_thru_stack(self, input):
        output = input
        for obj in self.obj_list:
            output = obj.do(output)
        pass

        return output

    def get_available_class_types(self):

        module_list = inspect.getmembers(self.module, inspect.isclass)
        self.available_class_types = dict(module_list)

        pass

    def set_module(self):
        pass


