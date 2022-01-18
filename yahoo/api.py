import requests
from apikey import API_KEY

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
            symbols.append((data.get('name'), data.get('symbol'), data.get('exch')))
    return symbols


if __name__ == "__main__":
    print(get_symbol("HFCL"))
    print(get_quote("HFCL.NS"))
