import streamlit as st
from backend.services.tv_gold_fetcher import fetch_gold_data
from backend.strategies.gold_strategy import apply_rsi_macd_strategy
from backend.strategies.bollinger_strategy import apply_bollinger_strategy
from backend.strategies.breakout_strategy import apply_breakout_strategy
from backend.services.backtester import backtest

from frontend.login import login

if not login():
    st.stop()

st.title("📊 Gold Strategy Analyzer (Daily)")

# Strategy selector
strategy_choice = st.sidebar.selectbox("📌 Choose Strategy", ["RSI + MACD", "Bollinger Bands", "Breakout"])

# Risk settings
st.sidebar.header("⚙️ Risk Management")
sl_pct = st.sidebar.slider("Stop Loss (%)", 0.5, 10.0, 1.0) / 100
tp_pct = st.sidebar.slider("Take Profit (%)", 0.5, 10.0, 2.0) / 100
risk_pct = st.sidebar.slider("Risk per Trade (%)", 0.5, 10.0, 2.0) / 100

# Load data and apply selected strategy
df = fetch_gold_data()
if strategy_choice == "RSI + MACD":
    df = apply_rsi_macd_strategy(df)
elif strategy_choice == "Bollinger Bands":
    df = apply_bollinger_strategy(df)
elif strategy_choice == "Breakout":
    df = apply_breakout_strategy(df)

trades, profit, final_balance = backtest(df, stop_loss_pct=sl_pct, take_profit_pct=tp_pct, risk_per_trade_pct=risk_pct)

st.subheader("📉 Gold Price & Strategy Signals")
st.line_chart(df[['close']])

st.subheader("📊 Backtest Results")
st.write(f"💰 Final Balance: ${final_balance:.2f}")
st.write(f"📈 Profit: ${profit:.2f}")
st.dataframe(trades)
