import MetaTrader5 as mt5
import time

def connect_to_mt5():
    # Login credentials — replace these with your demo credentials
    login = 12345678              # your demo account number
    password = "yourpassword"     # your demo password
    server = "ICMarkets-Demo"     # IC Markets demo server

    if not mt5.initialize(server=server, login=login, password=password):
        raise Exception(f"MT5 initialization failed: {mt5.last_error()}")
    print("✅ Connected to MetaTrader 5")
    return True

def shutdown_mt5():
    mt5.shutdown()
