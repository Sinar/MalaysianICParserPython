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
                self.data[row[0].text] = row[1].text
            self.data[row[2].text] = row[3].text
    
    def to_json(self):
        return json.dumps(self.data)
               
                

