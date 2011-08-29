import re
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
import datetime


class ICParser:
    def __init__(self,ic):
        ic_with_dash = r'\d{6}-\d{2}-\d{4}'
        ic_digits_only = r'\d{12}'
        ic_split_pattern = r'(\d{6})(\d{2})(\d{4})'
        if re.match(ic_digits_only,ic):
            self.ic_token = re.split(ic_split_pattern,ic)
            self.ic_token = [i for i in self.ic_token if i]
        elif re.match(ic_with_dash,ic):
            self.ic_token = ic.split('-')
        else:
            raise InvalidFormatException(ic)

        self.set_gender()
        self.set_birth_date()

    def set_birth_date(self):
        self.birth_date = parse(self.ic_token[0]).date()
        if self.birth_date > datetime.date.today():
            raise InvalidDateException(self.birth_date)

        today = datetime.date.today()
        date_diff = relativedelta(today,self.birth_date)
        
        if date_diff.years < 12:
            raise InvalidDateException(self.birth_date)

    def set_gender(self):
        last_no = self.ic_token[2][-1]
        if int(last_no) % 2:
            self.gender = 'M'
        else:
            self.gender = 'F'
    
    def set_birth_pace(self):
        pass      


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
   
