# _*_ coding:utf-8 _*_
"""
This module consist of 3 classes, that named as Options, Futures, Stocks and would be imported in main module.
"""

from variables import *


class Stocks(object):
    def __init__(self, array):
        self.array = array

    def main(self):
        self.append_file()

    def append_file(self):
        with open(RESULT_TEXT, "a") as _file:
            _file.writelines(self.array)


class Futures(Stocks):
    def __init__(self, array):
        self.array = array


class Options(Futures):
    def __init__(self, array):
        self.array = array
