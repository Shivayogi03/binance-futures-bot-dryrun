import argparse
from bot import TradingBot

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot (Dry-Run Mode)")

    parser.add_argument("--symbol", type=str, required=True, help="Trading pair (e.g. BTCUSDT)")
    parser.add_argument("--side", type=str, required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", type=str, required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float, required=False)
    parser.add_argument("--dry", action="store_true", help="Run in dry-run mode")

    args = parser.parse_args()

    bot = TradingBot(dry_run=args.dry)

    response = bot.place_order(
        symbol=args.symbol,
        side=args.side,
        order_type=args.type,
        quantity=args.quantity,
        price=args.price
    )

    print("\n===== ORDER RESULT =====")
    print(response)
    print("========================\n")

if __name__ == "__main__":
    main()
