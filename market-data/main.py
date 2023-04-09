import requests
import json
import re

class MarketData:
    main_info_url = 'http://www.tsetmc.com/tsev2/data/MarketWatchInit.aspx?h=0&r=0'

    def __init__(self):
        self.market_main_data = None
        self.shakhes_data = None

    def main_info(self):
        self.market_main_data = requests.get(self.main_info_url, timeout=10).text
        
        self.market_main_data = self.market_main_data.split('@')
        self.market_main_data = self.market_main_data[2].split(';')

        finall_data = []
        for data in self.market_main_data:
             
            data = data.split(',')

            try:
                company_id = data[0]
                name = data[2]
                namad = data[3]
                if re.search("\d",namad):
                    break
                time = data[4]
                first_price = data[5]
                end_price = data[6]
                last_price = data[7]
                transaction_count = data[8]
                trade_valum = data[9]
                trade_price = data[10]
                first_price = data[11]
                day_high_price = data[12]
                yesterday_price = data[13]
                EPS = data[14]
                mabna_valum = data[15]
                low_price_allow = data[19]
                high_price_allow = data[20]
                total_saham = data[21]
                


            except Exception as e:
                print(e)


c = MarketData()

c.main_info()
