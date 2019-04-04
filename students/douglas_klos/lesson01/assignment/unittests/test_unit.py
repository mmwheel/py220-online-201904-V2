#!/usr/bin/env python3
""" Pytest cases for inventory management classes """

# Douglas Klos
# April 3rd, 2019
# Python 220, Lesson 01
# test_unit.py

import unittest

from unittest import TestCase
from unittest.mock import MagicMock

from inventory_management.inventory_class import Inventory
from inventory_management.furniture_class import Furniture
from inventory_management.electric_appliances_class import ElectricAppliances
from inventory_management.market_prices import get_latest_price


class InventoryTests(TestCase):

    def setUp(self):
        self.product_dict = {}
        self.product_dict['description'] = 'Chair'
        self.product_dict['market_price'] = 200
        self.product_dict['rental_price'] = 50
        self.product_dict['product_code'] = 100
        self.inventory = Inventory(**self.product_dict)

    def test_init(self):
        """ Tests that inventory class initializes correctly """
        self.assertEqual(self.inventory.product_code, self.product_dict['product_code'])
        self.assertEqual(self.inventory.description, self.product_dict['description'])
        self.assertEqual(self.inventory.market_price, self.product_dict['market_price'])
        self.assertEqual(self.inventory.rental_price, self.product_dict['rental_price'])

    def test_return_as_dictionary(self):
        """ Tests that inventory class returns the expected dictionary """
        self.assertEqual(self.product_dict, self.inventory.return_as_dictionary())


class FurnitureTests(TestCase):

    def setUp(self):
        self.product_dict = {}
        self.product_dict['product_code'] = 100
        self.product_dict['description'] = 'Chair'
        self.product_dict['market_price'] = 200
        self.product_dict['rental_price'] = 50
        self.product_dict['material'] = 'Leather'
        self.product_dict['size'] = 'L'
        self.chair = Furniture(**self.product_dict)

    def test_init(self):
        """ Tests that furniture class initializes correctly """
        self.assertEqual(self.chair.product_code, self.product_dict['product_code'])
        self.assertEqual(self.chair.description, self.product_dict['description'])
        self.assertEqual(self.chair.market_price, self.product_dict['market_price'])
        self.assertEqual(self.chair.rental_price, self.product_dict['rental_price'])
        self.assertEqual(self.chair.material, self.product_dict['material'])
        self.assertEqual(self.chair.size, self.product_dict['size'])

    def test_return_as_dictionary(self):
        """ Tests that furniture class returns the expected dictionary """
        self.assertEqual(self.product_dict, self.chair.return_as_dictionary())


class ApplianceTest(TestCase):

    def setUp(self):
        self.product_dict = {}
        self.product_dict['product_code'] = 8942
        self.product_dict['description'] = 'Oven'
        self.product_dict['market_price'] = 600
        self.product_dict['rental_price'] = 200
        self.product_dict['brand'] = 'Topf and Sons'
        self.product_dict['voltage'] = 230
        self.oven = ElectricAppliances(**self.product_dict)

    def test_init(self):
        """ Tests that electric appliance class initializes correctly """
        self.assertEqual(self.oven.product_code, self.product_dict['product_code'])
        self.assertEqual(self.oven.description, self.product_dict['description'])
        self.assertEqual(self.oven.market_price, self.product_dict['market_price'])
        self.assertEqual(self.oven.rental_price, self.product_dict['rental_price'])
        self.assertEqual(self.oven.brand, self.product_dict['brand'])
        self.assertEqual(self.oven.voltage, self.product_dict['voltage'])

    def test_return_as_dictionary(self):
        """ Tests that electric appliance returns the expected dictionary """
        self.assertEqual(self.product_dict, self.oven.return_as_dictionary())


class MarketPricesTest(TestCase):

    def test_get_latest_price(self):
        """
        Tests that get latest price returns the expected value.
        In this case, the expected value is what we pass in.
        The function is very broken.
        """
        self.assertEqual(get_latest_price(100), 100)
        self.assertEqual(get_latest_price(1000), 1000)
        self.assertEqual(get_latest_price(-100), -100)
        self.assertEqual(get_latest_price(-1000), -1000)


if __name__ == '__main__':
    unittest.main()
