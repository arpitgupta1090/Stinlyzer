import requests
# from yahoo.apikey import API_KEY
import os

API_KEY = os.environ.get("API_KEY")

BASE_URL = "https://yfapi.net/v6/finance/"


def get_quote(symbol):

    url = BASE_URL + "quote"
    headers = {'X-API-KEY': API_KEY}
    params = {"region": "IN",
              "lang": "en",
              "symbols": symbol,
              }
    response = requests.get(url=url, headers=headers, params=params)
    result = response.json().get("quoteResponse").get("result")
    if result:
        return {"name": result[0].get("longName"),
                'exchange': result[0].get("exchange"),
                'symbol': result[0].get("symbol"),
                "price": result[0].get("regularMarketPrice")}


def get_symbol(name):
    symbols = list()
    url = BASE_URL + "autocomplete"
    headers = {'X-API-KEY': API_KEY}
    params = {"region": "IN",
              "lang": "en",
              "query": name,
              }
    response = requests.get(url=url, headers=headers, params=params)
    results = response.json().get("ResultSet").get("Result")
    if results:
        for data in results:
            if data.get("exch") in ("NSI", "BSE"):
                symbols.append({"company name": data.get('name'), "symbol": data.get('symbol'), "exchange": data.get('exch')})
    return symbols


if __name__ == "__main__":
    print(get_symbol("HFCL"))
    print(get_quote("HFCL.NS"))
