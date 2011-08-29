import urllib2
from BeautifulSoup import BeautifulSoup
import json

class NRDLocal:
    def __init__(self):
        self.url = 'http://www.jpn.gov.my/en/informasi/states-code'
        self.page = urllib2.urlopen(self.url)
        self.soup = BeautifulSoup(self.page)
        self.data = {}
    
        tbody = self.soup.findAll('tbody')
        for i in tbody[0].findAll('tr')[1:]:
            row = i.findAll('td')
            self.data[row[0].text] = row[1].text.split(',')
    
    def to_json(self):
        return json.dumps(self.data)
               
    def to_json_file(self,filename):
        fp = open(filename,'w+')
        json.dump(self.data,fp)
        fp.close()           
     
