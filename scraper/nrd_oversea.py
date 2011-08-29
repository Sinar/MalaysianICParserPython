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

import urllib2
from BeautifulSoup import BeautifulSoup
import json

class NRDOversea:
    def __init__(self):
        self.url = 'http://www.jpn.gov.my/en/informasi/countrys-code'
        self.page = urllib2.urlopen(self.url)
        self.soup = BeautifulSoup(self.page)
        self.data = {}
    
        tbody = self.soup.findAll('tbody')
        for i in tbody[0].findAll('tr')[2:]:
            row = i.findAll('td')
            if row[0].text != '&nbsp;':
                self.assemble_data(row[1].text,row[0].text)
            self.assemble_data(row[3].text,row[2].text)
    
    def assemble_data(self,key,value):
        if self.data.get(key):
            self.data[key].append(value)
        else:
            self.data[key] = [value]
  
    def to_json(self):
        return json.dumps(self.data)
               
    def to_json_file(self,filename):
        fp = open(filename,'w+')
        json.dump(self.data,fp)
        fp.close()           
               

