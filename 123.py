import hashlib
import hmac
import time

import requests

from MEXC.MEXC_endpoints import MEXCEndpoints


def test_order():
    # Replace these with your actual Binance API key and secret
    api_key = "mx0vgleFwQqXULvi0m"
    api_secret = "bef200a63a324dc18167cdccdae60fb8"

    symbol, side, type, quantity, price = 'MXUSDT', 'BUY', 'LIMIT', '50', '0.1'

    timestamp = int(time.time() * 1000)
    payload = f'symbol={symbol}&side={side}&type={type}&quantity={quantity}&price={price}&timestamp={timestamp}'
    signature = hmac.new(api_secret.encode(), payload.encode(), hashlib.sha256).hexdigest()
    url = f'{MEXCEndpoints.ORDER_TEST}?{payload}&signature={signature}'
    headers = {'APIKEY': api_key}
    response = requests.post(url, headers=headers)

    # Print the response

    if response.status_code == 200:
        print("Test Order placed successfully!")
    else:
        print(f"Error placing order. Status code: {response.status_code}")

# Call the function to place the test order
test_order()
