from ..queries import query as q

yahoo = q.yahoo()

def portfolio_net():
  print("Begin portfolio generation")
  try:
    print("Trying Finance Quote")
    querystring = "AAPL,BTC-USD,EURUSD=X"
    result = yahoo.get_finance_quote(querystring)
    print(result.text)
  except Exception as e:
    print("Error", e.__class__, "occurred.")
