import time
from utils import generate_signature, log_request, mock_binance_response
from config import BASE_URL

class TradingBot:
    def __init__(self, api_key="", api_secret="", dry_run=True):
        self.api_key = api_key
        self.api_secret = api_secret
        self.dry_run = dry_run

    def place_order(self, symbol, side, order_type, quantity, price=None):
        endpoint = "/fapi/v1/order"
        url = BASE_URL + endpoint

        timestamp = int(time.time() * 1000)

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
            "timestamp": timestamp
        }

        if price:
            params["price"] = price

        query_string = "&".join([f"{k}={v}" for k, v in params.items()])
        signature = generate_signature(self.api_secret or "dummy", query_string)
        params["signature"] = signature

        if self.dry_run:
            response = mock_binance_response(symbol, side, order_type, quantity, price)
        else:
            response = {"error": "Dry run disabled, but no real API call implemented."}

        log_request(url, params, response)
        return response
