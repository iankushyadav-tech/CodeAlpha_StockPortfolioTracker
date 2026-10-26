import csv
from datetime import datetime

STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "MSFT": 420.00,
    "GOOGL": 175.00,
    "AMZN": 190.00,
}

def track_portfolio():
    portfolio = []
    print("=" * 42)
    print("       CODEALPHA STOCK PORTFOLIO")
    print("=" * 42)
    print("Available stocks and sample prices (USD):")
    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol}: ${price:.2f}")

    while True:
        symbol = input("\nEnter stock symbol (or DONE to finish): ").strip().upper()
        if symbol == "DONE":
            break
        if symbol not in STOCK_PRICES:
            print("Stock not in this sample price list. Please try again.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {symbol}: "))
            if quantity <= 0:
                print("Quantity must be a positive whole number.")
                continue
        except ValueError:
            print("Please enter a whole number for quantity.")
            continue

        price = STOCK_PRICES[symbol]
        value = price * quantity
        portfolio.append({
            "stock": symbol,
            "quantity": quantity,
            "price_usd": f"{price:.2f}",
            "total_value_usd": f"{value:.2f}",
        })
        print(f"Added {quantity} {symbol} share(s): ${value:.2f}")

    if not portfolio:
        print("\nNo stocks were added. Nothing to save.")
        return

    total_investment = sum(float(item["total_value_usd"]) for item in portfolio)
    filename = "portfolio.csv"
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["stock", "quantity", "price_usd", "total_value_usd"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(portfolio)

    print("\n--- Portfolio Summary ---")
    for item in portfolio:
        print(f"{item['stock']}: {item['quantity']} x ${item['price_usd']} = ${item['total_value_usd']}")
    print(f"Total sample investment value: ${total_investment:.2f} USD")
    print(f"Saved portfolio to {filename}")
    print("\nNote: These are hardcoded sample prices for a programming task, not live market prices.")

if __name__ == "__main__":
    track_portfolio()
