import pandas as pd
import ta

def apply_bollinger_strategy(df):
    bb = ta.volatility.BollingerBands(close=df['close'], window=20, window_dev=2)
    df['bb_upper'] = bb.bollinger_hband()
    df['bb_lower'] = bb.bollinger_lband()

    df['signal'] = 0
    df.loc[df['close'] < df['bb_lower'], 'signal'] = 1  # Buy
    df.loc[df['close'] > df['bb_upper'], 'signal'] = -1  # Sell

    return df
