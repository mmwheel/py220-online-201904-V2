#!/usr/bin/env python3
'''
This class is for electric appliances
'''
from store_inventory import Inventory


# pylint: disable=R0903
# pylint: disable=R0913
class ElectricAppliances(Inventory):
    '''
    Here we have the Inventory management for electric appliances, below it is
    identified with product code, description, market and rental prices, brand,
    and... voltage I guess.
    '''

    def __init__(self, product_code, description, market_price, rental_price,
                 brand, voltage):
        '''
        Creates common instance variables from the parent class
        '''
        Inventory.__init__(self, product_code, description, market_price,
                           rental_price)

        self.brand = brand
        self.voltage = voltage

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
        output_dict['brand'] = self.brand
        output_dict['voltage'] = self.voltage

        return output_dict
