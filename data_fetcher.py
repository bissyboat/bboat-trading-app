
from forex_python.converter import CurrencyRates
import pandas as pd

def get_exchange_rate(base: str, target: str, start: str, end: str):
    cr = CurrencyRates()
    date_range = pd.date_range(start, end)
    data = []
    for date in date_range:
        try:
            rate = cr.get_rate(base, target, date)
            data.append({'date': date, 'rate': rate})
        except:
            continue
    return pd.DataFrame(data)
