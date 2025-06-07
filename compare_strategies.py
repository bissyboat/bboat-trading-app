import streamlit as st
from backend.services.tv_gold_fetcher import fetch_gold_data
from backend.strategies.gold_strategy import apply_rsi_macd_strategy
from backend.strategies.bollinger_strategy import apply_bollinger_strategy
from backend.strategies.breakout_strategy import apply_breakout_strategy
from backend.services.backtester import backtest
import pandas as pd

from frontend.login import login

if not login():
    st.stop()

st.title("📊 Gold Strategy Comparison (Daily Timeframe)")

st.sidebar.header("⚙️ Risk Settings")
sl_pct = st.sidebar.slider("Stop Loss (%)", 0.5, 10.0, 1.0) / 100
tp_pct = st.sidebar.slider("Take Profit (%)", 0.5, 10.0, 2.0) / 100
risk_pct = st.sidebar.slider("Risk per Trade (%)", 0.5, 10.0, 2.0) / 100

# Fetch data once
df = fetch_gold_data()

results = []

# Run backtest for each strategy
strategies = {
    "RSI + MACD": apply_rsi_macd_strategy,
    "Bollinger Bands": apply_bollinger_strategy,
    "Breakout": apply_breakout_strategy
}

for name, strategy_fn in strategies.items():
    df_copy = df.copy()
    df_with_signals = strategy_fn(df_copy)
    trades, profit, final_balance = backtest(
        df_with_signals, stop_loss_pct=sl_pct, take_profit_pct=tp_pct, risk_per_trade_pct=risk_pct)
    results.append({
        "Strategy": name,
        "Final Balance ($)": round(final_balance, 2),
        "Profit ($)": round(profit, 2),
        "Trades": len(trades)
    })

result_df = pd.DataFrame(results)

st.subheader("📈 Strategy Performance Summary")
st.dataframe(result_df)

# Highlight best performer
best = result_df.sort_values("Profit ($)", ascending=False).iloc[0]
st.success(f"🏆 Best Strategy: **{best['Strategy']}** with ${best['Profit ($)']} profit.")
