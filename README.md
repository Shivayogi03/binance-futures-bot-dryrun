
<img width="1536" height="1024" alt="banner" src="https://github.com/user-attachments/assets/3fc58e59-5cae-4c42-aad4-f4dad91ce36f" />[Uploading banner.png…]()

Binance Futures Trading Bot (Dry-Run Mode)

A clean, production-style Python trading bot that simulates Binance Futures orders using real futures-style signatures, CLI commands, and full request logging — all without needing API keys.

# Binance Futures Trading Bot (Dry-Run Mode)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)]()
[![Status](https://img.shields.io/badge/Mode-Dry%20Run-success.svg)]()
[![Logging](https://img.shields.io/badge/Logs-Enabled-important.svg)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)]()
[![Platform](https://img.shields.io/badge/Binance-Futures%20Testnet-yellow.svg)]()

A fully-structured, testnet-compatible **Binance Futures Trading Bot** built for the hiring task.  
Designed to simulate real futures trading via **dry-run mode**, including:

- ✔ Market & Limit Orders  
- ✔ Signed request generation (HMAC SHA256)  
- ✔ CLI-based user input  
- ✔ Full request/response logging  
- ✔ Mock trading engine for offline testing  
- ✔ Professional folder structure  
- ✔ Ready for extension to real API trading  

---

# 🚀 Features

| Feature | Status |
|--------|--------|
| Market Orders | ✅ |
| Limit Orders | ✅ |
| BUY & SELL | ✅ |
| Testnet-style Signature | ✅ |
| Logging (requests + errors) | ✅ |
| Mock Engine (Dry Run) | ✅ |
| CLI Interface | ✅ |
| Error Handling | ✅ |
| Extendable to Real API | 🔄 Optional |
| Advanced Order Types (OCO, Stop-Limit, TWAP) | 🔄 Optional |

---

# 🛠 Tech Stack

- **Python 3.10+**
- argparse
- logging
- hmac / hashlib (for Binance-style signatures)
- python-dotenv
- (Optional) python-binance for live API trading

---

# ⚙ How It Works Internally

Below is a high-level architecture explaining how the bot executes a trade.

## **1️⃣ User Input (CLI)**  
User runs:



python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001 --dry


CLI parses arguments → creates a `TradingBot` instance.

---

## **2️⃣ Bot Generates Request Parameters**

Example:

python
params = {
    "symbol": "BTCUSDT",
    "side": "BUY",
    "type": "MARKET",
    "quantity": 0.001,
    "timestamp": 1765562129706
}

### **CLI Market Order**

Perfect for assignments, interviews, learning HMAC signing, or testing trading logic safely.

🚀 Features
✅ Dry-Run Trading (No API keys needed)

Simulates real Binance Futures orders using mock responses.

✅ Market & Limit Orders

Supports both BUY and SELL directions.

✅ Futures-style HMAC Signatures

Query string signing works the same as Binance.

✅ CLI Interface for Quick Testing

Run orders directly from the terminal.

✅ Detailed Logging

Automatically records every request + response:

logs/requests.log  
logs/errors.log

✅ Clean, Modular Codebase

Separated into bot.py, utils.py, config.py, etc.

📁 Project Structure
trading-bot/
│
├── bot.py
├── cli.py
├── config.py
├── utils.py
├── requirements.txt
├── README.md
│
└── logs/
       ├── requests.log
       └── errors.log

🎆How It Works Internally
## 🔍 How It Works Internally

This project mimics how real Binance Futures order placement works—without using API keys and without sending real requests.

---

### 1. CLI → Bot
When you run:

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001 --dry

Your input is parsed and passed into `TradingBot.place_order()`.

---

### 2. Signature Generation (Real Binance Style)
Before an order is created, a query string like this is generated:

symbol=BTCUSDT&side=BUY&type=MARKET&quantity=0.001&timestamp=123456789

`generate_signature()` creates a SHA256 HMAC signature — the same way Binance requires.

---

### 3. Dry-Run Mock Order
Since dry-run mode is enabled:

- No API request is made  
- A realistic mock fill response is returned  
- Your order always returns status = `FILLED`

---

### 4. Logging Every Order
Two files are updated every run:

logs/requests.log → request & response logs
logs/errors.log → error logs

These logs are PERFECT for interview demonstration.

---

### 5. Safe by Design
- No API calls  
- No API keys required  
- No money at risk  
- Still behaves like a real algorithmic trading bot
  
⚙️ Installation
1️⃣ Clone or Download the Repository
git clone https://github.com/<your-username>/binance-futures-bot-dryrun.git
cd binance-futures-bot-dryrun

2️⃣ Install Dependencies
pip install -r requirements.txt

💻 How to Use
▶️ Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001 --dry

▶️ Limit Order
python cli.py --symbol ETHUSDT --side SELL --type LIMIT --quantity 0.002 --price 2000 --dry


The --dry flag enables Dry-Run Mode
(Real API mode is intentionally NOT implemented to keep this assignment safe.)

📚 Sample Output
===== ORDER RESULT =====
{'symbol': 'BTCUSDT', 'orderId': 1765562129, 'side': 'BUY',
 'type': 'MARKET', 'executedQty': 0.001, 'status': 'FILLED'}
========================
🎦Snapshot:
<img width="1336" height="824" alt="snapshot" src="https://github.com/user-attachments/assets/446c7f2b-29f2-4d37-8322-1ad556748728" />[Uploading snapshot.png…]()

📝 Logging

Every order is logged automatically.

Example requests.log:
2025-12-12 23:25:29 [INFO] URL: https://testnet.binancefuture.com/fapi/v1/order
2025-12-12 23:25:29 [INFO] PARAMS: {...}
2025-12-12 23:25:29 [INFO] RESPONSE: {...}


This helps in debugging and showing realistic behavior for evaluations.

📌 Notes

This bot does not place real trades.

Designed for assignments, demos, and dry-run practice.

Uses the same signing mechanism as Binance Futures API.

Safe to run — no API keys required.

💼 Ideal For

University or hiring assignments

Showcasing Python project skills

Demonstrating API request signing

Practicing CLI tools and logging

Creating a base for real trading bots later

🤝 Contributing

Pull requests are welcome.
For major changes, open an issue first to discuss improvements.

📄 License

This project is released under the MIT License.
