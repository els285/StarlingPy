from requests import get
import datetime

import pandas as pd 

from starlingpy.StarlingAPIs import Account_APIs

BASE_PATH = "https://api.starlingbank.com/api/v2/"


class TransactionHistory:

    """
    A history of transactions associated with the Starling account, between stipulated datetimes.
    Requires the StarlingAccount object to be passed
    """


    def __init__(self,Account,**kwargs):

        self.associated_Account = Account 
        self.transaction_List   = Account.get_transactions(**kwargs)
        self.full_Dataframe     = self.generate_transaction_dataframe(**kwargs)
        self.summary_Dataframe  = self.summary_transaction_dataframe()


    def generate_transaction_dataframe(self,**kwargs):

        """ Generates full transaction dataframe between dates """

        df = pd.DataFrame(self.transaction_List)
        running_balance = self.generate_running_balance_list(self.transaction_List)
        df['Balance Before'] = running_balance[1:]
        df['Balance After']  = running_balance[:-1]
        df["transactionTime"]= pd.to_datetime(df["transactionTime"])

        return df

    
    def summary_transaction_dataframe(self):

        """ Generates an abridged summary dataframe for using with plotting macros """

        df = self.full_Dataframe

        Amounts_df=df["amount"].apply(pd.Series)
        dfN = pd.concat([Amounts_df,df["transactionTime"],df["spendingCategory"]],ignore_index=False,axis=1)
        dfN.loc[dfN['spendingCategory'].isin(['INCOME']),'minorUnits'] = -dfN["minorUnits"]

        return dfN


    def generate_running_balance_list(self,transaction_list,**kwargs):

        """ Computes running balance based on totalEffectiveBalance field """

        balance            = self.associated_Account.get_balance()["totalEffectiveBalance"]["minorUnits"]
        running_balance = [balance]
        for trans in transaction_list:
            amount = trans["amount"]["minorUnits"] 
            if trans["spendingCategory"]=='INCOME': amount = -amount
            balance += amount
            running_balance.append(balance)
        
        return running_balance





class StarlingAccount:

    """
    Class which aligns to Starling bank account, with relevant attributes for that bank account, 
    Class methods for extracting information from the 
    """

    def fetch(self,url):
        r = get(url,headers=self.headers)
        r.raise_for_status()
        return r.json()

    def access_account_details(self):
        url = BASE_PATH + "accounts"
        return self.fetch(url)

    def __init__(self,PAT,**kwargs):
        self.PAT = PAT
        self.headers =  {"Authorization": "Bearer " + PAT}
        self.requests_object = self.access_account_details()
        self.account_details = self.requests_object['accounts'][0]
        self.accountUid      = self.account_details['accountUid']
        self.defaultCategory = self.account_details['defaultCategory']

    def get_balance(self):
        url = BASE_PATH + Account_APIs["Account Balance"].format(self.accountUid)
        return self.fetch(url)

    def show_balance(self):
        tEF = self.get_balance()["totalEffectiveBalance"]
        print(str( tEF["minorUnits"]/1e2) + " " + tEF["currency"])


    def get_recurring_payments(self):
        url = BASE_PATH + Account_APIs["Recurring Payments"].format(self.accountUid)
        return self.fetch(url) 


    def get_feed(self):
        url = BASE_PATH + Account_APIs["Feed"].format(self.accountUid,self.defaultCategory)
        return self.fetch(url) 


    def get_payees(self):
        url = BASE_PATH + Account_APIs["Payees"]
        return self.fetch(url) 


    def get_transactions(self,**kwargs):
        start_date = kwargs["start_date"] if "start_date" in kwargs else (datetime.datetime.now()-datetime.timedelta(days=1)).strftime("%Y-%m-%d") + "T00:00:00Z"
        end_date   = kwargs["end_date"]   if "end_date"   in kwargs else datetime.datetime.now().strftime("%Y-%m-%d") + "T00:00:00Z"
        url =  BASE_PATH + Account_APIs["Transactions Between"].format(self.accountUid,self.defaultCategory,start_date,end_date)
        return self.fetch(url)['feedItems']







        





