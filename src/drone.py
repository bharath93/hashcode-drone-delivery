import numpy as np

class Drone:

    def __init__(self, position, max_load, current_load=0, products=[]):

        self.location = position
        self.max_load = max_load
        self.current_load = current_load
        self.products = products

    def check_load(self, product_weight):

        if self.current_load + product_weight > self.max_load:
            return True
        else:
            return False
        
    def check_product(self, product_type):

        if product_type in self.products:
            return True
        else:
            return False

    def load_product(self, product_type, product_weight):

        if self.check_load(product_weight):
            self.products = self.products.append(product_type)
            self.current_load += product_weight
        
        else:
            raise Exception("Cannot Load product type {} due to breach of Max Load".format(product_type))
        
        return

    def unload_product(self, product_type, product_weight):

        if self.check_product(product_type):
            self.products = self.products.remove(product_type)
            self.current_load -= product_weight

        else:
            raise Exception("Product Type {} no in drone's inventory!")
        
        return

    




