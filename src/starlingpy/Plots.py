# StarlingPlots
import pandas as pd
import plotly.express as px
from datetime import datetime


"""
Types of plots:
* Spending over discrete / continuous time-scales
"""



def transaction_scatter(summary_df):

    fig = px.scatter(summary_df, x='transactionTime', y="minorUnits")
    fig.show()


def balance_line(full_df):

    """ Takes the full unabridged dataframe"""

    df = full_df
    df["Balance After"] = df["Balance After"]/1e2
    fig = px.line(df, x='transactionTime', y="Balance After",markers=True)
    fig.show()


def monthly_summary(df):
    # Turn the date strings into datetime objects

    #Split by month
    g=df.groupby(pd.Grouper(key='transactionTime', freq='M'))
    dfs = [group for _,group in g]


    summary_list = []

    for month in dfs:

        Y=month['transactionTime'].tolist()[0].year
        M=month['transactionTime'].tolist()[0].month

        print(month['spendingCategory'].isin(['INCOME']))
        input()

        # month['']





# def basic_bar_monthly(df):





# class TimeSeries_Plot:

#     def __init__(self,df):
#         fig = px.line(df, x='settlementTime', y="amount")
#         fig.show()



# class Transaction_Period:

#     def __init__(self,start_date,end_data,**kwargs)