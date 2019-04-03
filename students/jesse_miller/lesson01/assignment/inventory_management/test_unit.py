#!/usr/bin/env python3
'''
Testing methods for first lesson in Python220
'''
# import sys
from unittest import TestCase
from unittest.mock import Mock, MagicMock
import pytest
import electric_appliances
import home_furniture
import store_inventory
import market_prices
from main import main_menu
# sys.path.append('/Users/jmiller/School/Python_220/students/jesse_miller/\
#                lesson01/assignment/')

'''
I tried just importing the directory, but no love.
'''

###############################################################################
#
# Starting with electric_appliances.py
#
###############################################################################


class ElectricAppliancesTest(TestCase):
    '''
    Testing electric_appliances addition to dict.
    '''
    def test_return_as_dict(self):
        '''
        In this we will be making sure that output_dict functions correctly.
        '''
        electric_test = electric_appliances. \
            ElectricAppliances('12345', 'Testing', '123.45', '12.34',
                               'Testing Inc', '123.4')
        electric_dict_test = electric_test.return_as_dict()
        self.assertEqual(electric_dict_test, {'product_code': '12345',
                                              'description': 'Testing',
                                              'market_price': '123.45',
                                              'rental_price': '12.34',
                                              'brand': 'Testing Inc',
                                              'voltage': '123.4'})

###############################################################################
#
# Moving to home_furniture.py
#
###############################################################################


class HomeFurnatureTests(TestCase):
    '''
    Testing electric_appliances addition to dict.
    '''
    def test_return_as_dict(self):
        '''
        In this we will be making sure that output_dict functions correctly.
        '''
        furnature_test = home_furniture. \
            FurnitureClass('12345', 'Testing', '123.45', '12.34',
                           'Fur', '123')
        furnature_dict_test = furnature_test.return_as_dict()
        self.assertEqual(furnature_dict_test, {'product_code': '12345',
                                               'description': 'Testing',
                                               'market_price': '123.45',
                                               'rental_price': '12.34',
                                               'material': 'Fur',
                                               'size': '123'})
