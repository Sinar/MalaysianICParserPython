import urllib2
from BeautifulSoup import BeautifulSoup


class NRDLocal:
    def __init__(self):
        self.url = 'http://www.jpn.gov.my/en/informasi/states-code'
        self.page = urllib2.urlopen(self.url)
        self.soup = BeautifulSoup(self.page)
        self.data = {}
    
    def process(self):
        tbody = self.soup.findAll('tbody')
        for i in tbody[0].findAll('tr')[1:]:
            row = i.findAll('td')
            self.data[row[0].text] = row[1].text.split(',')
    
               
                

