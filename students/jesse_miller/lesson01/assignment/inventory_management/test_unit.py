#!/usr/bin/env python3
'''
Testing methods for first lesson in Python220
'''
# import sys
from unittest import TestCase
from unittest.mock import patch, MagicMock  # ,Mock
import pytest
import electric_appliances
import home_furniture
import store_inventory
import market_prices
import main
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

    def test_electric_dict(self):
        '''
        In this we will be making sure that output_dict functions correctly for
        inventory queries.  We do this by injecting dict input and then
        asserting that it exists when queried.
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

    def test_furnature_dict(self):
        '''
        In this we will be making sure that output_dict functions correctly for
        inventory queries.  We do this by injecting dict input and then
        asserting that it exists when queried.  As above.
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


###############################################################################
#
# And now, store_inventory.py
#
###############################################################################


class InventoryTests(TestCase):
    '''
    Testing store_inventory.py
    '''

    def test_inventory_dict(self):
        '''
        In this we will be making sure that output_dict functions correctly for
        inventory queries.  We do this by injecting dict input and then
        asserting that it exists when queried.  As above.
        '''
        inventory_test = store_inventory. \
            Inventory('12345', 'Testing', '123.45', '12.34')
        furnature_dict_test = inventory_test.return_as_dict()
        self.assertEqual(furnature_dict_test, {'product_code': '12345',
                                               'description': 'Testing',
                                               'market_price': '123.45',
                                               'rental_price': '12.34'})


###############################################################################
#
# I guess we can test market_prices, but I'm not sure of the point since it
# just returns '24' no matter what.
#
###############################################################################


class MarketPricesTests(TestCase):
    '''
    So, this will be easy.  Basically just asserting that it's '24' and not
    anything else.
    '''

    def test_market_price(self):
        '''
        As stated above.  I'm injecting a value that I know will be overwritten
        by '24'
        '''
        prices = market_prices.get_latest_price('123')
        self.assertEqual(prices, 24)


###############################################################################
#
# So, here's where it'll get complicated.  The main_menu tests are going to be
# the brunt of the testing since that's where all the interaction is.  I've
# never been to clear on input testing, but here goes.
#
###############################################################################


class MainMenuTests(TestCase):
    '''
    There's a lot going on here, basically we're going to be testing user
    input through and through.  Both injecting values from input, and mocking
    actual entries.
    '''

    dict_test_inv = {'product_code': '12345',
                     'description': 'Testing',
                     'market_price': '123.45',
                     'rental_price': '12.34'}

    dict_test_elec = {'product_code': '12345',
                      'description': 'Testing',
                      'market_price': '123.45',
                      'rental_price': '12.34',
                      'brand': 'Testing Inc',
                      'voltage': '123.4'}

    dict_test_furn = {'product_code': '12345',
                      'description': 'Testing',
                      'market_price': '123.45',
                      'rental_price': '12.34',
                      'material': 'Fur',
                      'size': '123'}
    '''
    These dicts exist to test dictionary manipulation isolated from everything
    aside from main.py   Essentially I want to make certain that main.py
    returns the right values.
    '''

    def test_menu_add(self):
        '''
        Here we test injecting a value of 1 in the menu
        '''
        while True:
            try:
                with patch('builtins.input', side_effect='1'):
                    self.assertEqual(main_menu(), main.\
                    add_new_item())
            except StopIteration as error_code:
                return error_code

    @patch('main.add_new_item', return_value=dict_test_inv)
    def test_dict_elec(self, add_new_item):
        '''
        Testing adding a new item inside main.
        '''
        dict_inv = {'product_code': '12345',
                    'description': 'Testing',
                    'market_price': '123.45',
                    'rental_price': '12.34'}
        self.assertEqual(add_new_item(), dict_inv)

    def test_exit(self):
        '''
        Testing the exit function for clean exiting of program.
        '''
        with self.assertRaises(SystemExit):
            main.exit_program()

    def test_get_latest_price(self):
        '''
        Testing pricing return
        '''
        # pylint: disable=W0201
        self.get_price = MagicMock(return_value=24)
        self.assertEqual(24, main.get_price(1))
