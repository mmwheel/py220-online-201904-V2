""" Pytest cases for inventory management integration """

# Douglas Klos
# April 3rd, 2019
# Python 220, Lesson 01
# test_integration.py

from inventory_management.inventory_class import Inventory
from inventory_management.furniture_class import Furniture
from inventory_management.electric_appliances_class import ElectricAppliances
from inventory_management.market_prices import get_latest_price
from main import get_price
# from unittest.mock import MagicMock
import pytest



@pytest.mark.parameterize('add_new_item', expected)
def test_get_price():
    pass