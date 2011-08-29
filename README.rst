==============================
Malaysia IC Parser For Python
==============================

The format of Malaysia Identification Card can be found at Wikipedia_


Datasource for State Code can be found at LocalCode_ and CountryCode_


The scraper is in the scraper folder, usage guide coming soon

.. _Wikipedia: http://en.wikipedia.org/wiki/NRIC_Number_(Malaysia)
.. _LocalCode: http://www.jpn.gov.my/en/informasi/states-code
.. _CountryCode: http://www.jpn.gov.my/en/informasi/countrys-code

============
Requirement
============
- python-dateutil
- BeautifulSoup (Used in the scraper)
- Nose (Used in unittest)

This is tested on python 2.7, I didn't tried on 2.6 yet. 

======
Usage
======

Python Module
==============

The python module is used this way::
    >>> from nric_parser import ICParser
    >>> parser = ICParser('840312145543') # or the dash format would work too
    >>> parser.birth_date
    datetime.date(1984, 3, 12)
    >>> parser.birth_place
    u'Wilayah Persekutuan (Kuala Lumpur)'
    >>> parser.gender
    'M'

Scrapper
=========

The scrapper is called from load_data.py
which will create a data/ folder, or if it doesn't exist create one. It will create 2 file, state_code.json and country_code.json. This is used by the python module to look up for state code and country code

These file already exist, so you probably do not need to do this, until there is a update on the code. 

To called load_data.py::

    python load_data.py

Still might have some issue, if many people use this i might just package it. 
