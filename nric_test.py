import unittest
import datetime
from dateutil.relativedelta import *
from nric_parser import ICParser
from nric_parser import InvalidFormatException
from nric_parser import InvalidDateException
from nric_parser import InvalidBirthPlace

class NRICTestCase(unittest.TestCase):

    def test_ic_format_with_dash(self):
        ic = '840312-14-5543'
        parser = ICParser(ic)
        self.assertTrue(parser)
    
    def test_ic_format_with_no_only(self):
        ic = '840312145543'
        parser = ICParser(ic)
        self.assertTrue(parser)
    
    def test_ic_format_invalid_char(self):
        ic = 'aaaaaaaaaaaaa'
        self.assertRaises(InvalidFormatException,ICParser,ic)
        ic = '.)92121312213'
        self.assertRaises(InvalidFormatException,ICParser,ic)

    def test_date_format_valid(self):
        ic = '840312145543'
        parser = ICParser(ic)
        self.assertTrue(parser.birth_date)
    
    def test_date_format_invalid(self):
        ic = '841331145543'
        self.assertRaises(ValueError,ICParser,ic)
    
    def test_date_in_future(self):
        ic = '120312145543'
        self.assertRaises(InvalidDateException,ICParser,ic) 
    
    def test_date_in_past(self):
        ic = '840312145543'
        parser = ICParser(ic)
        birthdate = datetime.date(1984,03,12)
        self.assertEqual(parser.birth_date,birthdate)

    def test_ic_less_12_year(self):
        ic = '010312145543'
        self.assertRaises(InvalidDateException,ICParser,ic) 
       
    def test_birthplace_valid(self):
        ic = '840312145543'
        parser = ICParser(ic)
        birth_place = 'Wilayah Persekutuan (Kuala Lumpur)'
        self.assertEqual(parser.birth_place,birth_place)
    
    def test_birthplace_invalid(self):
        ic = '840312145543'
        self.assertRaises(InvalidBirthPlace,ICParser,ic)
    
    def test_gender_male(self):
        ic = '840312145543'
        parser = ICParser(ic)
        self.assertEqual(parser.gender,'M') 
    
    def test_gender_female(self):
        ic = '840312145544'
        parser = ICParser(ic)
        self.assertEqual(parser.gender,'F') 

