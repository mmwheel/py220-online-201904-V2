#!/usr/bin/env python3
'''
This is the furniture class
'''
from store_inventory import Inventory


# pylint: disable=R0913
# pylint: disable=R0903
class FurnitureClass(Inventory):
    '''
    Creates common instance variables from the parent class
    '''
    def __init__(self, product_code, description, market_price, rental_price,
                 material, size):

        Inventory.__init__(self, product_code, description, market_price,
                           rental_price)

        self.material = material
        self.size = size

    def return_as_dict(self):
        '''
        Here we will populate the dictionary with the current Inventory
        numbers.
        '''
        output_dict = {}
        output_dict['product_code'] = self.product_code
        output_dict['description'] = self.description
        output_dict['market_price'] = self.market_price
        output_dict['rental_price'] = self.rental_price
        output_dict['material'] = self.material
        output_dict['size'] = self.size

        return output_dict
