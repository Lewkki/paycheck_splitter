def split_paycheck(paycheck, splits):
    for category, percent in splits.items():
        amount = paycheck * percent
        print(f'{category}: ${amount:.2f}')


def split_investments(investment_amount, investments):
    for stock, percent in investments.items():
        inv = investment_amount * percent
        print(f'{stock}: ${inv:.2f}')


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
investment_amount = paycheck * splits['Investing']

print("\n--- Paycheck Breakdown ---\n")

split_paycheck(paycheck, splits)

print("\n--- Investing Breakdown ---\n")

split_investments(investment_amount, investments)
