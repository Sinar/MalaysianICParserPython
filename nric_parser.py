import re
import datetime


class ICParser:
    def __init__(self,ic):
        ic_with_dash = r'\d{6}-\d{2}-\d{4}'
        ic_digits_only = r'\d{12}'
        ic_split_pattern = r'(\d{6})(\d{2})(\d{4})'
        if re.match(ic_digits_only,ic):
            ic_token = re.split(ic_split_pattern,ic)
            ic_token = [i for i in splitted if i]
        elif re.match(ic_with_dash,ic):
            ic_token = ic.split('-')
        else:
            raise InvalidFormatException(ic)
         

class InvalidFormatException(Exception):
    def __init__(self,value):
        self.value = value
    
    def __str__(self):
        return repr(self.value)


class InvalidDateException(Exception):
    def __init__(self,value):
        self.value = value
    
    def __str__(self):
        return repr(self.value)


class InvalidBirthPlace(Exception):
    def __init__(self,value):
        self.value = value
    
    def __str__(self):
        return repr(self.value)
   
