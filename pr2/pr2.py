import re
import json
import math

# class declared

class currency:
    value = 0

#constructor passed

    def __init__(self, value):
        self.value = value

#objects initialized

    def USD(self):
        result = 1 * self.value
        return result

    def USD_TO_INR(self):
        result = float(1 * self.value / 73.66) 
        return result
    
    def USD_TO_GBP(self):
        result = float(0.85 * self.value)
        return result
    
    def USD_TO_AUD(self):
        result = float(1 * self.value / 1.33)
        return result
    
    def USD_TO_JPY(self):
        result = float(1 * self.value / 112.63)
        return result

#class derived (inheritance)        

class notation(currency):
    pass

#input entered

input_value = float(input("Input currency in USD: "))
USD1 = currency(input_value)
print(USD1.USD(),"US DOLLARS")

input_value = float(input("Input currency in INR: "))
INR = currency(input_value)
print(INR.USD_TO_INR(),"US DOLLARS")

input_value = float(input("Input currency in GBP: "))
GBP = currency(input_value)
print(GBP.USD_TO_GBP(),"US DOLLARS")

input_value = float(input("Input currency in AUD: "))
AUD = currency(input_value)
print(AUD.USD_TO_AUD(),"US DOLLARS")

input_value = float(input("Input currency in JPY: "))
JPY = currency(input_value)
print(JPY.USD_TO_JPY(),"US DOLLARS")

#string matching expression
print(re.match("[A-Z a-z 0-9]+@+[a-z]+.+[a-z]","Pranavbhardhwaj98@gmail.com"))
