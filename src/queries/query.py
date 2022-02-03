import requests
import os

class yahoo:
    def __init__(self):
        self.headers = {'x-api-key':os.environ.get('API_KEY')}
        self.querystring = {"symbols":None}
        self.url = ""
        
    def get_finance_quote(self,querystring):
        # OPTIONS
        # region: US AU CA FR DE HK IT ES GB IN
        # lang: en fr de it es zh
        # symbols: Multiple symbols separated by commas. Max is 10 [Ex. AAPL,BTC-USD,EURUSD=X]
        self.url = "https://yfapi.net/v6/finance/quote"
        self.querystring["symbols"] = querystring
        return requests.request("GET", self.url, headers=self.headers, params=self.querystring)
