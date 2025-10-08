class EntryRules:
    def init(self):
        self.confirm_candles = 3

    def check_entry(self, trend_bias, candles):
        """
        Checks for entry opportunities aligned with the trend bias.
        Returns True if setup found, else False.
        """
        try:
            closes = [c['close'] for c in candles[-self.confirm_candles:]]
            last = closes[-1]

            if trend_bias == "BULLISH" and last > min(closes):
                return True
            elif trend_bias == "BEARISH" and last < max(closes):
                return True
            else:
                return False
        except Exception as e:
            print(f"❌ Entry rule error: {e}")
            return False
