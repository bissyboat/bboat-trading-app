from tvDatafeed import TvDatafeed, Interval
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_gold_data():
    username = os.getenv("TV_USERNAME")
    session = os.getenv("TV_SESSION")
    tv = TvDatafeed(username=username, password=None, session=session)
    df = tv.get_hist(symbol='XAUUSD', exchange='OANDA', interval=Interval.in_daily, n_bars=500)
    return df.reset_index().rename(columns={
        'datetime': 'date',
        'open': 'open',
        'high': 'high',
        'low': 'low',
        'close': 'close',
        'volume': 'volume'
    })
