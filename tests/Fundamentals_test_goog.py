
from data.get_statements import get_statement
from tools.fundamentals_class import Fundamentals 

import requests
import pandas as pd 
import numpy as np
import datetime

import matplotlib.pyplot as plt
import seaborn as sns

import pandas_datareader.data as web
import datetime
from pandas.util.testing import assert_frame_equal

def test(ticker, earnings_growth_rate, cap_ex_growth_rate, perpetual_growth_rate, confidence_intervals, bound, api):
    
    #get the statements
    inc = get_statement(company_ticker = ticker,
                    statement_name = 'income-statement',
                    api_key = api
                    )
    bs = get_statement(company_ticker = ticker,
                        statement_name = 'balance-sheet-statement',
                        api_key = api
                        )
    bsq = get_statement(company_ticker = ticker,
                        statement_name = 'balance-sheet-statement',
                        api_key = api,
                        frequency = 'quarter'
                        )
    cf = get_statement(company_ticker = ticker,
                        statement_name = 'cash-flow-statement',
                        api_key = api
                        )
    ev = get_statement(company_ticker = ticker,
                        statement_name = 'enterprise-value',
                        api_key = api
                        )
    fr = get_statement(company_ticker = ticker,
                        statement_name = 'financial-ratios',
                        api_key = api,
                        )
    
    #create the dcf object
    company = Fundamentals(income_statement = inc,
          balance_sheet_statement = bs,
          balance_sheet_statement_quarterly = bsq,
          cash_flow_statement = cf,
          enterprise_value = ev,
          financial_ratios = fr,
          company_ticker = ticker,
          forecasting_period = 4,
          api_key = api
          )

    #calculate dcf
    company.dcf(earnings_growth_rate = earnings_growth_rate,
            cap_ex_growth_rate = cap_ex_growth_rate,
            perpetual_growth_rate = perpetual_growth_rate)

    #Perform sensitivity analysis on the results
    company.sensitivity(confidence_intervals = confidence_intervals, bound = bound)

    #Perform Piotroski f-score
    company.f_score()
    
if __name__ == '__main__':
    
    api_key = #your financialmodelingprep api key
    test(ticker = 'GOOG', 
         earnings_growth_rate = 0.15, 
         cap_ex_growth_rate = 0.5, 
         perpetual_growth_rate = 0.2,
         confidence_intervals = [0.95, 0.9, 0.85, 0.8, 0.75, 0.7],
         bound = 0.3, 
         api = api_key)
         #I got the values for the growth rates from research, I need to implement the functionality to find this automatically.
    
