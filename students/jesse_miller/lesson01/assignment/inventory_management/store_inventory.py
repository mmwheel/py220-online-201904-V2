#!/usr/bin/env python3
'''
This will be our inventory class
'''


# pylint: disable=R0903
class Inventory:
    '''
    This class will track the inventory of the products housed
    '''

    def __init__(self, product_code, description, market_price, rental_price):
        self.product_code = product_code
        self.description = description
        self.market_price = market_price
        self.rental_price = rental_price

    def return_as_dict(self):
        '''
        Here we will populate the dictionary with the current inventory numbers
        for all departments.
        '''
        output_dict = {}
        output_dict['product_code'] = self.product_code
        output_dict['description'] = self.description
        output_dict['market_price'] = self.market_price
        output_dict['rental_price'] = self.rental_price

        return output_dict
