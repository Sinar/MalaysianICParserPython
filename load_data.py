from scraper.nrd_local import NRDLocal
from scraper.nrd_oversea import NRDOversea
import os

def load_data():
    try:
        os.listdir('data')
    except OSError:
        os.mkdir('data')
    
    local = NRDLocal()
    local.to_json_file('data/state_code.json')
    oversea = NRDOversea()
    oversea.to_json_file('data/country_code.json')
    

if __name__ == "__main__":
    load_data()
