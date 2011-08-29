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

======
Usage
======

The program is used this way::
    >>> parser = ICParser('840312145543') # or the dash format would work too
    >>> parser.birth_date
    datetime.date(1984, 3, 12)
    >>> parser.birth_place
    u'Wilayah Persekutuan (Kuala Lumpur)'
    >>> parser.gender
    'M'

Still might have some issue, if many people use this i might just package it. 
