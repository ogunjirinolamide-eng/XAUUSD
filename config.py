class Config:
    # --- Trading Core Settings ---
    SYMBOL = "XAUUSD"             # Gold
    TIMEFRAME_TREND_CONFIRM = "H4"
    TIMEFRAME_ENTRY = "M15"

    # --- Risk Management ---
    MAX_DAILY_RISK = 0.20         # 20% per day
    RISK_PER_TRADE = 0.05         # 5% per trade

    # --- Technical Settings ---
    TRAILING_STOP = True
    TRAILING_DISTANCE = 50         # in pips
    MIN_PULLBACK_CHECK = "M30"     # for small retracements
    MAX_OPEN_TRADES = 3

    # --- Scheduler Settings ---
    CHECK_INTERVAL = 15            # minutes per loop

    # --- Data Source (can integrate to broker later) ---
    API_SOURCE = "demo"            # placeholder for live API (e.g. MetaTrader, Binance, etc.)

    # --- Logging & Display ---
    SHOW_LOGS = True
    VERBOSE_MODE = True
