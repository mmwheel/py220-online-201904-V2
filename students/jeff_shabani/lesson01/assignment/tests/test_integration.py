#!/usr/bin/env python3

from changedirectory import changedirectory

changedirectory()

import os
import market_prices
import mock
import platform
import unittest

from pathlib import Path
from io import StringIO

import main
from main import addnewitem, ElectricAppliances, Furniture, Inventory, \
    mainmenu, exitprogram, get_latest_price

from unittest.mock import patch
from unittest.mock import MagicMock

APPLIANCE = {'productcode': 'F100',
             'description': 'Freezer',
             'marketprice': 300,
             'rentalprice': 400,
             'brand': 'GE',
             'voltage': 200}

CHAIR = {'productcode': 'C100',
         'description': 'Recliner',
         'marketprice': 900,
         'rentalprice': 1200,
         'material': 'leather',
         'size': 'large'}

GENERIC_INVETORY = {'productcode': 'AAAA',
                    'description': 'Object',
                    'marketprice': 1,
                    'rentalprice': 2}

NEW_INVETORY = {'productcode': 'NEW',
                'description': 'Brand New Item',
                'marketprice': 1000000,
                'rentalprice': 2500000}

"""The dictionarires above are used to test the functionality
of the inventory management modules"""


class TestInventoryManagement(unittest.TestCase):

    def setUp(self):
        self.appliance = ElectricAppliances(*APPLIANCE.values())
        self.furniture = Furniture(*CHAIR.values())
        self.inventory = Inventory(*GENERIC_INVETORY.values())

    def test_generic_inventory(self):
        """
        Test electric appliance dictionary output"""
        item = self.inventory
        expected = item.returnasdictionary()
        self.assertDictEqual(GENERIC_INVETORY, expected)

    def test_electric_appliance(self):
        """
        Test electric appliance dictionary output"""
        freezer = self.appliance
        expected = freezer.returnasdictionary()
        self.assertDictEqual(APPLIANCE, expected)

    def test_furniture(self):
        """
        Test furniture dictionary output"""
        recliner = self.furniture
        expected = recliner.returnasdictionary()
        self.assertDictEqual(CHAIR, expected)

    def test_get_market_price(self):
        """Test that get market price returns 24"""
        self.assertEqual(24, get_latest_price('placeholder'))

    def test_main_menu_add_new(self):
        """
        Tests for menu item 1 selection"""
        while True:
            try:
                with patch('builtins.input', side_effect='1'):
                    self.assertEqual(mainmenu(), main.addnewitem())
            except StopIteration as error:
                return error

    def test_main_get_item_info(self):
        """
        Tests for item menu 2 selection"""
        while True:
            try:
                with patch('builtins.input', side_effect='2'):
                    self.assertEqual(mainmenu(), main.addnewitem())
            except StopIteration as error:
                return error

    @mock.patch('builtins.input', mock.Mock(return_value='q'))
    def test_program_quit(self):
        """
        Test that the program quits properly"""
        with self.assertRaises(SystemExit):
            main.exitprogram()

    def tearDown(self):
        """
        Tears down setup items"""
        del self.appliance
        del self.furniture
        del self.inventory


if __name__ == '__main__':
    unittest.main()
