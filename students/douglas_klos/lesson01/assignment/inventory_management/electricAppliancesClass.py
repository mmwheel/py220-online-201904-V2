# Electric appliances class
from inventoryClass import inventory


class electricAppliances(inventory):

    def __init__(self, productCode, description, marketPrice, rentalPrice, brand, voltage):
        # Creates common instance variables from the parent class
        inventory.__init__(self, productCode, description, marketPrice, rentalPrice)
        self.brand = brand
        self.voltage = voltage

    def returnAsDictionary(self):
        outputDict = {}
        outputDict['productCode'] = self.productCode
        outputDict['description'] = self.description
        outputDict['marketPrice'] = self.marketPrice
        outputDict['rentalPrice'] = self.rentalPrice
        outputDict['brand'] = self.brand
        outputDict['voltage'] = self.voltage

        return outputDict
