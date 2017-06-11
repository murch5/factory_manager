import copy as copy

class FactoryManager:


    def __init__(self, factory_type, module):
        self.module = module
        self.factory_type = factory_type


        self.factory_list = []

        pass

    def add_factory_stack(self):

        new_factory = self.factory_type(self.module)
        self.factory_list.append(new_factory)

        return new_factory

    def clone_subset(self, input = None, output = None, subset = None):

        if subset:
            cloned_obj = input.get_subset_by_name(subset)

            for obj in cloned_obj:
                output.push_class_object(copy.deepcopy(obj))

        print(output)

        return output