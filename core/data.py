import random
import datetime

class MarketData:
    def init(self, symbol="XAUUSD"):
        self.symbol = symbol

    def get_latest_candles(self, timeframe="H1", count=50):
        """
        Simulates fetching candle data for the given timeframe.
        Each candle: {'open': ..., 'high': ..., 'low': ..., 'close': ...}
        """
        base_price = 2400  # example gold price
        candles = []
        for _ in range(count):
            open_p = base_price + random.uniform(-10, 10)
            close_p = open_p + random.uniform(-5, 5)
            high_p = max(open_p, close_p) + random.uniform(0, 5)
            low_p = min(open_p, close_p) - random.uniform(0, 5)
            candles.append({
                'open': round(open_p, 2),
                'high': round(high_p, 2),
                'low': round(low_p, 2),
                'close': round(close_p, 2)
            })
        return candles

    def current_price(self):
        """Simulated current market price."""
        return round(2400 + random.uniform(-10, 10), 2)

    def timestamp_now(self):
        """Returns readable timestamp for logs."""
        return datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
