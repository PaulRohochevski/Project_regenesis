#!C:\Python27\python.exe
# _*_ coding:utf-8 _*_
"""
Main module.
"""
from variables import *
from tickers import *
import os
import re


class Concat(object):
    def __init__(self, line):
        self.line = line

    # Append new line
    def add_nl(self, number):
        if not re.search("\s$", self.line[number - 1]):
            line_s = []
            line_s.append(self.line[number - 1] + "\n")
        else:
            line_s = self.line
        return line_s

    # Sort tickers
    def sort(self):
        if self.line:
            if len(self.line) == 1:
                stocks_var = Concat.add_nl(self, 1)     # Object of class Stocks
                obj_s = Stocks(stocks_var)
                obj_s.main()
            elif len(self.line) == 2:
                futures_var = Concat.add_nl(self, 2)    # Object of class Futures
                obj_f = Futures(futures_var)
                obj_f.main()
            elif len(self.line) == 3:
                options_var = Concat.add_nl(self, 3)    # Object of class Options
                obj_o = Options(options_var)
                obj_o.main()
            else:
                raise Exception, EXCEPTION_U


# Parse line
def parser(line):
    pars_line = re.split(' ', line)
    var = Concat(pars_line)
    var.sort()


class Reader(object):
    # Checking text files
    def check_text():
        file_array = []
        for _ in [TEXT_FROM_A, TEXT_FROM_B]:
            if os.path.isfile(_) and os.access(_, os.R_OK):
                print ("File \"{}\" exists and is readable".format(_))
                file_array.append(_)
            else:
                print ("\"{}\" file is missing or is not readable".format(_))
        return file_array

    # Reading text from files
    def read_text(file_array):
        for _file in file_array:
            text = open(_file, 'rt')
            for line in text:
                parser(line)
            text.close()

    if __name__ == '__main__':
        read_text(check_text())
