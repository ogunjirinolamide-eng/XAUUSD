class BiasDetector:
    def init(self):
        self.lookback = 20  # number of candles to analyze

    def detect_bias(self, candles):
        """
        Detects market bias (trend) based on simple moving averages and price movement.
        candles: list of dicts like [{'close': 1920}, {'close': 1930}, ...]
        """
        try:
            closes = [c['close'] for c in candles[-self.lookback:]]
            avg_short = sum(closes[-5:]) / 5
            avg_long = sum(closes) / len(closes)

            if avg_short > avg_long:
                return "BULLISH"
            elif avg_short < avg_long:
                return "BEARISH"
            else:
                return "NEUTRAL"
        except Exception as e:
            print(f"❌ Bias detection error: {e}")
            return "UNKNOWN"
