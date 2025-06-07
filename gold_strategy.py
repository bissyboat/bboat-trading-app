import pandas as pd
import ta

def apply_rsi_macd_strategy(df):
    df['rsi'] = ta.momentum.RSIIndicator(df['close'], window=14).rsi()
    macd = ta.trend.MACD(df['close'])
    df['macd'] = macd.macd()
    df['macd_signal'] = macd.macd_signal()

    df['signal'] = 0
    df.loc[(df['rsi'] < 30) & (df['macd'] > df['macd_signal']), 'signal'] = 1  # Buy
    df.loc[(df['rsi'] > 70) & (df['macd'] < df['macd_signal']), 'signal'] = -1  # Sell

    return df
