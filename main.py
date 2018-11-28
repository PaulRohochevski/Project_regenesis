import os

from tickers import *


class Concat(object):
    def __init__(self, line):
        self.line = line

    # Append new line
    def add_nl(self, number):
        if not re.search("\s$", self.line[number]):
            self.line[number] = self.line[number] + "\n"

    # Append space
    def add_space(self, number):
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
                Concat.add_space(self, 0)
                obj_f = Futures(self.line)
                obj_f.main()
            elif len(self.line) == 3:
                Concat.add_nl(self, 2)  # Object of class Options
                Concat.add_space(self, 0)
                Concat.add_space(self, 1)
                obj_o = Options(self.line)
                obj_o.main()
            else:
                raise Exception(EXCEPTION_U)


class DataParser(object):
    @staticmethod
    def parse(row):
        split_row: str = re.split(' ', row)
        var = Concat(split_row)
        var.sort()


class Reader(object):
    def __init__(self, file_vec: tuple):
        self.__validated_file_vec = self.__check_file_vec(file_vec)

    @staticmethod
    def __check_file_vec(file_vec: tuple):
        """
        Check files from vector.
        :param file_vec: tuple of file paths.
        :return:
        """
        file_array = []
        for file in file_vec:
            if os.path.isfile(file) and os.access(file, os.R_OK):
                print("File \"{}\" exists and readable".format(file))
                file_array.append(file)
            else:
                print("\"{}\" file is missing or isn't readable".format(file))
        return file_array

    # Reading text from files
    def read_text(self):
        for file in self.__validated_file_vec:
            with open(file, 'rt') as f:
                for row in f:
                    DataParser.parse(row)


if __name__ == '__main__':
    file_vec: tuple = (TEXT_FROM_A, TEXT_FROM_B)
    reader: Reader = Reader(file_vec)
    reader.read_text()

# Sort results in final file
# try:
#     _file = open(RESULT_TEXT, 'r+')
#     pos = 0
#     line = _file.readlines()
#     _file.seek(pos)
#     sort_text = sorted(line)
#     for new_line in sort_text:
#         _file.write(new_line)
#         pos = _file.tell()
#     _file.close()
# except IOError:
#     print(EXCEPTION_U)
