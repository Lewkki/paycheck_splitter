splits = {
    'Checking': 0.25,
    'Truck': 0.35,
    'Investing': 0.20,
    'Marriage': 0.15,
    'Travel': 0.05
}

paycheck = float(input("Enter the amount to split: $"))

print("\n--- Paycheck Breakdown ---\n")

for category, percent in splits.items():
    amount = paycheck * percent
    print(f'{category}: ${amount:.2f}')
