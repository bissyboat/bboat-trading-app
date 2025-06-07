import time
import pandas as pd
from datetime import datetime
from backend.services.tv_gold_fetcher import fetch_gold_data
from backend.strategies.gold_strategy import apply_rsi_macd_strategy
from backend.services.backtester import backtest
from backend.mt5.connect import connect_to_mt5, shutdown_mt5
from backend.mt5.trading import place_trade

def run_auto_trade(strategy_fn, stop_loss_pct=0.01, take_profit_pct=0.02, risk_per_trade_pct=0.02):
    connect_to_mt5()

    df = fetch_gold_data()
    df = strategy_fn(df)

    latest = df.iloc[-1]
    signal = latest['signal']
    close_price = latest['close']
    print(f"[{datetime.now()}] Signal: {signal}, Price: {close_price}")

    if signal == 1:
        print("📈 BUY signal triggered — placing trade.")
        place_trade(trade_type="BUY", sl_points=stop_loss_pct * 10000, tp_points=take_profit_pct * 10000)
    elif signal == -1:
        print("📉 SELL signal triggered — placing trade.")
        place_trade(trade_type="SELL", sl_points=stop_loss_pct * 10000, tp_points=take_profit_pct * 10000)
    else:
        print("⏸ No trade signal today.")

    shutdown_mt5()

# Example: run_auto_trade(apply_rsi_macd_strategy)
