
<img width="1536" height="1024" alt="banner" src="https://github.com/user-attachments/assets/3fc58e59-5cae-4c42-aad4-f4dad91ce36f" />[Uploading banner.png…]()

Binance Futures Trading Bot (Dry-Run Mode)

A clean, production-style Python trading bot that simulates Binance Futures orders using real futures-style signatures, CLI commands, and full request logging — all without needing API keys.

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
<img width="1536" height="1024" alt="snapshot" src="https://github.com/user-attachments/assets/446c7f2b-29f2-4d37-8322-1ad556748728" />[Uploading snapshot.png…]()

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
