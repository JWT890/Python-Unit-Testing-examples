import math

class Car:
    def __init__(self, ID, MAKE, MODEL, YEAR, COLOR, MILEAGE, PRICE_TO_DEALER, SALE_PRICE, PROFIT):
        self.__ID = ID
        self.__MAKE = MAKE
        self.__MODEL = MODEL
        self.__YEAR = YEAR
        self.__COLOR = COLOR
        self.__MILEAGE = MILEAGE
        self.__PRICE_TO_DEALER = PRICE_TO_DEALER
        self.__SALE_PRICE = SALE_PRICE
        self.__PROFIT = PROFIT

    def get_ID(self):
        return self.__ID

    def get_MAKE(self):
        return self.__MAKE

    def get_MODEL(self):
        return self.__MODEL

    def get_YEAR(self):
        return self.__YEAR

    def get_COLOR(self):
        return self.__COLOR

    def get_MILEAGE(self):
        return self.__MILEAGE

    def get_PRICE_TO_DEALER(self):
        return self.__PRICE_TO_DEALER

    def get_SALE_PRICE(self):
        return self.__SALE_PRICE

    def get_PROFIT(self):
        return self.__PROFIT

    def CAR_PROFIT(self):
        cp = self.__SALE_PRICE * self.__PRICE_TO_DEALER / self.__MILEAGE
        return cp
