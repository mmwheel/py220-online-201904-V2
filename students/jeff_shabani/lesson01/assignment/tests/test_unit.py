#!/usr/bin/env python3

from changedirectory import changedirectory

changedirectory()

import os
import mock
import platform
import unittest

from pathlib import Path
from io import StringIO
from electricappliancesclass import ElectricAppliances
from furnitureclass import Furniture
from inventoryclass import Inventory
from main import *

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

    @mock.patch('builtins.input', mock.Mock(return_value='q'))
    def test_program_quit(self):
        """Test that the program quits properly"""
        d = mainmenu()
        with self.assertRaises(SystemExit):
            d = exitprogram()

        del d


    def tearDown(self):
        del self.appliance
        del self.furniture
        del self.inventory


if __name__ == '__main__':
    unittest.main()



