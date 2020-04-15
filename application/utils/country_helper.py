import json


class CountryHelper():

    __countries = None
    __file_name = None

    @staticmethod
    def __set_file_name():
        __class__.__file_name = 'application/data/countries.txt'

    @staticmethod
    def get_file_name():
        if __class__.__file_name is None:
            __class__.__set_file_name()
        return __class__.__file_name

    @staticmethod
    def __get_countries_from_file():
        _file = __class__.get_file_name()
        with open(_file, 'r+') as file:
            __class__.__countries = eval(file.read())
    

    @staticmethod
    def get_countries():
        if __class__.__countries is None:
            __class__.__get_countries_from_file()
        return __class__.__countries
