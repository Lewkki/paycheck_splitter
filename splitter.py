splits = {
    'Checking': 0.25,
    'Truck': 0.35,
    'Investing': 0.20,
    'Marriage': 0.15,
    'Travel': 0.05
}

investments = {
    'VOO': 0.60,
    'QQQM': 0.30,
    'SCHD': 0.10
}

paycheck = float(input("Enter the amount to split: $"))
investment_amount = paycheck * 0.20

print("\n--- Paycheck Breakdown ---\n")

for category, percent in splits.items():
    amount = paycheck * percent
    print(f'{category}: ${amount:.2f}')


print("\n--- Investing Breakdown ---\n")

for stock, percent in investments.items():
    inv = investment_amount * percent
    print(f'{stock}: ${inv}')
