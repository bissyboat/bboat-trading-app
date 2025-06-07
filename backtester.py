def backtest(df, stop_loss_pct=0.01, take_profit_pct=0.02, risk_per_trade_pct=0.02, initial_balance=10000):
    balance = initial_balance
    position = 0
    entry_price = 0
    trades = []
    risk_amount = balance * risk_per_trade_pct

    for i in range(1, len(df)):
        price = df['close'][i]
        signal = df['signal'][i]

        if signal == 1 and position == 0:  # Buy
            entry_price = price
            stop_loss = entry_price * (1 - stop_loss_pct)
            take_profit = entry_price * (1 + take_profit_pct)
            qty = risk_amount / (entry_price - stop_loss)
            position = qty
            trades.append({
                'type': 'BUY',
                'entry_price': entry_price,
                'stop_loss': stop_loss,
                'take_profit': take_profit,
                'qty': qty
            })

        elif position > 0:
            if price <= stop_loss or price >= take_profit or signal == -1:
                exit_price = price
                pnl = (exit_price - entry_price) * position
                balance += pnl
                trades[-1].update({
                    'exit_price': exit_price,
                    'pnl': pnl,
                    'balance_after': balance
                })
                position = 0

        risk_amount = balance * risk_per_trade_pct

    final_balance = balance
    profit = final_balance - initial_balance
    return trades, profit, final_balance
