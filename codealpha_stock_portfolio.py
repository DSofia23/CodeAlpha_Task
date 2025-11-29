# Hardcoded stock prices
prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130
}

total_investment = 0

while True:
    stock = input("Enter stock symbol (or type 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in prices:
        print("Stock not found in price list.")
        continue

    qty = int(input(f"Enter quantity of {stock}: "))

    investment = qty * prices[stock]
    total_investment += investment

    print(f"{stock} → {qty} × {prices[stock]} = {investment}\n")

print("====================================")
print(f"Total Investment Value = {total_investment}")
print("====================================")

# OPTIONAL: Save to file
save = input("Do you want to save the result? (yes/no): ")

if save.lower() == "yes":
    with open("portfolio.txt", "w") as file:
        file.write(f"Total Investment Value = {total_investment}")

    print("Saved to portfolio.txt!")
