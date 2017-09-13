
import inspect as inspect
import sys as sys
import io_util.xml_parse as xml_parser

import logging

logger = logging.getLogger(__name__)

class FactoryStack():

    def __init__(self, module, kwargs = None):
        self.obj_list = []
        self.module = module
        self.available_class_types = self.get_available_class_types()

        logger.debug("------ Available class types: " + str(self.available_class_types))

        if kwargs:
            for k in kwargs.keys():
                self.__setattr__(k,kwargs[k])

        self.initialize()

        pass

    def get(self, attr):
        return self.__getattribute__(attr)

    def set(self, attr, val):
        return self.__setattr__(attr, val)

    def add(self, type, settings, child_node=False):

        logger.debug("------ Add new class obj - type: " + str(type))
        logger.debug("------ From available class: " + str(self.available_class_types))
        logger.debug("------ Initialization settings: " + str(settings))
        new_class_obj = self.available_class_types[type](settings)
        if child_node==False:
            self.obj_list.append(new_class_obj)
        return new_class_obj


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

    def initialize(self):
        pass

    def push_all(self,key,value):
        for obj in self.obj_list:
            obj.set(key,value)
        pass

    def push_attr(self,index,key,value):
        self.obj_list[index].set(key,value)
        pass

    def call_all(self, func, input=None):
        output = None
        if input:
            output = input
            for obj in self.obj_list:
                input = obj.get(func)(output)

        else:

            for obj in self.obj_list:
                obj.get(func)()

        return output

    def get_all(self, attr):
        return [obj.get(attr) for obj in self.obj_list]

    def call(self, index, func):
        self.obj_list[index].get(func)()
        pass

    def populate_from_xml(self, xml):

        def recurse(xml,parent_obj):
            for child in xml:
                child_dict = xml_parser.xml_to_dict(child)
                if parent_obj is None:
                    new_obj = self.add(child.tag,child_dict.get(child.tag))
                else:
                    new_obj = parent_obj.add_child_object(self.add(child.tag,child_dict.get(child.tag),child_node=True))

                if child.find("children"):
                   recurse(child.find("children"),new_obj)
            pass

        return recurse(xml,None)
