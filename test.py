# Copyright 2011 sweemeng<sweester@gmail.com. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, are
# permitted provided that the following conditions are met:
#
#    1. Redistributions of source code must retain the above copyright notice, this list of
#       conditions and the following disclaimer.
#
#    2. Redistributions in binary form must reproduce the above copyright notice, this list
#       of conditions and the following disclaimer in the documentation and/or other materials
#       provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY SWEEMENG ''AS IS'' AND ANY EXPRESS OR IMPLIED
# WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# The views and conclusions contained in the software and documentation are those of the
# authors and should not be interpreted as representing official policies, either expressed
# or implied, of sweemeng.
import unittest
import datetime
from dateutil.relativedelta import *
from nric_parser import ICParser
from nric_parser import InvalidFormatException
from nric_parser import InvalidDateException
from nric_parser import InvalidBirthPlace
from nric_parser import DateInFutureException

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
        self.assertRaises(DateInFutureException,ICParser,ic) 
    
    def test_date_in_past(self):
        ic = '840312145543'
        parser = ICParser(ic)
        birthdate = datetime.date(1984,03,12)
        self.assertEqual(parser.birth_date,birthdate)

    def test_ic_less_12_year(self):
        ic = '010312145543'
        self.assertRaises(InvalidDateException,ICParser,ic) 
       
    def test_birthplace_local_valid(self):
        ic = '840312145543'
        parser = ICParser(ic)
        birth_place = 'Wilayah Persekutuan (Kuala Lumpur)'
        self.assertEqual(parser.birth_place,birth_place)
    
    def test_birthplace_oversea_valid(self):
        ic = '840312895543'
        parser = ICParser(ic)
        birth_place = 'Japan,Korea Selatan,Korea Utara,Taiwan'
        self.assertEqual(parser.birth_place,birth_place)
   
    def test_birthplace_invalid(self):
        ic = '840312995543'
        self.assertRaises(InvalidBirthPlace,ICParser,ic)

    def test_birthplace_data_on_file(self):
        ic = '840312145543'
        parser = ICParser(ic,
                 state_file='data/state_code.json',
                 country_file='data/country_code.json')
        birth_place = 'Wilayah Persekutuan (Kuala Lumpur)'
        self.assertEqual(parser.birth_place,birth_place)
    
    def test_birthplace_data_bad_file(self):
        ic = '840312145543'
        self.assertRaises(IOError,ICParser,ic,
                 state_file='data/state_bad.json',
                 country_file='data/country_bad.json')
 
    def test_gender_male(self):
        ic = '840312145543'
        parser = ICParser(ic)
        self.assertEqual(parser.gender,'M') 
    
    def test_gender_female(self):
        ic = '840312145544'
        parser = ICParser(ic)
        self.assertEqual(parser.gender,'F') 

