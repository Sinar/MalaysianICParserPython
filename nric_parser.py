import re

class ICParser:
    def __init__(self,ic):
        ic_with_dash = r'\d{6}-\d{2}-\d{4}'
        if re.match(r'\d{12}',ic):
            pass
        elif re.match(ic_with_dash,ic):
            pass
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
   
