import requests
from config import API_KEY

def get_price(symbol):
    url = f"https://api.example.com/stock/{symbol}?apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    price = data.get('price') or data.get('c')  # depends on API format
    print(f"Current price of {symbol}: {price}")

get_price("AAPL")
