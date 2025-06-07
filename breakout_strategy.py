import pandas as pd

def apply_breakout_strategy(df, window=20):
    df['rolling_max'] = df['high'].rolling(window).max()
    df['rolling_min'] = df['low'].rolling(window).min()

    df['signal'] = 0
    df.loc[df['close'] > df['rolling_max'].shift(1), 'signal'] = 1  # Buy breakout
    df.loc[df['close'] < df['rolling_min'].shift(1), 'signal'] = -1  # Sell breakdown

    return df
