
def sma_strategy(df, short=5, long=20):
    df['SMA_short'] = df['rate'].rolling(window=short).mean()
    df['SMA_long'] = df['rate'].rolling(window=long).mean()
    df['signal'] = 0
    df.loc[df['SMA_short'] > df['SMA_long'], 'signal'] = 1
    df.loc[df['SMA_short'] < df['SMA_long'], 'signal'] = -1
    return df
