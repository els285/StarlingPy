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

## Transaction History

The Starling API provides access to full transaction history. This history is wrapped in the `TransactionHistory` class, which provides methods for summarising and visualising this data.

```python3
from starlingpy.StarlingClass import TransactionHistory
tH = TransactionHistory(Account,start_date="2021-02-17T00:00:00Z",end_date="2022-02-24T00:00:00Z")
```
The `TransactionHistory` object stores the full historical information in a dataframe, and also provides an abridged summary dataframe.

TransactionHistory can also be accessed using the member function `generate_transaction_history`:
```python3
tH = Account.generate_transaction_history(start_date="2021-02-17T00:00:00Z",end_date="2022-02-24T00:00:00Z")
```

