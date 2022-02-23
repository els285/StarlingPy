# StarlingPy
A package for financial analytics for Starling Bank account holders

## Installation
```bash
python3 -m pip install git+https://github.com/ethansimpson285/StarlingPy
```

## Basic Usage
Assign a `StarlingAccount` class to your Starling bank account:
```python3
from starlingpy.StarlingClass import StarlingAccount
Account = StarlingAccount(<PAT>)
```
where `<PAT>` is your Starling Bank Developer access token.

Access relevant account information:
```python3

# Print the account balance
Account.show_balance()

# Access information on recurring payments
Account.get_recurring_payments()

# Access information on payees
Account.get_payees()
```
