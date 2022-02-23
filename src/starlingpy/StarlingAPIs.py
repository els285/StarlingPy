"""
STARLING APIs
"""

Account_APIs = {
    'Account Holder'        : 'account-holder',
    'Account Holder Name'   : 'account-holder/name',
    'Account Balance'       : 'accounts/{0}/balance',
    'Addresses'             : 'addresses',                              # I do not have current access
    'Recurring Payments'    : 'accounts/{0}/recurring-payment',
    'Feed'                  : 'feed/account/{0}/category/{1}',
    'Payees'                : 'payees',
    'Transactions Between'  : 'feed/account/{0}/category/{1}/transactions-between?minTransactionTimestamp={2}&maxTransactionTimestamp={3}'
}