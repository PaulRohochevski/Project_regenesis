# _*_ coding:utf-8 _*_
"""
This module consist of 3 classes, that named as Options, Futures, Stocks and would be imported in main module.
"""

from variables import *
import re


class Stocks(object):
    stocks_counter = 0  # Number counter of stocks

    def __init__(self, array):
        self.array = array
        Stocks.stocks_counter += 1

    def main(self):
        self.append_file()

    # Add ticker and data to final file
    def append_file(self):
        with open(RESULT_TEXT, "a") as _file:
            _file.write("stock#{} ".format(str(Stocks.stocks_counter)))
            _file.writelines(self.array)


class Futures(Stocks):
    futures_counter = 0  # Number counter of futures

    def __init__(self, array):
        self.array = array
        Futures.futures_counter += 1

    def main(self):
        self.expiration_date()
        self.append_file()

    # Changes the separator in the expiration date
    def expiration_date(self):
        m = re.split("\D", self.array[1])
        if len(self.array) == 2:
            var_m = SEPARATOR.join(m[:3]) + "\n"
        else:
            var_m = SEPARATOR.join(m[:3]) + " "
        self.array[1] = var_m

    # Add ticker and data to final file
    def append_file(self):
        with open(RESULT_TEXT, "a") as _file:
            _file.write("futures#{} ".format(str(Futures.futures_counter)))
            _file.writelines(self.array)


class Options(Futures):
    options_counter = 0  # Number counter of options

    def __init__(self, array):
        self.array = array
        Options.options_counter += 1

    # Add ticker and data to final file
    def append_file(self):
        with open(RESULT_TEXT, "a") as _file:
            _file.write("option#{} ".format(str(Options.options_counter)))
            _file.writelines(self.array)
