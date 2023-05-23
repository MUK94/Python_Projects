# Predine some common currencies
currencies = {
    "USD": {
        'EUR': 0.85,
        'GBP': 0.72,
        'CAD': 1.21,
    },
    "EUR": {
        'USD': 1.18,
        'GBP': 0.72,
        'CAD': 1.21,
    },
    "CAD": {
        'USD': 0.83,
        'EUR': 0.68,
        'GBP': 0.59,
    },
    "GPB": {
        'USD': 1.39,
        'EUR': 1.17,
        'CAD': 1.71,
    }
}

# Currency Function
def curr_converter(amount, from_curr, to_curr):
    try:
        result = amount * currencies[from_curr][to_curr]
        return result
    except KeyError:
        None

# Get User inputs
amount = float(input("Enter the amount to be converted: "))
from_curr = input("From which currency (Currency code) ?: ").upper()
to_curr = input("To which currency (Currency code) ?: ").upper()

converted_amount = curr_converter(amount, from_curr, to_curr)
print(f"{amount} {from_curr} is equal to {converted_amount} {to_curr}")
