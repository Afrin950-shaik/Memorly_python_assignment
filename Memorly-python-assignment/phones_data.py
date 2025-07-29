# This is a phone stock data
# Each phone has: model name, condition, how many you have in stock, price, and whether it’s already sold

phones = [
    {
        "model": "iPhone 12",
        "condition": "Like New",
        "stock": 3,
        "base_price": 40000,
        "sold": False
    },
    {
        "model": "OnePlus 9",
        "condition": "Good",
        "stock": 2,
        "base_price": 30000,
        "sold": True     # Already sold, so don't list it
    },
    {
        "model": "Galaxy A52",
        "condition": "Fair",
        "stock": 0,
        "base_price": 15000,
        "sold": False    # Stock is 0, don't list
    },
    {
        "model": "iPhone XR",
        "condition": "Like New",
        "stock": 1,
        "base_price": 28000,
        "sold": False
    },
    {
        "model": "Redmi Note 10",
        "condition": "Fair",
        "stock": 5,
        "base_price": 10000,
        "sold": False
    }
]