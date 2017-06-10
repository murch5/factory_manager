
import inspect as inspect
import sys as sys

import logging

logger = logging.getLogger(__name__)

class FactoryStack():

    def __init__(self, module):
        self.obj_list = []
        self.module = module
        self.available_class_types = self.get_available_class_types()

        logger.debug("------ Available class types: " + str(self.available_class_types))

        self.initialize_attr()

        pass

    def add_class_object(self, type, settings):

        logger.debug("------ Add new class obj - type: " + str(type))
        logger.debug("------ From available class: " + str(self.available_class_types))
        logger.debug("------ Initialization settings: " + str(settings))
        new_class_obj = self.available_class_types[type](settings)
        self.obj_list.append(new_class_obj)
        pass

    def push_class_object(self,new_obj):
        self.obj_list.append(new_obj)
        pass

    def get_obj_list(self):
        return self.obj_list

    def evaluate_stack(self):
        for obj in self.obj_list:
            obj.do(None)
        pass

    def pass_thru_stack(self, input):
        output = input
        for obj in self.obj_list:
            output = obj.do(output)
        pass
        return output

    def initialize_attr(self):
        pass

    def get_available_class_types(self):
        module_list = inspect.getmembers(self.module, inspect.isclass)
        return dict(module_list)

        pass

    def generate_obj_name_list(self):
        obj_name_list = []
        for obj in self.obj_list:
            obj_name_list.append(obj.get_name())

        return obj_name_list


    def get_subset_by_name(self,name_list=None):

        subset = []
        obj_name_list = self.generate_obj_name_list()

        #Generate object name list
        if name_list:
            for name in name_list:
                if name in obj_name_list:
                    subset.append(self.obj_list[obj_name_list.index(name)])
        else:
            logger.warning("No name list for subset operation - skipping...")

        return subset