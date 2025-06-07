import MetaTrader5 as mt5
import datetime

def place_trade(symbol="XAUUSD", lot=0.01, trade_type="BUY", sl_points=200, tp_points=400):
    if not mt5.symbol_select(symbol, True):
        raise Exception(f"Failed to select symbol {symbol}")

    price = mt5.symbol_info_tick(symbol).ask if trade_type == "BUY" else mt5.symbol_info_tick(symbol).bid
    sl = price - sl_points * mt5.symbol_info(symbol).point if trade_type == "BUY" else price + sl_points * mt5.symbol_info(symbol).point
    tp = price + tp_points * mt5.symbol_info(symbol).point if trade_type == "BUY" else price - tp_points * mt5.symbol_info(symbol).point

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": mt5.ORDER_TYPE_BUY if trade_type == "BUY" else mt5.ORDER_TYPE_SELL,
        "price": price,
        "sl": sl,
        "tp": tp,
        "deviation": 10,
        "magic": 234000,
        "comment": "Gold strategy trade",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        raise Exception(f"Trade failed: {result.retcode}")
    return result
