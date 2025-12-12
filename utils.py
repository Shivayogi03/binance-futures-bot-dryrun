import time
import hashlib
import hmac
import logging
from config import LOG_PATH, ERROR_LOG_PATH

# Logging Setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_PATH),
        logging.StreamHandler()
    ]
)

error_logger = logging.getLogger("errors")
error_file = logging.FileHandler(ERROR_LOG_PATH)
error_logger.addHandler(error_file)

# HMAC Signature
def generate_signature(secret_key, query_string):
    return hmac.new(secret_key.encode(), query_string.encode(), hashlib.sha256).hexdigest()

# Log API Request
def log_request(url, params, response):
    logging.info(f"URL: {url}")
    logging.info(f"PARAMS: {params}")
    logging.info(f"RESPONSE: {response}")

# Mock Binance Response
def mock_binance_response(symbol, side, order_type, qty, price=None):
    return {
        "symbol": symbol,
        "orderId": int(time.time()),
        "side": side,
        "type": order_type,
        "price": price,
        "executedQty": qty,
        "status": "FILLED",
        "clientOrderId": "dryrun-order",
        "updateTime": int(time.time()),
    }
