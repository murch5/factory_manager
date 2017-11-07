import copy as copy

class FactoryManager:


    def __init__(self, factory_type, module):
        self.module = module
        self.factory_type = factory_type
        self.factory_list = []

        pass

    def add_factory_stack(self, kwargs = None):

        new_factory = self.factory_type(self.module, kwargs)
        self.factory_list.append(new_factory)

        return new_factory

    def clone_subset(self, input = None, output = None, subset = None):

        if subset:
            cloned_obj = input.get_subset_by_name(subset)

            for obj in cloned_obj:
                output.push_class_object(copy.deepcopy(obj))



        return(output)

    def get_factory(self):
        return self.factory_list

    def push_all(self,key,value):
        for obj in self.factory_list:
            obj.set(key,value)
        pass

    def push_attr(self,index,key,value):
        self.factory_list[index].set(key,value)
        pass

    def call_all(self, func, input=None):
        output = None
        if input:
            output = input
            for obj in self.factory_list:
                input = obj.get(func)(output)

        else:

            for obj in self.factory_list:
                obj.get(func)()


        return output

    def get_all(self, attr):
        return [obj.get(attr) for obj in self.factory_list]

    def call(self, index, func):
        self.factory_list[index].get(func)()
        pass
