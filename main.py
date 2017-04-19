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
        if not re.search("\s$", self.line[number]):
            self.line[number] = self.line[number] + "\n"

    # Append spase
    def add_spase(self, number):
        if not re.search("\s$", self.line[number]):
            self.line[number] = self.line[number] + " "

    # Sort tickers
    def sort(self):
        if self.line:
            if len(self.line) == 1:
                Concat.add_nl(self, 0)  # Object of class Stocks
                obj_s = Stocks(self.line)
                obj_s.main()
            elif len(self.line) == 2:
                Concat.add_nl(self, 1)  # Object of class Futures
                Concat.add_spase(self, 0)
                obj_f = Futures(self.line)
                obj_f.main()
            elif len(self.line) == 3:
                Concat.add_nl(self, 2)  # Object of class Options
                Concat.add_spase(self, 0)
                Concat.add_spase(self, 1)
                obj_o = Options(self.line)
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

# Sort results in final file
try:
    _file = open(RESULT_TEXT, 'r+')
    pos = 0
    line = _file.readlines()
    _file.seek(pos)
    sort_text = sorted(line)
    for new_line in sort_text:
        _file.write(new_line)
        pos = _file.tell()
    _file.close()
except IOError:
    print(EXCEPTION_U)
