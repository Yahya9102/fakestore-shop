import requests

FAKESTORE_BASE_URL = "https://fakestoreapi.com/products"

def fetch_products():
    response = requests.get(FAKESTORE_BASE_URL, timeout=10)
    response.raise_for_status()
    return response.json()